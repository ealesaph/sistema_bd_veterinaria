use clinica_db;

insert into especialidad (nombre, descripcion)
values ('Cardiología', 'Cardiología adultos');
insert into especialidad (nombre, descripcion)
values ('Neurología', 'Neurología adultos');
insert into especialidad (nombre, descripcion)
values ('Pediatría', 'Pediatría clinica');

insert into consultorio (num_consultorio, piso)
values(101, 'Edificio A, Piso 1');
insert into consultorio (num_consultorio, piso)
values(102, 'Edificio A, Piso 1');
insert into consultorio (num_consultorio, piso)
values(201, 'Edificio A, Piso 2');
insert into consultorio (num_consultorio, piso)
values(210, 'Edificio A, Piso 2');

start transaction;
insert into persona
values('12345678-9', 'Juan', 'Pérez', '123456789', 'juan.perez@example.com');
insert into medico (rut, num_licencia, sueldo_base)
values('12345678-9', 123456, 4986000);
commit;

start transaction;
insert into persona
values('98765432-1', 'Maria', 'González', '987654321', 'maria.gonzalez@example.com');
insert into paciente (rut, num_ficha, fecha_nacimiento)
values('98765432-1', 123456, str_to_date('15-10-1999', '%d-%m-%Y'));
commit;
