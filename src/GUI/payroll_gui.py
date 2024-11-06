from kivy.app import App

from kivy.uix.label import Label 
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.popup import Popup
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window

import sys 
sys.path.append("src")

from logic.payroll_calculator import *
class PayrollApp(App):
    def build(self):
        # Fondo claro para la ventana principal 
        Window.clearcolor = (0.9,0.9,0.9,1)
        container = GridLayout(rows = 6, cols = 2, padding = 20, spacing = 20)

        # Label salary y text input salary
        container.add_widget(Label(text="Ingrese su salario:", font_size=20, color=(0, 0, 0, 1)))
        self.salary = TextInput(font_size = 20, multiline = False, input_filter = 'float')
        container.add_widget(self.salary)

        # Label días trabajados y text input días trabajados 
        container.add_widget(Label(text="Ingrese los días trabajados totales:", font_size=20, color=(0, 0, 0, 1)))
        self.days_worked = TextInput(font_size = 20, multiline=False, input_filter='int')
        container.add_widget(self.days_worked)

        # Label horas trabajadas por día y text input horas trabajadas 
        container.add_widget(Label(text="Ingrese las horas trabajadas por día:", font_size=20, color=(0, 0, 0, 1)))
        self.hours_worked = TextInput(font_size = 20, multiline=False, input_filter='int')
        container.add_widget(self.hours_worked)

        # Label comisiones totales y text input comisiones 
        container.add_widget(Label(text="Ingrese las comisiones totales:", font_size=20, color=(0, 0, 0, 1)))
        self.comissions = TextInput(font_size = 20, multiline=False, input_filter='float')
        container.add_widget(self.comissions)

        # Label horas extras totales y text input horas extras 
        container.add_widget(Label(text="Ingrese las horas extras totales:", font_size=20, color=(0, 0, 0, 1)))
        self.overtime_hours = TextInput(font_size = 20, multiline=False, input_filter='float')    
        container.add_widget(self.overtime_hours)

        # Boton 
        calculate = Button(text = "Calcular", font_size = 24, background_color=(0.2, 0.6, 0.8, 1), color=(1, 1, 1, 1))
        container.add_widget(calculate)

        # Resultado 
        self.result = Label(text="Resultado: ", font_size=20, color=(0, 0, 0, 1))
        container.add_widget(self.result)

        # Conectar el evento on_press
        calculate.bind(on_press=self.calc_payroll)

        return container
    

    def calc_payroll(self, value):
            try:
                # Validamos los inputs antes de realizar el cálculo
                self.validate()

                # Crear instancia de PayrollCalculator
                calculator = PayrollCalculator(
                    salary=float(self.salary.text),
                    days_worked=int(self.days_worked.text),
                    hours_worked=int(self.hours_worked.text),
                    commissions=float(self.comissions.text),
                    overtime_hours=int(self.overtime_hours.text)
                )

                # Realizamos el cálculo de la nómina
                payroll_data = calculator.calculate_payroll()

                # Mostramos el resultado
                self.result.text = f"Resultado: {round(payroll_data['final_payroll'], 2)}"

            except ValueError:
                self.result.text = "El valor ingresado no es un número valido. Ingrese un número correcto, por ejemplo 5000000"

            except Exception as err:
                self.show_error(err)

    def show_error(self, err):
        """ 
        Abre una ventana emergente, con un texto y un botón para cerrar 
        Parámetros: 
        err: Mensaje de error que queremos mostrar en la ventana        
        """
        # Contenedor para el popup
        box = BoxLayout(orientation="vertical", padding=10, spacing=10)

        # Mensaje de error 
        error_label = Label(text=str(err), font_size=18, color=(1,0,0,1))
        box.add_widget(error_label)

        # Boton para cerrar el popup 
        close_button = Button(text="Cerrar", size_hint=(1,0.5), background_color=(0.8,0.1,0.1,1), color=(1,1,1,1))
        box.add_widget(close_button)

        # Crear el popup 
        popup = Popup(title="Error", content=box, size_hint=(0.8,0.4), auto_dismiss=False)
        close_button.bind(on_press = popup.dismiss)

        # Mostrar el popup 
        popup.open()


    def validate(self):
        """
        Verifica que todos los datos ingresados por el usuario sean correctos
        """
        # Validar el salario
        try:
            salary = float(self.salary.text)
            if salary <= 0:
                raise InvalidSalaryError("El salario debe ser un número mayor que cero.")
        except ValueError:
            raise InvalidSalaryError("El salario debe ser un número valido.")
        
        # Validar los días trabajados
        try:
            days_worked = int(self.days_worked.text)
            if days_worked <= 0 or days_worked > 31:
                raise InvalidDaysWorkedError("Los días trabajados deben estar entre 1 y 31.")
        except ValueError:
            raise InvalidDaysWorkedError("Los días trabajados deben ser un número entero.")

        # Validar las horas trabajadas
        try:
            hours_worked = int(self.hours_worked.text)
            if hours_worked <= 0 or hours_worked > 24:
                raise InvalidHoursWorkedError("Las horas trabajadas deben estar entre 1 y 24.")
        except ValueError:
            raise InvalidHoursWorkedError("Las horas trabajadas deben ser un número entero.")

        # Validar las comisiones
        try:
            commissions = float(self.comissions.text)
            if commissions < 0:
                raise NegativeCommissionError("Las comisiones no pueden ser un valor negativo.")
        except ValueError:
            raise NegativeCommissionError("Las comisiones deben ser un número válido.")

        # Validar las horas extras
        try:
            overtime_hours = int(self.overtime_hours.text)
            if overtime_hours < 0:
                raise NegativeOvertimeHoursError("Las horas extras no pueden ser un valor negativo.")
        except ValueError:
            raise NegativeOvertimeHoursError("Las horas extras deben ser un número entero.")


if __name__ == "__main__":
    PayrollApp().run()