import sys
import csv
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget, QLineEdit, QPushButton, QTableWidgetItem, QTableWidget, QDateEdit, QComboBox, QMessageBox,QDateTimeEdit
from PyQt6.QtCore import Qt

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

class TurnosApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("TurnosApp")
        self.setGeometry(200, 200, 500, 500)

        self.login_widget = QWidget()
        self.setCentralWidget(self.login_widget)
        self.login_layout = QVBoxLayout()
        self.login_widget.setLayout(self.login_layout)

        self.username_input = QLineEdit()
        self.password_input = QLineEdit()
        self.password_input.setEchoMode(QLineEdit.EchoMode.Password)
        self.birthdate_input = QDateEdit()
        self.occupation_input = QLineEdit()

        self.login_button = QPushButton("Iniciar sesión")
        self.register_button = QPushButton("Registrarse")
        self.back_button = QPushButton("Volver")

        self.login_button.clicked.connect(self.login)
        self.register_button.clicked.connect(self.register)
        self.back_button.clicked.connect(self.back)

        self.login_layout.addWidget(QLabel("Usuario:"))
        self.login_layout.addWidget(self.username_input)
        self.login_layout.addWidget(QLabel("Contraseña:"))
        self.login_layout.addWidget(self.password_input)
        self.login_layout.addWidget(QLabel("Fecha de Nacimiento:"))
        self.login_layout.addWidget(self.birthdate_input)
        self.login_layout.addWidget(QLabel("Ocupación:"))
        self.login_layout.addWidget(self.occupation_input)
        self.login_layout.addWidget(self.login_button)
        self.login_layout.addWidget(self.register_button)
        self.login_layout.addWidget(self.back_button)

        self.gerente_window = GerenteWindow()
        self.ejecutivo_window = EjecutivoWindow()
        self.logistica_window = LogisticaWindow()

    def login(self):
        username = self.username_input.text()
        password = self.password_input.text()

        if username == "gerente" and password == "gerente123":
            self.close()
            self.gerente_window.show()
        elif username == "ejecutivo" and password == "ejecutivo123":
            self.close()
            self.ejecutivo_window.show()
        elif username == "logistica" and password == "logistica123":
            self.close()
            self.logistica_window.show()
        else:
            error_dialog = QMessageBox()
            error_dialog.setIcon(QMessageBox.Icon.Critical)
            error_dialog.setWindowTitle("Error de inicio de sesión")
            error_dialog.setText("Usuario o contraseña incorrectos.")
            error_dialog.exec()

    def register(self):
        username = self.username_input.text()
        password = self.password_input.text()
        birthdate = self.birthdate_input.date().toString(Qt.DateFormat.ISODate)
        occupation = self.occupation_input.text()

        if len(password) > 8:
            error_dialog = QMessageBox()
            error_dialog.setIcon(QMessageBox.Icon.Critical)
            error_dialog.setWindowTitle("Error de registro")
            error_dialog.setText("La contraseña no puede tener más de 8 caracteres.")
            error_dialog.exec()
            return

        if username and password and birthdate and occupation:
            try:
                with open('registro_de_cuentas.csv', 'a', newline='', encoding='utf-8-sig') as file:
                    writer = csv.writer(file)
                    writer.writerow([username, password, birthdate, occupation])
            except OSError as e:
                error_dialog = QMessageBox()
                error_dialog.setIcon(QMessageBox.Icon.Critical)
                error_dialog.setWindowTitle("Error de registro")
                error_dialog.setText("Error al escribir en el archivo CSV.")
                error_dialog.exec()
                print(f"Error al escribir en el archivo CSV: {e}")
                return

            print("Registro exitoso")
            self.close()
            self.login_window.show()
        else:
            error_dialog = QMessageBox()
            error_dialog.setIcon(QMessageBox.Icon.Critical)
            error_dialog.setWindowTitle("Error de registro")
            error_dialog.setText("Por favor, ingresatodos los campos de registro.")
            error_dialog.exec()

    def back(self):
        self.username_input.clear()
        self.password_input.clear()
        self.birthdate_input.setDate(QDate.currentDate())
        self.occupation_input.clear()

# Función principal
def main():
    app = QApplication(sys.argv)
    window = TurnosApp()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
