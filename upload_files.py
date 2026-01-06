import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
# Lấy ID và xóa bỏ khoảng trắng hoặc dấu nháy thừa nếu có
vs_id = os.getenv("VECTOR_STORE_ID").strip().replace("'", "").replace('"', "")

def upload_knowledge_base():
    path = "articles_md" # Thư mục chứa 30 file .md của bạn
    file_paths = [os.path.join(path, f) for f in os.listdir(path) if f.endswith('.md')]
    
    print(f"Đang chuẩn bị upload {len(file_paths)} file...")
    
    # Mở các file dưới dạng binary
    file_streams = [open(p, "rb") for p in file_paths]

    # Upload và chờ OpenAI xử lý (Embedding)
    file_batch = client.beta.vector_stores.file_batches.upload_and_poll(
        vector_store_id=vs_id,
        files=file_streams
    )

    print(f"Trạng thái: {file_batch.status}")
    print(f"Số lượng file thành công: {file_batch.file_counts.completed}")
    
    # Đóng các file stream
    for f in file_streams:
        f.close()

if __name__ == "__main__":
    if vs_id:
        upload_knowledge_base()
    else:
        print("Lỗi: Chưa có VECTOR_STORE_ID trong .env. Hãy chạy initialize_bot.py trước.")