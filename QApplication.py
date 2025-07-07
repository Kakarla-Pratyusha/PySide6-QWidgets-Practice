from PySide6.QtWidgets import QApplication, QLabel 
import sys

app = QApplication(sys.argv)
label = QLabel("Hello")
label.show()
app.exec()
