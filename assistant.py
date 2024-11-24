import sys
import pyttsx3
import speech_recognition as sr
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QTextEdit, QLabel, QVBoxLayout, QWidget
from PyQt5.QtGui import QFont
from vpython import sphere, rate, color
from commands import execute_command
from threading import Thread

class VirtualAssistantGUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()
        self.voice_engine = pyttsx3.init()
        self.recognizer = sr.Recognizer()

    def init_ui(self):
        self.setWindowTitle("3D Virtual Assistant - Ron")
        self.setGeometry(100, 100, 800, 600)

        # Main layout
        layout = QVBoxLayout()

        # Label
        self.label = QLabel("Hello, I am Ron, your virtual assistant.")
        self.label.setFont(QFont("Arial", 16))
        layout.addWidget(self.label)

        # Text area
        self.text_area = QTextEdit()
        self.text_area.setFont(QFont("Arial", 14))
        self.text_area.setReadOnly(True)
        layout.addWidget(self.text_area)

        # Buttons
        self.speak_button = QPushButton("Speak")
        self.speak_button.setFont(QFont("Arial", 14))
        self.speak_button.clicked.connect(self.start_listening)
        layout.addWidget(self.speak_button)

        self.exit_button = QPushButton("Exit")
        self.exit_button.setFont(QFont("Arial", 14))
        self.exit_button.clicked.connect(self.close)
        layout.addWidget(self.exit_button)

        # Central widget
        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

        # Start 3D animation in a separate thread
        self.start_3d_animation()

    def start_listening(self):
        """Start voice recognition."""
        self.label.setText("Listening...")
        query = self.take_command()
        if query:
            self.text_area.append(f"You said: {query}")
            if "exit" in query or "quit" in query:
                self.speak("Goodbye! Have a great day.")
                self.close()
            elif "shutdown" in query or "restart" in query or "log off" in query:
                self.speak("Sorry, I cannot assist with that. Please perform this action manually.")
            else:
                execute_command(query)
        else:
            self.text_area.append("I didn't catch that.")

    def take_command(self):
        """Listen for a voice command."""
        with sr.Microphone() as source:
            self.recognizer.adjust_for_ambient_noise(source)
            try:
                audio = self.recognizer.listen(source, timeout=5, phrase_time_limit=5)
                query = self.recognizer.recognize_google(audio, language="en-in")
                return query.lower()
            except sr.UnknownValueError:
                self.speak("Sorry, I didn't catch that. Please say it again.")
                return ""
            except sr.RequestError:
                self.speak("There seems to be an issue with the speech service.")
                return ""

    def speak(self, text):
        """Speak the given text."""
        self.voice_engine.setProperty("rate", 175)
        self.voice_engine.say(text)
        self.voice_engine.runAndWait()

    def start_3d_animation(self):
        """Start a 3D animation using VPython."""
        def animate():
            ball = sphere(color=color.cyan, radius=0.5)
            while True:
                for _ in range(100):
                    rate(50)
                    ball.color = color.red if ball.color == color.cyan else color.cyan

        thread = Thread(target=animate, daemon=True)
        thread.start()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    assistant_gui = VirtualAssistantGUI()
    assistant_gui.show()
    sys.exit(app.exec_())
