import sys
import random
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt
from ui_expression_generator import Ui_MainWindow

class ExpressionManager:
    def __init__(self):
        self.data = {
            "ყველაფერი": [
                ("წყალს გაატანა", "ვიღაცამ რაღაც საკითხს ყურადღება აღარ მიაქცია"),
                ("ტვინი შეჭამა", "ვიღაცამ ძალიან შეაწუხა სხვა ადამიანი საუბრით"),
            ],
            "გრძნობები": [
                ("გული მოეწურა", "ძალიან ცუდად გახდა ემოციურად"),
                ("სისხლი ეყინა", "ძალიან შეეშინდა"),
            ],
            "ხასიათი": [
                ("სულსწრაფი იყო", "ძალიან მოუთმენელი ადამიანი"),
                ("გრძელი ენა აქვს", "ჭორიკანა ან ბევრს ლაპარაკობს"),
            ],
        }

    def get_expression(self, topic):
        if topic == "ყველაფერი":
            all_exprs = sum(self.data.values(), [])
            return random.choice(all_exprs)
        return random.choice(self.data.get(topic, []))

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.manager = ExpressionManager()

        # Signal-slot connections
        self.btn_generate.clicked.connect(self.generate_expression)
        self.combo_topic.currentIndexChanged.connect(self.generate_expression)
        self.checkbox_explanation.stateChanged.connect(self.toggle_explanation)

        self.label_explanation.setVisible(False)

        # Fonts and styling
        font_expr = QFont("BPG Glaho", 16, QFont.Bold)
        font_expl = QFont("BPG Glaho", 12, QFont.StyleItalic)
        self.label_expression.setFont(font_expr)
        self.label_explanation.setFont(font_expl)

        # Modern look with stylesheets
        self.setStyleSheet("""
            QWidget {
                background-color: #fdf6e3;
                font-family: 'BPG Glaho';
            }
            QPushButton {
                background-color: #268bd2;
                color: white;
                padding: 8px 12px;
                border-radius: 10px;
                font-size: 14px;
            }
            QPushButton:hover {
                background-color: #1c75bc;
            }
            QLabel {
                color: #073642;
            }
            QComboBox, QCheckBox {
                padding: 5px;
                font-size: 13px;
            }
        """)

    def generate_expression(self):
        topic = self.combo_topic.currentText()
        expression, explanation = self.manager.get_expression(topic)
        self.label_expression.setText(expression)

        if self.checkbox_explanation.isChecked():
            self.label_explanation.setText(explanation)
            self.label_explanation.setVisible(True)
        else:
            self.label_explanation.setVisible(False)

    def toggle_explanation(self):
        self.generate_expression()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.setWindowTitle("✨ ქართული გამოთქმების გენერატორი")
    window.resize(500, 350)
    window.show()
    sys.exit(app.exec_())

