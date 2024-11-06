# test_app.py

import unittest
import sys
import os

# Agrega el directorio que contiene app.py al sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '.')))
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)
from app import app
from controller.controlador_usuarios import Borrar

class TestFlaskApp(unittest.TestCase):

    def setUp(self):
        # Configuración antes de cada prueba
        self.app = app.test_client()
        self.app.testing = True

    def tearDown(self):
        # Se ejecuta después de cada prueba
        pass

    def test_index_page(self):
        # Prueba que la página de inicio carga correctamente
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Men\xc3\xba de Operaciones de Usuarios', response.data)

    def test_crear_tabla(self):
        # Prueba la creación de la tabla
        response = self.app.get('/crear_tabla')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Tabla de usuarios creada exitosamente.', response.data)

    def test_insertar_usuario(self):
        # Prueba insertar un usuario
        data = {
            'cedula': '9999999999',
            'nombre': 'Test User',
            'salario': '3000',
            'dias_trabajados': '20',
            'horas_trabajadas': '160',
            'comisiones': '500',
            'horas_extras': '10'
        }
        response = self.app.post('/insertar_usuario', data=data, follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Usuario con c\xc3\xa9dula 9999999999 insertado exitosamente.', response.data)

        # Limpieza
        Borrar('9999999999')

    def test_actualizar_usuario(self):
        # Prueba actualizar un usuario existente
        # Primero, insertar un usuario
        data_insert = {
            'cedula': '8888888888',
            'nombre': 'User to Update',
            'salario': '2800',
            'dias_trabajados': '18',
            'horas_trabajadas': '144',
            'comisiones': '400',
            'horas_extras': '5'
        }
        self.app.post('/insertar_usuario', data=data_insert, follow_redirects=True)

        # Ahora, actualizar el usuario
        data_update = {
            'cedula': '8888888888',
            'nombre': 'Updated User',
            'salario': '3000',
            'dias_trabajados': '20',
            'horas_trabajadas': '160',
            'comisiones': '600',
            'horas_extras': '8'
        }
        response = self.app.post('/actualizar_usuario', data=data_update, follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Usuario con c\xc3\xa9dula 8888888888 actualizado exitosamente.', response.data)

        # Limpieza
        Borrar('8888888888')

    def test_borrar_usuario(self):
        # Prueba borrar un usuario
        # Primero, insertar un usuario
        data_insert = {
            'cedula': '7777777777',
            'nombre': 'User to Delete',
            'salario': '3500',
            'dias_trabajados': '22',
            'horas_trabajadas': '176',
            'comisiones': '700',
            'horas_extras': '12'
        }
        self.app.post('/insertar_usuario', data=data_insert, follow_redirects=True)

        # Ahora, borrar el usuario
        data_delete = {
            'cedula': '7777777777'
        }
        response = self.app.post('/borrar_usuario', data=data_delete, follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Usuario con c\xc3\xa9dula 7777777777 borrado exitosamente.', response.data)

    def test_buscar_usuario(self):
        # Prueba buscar un usuario
        # Primero, insertar un usuario
        data_insert = {
            'cedula': '6666666666',
            'nombre': 'User to Search',
            'salario': '3200',
            'dias_trabajados': '19',
            'horas_trabajadas': '152',
            'comisiones': '500',
            'horas_extras': '6'
        }
        self.app.post('/insertar_usuario', data=data_insert, follow_redirects=True)

        # Ahora, buscar el usuario
        data_search = {
            'cedula': '6666666666'
        }
        response = self.app.post('/buscar_usuario', data=data_search, follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Informaci\xc3\xb3n del Usuario', response.data)
        self.assertIn(b'6666666666', response.data)
        self.assertIn(b'User to Search', response.data)

        # Limpieza
        Borrar('6666666666')

    def test_ruta_inexistente(self):
        # Prueba acceder a una ruta inexistente
        response = self.app.get('/ruta_inexistente')
        self.assertEqual(response.status_code, 404)

    def test_content_type(self):
        # Prueba que el content type sea text/html
        response = self.app.get('/')
        self.assertEqual(response.content_type, 'text/html; charset=utf-8')

    def test_buscar_usuario_no_existente(self):
        # Prueba buscar un usuario que no existe
        data_search = {
            'cedula': '0000000000'
        }
        response = self.app.post('/buscar_usuario', data=data_search, follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Error al buscar usuario', response.data)

if __name__ == '__main__':
    unittest.main()
