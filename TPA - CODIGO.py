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

        # Guardar los datos de registro en el archivo CSV
        with open("registro_de_cuentas.csv", "a") as file:
        with open("registro_de_cuentas.csv", "a", newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow([username, password])
class LogisticaWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Ventana del Encargado de Logística")
        self.resize(700, 600)
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        # Crear una tabla para mostrar los turnos de los guías
        self.guia_table = QTableWidget()
        self.guia_table.setColumnCount(5)
        self.guia_table.setHorizontalHeaderLabels(["Nombre", "RUT", "Fecha", "Plan", "Turno"])
        self.guia_table.setColumnCount(6)
        self.guia_table.setHorizontalHeaderLabels(["Nombre", "RUT", "Fecha", "Plan", "Turno",'Eliminar'])
        self.layout.addWidget(self.guia_table)

        # Campos de entrada de datos
def __init__(self):
        self.agregar_button.clicked.connect(self.agregar_turno)
        self.layout.addWidget(self.agregar_button)

        # Agregar los campos y botón a la interfaz
        self.layout.addWidget(QLabel("Nombre del Excursionista:"))
        self.layout.addWidget(self.nombre_input)
        self.layout.addWidget(QLabel("RUT de la Persona:"))
        self.layout.addWidget(self.rut_input)
        self.layout.addWidget(QLabel("Fecha:"))
        self.layout.addWidget(self.fecha_input)
        self.layout.addWidget(QLabel("Tipo de Plan:"))
        self.layout.addWidget(self.plan_input)
        self.layout.addWidget(QLabel("Turno:"))
        self.layout.addWidget(self.turno_input)
        self.layout.addWidget(self.agregar_button)

        # Cargar los turnos existentes desde el archivo CSV
        self.cargar_turnos()
        self.boton_eliminar()

    def cargar_turnos(self):
        self.guia_table.setRowCount(0)

        # Verificar si el archivo "registro_de_cuentas.csv" existe
        try:
            with open("registro_de_cuentas.csv", "r") as file:
            with open("turnos.csv", "r",newline='', encoding='utf-8') as file:
                reader = csv.reader(file)
                for row in reader:
                    self.guia_table.insertRow(self.guia_table.rowCount())
                    for i, item in enumerate(row):
                        self.guia_table.setItem(self.guia_table.rowCount() - 1, i, QTableWidgetItem(item))
        except FileNotFoundError:
            pass


    def boton_eliminar(self):
        i = 1
        with open('turnos.csv', newline='') as file:
            reader = csv.reader(file) 
            for row in reader:
                if row:
                    delete_button = QPushButton('Eliminar')
                    delete_button.clicked.connect(self.eliminar)
                    self.guia_table.setCellWidget(self.guia_table.rowCount() - i , 5, delete_button)
                i += 1

    def agregar_turno(self):
        nombre = self.nombre_input.text()
        rut = self.rut_input.text()
        fecha = self.fecha_input.date().toString(Qt.DateFormat.ISODate)
        plan = self.plan_input.currentText()
        turno = self.turno_input.currentText()
        boton_eliminar = QPushButton('Eliminar')
        boton_eliminar.clicked.connect(self.eliminar)

        if nombre != '' and rut != '':
            with open('turnos.csv', 'a', newline='', encoding='utf-8') as file:
                writer = csv.writer(file)
                writer.writerow([nombre,rut,fecha,plan,turno])
        else:
            error_dialog = QMessageBox()
            error_dialog.setIcon(QMessageBox.Icon.Critical)
            error_dialog.setWindowTitle("Error de datos ingresados")
            error_dialog.setText("Por favor rellenar los campos antes de añadir un nuevo turno. ")
            error_dialog.exec()

        self.guia_table.insertRow(self.guia_table.rowCount())
        self.guia_table.setItem(self.guia_table.rowCount() - 1, 0, QTableWidgetItem(nombre))
        self.guia_table.setItem(self.guia_table.rowCount() - 1, 1, QTableWidgetItem(rut))
        self.guia_table.setItem(self.guia_table.rowCount() - 1, 2, QTableWidgetItem(fecha))
        self.guia_table.setItem(self.guia_table.rowCount() - 1, 3, QTableWidgetItem(plan))
        self.guia_table.setItem(self.guia_table.rowCount() - 1, 4, QTableWidgetItem(turno))
        self.guia_table.setCellWidget(self.guia_table.rowCount() - 1, 5, boton_eliminar)

        self.nombre_input.clear()
        self.rut_input.clear() 

    def open_registro_window(self):
        self.registro_window = RegistroWindow()
        self.registro_window.show()

    def eliminar(self):
        button = self.sender()
        if button:
            row = self.guia_table.indexAt(button.pos()).row()
            product_name = self.guia_table.item(row, 0).text()
            with open('turnos.csv', "r", encoding='utf-8') as file:
                rows = list(csv.reader(file))

            with open('turnos.csv', "w", newline="", encoding='utf-8') as file:
                writer = csv.writer(file)
                for r in rows:
                    if len(r) > 0 and r[0] != product_name:  
                        writer.writerow(r)
            self.cargar_turnos()
            self.boton_eliminar()


# Ventana de inicio de sesión
class TurnosApp(QMainWindow):
    def login(self):
        with open('registro_de_cuentas.csv',newline='') as cuentas:
            reader = csv.DictReader(cuentas)
            for row in reader:
                print(row)
                if username == row['logistica'] and password == row['abcd']:
                    print("Inicio de sesión exitoso")
                    self.open_logistica_window()
                    self.close()
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