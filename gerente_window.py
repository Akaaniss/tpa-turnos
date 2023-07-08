from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel

class GerenteWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Ventana del Gerente")
        self.layout = QVBoxLayout()
        self.layout.addWidget(QLabel("¡Bienvenido, Gerente!"))
        self.setLayout(self.layout)

 
