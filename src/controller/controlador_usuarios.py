#src/controller/controlador_usuarios.py

import sys
sys.path.append("src")
from logic.payroll_calculator import Usuario
import psycopg2
import SecretConfig

class ErrorInsertar(Exception):
    pass

class ErrorActualizar(Exception):
    pass

class ErrorBuscar(Exception):
    pass

class ErrorBorrar(Exception):
    pass

def ObtenerCursor( ) :
    """
    Crea la conexion a la base de datos y retorna un cursor para ejecutar instrucciones
    """
    DATABASE = SecretConfig.PGDATABASE
    USER = SecretConfig.PGUSER
    PASSWORD = SecretConfig.PGPASSWORD
    HOST = SecretConfig.PGHOST
    PORT = SecretConfig.PGPORT
    connection = psycopg2.connect(database=DATABASE, user=USER, password=PASSWORD, host=HOST, port=PORT)
    return connection.cursor()

#Crear Tabla

def CrearTabla():
    """
    Crea la tabla de usuarios, en caso de que no exista
    """    
    sql = ""
    with open("sql/crear-usuarios.sql","r") as f:
        sql = f.read()

    cursor = ObtenerCursor()

    try:
        cursor.execute( sql )
        cursor.connection.commit()
    except:
        cursor.connection.rollback()

def BorrarFilas():
    """
    Borra todas las filas de la tabla (DELETE)
    ATENCION: EXTREMADAMENTE PELIGROSO.
    """
    sql = "Delete from usuarios"
    cursor = ObtenerCursor()
    cursor.execute( sql )
    cursor.connection.commit()

#Insertar datos en la BD

def Insertar( usuario : Usuario ):
    """ Guarda un Usuario en la base de datos """

    try:
        cursor = ObtenerCursor()
        if BuscarPorCedulaUsuarioExistente(usuario.cedula) is False:
            raise ErrorInsertar(f"Ya existe un registro asociado a la cedula = {usuario.cedula}")

        cursor.execute(f"""
        insert into usuarios (
            cedula, nombre,  salario,  dias_trabajados,  horas_trabajadas, comisiones, horas_extras)
        values 
        (
            '{usuario.cedula}',  '{usuario.nombre}', '{usuario.salary}', '{usuario.days_worked}', '{usuario.hours_worked}', '{usuario.commissions}', '{usuario.overtime_hours}'
        );
                        """)
        
        cursor.connection.commit()
    except:
        raise ErrorInsertar(f"No se pudo insertar el registro en la BD")
    
#Modificar Datos
    
def Actualizar(usuario: Usuario):
    """
    Actualiza los datos de un usuario en la base de datos.
    """
    try:
        cursor = ObtenerCursor()
        if BuscarPorCedulaUsuarioExistente(usuario.cedula) == True:
            raise ErrorActualizar
        cursor.execute(f"""
            update usuarios
            set 
                nombre='{usuario.nombre}',
                salario='{usuario.salary}',
                dias_trabajados='{usuario.days_worked}',
                horas_trabajadas='{usuario.hours_worked}',
                comisiones='{usuario.commissions}',
                horas_extras='{usuario.overtime_hours}'
            where cedula='{usuario.cedula}'
        """)
        cursor.connection.commit()
        cursor.connection.rollback()
    except:
        raise ErrorActualizar(f"Ya existe un registro asociado a la cedula = {usuario.cedula}")



#Delete
def Borrar(cedula: str):
    """ Elimina la fila que contiene a un usuario en la BD """
    try:    
        cursor = ObtenerCursor()
        sql = f"DELETE from usuarios where cedula = '{cedula}'"
        if BuscarPorCedulaUsuarioExistente(cedula) == True:
            raise ErrorBorrar
        cursor.execute(sql)
        cursor.connection.commit()
    except:
        raise ErrorBorrar(f"No se pudo borrar el registro asociado a la cedula = {cedula}")


#Consultar Datos 

def BuscarPorCedula(cedula: str):
    """ Busca un usuario por el número de Cedula """
    cursor = ObtenerCursor()
    cursor.execute(f"""
        SELECT cedula, nombre, salario, dias_trabajados, horas_trabajadas, comisiones, horas_extras 
        FROM usuarios 
        WHERE cedula = '{cedula}' """)
        
    fila = cursor.fetchone()
        
    if fila is None:
        raise ErrorBuscar(f"No se encontro registro asocaido a la cedula = {cedula}")
        
    return Usuario(fila[1],fila[0],fila[2],fila[3],fila[4],fila[5],fila[6])
    
def BuscarPorCedulaUsuarioExistente(cedula: str):
    """ Busca un usuario por el número de Cedula """
    cursor = ObtenerCursor()
    cursor.execute("""
        SELECT cedula, nombre, salario, dias_trabajados, horas_trabajadas, comisiones, horas_extras 
        FROM usuarios 
        WHERE cedula = %s
    """, (cedula,))
        
    fila = cursor.fetchone()
        
    if fila is None:
        return True
    else:
        return False