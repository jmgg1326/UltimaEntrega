# Payroll Calculator 

## Autores 
Realizado por: 
- Alejandro Bustamante 
- Tomas López 
## Correciones por:
- Juan José Peñuela Herrera
- Santiago Cano
## Segunda Correccion por:
- Juan Manuel García Gómez
- Santiago Perez Jimenez 

## Descripción del proyecto 
Este programa permite a los empleados o usuarios calcular la liquidación de su nómina fácilmente, permitiendoles 
ver los respectivos cálculos como: total devengado, deducciones por salud, deducciones por pensión, total deducido y la nómina final. 

## Cómo funciona?
El programa solicita al usuario su información personal: nombre, salario, dias trabajados, horas trabajadas, 
comisiones, horas extras. Con la información obtenida se hacen los respectivos calculos de su nómina, como el total devengado, deducciones por salud, deducciones por pensión, total deducido y la nómina final. 
En caso de obtener algún dato incorrecto por parte del usuario se hará manejo de este error a través de las exepciones. 

## Cómo puedo correr la intefaz de consola?
1. Instalar python 
2. Clona el repositorio 
3. Abre el Símbolo del Sistema y ubicate en la carpeta donde clonaste el repositorio. 
4. En la terminal instale la libreria flask con "pip install flask"
5. Luego ejecuta el siguiente comando `python app.py` para ejecutar la aplicación.
6. Para ejecuta el siguiente comando `python  test/test_html.py` para ejecutar las pruebas unitarias.



## cómo puedo configurar el SecretConfig-sample.py?
### Datos secretos que no deben publicarse en el repositorio

Diligencie estos datos y guarde este archivo como SecretConfig.py en la carpeta src
para poder ejecutar la aplicación

PGDATABASE = "ESCRIBA EL NOMBRE DE LA BASE DE DATOS"
PGUSER = "ESCRIBA EL USUARIO DE LA DB"
PGPASSWORD = "ESCRIBA LA CONSTRASEÑA"
PGHOST = "ESCRIBA LA DIRECCION DNS O DIRECCION IP DEL SERVIDOR"
PGPORT = 5432 # POR DEFECTO ES 5432, PERO PUEDE CAMBIAR EN SU DB


## Para Clonar el repositorio
```markdown
https://github.com/Santiagocano46/Payroll-Calculator-
```

## Para Ejecutar las puebas unitarias del controlador
```markdown
python test/controller_test.py
```

## Para ejecutar la consola de la BD
```markdown
python console/ConsolaBD.py
```