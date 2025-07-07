from PySide6.QtWidgets import QApplication, QLabel, QWidget, QMessageBox, QLineEdit, QVBoxLayout, QPushButton
import sys
app = QApplication(sys.argv)
window = QWidget()
layout = QVBoxLayout()

label1 = QLabel("Username")
input1 = QLineEdit()
label2 = QLabel("Password")
input2 = QLineEdit()
button = QPushButton("login")

layout.addWidget(label1)
layout.addWidget(input1)
layout.addWidget(label2)
layout.addWidget(input2)

window.setLayout(layout)
window.setWindowTitle("Login Page")
window.resize(300,200)
window.show()

app.exec()