from abc import ABC, abstractmethod
import datetime as dt

class Especialidad:
    def __init__(self, id: int, nombre: str, descripcion: str):
        self.__id_especialidad = id
        self.__nombre = nombre
        self.__descripcion = descripcion

    def obtener_id(self):
        return self.__id_especialidad

    def obtener_nombre(self):
        return self.__nombre

    def modificar_nombre(self, nombre: str):
        self.__nombre = nombre

    def obtener_descripcion(self):
        return self.__descripcion

    def modificar_descripcion(self, descripcion: str):
        self.__descripcion = descripcion

    def __str__(self):
        return f"{self.__nombre} - {self.__descripcion}"

class Persona(ABC):
    def __init__(self, rut: str, nombres: str, apellidos: str, telefono: str, correo: str):
        self.__rut = rut
        self.__nombres = nombres
        self.__apellidos = apellidos
        self.__telefono = telefono
        self.__correo = correo

    def obtener_rut(self):
        return self.__rut

    def obtener_nombres(self):
        return self.__nombres

    def obtener_apellidos(self):
        return self.__apellidos

    def obtener_telefono(self):
        return self.__telefono

    def modificar_telefono(self, telefono: str):
        self.__telefono = telefono

    def obtener_correo(self):
        return self.__correo

    def modificar_correo(self, correo: str):
        self.__correo = correo

    @abstractmethod
    def __str__(self):
        return f"{self.__rut} - {self.__nombres} {self.__apellidos}"

class Medico(Persona):
    def __init__(self, rut: str, nombres: str, apellidos: str, telefono: str, correo: str, id: int, num_licencia: str, sueldo: int):
        super().__init__(rut, nombres, apellidos, telefono, correo)
        self.__id_medico = id
        self.__num_licencia = num_licencia
        self.__sueldo = sueldo
        self.__especialidades: list[Especialidad] = []

    def obtener_especialidades(self):
        return self.__especialidades

    def agregar_especialidad(self, especialidad: Especialidad):
        self.__especialidades.append(especialidad)

    def quitar_especialidad(self, especialidad: Especialidad):
        self.__especialidades.remove(especialidad)

    def obtener_id(self):
        return self.__id_medico

    def obtener_num_licencia(self):
        return self.__num_licencia

    def obtener_sueldo(self):
        return self.__sueldo

    def cambiar_sueldo(self, sueldo: int):
        self.__sueldo = sueldo

    def __str__(self):
        return f"{super().__str__()} (Licencia N°{self.__num_licencia})"

class Paciente(Persona):
    def __init__(self, rut: str, nombres: str, apellidos: str, telefono: str, correo: str, id: int, num_ficha: str, fecha_nacimiento: dt.date):
        super().__init__(rut, nombres, apellidos, telefono, correo)
        self.__id_paciente = id
        self.__num_ficha = num_ficha
        self.__fecha_nacimiento = fecha_nacimiento

    def obtener_id(self):
        return self.__id_paciente

    def obtener_num_ficha(self):
        return self.__num_ficha

    def obtener_fecha_nacimiento(self):
        return self.__fecha_nacimiento

    def __str__(self):
        return f"{super().__str__()} (Ficha N° {self.__num_ficha})"

class Consultorio:
    def __init__(self, id: int, numero: str, piso: str):
        self.__id_consultorio = id
        self.__numero = numero
        self.__piso = piso

    def obtener_id(self):
        return self.__id_consultorio
        
    def obtener_numero(self):
        return self.__numero

    def obtener_piso(self):
        return self.__piso

    def __str__(self):
        return f"Consultorio N° {self.__numero} - {self.__piso}"

class Cita:
    def __init__(self, id:int, estado: str, motivo:str, paciente: Paciente, medico: Medico):
        self.__id_cita = id
        self.__fecha = dt.date.today()
        self.__estado = estado
        self.__motivo = motivo
        self.__paciente = paciente
        self.__medico = medico
        self.__consultorio = None

    def obtener_paciente(self):
        return self.__paciente

    def obtener_medico(self):
        return self.__medico

    def modificar_medico(self, medico: Medico):
        self.__medico = medico

    def obtener_consultorio(self):
        return self.__consultorio

    def modificar_consultorio(self, consultorio: Consultorio):
        self.__consultorio = consultorio

    def obtener_id(self):
        return self.__id_cita

    def obtener_fecha(self):
        return self.__fecha

    def obtener_estado(self):
        return self.__estado

    def modificar_estado(self, estado: str):
        self.__estado = estado

    def obtener_motivo(self):
        return self.__motivo

    def modificar_motivo(self, motivo: str):
        self.__motivo = motivo

    def __str__(self):
        return f"Cita {self.__fecha} - {self.__estado}"
