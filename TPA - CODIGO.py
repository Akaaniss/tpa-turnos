import sys
import csv
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget, QLineEdit, QPushButton, QTableWidgetItem, QTableWidget, QDateEdit, QComboBox, QMessageBox
from PyQt6.QtCore import Qt, QDate
import re

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

        self.eliminar_button = QPushButton("Eliminar Turno")
        self.eliminar_button.clicked.connect(self.eliminar_turno)
        self.layout.addWidget(self.eliminar_button)

        # Configurar la selección de elementos en la tabla
        self.guia_table.setSelectionBehavior(QTableWidget.SelectionBehavior.SelectRows)
        self.guia_table.setSelectionMode(QTableWidget.SelectionMode.ExtendedSelection)

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

    def cargar_turnos(self):
        self.guia_table.setRowCount(0)

        # Verificar si el archivo "turnos.csv" existe
        try:
            with open("turnos.csv", "r", encoding='latin-1') as file:
                reader = csv.reader(file)
                for row in reader:
                    self.guia_table.insertRow(self.guia_table.rowCount())
                    for i, item in enumerate(row):
                        self.guia_table.setItem(self.guia_table.rowCount() - 1, i, QTableWidgetItem(item))
        except FileNotFoundError:
            pass

    def agregar_turno(self):
        # Obtener el valor del campo de entrada de texto del nombre
        nombre = self.nombre_input.text()

        # Verificar si el campo de entrada de texto del nombre está vacío
        if nombre == '':
            error_dialog = QMessageBox()
            error_dialog.setIcon(QMessageBox.Icon.Critical)
            error_dialog.setWindowTitle("Error de datos ingresados")
            error_dialog.setText("Por favor, ingresa un nombre antes de añadir un nuevo turno.")
            error_dialog.exec()
            return

        rut = self.rut_input.text()
        fecha = self.fecha_input.date().toString(Qt.DateFormat.ISODate)
        plan = self.plan_input.currentText()
        turno = self.turno_input.currentText()

        while True:
            # Verificar si el RUT tiene el formato correcto
            if re.match(r'^(\d{1,2}\.)?\d{3}\.\d{3}-[0-9kK]$', rut):
                break
            else:
                error_dialog = QMessageBox()
                error_dialog.setIcon(QMessageBox.Icon.Critical)
                error_dialog.setWindowTitle("Error de datos ingresados")
                error_dialog.setText("El RUT ingresado es inválido. Por favor, inténtalo nuevamente.")
                error_dialog.exec()
                rut = self.rut_input.text()
                return

        # Formatear el RUT
        if len(rut) == 9:
            rut = f"{rut[0:2]}.{rut[2:5]}.{rut[5:8]}-{rut[8]}"
        elif len(rut) == 10:
            rut = f"{rut[0]}.{rut[1:4]}.{rut[4:7]}-{rut[7]}"
        else:
            # Aquí puedes manejar el caso si el RUT no tiene 8 o 9 cifras
            pass

        # Guardar los datos en el archivo CSV solo si el nombre y el RUT son válidos
        if nombre != '' and rut != '':
            with open('turnos.csv', 'a', newline='', encoding='utf-8') as file:
                writer = csv.writer(file)
                writer.writerow([nombre, rut, fecha, plan, turno])
        else:
            error_dialog = QMessageBox()
            error_dialog.setIcon(QMessageBox.Icon.Critical)
            error_dialog.setWindowTitle("Error de datos ingresados")
            error_dialog.setText("Por favor, rellena los campos antes de añadir un nuevo turno.")
            error_dialog.exec()
            return

        # Insertar una nueva fila en la tabla y mostrar los datos ingresados
        row_count = self.guia_table.rowCount()
        self.guia_table.insertRow(row_count)
        self.guia_table.setItem(row_count, 0, QTableWidgetItem(nombre))
        self.guia_table.setItem(row_count, 1, QTableWidgetItem(rut))
        self.guia_table.setItem(row_count, 2, QTableWidgetItem(fecha))
        self.guia_table.setItem(row_count, 3, QTableWidgetItem(plan))
        self.guia_table.setItem(row_count, 4, QTableWidgetItem(turno))

    def eliminar_turno(self):
        selected_items = self.guia_table.selectedItems()
        if selected_items:
            rows = set()
            for item in selected_items:
                rows.add(item.row())

            rows_to_keep = []
            with open('turnos.csv', 'r', newline='', encoding='latin-1') as file:
                reader = csv.reader(file)
                for i, row in enumerate(reader):
                    if i not in rows:
                        rows_to_keep.append(row)

            with open('turnos.csv', 'w', newline='', encoding='latin-1') as file:
                writer = csv.writer(file)
                writer.writerows(rows_to_keep)

            self.cargar_turnos()
        else:
            QMessageBox.warning(self, "Eliminar Turno", "Selecciona al menos un turno para eliminar")




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
        username = self.username_input.text()
        password = self.password_input.text()

        if self.login_window is not None:
            self.login_window.close()

        # Verificar si el usuario y contraseña coinciden con los registros
        with open('registro_de_cuentas.csv', newline='') as cuentas:
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
