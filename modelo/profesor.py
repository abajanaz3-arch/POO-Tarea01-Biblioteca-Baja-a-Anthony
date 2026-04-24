from modelo.persona import Persona

class Profesor(Persona):
    """Clase que representa a un profesor, hereda de Persona."""

    def __init__(self, cedula: str, nombre: str, apellido: str, departamento: str):
        super().__init__(cedula, nombre, apellido)
        self._departamento = departamento

    @property
    def departamento(self) -> str:
        return self._departamento

    def __str__(self) -> str:
        return f"{super().__str__()} | Departamento: {self._departamento} (Profesor)"