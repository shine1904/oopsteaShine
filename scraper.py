import requests
import os
import re
from markdownify import markdownify as md

SUBDOMAIN = "optisignshelp" 
BASE_API_URL = f"https://{SUBDOMAIN}.zendesk.com/api/v2/help_center/en-us/articles.json"
OUTPUT_DIR = "articles_md"

def scrape_all_articles(limit=100):
    """Đổi tên từ fetch_articles_via_api thành scrape_all_articles để khớp với main.py"""
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)

    params = {'page[size]': limit}
    articles_data = {} # Dictionary để lưu {url: content} phục vụ Delta Detection
    
    try:
        response = requests.get(BASE_API_URL, params=params)
        response.raise_for_status()
        data = response.json()
        articles = data.get('articles', [])

        for article in articles:
            title = article['title']
            body = article['body']
            url = article['html_url']
            
            markdown_content = md(body, heading_style="ATX")
            
            final_text = (
                f"Article URL: {url}\n"
                f"--- DOCUMENT START ---\n\n"
                f"# {title}\n\n"
                f"{markdown_content}\n\n"
                f"--- DOCUMENT END ---\n"
                f"For more details, please visit: Article URL: {url}"
            )
            
            # Lưu vào dictionary để trả về cho main.py
            articles_data[url] = final_text
            
            # (Tùy chọn) Vẫn lưu file local để kiểm tra
            slug = re.sub(r'[^a-z0-9]+', '-', title.lower()).strip('-')
            file_path = os.path.join(OUTPUT_DIR, f"{slug}.md")
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(final_text)
            
        return articles_data # Quan trọng: Phải trả về dữ liệu
        
    except Exception as e:
        print(f"Lỗi khi gọi API: {e}")
        return {}