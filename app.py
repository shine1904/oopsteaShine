import streamlit as st
from openai import OpenAI
import os
import re
import json
from dotenv import load_dotenv

# Load môi trường
load_dotenv()

def get_clean_env(key):
    value = os.getenv(key)
    return value.strip().replace("'", "").replace('"', "") if value else ""

# Khởi tạo Client
client = OpenAI(api_key=get_clean_env("OPENAI_API_KEY"))
assistant_id = get_clean_env("ASSISTANT_ID")

# Tải bản đồ URL từ file JSON (đã tạo từ chunk_processor.py)
try:
    with open("url_map.json", "r", encoding="utf-8") as f:
        url_mapping = json.load(f)
except FileNotFoundError:
    url_mapping = {}

# --- HÀM XỬ LÝ HẬU KỲ (POST-PROCESSING) ---
def refine_response(text, detected_url=""):
    """Làm sạch câu trả lời và dán URL chuẩn vào cuối."""
    # 1. Xóa citation hệ thống (【...】)
    text = re.sub(r'【[^】]+】', '', text)
    
    # 2. Xóa định dạng link Markdown để tránh lặp
    text = re.sub(r'\[.*?\]\((https?://.*?)\)', r'\1', text)
    
    # 3. Làm sạch text khỏi các dòng URL cũ hoặc URL trần
    if detected_url:
        text = text.replace(detected_url, "")
    text = text.replace("Article URL:", "").strip()

    # 4. Lấy tối đa 5 dòng nội dung chính
    raw_lines = text.split('\n')
    content_lines = [l.strip() for l in raw_lines if l.strip()][:5]
    final_content = "\n".join(content_lines)
    
    # 5. Kết hợp nội dung và Article URL chuẩn
    if detected_url:
        return f"{final_content}\n\nArticle URL: {detected_url}"
    return final_content

# --- GIAO DIỆN STREAMLIT ---
st.set_page_config(page_title="OptiBot Support", page_icon="🤖")
st.title("🤖 OptiBot Support Assistant")
st.caption("Giao diện hỗ trợ khách hàng sử dụng Dynamic Metadata Mapping.")

if "messages" not in st.session_state:
    st.session_state.messages = []

# Hiển thị lịch sử chat
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.text(message["content"])

if prompt := st.chat_input("Hỏi về YouTube, Payment, hoặc Disk Encryption..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.spinner('Đang truy xuất dữ liệu từ hệ thống...'):
        try:
            thread = client.beta.threads.create()
            client.beta.threads.messages.create(thread_id=thread.id, role="user", content=prompt)
            
            run = client.beta.threads.runs.create_and_poll(thread_id=thread.id, assistant_id=assistant_id)
            
            if run.status == 'completed':
                messages = client.beta.threads.messages.list(thread_id=thread.id)
                msg_obj = messages.data[0].content[0].text
                raw_response = msg_obj.value
                annotations = msg_obj.annotations
                print(f"DEBUG - Annotations found: {len(annotations)}") # Kiểm tra xem có annotation không
                
                found_url = ""

                # ƯU TIÊN 1: Tìm URL có sẵn trong văn bản trả về
                url_match = re.search(r'https://support\.optisigns\.com/hc/\S+', raw_response)
                if url_match:
                    found_url = url_match.group(0).strip('.,)')
                
                # ƯU TIÊN 2: Nếu AI không viết link, truy xuất từ Metadata (Annotations)
                if not found_url and annotations:
                    for annot in annotations:
                        if file_citation := getattr(annot, 'file_citation', None):
                            # Lấy File ID từ hệ thống OpenAI
                            f_id = file_citation.file_id
                            # Gọi API lấy thông tin file để biết tên file gốc
                            file_info = client.files.retrieve(f_id)
                            # Tra cứu trong url_map.json
                            found_url = url_mapping.get(file_info.filename, "")
                            if found_url:
                                break

                # Áp dụng hậu kỳ
                final_response = refine_response(raw_response, found_url)
                
                with st.chat_message("assistant"):
                    st.code(final_response, language=None) 
                
                st.session_state.messages.append({"role": "assistant", "content": final_response})
            else:
                st.error(f"Lỗi phản hồi: {run.status}")
                
        except Exception as e:
            st.error(f"Lỗi hệ thống: {str(e)}")