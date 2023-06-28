import sys
import csv
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget, QLineEdit, QPushButton, QTableWidgetItem, QTableWidget, QDateEdit, QComboBox

# PARA INGRESAR A LA INTERFAZ DE LA LOGISTICA INGRESAR USERNAME: logistica CONTRASEÑA: abcd
# EL PROGRAMA YA PERMITE GUARDAR LOS DATOS INGRESADOS POR LOGISTICA EN UN .CSV LLAMADO TURNOS
# QUE SE GENERA UNA VEZ PRESIONADO EL BOTON "AGREGAR TURNO"




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
        self.plan_combo = QComboBox()
        self.plan_combo.addItems(["Excursión Light", "Excursión Plus", "Excursión Heavy"])
        self.turno_combo = QComboBox()
        self.turno_combo.addItems(["Mañana", "Tarde"])

        # Botón para agregar un turno
        self.agregar_button = QPushButton("Agregar Turno")
        self.agregar_button.clicked.connect(self.agregar_turno)

        # Agregar los campos y botón a la interfaz
        self.layout.addWidget(QLabel("Nombre del Excursionista:"))
        self.layout.addWidget(self.nombre_input)
        self.layout.addWidget(QLabel("RUT de la Persona:"))
        self.layout.addWidget(self.rut_input)
        self.layout.addWidget(QLabel("Fecha:"))
        self.layout.addWidget(self.fecha_input)
        self.layout.addWidget(QLabel("Tipo de Plan:"))
        self.layout.addWidget(self.plan_combo)
        self.layout.addWidget(QLabel("Turno:"))
        self.layout.addWidget(self.turno_combo)
        self.layout.addWidget(self.agregar_button)

    def agregar_turno(self):
        # Obtener los datos ingresados en los campos de entrada
        nombre = self.nombre_input.text()
        rut = self.rut_input.text()
        fecha = self.fecha_input.date().toString("dd/MM/yyyy")
        plan = self.plan_combo.currentText()
        turno = self.turno_combo.currentText()

        # Insertar los datos en la tabla de turnos
        row_count = self.guia_table.rowCount()
        self.guia_table.insertRow(row_count)
        self.guia_table.setItem(row_count, 0, QTableWidgetItem(nombre))
        self.guia_table.setItem(row_count, 1, QTableWidgetItem(rut))
        self.guia_table.setItem(row_count, 2, QTableWidgetItem(fecha))
        self.guia_table.setItem(row_count, 3, QTableWidgetItem(plan))
        self.guia_table.setItem(row_count, 4, QTableWidgetItem(turno))

        # Limpiar los campos de entrada
        self.nombre_input.clear()
        self.rut_input.clear()

        # Guardar los turnos en un archivo CSV
        self.guardar_turnos_csv()

    def guardar_turnos_csv(self):
        turnos = []

        # Obtener los datos de la tabla de turnos
        for row in range(self.guia_table.rowCount()):
            nombre = self.guia_table.item(row, 0).text()
            rut = self.guia_table.item(row, 1).text()
            fecha = self.guia_table.item(row, 2).text()
            plan = self.guia_table.item(row, 3).text()
            turno = self.guia_table.item(row, 4).text()

            turno_data = [nombre, rut, fecha, plan, turno]
            turnos.append(turno_data)

        # Guardar los turnos en un archivo CSV
        with open("turnos.csv", "w", newline="") as csvfile:
            writer = csv.writer(csvfile)
            writer.writerows(turnos)

# Clase principal de la aplicación
class TurnosApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Sistema de Turnos y Gestión de Personal")
        self.setGeometry(200, 200, 500, 500)

        # Widget de inicio de sesión
        self.login_widget = QWidget(self)
        self.setCentralWidget(self.login_widget)

        self.login_layout = QVBoxLayout()
        self.login_widget.setLayout(self.login_layout)

        self.username_input = QLineEdit()
        self.password_input = QLineEdit()
        self.password_input.setEchoMode(QLineEdit.Password)
        self.login_button = QPushButton("Iniciar sesión")
        self.login_button.clicked.connect(self.login)

        self.login_layout.addWidget(QLabel("Nombre de usuario:"))
        self.login_layout.addWidget(self.username_input)
        self.login_layout.addWidget(QLabel("Contraseña:"))
        self.login_layout.addWidget(self.password_input)
        self.login_layout.addWidget(self.login_button)

    def login(self):
        username = self.username_input.text()
        password = self.password_input.text()

        # Verificar el nombre de usuario y la contraseña para determinar el tipo de usuario
        if username == "gerente" and password == "1234":
            self.gerente_window = GerenteWindow()
            self.setCentralWidget(self.gerente_window)
        elif username == "ejecutivo" and password == "5678":
            self.ejecutivo_window = EjecutivoWindow()
            self.setCentralWidget(self.ejecutivo_window)
        elif username == "logistica" and password == "abcd":
            self.logistica_window = LogisticaWindow()
            self.setCentralWidget(self.logistica_window)
        else:
            # Mostrar un mensaje de error si el nombre de usuario o la contraseña son incorrectos
            error_label = QLabel("Error: Nombre de usuario o contraseña incorrectos")
            self.login_layout.addWidget(error_label)

        self.username_input.clear()
        self.password_input.clear()


if __name__ == "__main__":
    app = QApplication(sys.argv)

    turnos_app = TurnosApp()
    turnos_app.show()

    sys.exit(app.exec_())
