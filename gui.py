import sys

from PyQt6.QtWidgets import (
    QApplication,
    QFormLayout,
    QPushButton,
    QLineEdit,
    QWidget,
    QLabel,
    QDialog,
)

from test import run_gpt

def run():
    print("run button clicked!")
    prompt = le_prompt.text()
    answer = run_gpt(prompt, True)
    lb_answer.setText(answer)

app = QApplication([])
# window = QDialog()
window = QWidget()
window.setWindowTitle("GPT ChatBot Test")
window.setFixedWidth(800)
window.setFixedHeight(600)

layout = QFormLayout()

le_prompt = QLineEdit()
pb_run = QPushButton("Run")
pb_run.clicked.connect(run)
lb_answer = QLabel()
lb_answer.setWordWrap(True)

layout.addRow("Prompt:", le_prompt)
layout.addRow(pb_run)
layout.addRow("Answer:", lb_answer)
window.setLayout(layout)

window.show()
sys.exit(app.exec())