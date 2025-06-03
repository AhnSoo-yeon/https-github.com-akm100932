# 간단한 챗봇 예제

이 저장소는 파이썬으로 작성한 간단한 챗봇 예제를 포함합니다. 콘솔 버전과 GUI 애플리케이션이 모두 제공됩니다.

## 콘솔 실행 방법

```bash
python3 chatbot.py
```

실행 후 대화를 입력하면 챗봇이 간단한 응답을 해 줍니다. 종료하려면 `exit`을 입력하세요.

## GUI 애플리케이션 실행

```bash
python3 chatbot_gui.py
```

Tkinter 기반 창이 열리며 메시지를 입력하고 전송 버튼을 누르면 챗봇의 답변을 볼 수 있습니다. `exit`을 입력하면 프로그램이 종료됩니다.

## 애플리케이션으로 패키징

PyInstaller를 사용하면 이 챗봇을 독립 실행형 애플리케이션으로 만들 수 있습니다. 
먼저 PyInstaller를 설치합니다.

```bash
pip install pyinstaller
```

그 다음 다음 명령을 실행하면 `dist` 디렉터리에 실행 파일이 생성됩니다.

```bash
./build.sh
```

Windows나 macOS에서도 PyInstaller를 이용해 동일하게 패키징할 수 있습니다.
