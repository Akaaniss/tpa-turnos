import csv
import re
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QTableWidget, QLineEdit, QPushButton, QTableWidgetItem, QDateEdit, QComboBox, QMessageBox
from PyQt6.QtCore import Qt, QDate

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
