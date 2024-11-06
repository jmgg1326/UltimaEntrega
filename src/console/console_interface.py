#src/console/console_interface.py

import sys 
sys.path.append("src")

from logic.payroll_calculator import *

def get_user_input():
    name = input("Ingrese su nombre: ")
    salary = float(input("Ingrese su sueldo: "))
    days_worked = int(input("Ingrese los días trabajados: "))
    hours_worked = int(input("Ingrese las horas trabajadas por día: "))
    commissions = float(input("Ingrese las comisiones totales ganadas: "))
    overtime_hours = int(input("Ingrese las horas extras trabajadas: "))

    return name, salary, days_worked, hours_worked, commissions, overtime_hours

def display_payroll_info(name, payroll_info):
    print(f"\nHola {name}, aquí está la información de tu nómina:")
    print(f"Total Devengado: {payroll_info['total_earned']:.2f}")
    print(f"Deducciones por Salud: {payroll_info['health_deductions']:.2f}")
    print(f"Deducciones por Pensión: {payroll_info['pension_deductions']:.2f}")
    print(f"Total Deducido: {payroll_info['total_deductions']:.2f}")
    print(f"Nómina Final: {payroll_info['final_payroll']:.2f}")

def main():
    try:
        # Obtener los datos del usuario
        name, salary, days_worked, hours_worked, commissions, overtime_hours = get_user_input()

        # Crear instancia de PayrollCalculator sin pasar parámetros al __init__
        calculator_console = PayrollCalculator(
            salary=salary, 
            days_worked=days_worked, 
            hours_worked=hours_worked, 
            commissions=commissions, 
            overtime_hours=overtime_hours
        )
        
        # Realizar el cálculo de la nómina
        payroll_info = calculator_console.calculate_payroll()
        
        # Mostrar la información de la nómina
        display_payroll_info(name, payroll_info)

    except (InvalidSalaryError, InvalidDaysWorkedError, InvalidHoursWorkedError, NegativeCommissionError, NegativeOvertimeHoursError) as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
