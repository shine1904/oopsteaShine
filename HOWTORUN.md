 Docker Commands Guide for Optibot Project

## 1. Build Docker Image

Run this command to package all code into an image named optibot-app:

```powershell
docker build -t optibot-app .
```

## 2. Launch Web Interface (Streamlit)

This command will run a container named optibot-web from the optibot-app image:

```powershell
# Note: Remember to delete the old container if you get a Conflict error
docker rm -f optibot-web 

docker run -d -p 8501:8501 --env-file .env -v "${PWD}:/app" --name optibot-web optibot-app
```

**`-v "${PWD}:/app"`**: Syncs metadata files between your computer and Docker.

## 3. Run Scraper Job (Update Data)

If you only want to run the scraper script inside Docker environment without opening the web interface:

```powershell
docker run --rm --env-file .env -v "${PWD}:/app" optibot-app python main.py
```

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
 Tổng hợp lệnh Docker chuẩn cho dự án Optibot
1. Xây dựng Docker Image (Build)
Bạn chạy lệnh này để đóng gói toàn bộ code vào một Image có tên là optibot-app:

PowerShell

docker build -t optibot-app .
2. Khởi chạy Giao diện Web (Streamlit)
Lệnh này sẽ chạy container tên là optibot-web từ image optibot-app.

PowerShell

# Lưu ý: Nhớ xóa container cũ nếu bị báo lỗi Conflict như lúc nãy
docker rm -f optibot-web 

docker run -d -p 8501:8501 --env-file .env -v "${PWD}:/app" --name optibot-web optibot-app
-v "${PWD}:/app": Giúp đồng bộ file metadata giữa máy tính của bạn và Docker.

3. Chạy Scraper Job (Cập nhật dữ liệu)
Nếu bạn chỉ muốn chạy script cào dữ liệu bên trong môi trường Docker mà không mở web:

PowerShell

docker run --rm --env-file .env -v "${PWD}:/app" optibot-app python main.py