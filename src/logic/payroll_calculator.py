class PayrollException(Exception):
    """Base class for payroll exceptions"""
    pass

class InvalidSalaryError(PayrollException):
    """Raised when the salary is less than or equal to zero"""
    pass

class InvalidDaysWorkedError(PayrollException):
    """Raised when the days worked are out of the valid range"""
    pass

class InvalidHoursWorkedError(PayrollException):
    """Raised when the hours worked are out of the valid range"""
    pass

class NegativeCommissionError(PayrollException):
    """Raised when the commissions are negative"""
    pass

class NegativeOvertimeHoursError(PayrollException):
    """Raised when the overtime hours are negative"""
    pass

class Usuario:
    def __init__(self, nombre: str, cedula: str, salary: float, days_worked: int, hours_worked: int, commissions: float, overtime_hours: int):
        self.nombre = nombre
        self.cedula = cedula
        self.salary = salary
        self.days_worked = days_worked
        self.hours_worked = hours_worked
        self.commissions = commissions
        self.overtime_hours = overtime_hours

class PayrollCalculator:

    #Definicion de constantes
    DAYS_IN_MONTH = 30
    HOURS_IN_MONTH = 240
    OVERTIME_MULTIPLIER = 1.25
    HEALTH_DEDUCTION_PERCENTAGE = 0.04
    PENSION_DEDUCTION_PERCENTAGE = 0.04 

    def __init__(self, usuario: Usuario):
        self.usuario = usuario
        self.final_payroll = None  # Variable de instancia para almacenar el resultado final

    def validate_inputs(self):
        if self.salary <= 0:
            raise InvalidSalaryError("El sueldo debe ser mayor que 0")
        if self.days_worked <= 0 or self.usuario.days_worked > PayrollCalculator.DAYS_IN_MONTH:
            raise InvalidDaysWorkedError(f"Los días trabajados deben estar entre 1 y {PayrollCalculator.DAYS_IN_MONTH}")
        if self.hours_worked < 0 or self.usuario.hours_worked > 24:
            raise InvalidHoursWorkedError("Las horas trabajadas deben estar entre 0 y 24")
        if self.usuario.commissions < 0:
            raise NegativeCommissionError("Las comisiones no pueden ser negativas")
        if self.usuario.overtime_hours < 0:
            raise NegativeOvertimeHoursError("Las horas extras no pueden ser negativas")

    def calculate_daily_payment(self):
        return self.usuario.salary / PayrollCalculator.DAYS_IN_MONTH

    def calculate_hourly_payment(self):
        return self.usuario.salary / PayrollCalculator.HOURS_IN_MONTH  # Usamos la constante para horas mensuales

    def calculate_overtime_payment(self, hourly_payment):
        return hourly_payment * self.usuario.overtime_hours * PayrollCalculator.OVERTIME_MULTIPLIER  # Usamos la constante para el multiplicador de horas extras

    def calculate_health_deductions(self, total_earned):
        return total_earned * PayrollCalculator.HEALTH_DEDUCTION_PERCENTAGE  # Deducción por salud

    def calculate_pension_deductions(self, total_earned):
        return total_earned * PayrollCalculator.PENSION_DEDUCTION_PERCENTAGE  # Deducción por pensión

    def calculate_payroll(self):
    # Validar las entradas del usuario antes de realizar cálculos
        self.validate_inputs()

    # Calcular los pagos
        daily_payment = self.calculate_daily_payment()  # Pago diario
        hourly_payment = self.calculate_hourly_payment()  # Pago por hora
        overtime_payment = self.calculate_overtime_payment(hourly_payment)  # Pago por horas extras

    # Calcular el total ganado
        total_earned = (daily_payment * self.usuario.days_worked) + self.usuario.commissions + overtime_payment

    # Calcular deducciones
        health_deductions = self.calculate_health_deductions(total_earned)  # Deducciones de salud
        pension_deductions = self.calculate_pension_deductions(total_earned)  # Deducciones de pensión

    # Calcular el total de deducciones
        total_deductions = health_deductions + pension_deductions

    # Calcular la nómina final
        self.final_payroll = total_earned - total_deductions

    # Retornar un diccionario con todos los resultados
        return {
        "total_earned": total_earned,
        "health_deductions": health_deductions,
        "pension_deductions": pension_deductions,
        "total_deductions": total_deductions,
        "final_payroll": self.final_payroll
    }

