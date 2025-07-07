from PySide6.QtWidgets import QApplication, QLabel, QVBoxLayout, QWidget, QLineEdit,QMessageBox, QPushButton
import sys

students = {
    "101": {"name": "Aarav Sharma", "course": "B.Tech CSE", "marks": 88},
    "102": {"name": "Diya Patel", "course": "B.Sc Physics", "marks": 91},
    "103": {"name": "Kabir Mehra", "course": "B.Com", "marks": 76},
    "104": {"name": "Sneha Rao", "course": "B.A English", "marks": 84}
}

app = QApplication(sys.argv)

window = QWidget()
layout = QVBoxLayout()

label = QLabel("Enter roll no. -")
line_edit = QLineEdit()
button = QPushButton("Submit")
result = QLabel("")

def submit():
    roll = line_edit.text().strip()
    if roll in students:
        info = students[roll]
        result.setText(
            f"Name: {info['name']}\n"
            f"Course: {info['course']}\n"
            f"Marks: {info['marks']}"
        )
    else:
        QMessageBox.warning(window, "Not Found", "Roll number not found.")
        result.setText("")

button.clicked.connect(submit)

layout.addWidget(label)
layout.addWidget(line_edit)
layout.addWidget(button)
layout.addWidget(result)

window.setLayout(layout)
window.setWindowTitle("Student Roll Number Lookup")
window.resize(300,200)
window.show()

app.exec()