import sys
from PySide6.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout

# Only create app if it doesn't already exist
app = QApplication.instance()
if not app:
    app = QApplication(sys.argv)

# Create the main window
window = QWidget()
window.setWindowTitle("QLineEdit Example")

label = QLabel("Enter your name:")
line_edit = QLineEdit()
button = QPushButton("Submit")
greeting_label = QLabel("")

def show_greeting():
    name = line_edit.text()
    greeting_label.setText(f"Hello, {name}!")

button.clicked.connect(show_greeting)

layout = QVBoxLayout()
layout.addWidget(label)
layout.addWidget(line_edit)
layout.addWidget(button)
layout.addWidget(greeting_label)

window.setLayout(layout)
window.show()

# Only start event loop if not already running
if not QApplication.instance().exec():
    sys.exit()
