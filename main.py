import os
import json
import hashlib
from scraper import scrape_all_articles
from chunk_processor import process_single_article
from openai import OpenAI
from dotenv import load_dotenv

# Load biến môi trường (GitHub Actions sẽ truyền vào qua env)
load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
vector_store_id = os.getenv("VECTOR_STORE_ID")

METADATA_FILE = "scrape_metadata.json"
URL_MAP_FILE = "url_map.json"

def get_hash(content):
    return hashlib.md5(content.encode('utf-8')).hexdigest()

def run_daily_job():
    # 1. Load Metadata cũ từ Repo
    old_metadata = {}
    if os.path.exists(METADATA_FILE):
        with open(METADATA_FILE, "r") as f: old_metadata = json.load(f)

    # 2. Load URL Map cũ
    url_mapping = {}
    if os.path.exists(URL_MAP_FILE):
        with open(URL_MAP_FILE, "r") as f: url_mapping = json.load(f)

    # 3. Quét website
    print("--- 1. Đang quét dữ liệu mới nhất... ---")
    current_articles = scrape_all_articles() 
    
    stats = {"added": 0, "updated": 0, "skipped": 0}
    new_metadata = {}

    for url, content in current_articles.items():
        curr_hash = get_hash(content)
        new_metadata[url] = curr_hash
        
        # Delta Detection
        if url not in old_metadata or old_metadata[url] != curr_hash:
            status = "added" if url not in old_metadata else "updated"
            print(f"[{status.upper()}] - {url}")
            
            # Sử dụng module chunk_processor của bạn
            filename_base = url.split('/')[-1] or "article"
            new_chunks = process_single_article(url, content, filename_base) 
            
            for chunk_path in new_chunks:
                with open(chunk_path, "rb") as f:
                    file_obj = client.files.create(file=f, purpose="assistants")
                    client.beta.vector_stores.files.create(
                        vector_store_id=vector_store_id, file_id=file_obj.id
                    )
                    url_mapping[file_obj.filename] = url
                os.remove(chunk_path)
            stats[status] += 1
        else:
            stats["skipped"] += 1

    # 4. Lưu lại (GitHub Action sẽ commit file này lên Repo)
    with open(METADATA_FILE, "w") as f: json.dump(new_metadata, f, indent=4)
    with open(URL_MAP_FILE, "w") as f: json.dump(url_mapping, f, indent=4)

    print(f"\n--- KẾT QUẢ JOB ---")
    print(f"Mới: {stats['added']}, Cập nhật: {stats['updated']}, Bỏ qua: {stats['skipped']}")

if __name__ == "__main__":
    run_daily_job()