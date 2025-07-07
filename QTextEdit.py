from PySide6.QtWidgets import QApplication, QWidget, QTextEdit, QLabel, QPushButton, QVBoxLayout

# Create the app
app = QApplication([])

# Create main window
window = QWidget()
window.setWindowTitle("QTextEdit Example")

# Create widgets
text_edit = QTextEdit()
text_edit.setPlaceholderText("Type your message here...")

button = QPushButton("Show Message")
display_label = QLabel("")

# Function to display the text
def show_message():
    message = text_edit.toPlainText()  # Gets plain text
    display_label.setText(f"You wrote:\n{message}")

# Connect button click to function
button.clicked.connect(show_message)

# Layout
layout = QVBoxLayout()
layout.addWidget(text_edit)
layout.addWidget(button)
layout.addWidget(display_label)

window.setLayout(layout)
window.show()

# Run the app
app.exec()
