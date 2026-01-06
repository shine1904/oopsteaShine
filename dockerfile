FROM python:3.11-slim

WORKDIR /app

# Cài đặt các thư viện hệ thống cần thiết (nếu có)
RUN apt-get update && apt-get install -y \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Copy và cài đặt dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy toàn bộ mã nguồn vào container
COPY . .

# Khai báo cổng 8501 để Docker có thể ánh xạ ra ngoài
EXPOSE 8501

# Lệnh khởi chạy Streamlit làm mặc định
# Chế độ --server.address=0.0.0.0 giúp truy cập được từ máy chủ host
CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]