import sys
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QPushButton, QTextEdit, QLabel, QVBoxLayout, QWidget
)
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import QFont, QPalette, QLinearGradient, QColor, QBrush
from commands import execute_command
import speech_recognition as sr
import pyttsx3
from threading import Thread


class FuturisticAssistant(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()
        self.voice_engine = pyttsx3.init()
        self.recognizer = sr.Recognizer()
        self.start_greeting()

    def init_ui(self):
        """Initialize the UI components."""
        self.setWindowTitle("Ron - Futuristic Virtual Assistant")
        self.setGeometry(100, 100, 900, 600)

        # Set gradient background
        palette = QPalette()
        gradient = QLinearGradient(0, 0, 0, 1)
        gradient.setCoordinateMode(QLinearGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QColor(20, 20, 40))
        gradient.setColorAt(1.0, QColor(0, 255, 255))
        palette.setBrush(QPalette.Window, QBrush(gradient))
        self.setPalette(palette)

        # Main layout
        layout = QVBoxLayout()

        # Greeting Label
        self.greeting_label = QLabel("Hello, I am Ron, your AI assistant!")
        self.greeting_label.setFont(QFont("Arial", 24))
        self.greeting_label.setStyleSheet("color: white;")
        self.greeting_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.greeting_label)

        # Command Output Area
        self.text_area = QTextEdit()
        self.text_area.setFont(QFont("Arial", 14))
        self.text_area.setStyleSheet("background: rgba(0, 0, 0, 0.5); color: white; border: none;")
        self.text_area.setReadOnly(True)
        layout.addWidget(self.text_area)

        # Buttons
        self.listen_button = QPushButton("Speak")
        self.listen_button.setFont(QFont("Arial", 14))
        self.listen_button.setStyleSheet(self.button_style())
        self.listen_button.clicked.connect(self.start_listening)
        layout.addWidget(self.listen_button)

        self.exit_button = QPushButton("Exit")
        self.exit_button.setFont(QFont("Arial", 14))
        self.exit_button.setStyleSheet(self.button_style())
        self.exit_button.clicked.connect(self.close)
        layout.addWidget(self.exit_button)

        # Set central widget
        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

    def start_greeting(self):
        """Greet the user with an animated introduction."""
        self.greeting_label.setText("Welcome to the future!")
        self.text_area.append("Hello, I am Ron, your AI assistant. Ready to help you!")

    def start_listening(self):
        """Activate voice recognition."""
        self.text_area.append("Listening for your command...")
        thread = Thread(target=self.listen_command, daemon=True)
        thread.start()

    def listen_command(self):
        """Listen for a voice command."""
        with sr.Microphone() as source:
            self.recognizer.adjust_for_ambient_noise(source)
            try:
                audio = self.recognizer.listen(source, timeout=5, phrase_time_limit=5)
                command = self.recognizer.recognize_google(audio, language="en-in")
                self.text_area.append(f"You said: {command}")
                self.process_command(command)
            except sr.UnknownValueError:
                self.text_area.append("Sorry, I didn't catch that. Please say it again.")
            except sr.RequestError:
                self.text_area.append("Speech service error. Please try again.")

    def process_command(self, command):
        """Process the voice command."""
        if "exit" in command or "quit" in command:
            self.speak("Goodbye! Have a great day.")
            self.close()
        else:
            self.speak(f"Executing command: {command}")
            execute_command(command)

    def speak(self, text):
        """Convert text to speech."""
        self.voice_engine.setProperty("rate", 175)
        self.voice_engine.say(text)
        self.voice_engine.runAndWait()

    @staticmethod
    def button_style():
        """Return the button stylesheet."""
        return """
            QPushButton {
                background-color: #00bcd4;
                color: white;
                border-radius: 10px;
                padding: 10px;
            }
            QPushButton:hover {
                background-color: #0097a7;
            }
        """


if __name__ == "__main__":
    app = QApplication(sys.argv)
    assistant_gui = FuturisticAssistant()
    assistant_gui.show()
    sys.exit(app.exec_())
