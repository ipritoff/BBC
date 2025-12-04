import sys
from PyQt6.QtWidgets import (QApplication, QWidget, QTextEdit, QScrollBar, QPushButton, QLabel, QVBoxLayout, QHBoxLayout)
from PyQt6.QtCore import Qt


class SEOAnalyzerWindow(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.setup_ui()

    def setup_ui(self) -> None:
        self.setWindowTitle("SEO анализ")

        layout = QVBoxLayout(self)
        layout.setSpacing(10)


        text_edit = QTextEdit()
        text_edit.setFixedHeight(120)
        text_edit.setPlaceholderText("Введите текст для анализа...")

        scroll = QScrollBar(Qt.Orientation.Vertical)
        scroll.setFixedHeight(120)

        top_layout = QHBoxLayout()
        top_layout.addWidget(text_edit)
        top_layout.addWidget(scroll)
        layout.addLayout(top_layout)

        # Кнопка
        button = QPushButton("Анализ")
        layout.addWidget(button)

        # Результат
        self.result_label = QLabel("")
        layout.addWidget(self.result_label)


        button.clicked.connect(self.on_analyze_clicked)

    def on_analyze_clicked(self) -> None:
        self.result_label.setText("Результат: SEO анализ текста")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SEOAnalyzerWindow()
    window.show()
    sys.exit(app.exec())