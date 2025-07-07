import sys
import os
from PySide6.QtWidgets import (
    QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QFileDialog
)
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Qt


class ImageViewer(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Image Viewer")
        self.resize(600, 400)

        # Create UI components
        self.image_label = QLabel()
        self.image_label.setAlignment(Qt.AlignCenter)
        self.image_label.setStyleSheet("border: 1px solid gray;")

        self.open_button = QPushButton("Open Image")
        self.open_button.clicked.connect(self.open_image)

        # Layout setup
        layout = QVBoxLayout()
        layout.addWidget(self.image_label)
        layout.addWidget(self.open_button)
        self.setLayout(layout)

        # Load sample image at startup
        self.load_sample_image()

    def load_sample_image(self):
        sample_path = os.path.join(os.path.dirname(__file__), "sample.jpg")
        if os.path.exists(sample_path):
            self.display_image(sample_path)
        else:
            self.image_label.setText("No image loaded (sample.jpg not found)")

    def open_image(self):
        file_path, _ = QFileDialog.getOpenFileName(
            self, "Open Image", "", "Image Files (*.png *.jpg *.jpeg *.bmp)"
        )

        if file_path:
            self.display_image(file_path)

    def display_image(self, file_path):
        pixmap = QPixmap(file_path)
        if pixmap.isNull():
            self.image_label.setText("Failed to load image")
        else:
            self.image_label.setPixmap(pixmap.scaled(
                self.image_label.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation
            ))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    viewer = ImageViewer()
    viewer.show()
    sys.exit(app.exec())
 