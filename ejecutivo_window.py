from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel

class EjecutivoWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Ventana del Ejecutivo de Viaje")
        self.layout = QVBoxLayout()
        self.layout.addWidget(QLabel("¡Bienvenido, Ejecutivo de Viaje!"))
        self.setLayout(self.layout)
