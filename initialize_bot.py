import os
from dotenv import load_dotenv, set_key
from openai import OpenAI

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def initialize_optibot():
    # 1. Tạo Vector Store
    print("--- Đang tạo Vector Store... ---")
    vector_store = client.beta.vector_stores.create(name="OptiBot_Knowledge_Base")
    
    # 2. Lưu Vector Store ID (Ép không dùng dấu nháy)
    set_key(".env", "VECTOR_STORE_ID", vector_store.id, quote_mode="never")
    print(f"Đã tạo Vector Store ID: {vector_store.id}")

    # 3. Định nghĩa System Prompt (Giữ nguyên văn - Verbatim)
    system_prompt = """You are OptiBot, the customer-support bot for OptiSigns.com.
• Tone: helpful, factual, concise.
• Only answer using the uploaded docs.
• Max 5 bullet points; else link to the doc.
• Cite up to 3 "Article URL:" lines per reply."""

    print("--- Đang tạo Assistant với cấu hình tối ưu định dạng... ---")
    
    # 4. Tạo Assistant
    assistant = client.beta.assistants.create(
        name="OptiBot Mini-Clone",
        instructions=system_prompt,
        model="gpt-4o",
        tools=[{"type": "file_search"}],
        tool_resources={
            "file_search": {
                "vector_store_ids": [vector_store.id]
            }
        },
        temperature=0.1,
        top_p=0.1
    )
    
    # 5. Lưu Assistant ID vào file .env (Ép không dùng dấu nháy)
    set_key(".env", "ASSISTANT_ID", assistant.id, quote_mode="never")
    print(f"Đã tạo Assistant ID: {assistant.id}")
    print("\n--- Khởi tạo thành công với cấu hình Deterministic và ID sạch! ---")

if __name__ == "__main__":
    initialize_optibot()