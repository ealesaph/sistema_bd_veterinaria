drop database if exists clinica_db;
create database clinica_db
character set utf8mb4
collate utf8mb4_general_ci;

use clinica_db;

create table persona (
rut varchar(12),
nombres varchar(100) not null,
apellidos varchar(100) not null,
telefono varchar(15),
correo varchar(200),
primary key (rut)
);

create table medico (
id_medico integer auto_increment,
rut varchar(12) not null unique,
num_licencia integer not null,
sueldo_base integer not null,
primary key (id_medico),
constraint fk_persona_medico foreign key (rut)
references persona(rut)
on delete cascade
);

create table paciente (
id_paciente integer auto_increment,
rut varchar(12) not null unique,
num_ficha integer not null,
fecha_nacimiento date,
primary key (id_paciente),
constraint fk_persona_paciente foreign key (rut)
references persona(rut)
on delete cascade
);

create table especialidad (
id_especialidad integer auto_increment,
nombre varchar(100) not null,
descripcion text,
primary key (id_especialidad)
);

create table consultorio (
id_consultorio integer auto_increment,
num_consultorio integer not null,
piso varchar(50),
primary key (id_consultorio)
);

create table cita (
id_cita integer auto_increment,
fecha date not null,
estado varchar(50) default 'Sin confirmar',
motivo text,
id_paciente integer not null,
id_medico integer not null,
id_consultorio integer,
primary key (id_cita),
constraint estado_chk check (estado in ('Sin confirmar', 'Confirmada', 'Cancelada', 'Realizada')),
constraint fk_cita_paciente foreign key (id_paciente)
references paciente(id_paciente),
constraint fk_cita_medico foreign key (id_medico)
references medico(id_medico),
constraint fk_cita_consultorio foreign key (id_consultorio)
references consultorio(id_consultorio)
);

create table medico_especialidad (
id_medico integer,
id_especialidad integer,
primary key (id_medico, id_especialidad),
constraint fk_relacion_medico foreign key (id_medico)
references medico(id_medico),
constraint fk_relacion_med_especialidad foreign key (id_especialidad)
references especialidad(id_especialidad)
);

create table consultorio_especialidad (
id_consultorio integer,
id_especialidad integer,
primary key (id_consultorio, id_especialidad),
constraint fk_relacion_consultorio foreign key (id_consultorio)
references consultorio(id_consultorio),
constraint fk_relacion_cons_especialidad foreign key (id_especialidad)
references especialidad(id_especialidad)
);