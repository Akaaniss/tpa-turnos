import sys
import csv
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget, QLineEdit, QPushButton, QTableWidgetItem, QTableWidget, QDateEdit, QComboBox, QMessageBox
from PyQt6.QtCore import Qt, QDate


# Ventana de Registro
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

# Ventana del Gerente
class GerenteWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Ventana del Gerente")
        self.layout = QVBoxLayout()
        self.layout.addWidget(QLabel("¡Bienvenido, Gerente!"))
        self.setLayout(self.layout)

# Ventana del Ejecutivo de Viaje
class EjecutivoWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Ventana del Ejecutivo de Viaje")
        self.layout = QVBoxLayout()
        self.layout.addWidget(QLabel("¡Bienvenido, Ejecutivo de Viaje!"))
        self.setLayout(self.layout)

# Ventana del Encargado de Logística
class LogisticaWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Ventana del Encargado de Logística")
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        # Crear una tabla para mostrar los turnos de los guías
        self.guia_table = QTableWidget()
        self.guia_table.setColumnCount(5)
        self.guia_table.setHorizontalHeaderLabels(["Nombre", "RUT", "Fecha", "Plan", "Turno"])
        self.layout.addWidget(self.guia_table)

        # Campos de entrada de datos
        self.nombre_input = QLineEdit()
        self.rut_input = QLineEdit()
        self.fecha_input = QDateEdit()
        self.fecha_input.setDate(QDate.currentDate())
        self.plan_input = QComboBox()
        self.plan_input.addItems(["Plan A", "Plan B", "Plan C"])
        self.turno_input = QComboBox()
        self.turno_input.addItems(["Mañana", "Tarde"])

        # Botón para agregar un turno
        self.agregar_button = QPushButton("Agregar Turno")
        self.agregar_button.clicked.connect(self.agregar_turno)
        self.layout.addWidget(self.agregar_button)

        # Cargar los turnos existentes desde el archivo CSV
        self.cargar_turnos()

    def cargar_turnos(self):
        self.guia_table.setRowCount(0)

        # Verificar si el archivo "registro_de_cuentas.csv" existe
        try:
            with open("registro_de_cuentas.csv", "r") as file:
                reader = csv.reader(file)
                for row in reader:
                    self.guia_table.insertRow(self.guia_table.rowCount())
                    for i, item in enumerate(row):
                        self.guia_table.setItem(self.guia_table.rowCount() - 1, i, QTableWidgetItem(item))
        except FileNotFoundError:
            pass

    def agregar_turno(self):
        nombre = self.nombre_input.text()
        rut = self.rut_input.text()
        fecha = self.fecha_input.date().toString(Qt.DateFormat.ISODate)
        plan = self.plan_input.currentText()
        turno = self.turno_input.currentText()

        self.guia_table.insertRow(self.guia_table.rowCount())
        self.guia_table.setItem(self.guia_table.rowCount() - 1, 0, QTableWidgetItem(nombre))
        self.guia_table.setItem(self.guia_table.rowCount() - 1, 1, QTableWidgetItem(rut))
        self.guia_table.setItem(self.guia_table.rowCount() - 1, 2, QTableWidgetItem(fecha))
        self.guia_table.setItem(self.guia_table.rowCount() - 1, 3, QTableWidgetItem(plan))
        self.guia_table.setItem(self.guia_table.rowCount() - 1, 4, QTableWidgetItem(turno))

    def open_registro_window(self):
        self.registro_window = RegistroWindow()
        self.registro_window.show()


>>>>>>> parent of 1f6cd6b (update turnos)
# Ventana de inicio de sesión
class TurnosApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Turnos App")
        self.resize(800, 600)

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
        username = self.username_input.text()
        password = self.password_input.text()

        # Verificar si el usuario y contraseña coinciden con los registros
        with open('registro_de_cuentas.csv',newline='') as cuentas:
            reader = csv.DictReader(cuentas)
            for row in reader:
                print(row)
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
        self.registro_window = RegistroWindow()
        self.registro_window.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = TurnosApp()
    window.show()
    sys.exit(app.exec())
