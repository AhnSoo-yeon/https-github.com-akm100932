import tkinter as tk
import random

responses = {
    "안녕": "안녕하세요!",
    "안녕하세요": "안녕하세요, 만나서 반가워요.",
    "이름": "저는 간단한 챗봇입니다.",
    "잘가": "안녕히 가세요.",
    "hello": "Hello!",
    "hi": "Hi there!",
    "bye": "Goodbye!",
}

fallback = [
    "말씀을 잘 이해하지 못했어요.",
    "다시 한번 말해 주세요.",
    "그렇게 생각하시나요?"
]


def get_response(text: str) -> str:
    for key, value in responses.items():
        if key.lower() in text.lower():
            return value
    return random.choice(fallback)


def send_message(event=None):
    user_text = entry.get().strip()
    if not user_text:
        return
    chat_listbox.insert(tk.END, f"당신: {user_text}")
    if user_text.lower() == "exit":
        root.quit()
        return
    response = get_response(user_text)
    chat_listbox.insert(tk.END, f"챗봇: {response}")
    entry.delete(0, tk.END)
    chat_listbox.yview_moveto(1.0)


root = tk.Tk()
root.title("챗봇 애플리케이션")

chat_listbox = tk.Listbox(root, width=50, height=15)
chat_listbox.pack(padx=10, pady=10)

entry = tk.Entry(root, width=40)
entry.pack(side=tk.LEFT, padx=10, pady=10)
entry.bind("<Return>", send_message)

send_button = tk.Button(root, text="전송", command=send_message)
send_button.pack(side=tk.LEFT, padx=5)

chat_listbox.insert(tk.END, "챗봇에 오신 걸 환영합니다. 'exit'을 입력하면 종료됩니다.")

entry.focus()
root.mainloop()
