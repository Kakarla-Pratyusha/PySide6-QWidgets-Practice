from PySide6.QtWidgets import QApplication, QLabel, QPushButton, QLineEdit, QWidget, QVBoxLayout
import sys
app = QApplication([])

window = QWidget()
layout = QVBoxLayout()

line_edit = QLineEdit()
label = QLabel("Enter Your Name")
pushbutton = QPushButton("Greet")
greeting = QLabel("")

def greet():
     greeting.setText(f"Hello, {line_edit.text()}!")
 
pushbutton.clicked.connect(greet)

layout.addWidget(label)
layout.addWidget(line_edit)
layout.addWidget(pushbutton)
layout.addWidget(greeting)

window.setLayout(layout)
window.setWindowTitle("Greeting App")
window.show()

app.exec()
