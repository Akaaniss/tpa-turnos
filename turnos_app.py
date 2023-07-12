import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QLineEdit, QPushButton, QLabel, QVBoxLayout, QWidget, QMessageBox
from PyQt6.QtCore import Qt
from registro_window import RegistroWindow
from gerente_window import GerenteWindow
from ejecutivo_window import EjecutivoWindow
from logistica_window import LogisticaWindow
import csv
import os 

# Ventana de inicio de sesión
class TurnosApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Turnos App")
        self.resize(800, 600)
        self.login_window = None

        # Crear una barra de menú
        menu_bar = self.menuBar()

        # Crear un menú "Rol" con opciones para el Gerente, Ejecutivo de Viaje y Encargado de Logística
        rol_menu = menu_bar.addMenu("Rol")

        # Acción para abrir la ventana del Gerente
        gerente_action = rol_menu.addAction("Gerente")
        gerente_action.triggered.connect(self.open_gerente_window)

        # Acción para abrir la ventana del Ejecutivo de Viaje
        ejecutivo_action = rol_menu.addAction("Ejecutivo de Viaje")
        ejecutivo_action.triggered.connect(self.open_ejecutivo_window)

        # Acción para abrir la ventana del Encargado de Logística
        logistica_action = rol_menu.addAction("Encargado de Logística")
        logistica_action.triggered.connect(self.open_logistica_window)

        # Crear la ventana de inicio de sesión
        self.login_widget = QWidget()
        self.login_layout = QVBoxLayout()
        self.login_widget.setLayout(self.login_layout)

        # Campo de entrada de usuario
        self.username_input = QLineEdit()
        self.login_layout.addWidget(QLabel("Usuario:"))
        self.login_layout.addWidget(self.username_input)

        # Campo de entrada de contraseña
        self.password_input = QLineEdit()
        self.password_input.setEchoMode(QLineEdit.EchoMode.Password)
        self.login_layout.addWidget(QLabel("Contraseña:"))
        self.login_layout.addWidget(self.password_input)

        # Botón de inicio de sesión
        self.login_button = QPushButton("Iniciar Sesión")
        self.login_button.clicked.connect(self.login)
        self.login_layout.addWidget(self.login_button)

        # Botón de registro
        self.register_button = QPushButton("Registrarse")
        self.register_button.clicked.connect(self.open_registro_window)
        self.login_layout.addWidget(self.register_button)

        self.setCentralWidget(self.login_widget)

    def login(self):
        excel = os.path.join(os.getcwd(), "registro_de_cuentas.csv")
        username = self.username_input.text()
        password = self.password_input.text()

        if self.login_window is not None:
            self.login_window.close()

        # Verificar si el usuario y contraseña coinciden con los registros
        with open(excel, newline='') as cuentas:
            fielnames = ['logistica','abcd']
            reader = csv.DictReader(cuentas,fielnames)
            for row in reader:
                if username == row['logistica'] and password == row['abcd']:
                    print("Inicio de sesión exitoso")
                    self.open_logistica_window()
                    break
            else:
                error_dialog = QMessageBox()
                error_dialog.setIcon(QMessageBox.Icon.Critical)
                error_dialog.setWindowTitle("Error de inicio de sesión")
                error_dialog.setText("Usuario o contraseña incorrectos.")
                print("Inicio de sesión fallido")
                error_dialog.exec()

    def open_gerente_window(self):
        self.gerente_window = GerenteWindow()
        self.gerente_window.show()

    def open_ejecutivo_window(self):
        self.ejecutivo_window = EjecutivoWindow()
        self.ejecutivo_window.show()

    def open_logistica_window(self):
        self.logistica_window = LogisticaWindow()
        self.logistica_window.show()

    def open_registro_window(self):
        self.login_widget.close()
        self.registro_window = RegistroWindow(self)
        self.registro_window.show()
        self.login_window = self.registro_window

    def open_login_window(self):
        self.login_widget.setVisible(True)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = TurnosApp()
    window.show()
    sys.exit(app.exec())