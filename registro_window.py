import sys
import csv
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QLineEdit, QPushButton, QMessageBox
from PyQt6.QtCore import Qt

class RegistroWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Registro")
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        # Campos de entrada de datos para el registro
        self.username_input = QLineEdit()
        self.layout.addWidget(QLabel("Usuario:"))
        self.layout.addWidget(self.username_input)

        self.password_input = QLineEdit()
        self.password_input.setEchoMode(QLineEdit.EchoMode.Password)
        self.layout.addWidget(QLabel("Contraseña:"))
        self.layout.addWidget(self.password_input)

        # Botón para registrar una cuenta
        self.registrar_button = QPushButton("Registrarse")
        self.registrar_button.clicked.connect(self.registrar_cuenta)
        self.layout.addWidget(self.registrar_button)

    def registrar_cuenta(self):
        username = self.username_input.text()
        password = self.password_input.text()

        # Verificar si el archivo "registro_de_cuentas.csv" existe
        '''
        try:
            with open("registro_de_cuentas.csv", "r") as file:
                reader = csv.reader(file)
                for row in reader:
                    if row[0] == username:
                        QMessageBox.warning(self, "Error de registro", "El usuario ya existe")
                        return
        except FileNotFoundError:
            pass
        '''
        # Guardar los datos de registro en el archivo CSV
        with open("registro_de_cuentas.csv", "a") as file:
            writer = csv.writer(file)
            writer.writerow([username, password])

        QMessageBox.information(self, "Registro exitoso", "La cuenta ha sido registrada con éxito")
        self.close()