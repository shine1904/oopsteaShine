import os

def add_article_to_source():
    # Nhập thông tin từ bàn phím
    print("--- Thêm bài viết mới vào kho tri thức ---")
    url = input("Nhập Article URL: ").strip()
    filename = input("Nhập tên file (ví dụ: youtube-guide): ").strip()
    
    print("\nNhập/Dán nội dung bài viết (Gõ 'EOF' ở dòng mới để kết thúc):")
    lines = []
    while True:
        line = input()
        if line.strip() == "EOF":
            break
        lines.append(line)
    
    content = "\n".join(lines)

    # Cấu trúc lại file theo chuẩn để chunk_processor có thể đọc được
    full_content = f"Article URL: {url}\n\n{content}\n\nFor more details, please visit: Article URL: {url}"

    # Lưu vào thư mục articles_md
    os.makedirs("articles_md", exist_ok=True)
    file_path = os.path.join("articles_md", f"{filename}.md")
    
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(full_content)
    
    print(f"\n--- THÀNH CÔNG: Đã lưu tại {file_path} ---")

if __name__ == "__main__":
    add_article_to_source()