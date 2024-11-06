import sys
sys.path.append("src")
import unittest
from controller import controlador_usuarios as Controlador


class TestControladorUsuarios(unittest.TestCase):
    """
        Pruebas a la clase Controlador de la app
    """

    def setUpClass():
        """ Se ejecuta al inicio de todas las pruebas """
        print("Invocando setUpClass")
        Controlador.CrearTabla()  # Asegura que al inicio de las pruebas, la tabla este creada

    def setUp(self):
        """ Se ejecuta siempre antes de cada metodo de prueba """
        print("Invocando setUp")
        Controlador.BorrarFilas() # Asegura que antes de cada metodo de prueba, se borren todos los datos de la tabla

    def tearDown(self):
        """ Se ejecuta al final de cada test """
        print("Invocando tearDown")

    def tearDownClass():
        """ Se ejecuta al final de todos los tests """
        print("Invocando tearDownClass")
    
    #Test Insertar

    def testInsert(self):
        """ Verifica que funcione bien la creacion y la busqueda de un usuario """
        # Pedimos crear un usuario
        print("Ejecutando testInsert")

        Usuario_prueba = Controlador.Usuario("Juan", "1038262560", 1300000, 30, 270, 0, 0)

        Controlador.Insertar(Usuario_prueba)

        usuario_buscado = Controlador.BuscarPorCedula(Usuario_prueba.cedula)

        self.assertEqual(str(Usuario_prueba.nombre), usuario_buscado.nombre)
        self.assertEqual(str(Usuario_prueba.cedula), usuario_buscado.cedula)
        self.assertEqual(str(Usuario_prueba.salary), usuario_buscado.salary)
        self.assertEqual(str(Usuario_prueba.days_worked), usuario_buscado.days_worked)
        self.assertEqual(str(Usuario_prueba.hours_worked), usuario_buscado.hours_worked)
        self.assertEqual(str(Usuario_prueba.commissions), usuario_buscado.commissions)
        self.assertEqual(str(Usuario_prueba.overtime_hours), usuario_buscado.overtime_hours)

    #Test insert Invalido 2 Usuarios con la misma primary key
    def testInsertFail(self):
        """ Verifica que funcione bien la creacion y la busqueda de un usuario """
        # Pedimos crear un usuario
        print("Ejecutando testInsert")
        Usuario_prueba = Controlador.Usuario("Juan", "1038262560", 1300000, 30, 270, 0, 0)
        usuario_prueba2 = Controlador.Usuario("Julian", "1038262560", 1600000, 50, 270, 0, 34)

        Controlador.Insertar(Usuario_prueba)
        with self.assertRaises(Controlador.ErrorInsertar):
            Controlador.Insertar(usuario_prueba2)

    #Test buscar
    def testBuscar(self):
        """
            Verificamos si funciona la funcion buscar
        """
        Usuario_prueba = Controlador.Usuario("Juan", "1038262560", 1300000, 30, 270, 0, 0)
        Controlador.Insertar(Usuario_prueba)

        usuario_buscado = Controlador.BuscarPorCedula(Usuario_prueba.cedula)

        self.assertEqual(str(Usuario_prueba.nombre), usuario_buscado.nombre)
        self.assertEqual(str(Usuario_prueba.cedula), usuario_buscado.cedula)
        self.assertEqual(str(Usuario_prueba.salary), usuario_buscado.salary)
        self.assertEqual(str(Usuario_prueba.days_worked), usuario_buscado.days_worked)
        self.assertEqual(str(Usuario_prueba.hours_worked), usuario_buscado.hours_worked)
        self.assertEqual(str(Usuario_prueba.commissions), usuario_buscado.commissions)
        self.assertEqual(str(Usuario_prueba.overtime_hours), usuario_buscado.overtime_hours)

    def testBuscarFail(self):
        """
            Verificamos que funciona la excepcion de Buscar
        """

        usuario_prueba = Controlador.Usuario("Juan", "1038262560", 1300000, 30, 270, 0, 0)
        cedula_error = "102301203498123"
        Controlador.Insertar(usuario_prueba)

        with self.assertRaises(Controlador.ErrorBuscar):
            Controlador.BuscarPorCedula(cedula_error)


    #Test Update
    def testUpdate(self):
        """
            Verifica la funcionalidad de actualizar
        """
        print("Ejecutando testUpdate")

        usuario_prueba = Controlador.Usuario("Juan", "1038262560", 1300000, 30, 270, 0, 0)

        Controlador.Insertar(usuario_prueba)

        usuario_prueba.nombre = "Juan Diego"
        usuario_prueba.salary = 2000000
        usuario_prueba.days_worked = 45
        usuario_prueba.hours_worked = 450
        usuario_prueba.commissions = 0
        usuario_prueba.overtime_hours = 40

        Controlador.Actualizar(usuario_prueba)

        usuario_actualizado = Controlador.BuscarPorCedula(usuario_prueba.cedula)

        self.assertEqual(str(usuario_prueba.nombre), usuario_actualizado.nombre)
        self.assertEqual(str(usuario_prueba.cedula), usuario_actualizado.cedula)
        self.assertEqual(str(usuario_prueba.salary), usuario_actualizado.salary)
        self.assertEqual(str(usuario_prueba.days_worked), usuario_actualizado.days_worked)
        self.assertEqual(str(usuario_prueba.hours_worked), usuario_actualizado.hours_worked)
        self.assertEqual(str(usuario_prueba.commissions), usuario_actualizado.commissions)
        self.assertEqual(str(usuario_prueba.overtime_hours), usuario_actualizado.overtime_hours)

    #Test Update Error No encuentra usuario para actualizar
    def testUpdateFail(self):
        """
            Verifica la funcionalidad la excepcion de actualizar
        """
        print("Ejecutando testUpdate")

        usuario_prueba = Controlador.Usuario("Juan", "1038262560", 1300000, 30, 270, 0, 0)
        usuario_prueba2 = Controlador.Usuario("Juan Diego", "1040", 2000000, 20, 250, 0 , 10 )

        Controlador.Insertar(usuario_prueba)
        with self.assertRaises(Controlador.ErrorActualizar):
            Controlador.Actualizar(usuario_prueba2)
            

   #Test Delete
    def testDelete(self):
        """ Prueba la funcionalidad de borrar usuarios """
        print("Ejecutando testDelete")

        usuario_prueba = Controlador.Usuario("Juan", "1038262560", 1300000, 30, 270, 0, 0)
        Controlador.Insertar( usuario_prueba )

        Controlador.Borrar( usuario_prueba.cedula)

        with self.assertRaises(Controlador.ErrorBuscar):
            Controlador.BuscarPorCedula(usuario_prueba.cedula)

    def testDeleteFail(self):
        """ Prueba la funcionalidad de borrar usuarios """
        print("Ejecutando testDelete")
        # 1. Crear el usuario e insertarlo
        usuario_prueba = Controlador.Usuario("Juan", "1038262560", 1300000, 30, 270, 0, 0)
        Controlador.Insertar( usuario_prueba )
        cedula_error = "123123432"

        with self.assertRaises(Controlador.ErrorBorrar):
            Controlador.Borrar(cedula_error)

if __name__ == '__main__':
    unittest.main()