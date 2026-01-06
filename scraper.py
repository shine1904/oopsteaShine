import requests
import os
import re
from markdownify import markdownify as md

# Cấu hình
SUBDOMAIN = "optisignshelp" 
BASE_API_URL = f"https://{SUBDOMAIN}.zendesk.com/api/v2/help_center/en-us/articles.json"
OUTPUT_DIR = "articles_md"

def fetch_articles_via_api(limit=30):
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)

    params = {'page[size]': limit}
    print(f"--- Đang lấy dữ liệu từ Zendesk API... ---")
    
    try:
        response = requests.get(BASE_API_URL, params=params)
        response.raise_for_status()
        data = response.json()
        articles = data.get('articles', [])

        saved_count = 0
        for article in articles:
            title = article['title']
            body = article['body']
            url = article['html_url']
            
            # Chuyển HTML body sang Markdown
            markdown_content = md(body, heading_style="ATX")
            
            # --- CHIẾN THUẬT SONG BẢO HIỂM ---
            # 1. URL ở Metadata đầu file (dùng để Indexing)
            # 2. URL ở Text thường cuối file (dùng để ép AI copy-paste)
            final_text = (
                f"Article URL: {url}\n"  # Metadata cho hệ thống
                f"--- DOCUMENT START ---\n\n"
                f"# {title}\n\n"
                f"{markdown_content}\n\n"
                f"--- DOCUMENT END ---\n"
                f"For more details, please visit: Article URL: {url}" # Text thường cho AI
            )
            
            # Tạo slug cho tên file
            slug = re.sub(r'[^a-z0-9]+', '-', title.lower()).strip('-')
            file_path = os.path.join(OUTPUT_DIR, f"{slug}.md")
            
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(final_text)
            
            saved_count += 1
            print(f"Đã lưu: {slug}.md")
            
        print(f"--- HOÀN THÀNH: Đã lưu {saved_count} file vào '{OUTPUT_DIR}' ---")
        
    except Exception as e:
        print(f"Lỗi khi gọi API: {e}")

if __name__ == "__main__":
    fetch_articles_via_api(30)