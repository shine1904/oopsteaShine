import os
import re
import json

OUTPUT_DIR = "articles_chunked"

def clean_markdown_source(text):
    """Xóa định dạng Markdown link để AI chỉ đọc văn bản thuần."""
    # Biến [Text](URL) thành Text (URL)
    text = re.sub(r'\[([^\]]+)\]\((https?://[^\)]+)\)', r'\1 (\2)', text)
    # Biến [Text](mailto:...) thành Text (Email)
    text = re.sub(r'\[([^\]]+)\]\(mailto:([^\)]+)\)', r'\1 (\2)', text)
    return text

def process_single_article(url, content, filename_base="article"):
    """
    Xử lý một bài viết đơn lẻ: Clean -> Chunk -> Save.
    Trả về danh sách đường dẫn các file chunk đã tạo.
    """
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)

    created_chunks = []
    title = filename_base.replace(".md", "").replace("-", " ").title()

    # 1. Làm sạch nội dung
    cleaned_text = clean_markdown_source(content)
    
    # 2. Chia nhỏ nội dung theo các tiêu đề ##
    sections = re.split(r'\n(?=## )', cleaned_text)

    for i, section in enumerate(sections):
        section = section.strip()
        if not section: continue

        # 3. Tạo nội dung chunk kèm Metadata
        chunk_content = (
            f"Article URL: {url}\n"
            f"Topic: {title}\n\n"
            f"{section}"
        )

        # 4. Lưu file chunk tạm thời
        safe_name = re.sub(r'[^\w\-]', '_', filename_base.replace(".md", ""))
        chunk_filename = f"{safe_name}_chunk_{i}.md"
        chunk_path = os.path.join(OUTPUT_DIR, chunk_filename)
        
        with open(chunk_path, "w", encoding="utf-8") as f:
            f.write(chunk_content)
        
        created_chunks.append(chunk_path)

    return created_chunks

def chunk_all_local_files(input_dir="articles_md"):
    """
    Hàm bổ trợ để quét toàn bộ thư mục (giữ logic cũ cho bạn).
    """
    if not os.path.exists(input_dir):
        print(f"Thư mục {input_dir} không tồn tại.")
        return

    url_map = {}
    for filename in os.listdir(input_dir):
        if filename.endswith(".md"):
            with open(os.path.join(input_dir, filename), "r", encoding="utf-8") as f:
                content = f.read()
            
            # Trích xuất URL
            url_match = re.search(r"Article URL:\s*(https?://[^\s\n]+)", content)
            url = url_match.group(1) if url_match else "URL_NOT_FOUND"
            
            # Gọi hàm xử lý đơn lẻ
            chunks = process_single_article(url, content, filename)
            
            # Cập nhật vào url_map cho các chunk vừa tạo
            for path in chunks:
                fname = os.path.basename(path)
                url_map[fname] = url

    # Xuất file map sau khi xử lý xong tất cả
    with open("url_map.json", "w", encoding="utf-8") as f:
        json.dump(url_map, f, ensure_ascii=False, indent=4)
    
    print(f"--- Đã xử lý xong toàn bộ file nội bộ và cập nhật url_map.json ---")

if __name__ == "__main__":
    # Nếu chạy trực tiếp file này, nó sẽ xử lý toàn bộ thư mục articles_md
    chunk_all_local_files()