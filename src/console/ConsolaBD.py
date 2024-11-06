#src/console/ConsolaBD.py
import sys
sys.path.append("src")
from logic.payroll_calculator import Usuario
from controller.controlador_usuarios import Insertar, Actualizar, Borrar, BuscarPorCedula, CrearTabla

# Variable global para rastrear si la tabla ya fue creada
tabla_creada = False

def mostrar_menu():
    print("\n===== Menú de Operaciones de Usuarios =====")
    if not tabla_creada:  # Mostrar la opción de crear tabla solo si no ha sido creada
        print("1. Crear tabla de usuarios")
    print("2. Insertar un nuevo usuario")
    print("3. Actualizar un usuario existente")
    print("4. Borrar un usuario")
    print("5. Buscar usuario por cédula")
    print("6. Salir")
    opcion = input("\nSelecciona una opción: ")
    return opcion

def pedir_datos_usuario():
    """ Solicita los datos del usuario para crear o actualizar """
    cedula = input("Cédula: ")
    nombre = input("Nombre: ")
    salario = float(input("Salario: "))
    dias_trabajados = int(input("Días trabajados: "))
    horas_trabajadas = int(input("Horas trabajadas: "))
    comisiones = float(input("Comisiones: "))
    horas_extras = int(input("Horas extras: "))

    return Usuario(nombre, cedula, salario, dias_trabajados, horas_trabajadas, comisiones, horas_extras)

def main():
    global tabla_creada  # Declarar como global para modificarla
    while True:
        opcion = mostrar_menu()

        if opcion == "1" and not tabla_creada:
            # Crear tabla de usuarios
            print("\n--- Crear la tabla de usuarios ---")
            try:
                CrearTabla()
                tabla_creada = True  # Cambia el estado a True
                print("Tabla de usuarios creada exitosamente.")
            except Exception as e:
                print(f"Error al crear la tabla: {e}")

        elif opcion == "2":
            # Insertar nuevo usuario
            print("\n--- Insertar un nuevo usuario ---")
            usuario = pedir_datos_usuario()
            try:
                Insertar(usuario)
                print(f"Usuario con cédula {usuario.cedula} insertado exitosamente.")
            except Exception as e:
                print(f"Error al insertar usuario: {e}")
        
        elif opcion == "3":
            # Actualizar usuario
            print("\n--- Actualizar un usuario existente ---")
            usuario = pedir_datos_usuario()
            try:
                Actualizar(usuario)
                print(f"Usuario con cédula {usuario.cedula} actualizado exitosamente.")
            except Exception as e:
                print(f"Error al actualizar usuario: {e}")

        elif opcion == "4":
            # Borrar usuario
            print("\n--- Borrar un usuario ---")
            cedula = input("Ingresa la cédula del usuario a borrar: ")
            try:
                Borrar(cedula)
                print(f"Usuario con cédula {cedula} borrado exitosamente.")
            except Exception as e:
                print(f"Error al borrar usuario: {e}")

        elif opcion == "5":
            # Buscar usuario por cédula
            print("\n--- Buscar un usuario por cédula ---")
            cedula = input("Ingresa la cédula del usuario: ")
            try:
                resultado = BuscarPorCedula(cedula)
                print(f"Resultado: {resultado}")
            except Exception as e:
                print(f"Error al buscar usuario: {e}")
        
        elif opcion == "6":
            print("Saliendo del sistema...")
            break

        else:
            print("Opción no válida. Intenta de nuevo.")

if __name__ == "__main__":
    main()
