from PySide6.QtWidgets import QWidget, QPushButton
from ui_widget import Ui_widget

class Widget(QWidget, Ui_widget):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("chinese boy")
        self.setGeometry(200, 455, 300, 450)
        self.setMaximumHeight(450)
        self.setMaximumWidth(300)
        self.setMinimumHeight(450)
        self.setMinimumWidth(300)
    
        self.button_0.clicked.connect(self.on_button_click)
        self.button_1.clicked.connect(self.on_button_click)
        self.button_2.clicked.connect(self.on_button_click)
        self.button_3.clicked.connect(self.on_button_click)
        self.button_4.clicked.connect(self.on_button_click)
        self.button_5.clicked.connect(self.on_button_click)
        self.button_6.clicked.connect(self.on_button_click)
        self.button_7.clicked.connect(self.on_button_click)
        self.button_8.clicked.connect(self.on_button_click)
        self.button_9.clicked.connect(self.on_button_click)
        self.button_plus.clicked.connect(self.on_button_click)
        self.button_minus.clicked.connect(self.on_button_click)
        self.button_multiply.clicked.connect(self.on_button_click)
        self.button_divide.clicked.connect(self.on_button_click)
        self.button_clear.clicked.connect(self.on_button_click)
        self.button_equal.clicked.connect(self.on_button_click)
        self.button_decimal.clicked.connect(self.on_button_click)
        
    def on_button_click(self):
        button = self.sender()
        current_text = self.display_input.text()
        
        if current_text == "0":
            current_text = ""
            
        if button.text() == "":
            try:
                result = str(eval(current_text))
                self.display_input.setText(result)
                self.display_output.setText(current_text + button.text())
                
            except ZeroDivisionError:
                self.display_input.setText("Can't divide by zero!")
            except Exception as e:
                self.display_input.setText("Invalid expression!")
                
        else:
            self.display_input.setText(current_text + button.text())
            self.display_output.setText(current_text + button.text())
            
        if button.text() == "C":
            self.display_input.setText("0")
            self.display_output.setText("")
            