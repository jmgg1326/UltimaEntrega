-- Crea la tabla de usuarios
--crear-usuarios.sql
create table usuarios(
    cedula text not null PRIMARY KEY,
    nombre text not null,
    salario varchar(40),
    dias_trabajados text,
    horas_trabajadas text,
    comisiones varchar(40),
    horas_extras varchar(40)
) 
