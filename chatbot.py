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


def main():
    print("챗봇에 오신 걸 환영합니다. 종료하려면 'exit'을 입력하세요.")
    while True:
        user_input = input("당신: ").strip()
        if user_input.lower() == "exit":
            print("챗봇: 안녕히 가세요.")
            break

        response_found = False
        for key, value in responses.items():
            if key.lower() in user_input.lower():
                print("챗봇:", value)
                response_found = True
                break
        if not response_found:
            print("챗봇:", random.choice(fallback))


if __name__ == "__main__":
    main()
