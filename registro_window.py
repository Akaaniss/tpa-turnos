import sys
import csv
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QLineEdit, QPushButton, QMessageBox
from PyQt6.QtCore import Qt

# Ventana de Registro
class RegistroWindow(QWidget):
    def __init__(self, main_window):
        super().__init__()
        self.setWindowTitle("Registro")
        self.resize(400, 300)
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)
        self.main_window = main_window

        # Campos de entrada de datos para el registro
        self.username_input = QLineEdit()
        self.layout.addWidget(QLabel("Usuario:"))
        self.layout.addWidget(self.username_input)
        self.username_input.setMaximumWidth(200)

        self.password_input = QLineEdit()
        self.password_input.setEchoMode(QLineEdit.EchoMode.Password)
        self.layout.addWidget(QLabel("Contraseña:"))
        self.layout.addWidget(self.password_input)
        self.password_input.setMaximumWidth(200)

        # Botón para registrar una cuenta
        self.registrar_button = QPushButton("Registrarse")
        self.registrar_button.clicked.connect(self.registrar_cuenta)
        self.layout.addWidget(self.registrar_button)
        self.registrar_button.setMaximumWidth(200)

        # Botón "Atrás"
        self.atras_button = QPushButton("Atrás")
        self.atras_button.clicked.connect(self.atras_button_clicked)
        self.layout.addWidget(self.atras_button)
        self.atras_button.setMaximumWidth(200)

        font = self.font()
        font.setPointSize(14)
        self.username_input.setFont(font)
        self.password_input.setFont(font)
        self.registrar_button.setFont(font)
        self.atras_button.setFont(font)

    def atras_button_clicked(self):
        self.close()
        self.main_window.open_login_window()

    def registrar_cuenta(self):
        username = self.username_input.text()
        password = self.password_input.text()

        # Guardar los datos de registro en el archivo CSV
        with open("registro_de_cuentas.csv", "a") as file:
            writer = csv.writer(file)
            writer.writerow([username, password])

        QMessageBox.information(self, "Registro exitoso", "La cuenta ha sido registrada con éxito")
        self.close()
