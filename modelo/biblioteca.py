from modelo.libro import Libro
from modelo.persona import Persona # <-- Cambiamos Estudiante por Persona
from modelo.prestamo import Prestamo

class Biblioteca:
    """Gestiona libros, personas (estudiantes/profesores) y préstamos."""

    def __init__(self, nombre: str):
        self._nombre = nombre
        self._libros = []
        self._personas = []  # <-- CAMBIO: Lista general de personas
        self._prestamos = []

    def registrar_libro(self, libro: Libro) -> None:
        self._libros.append(libro)
        print(f"  ✓ Libro registrado: {libro.titulo}")

    def registrar_persona(self, persona: Persona) -> None:
        """Registra a cualquier persona (Estudiante o Profesor)."""
        self._personas.append(persona)
        # Identifica si es Profesor o Estudiante para el mensaje
        tipo = type(persona).__name__ 
        print(f"  ✓ {tipo} registrado: {persona.nombre} {persona.apellido}")

    def _buscar_libro(self, isbn: str) -> Libro:
        for libro in self._libros:
            if libro.isbn == isbn:
                return libro
        return None

    def _buscar_persona(self, cedula: str) -> Persona:
        """Busca una persona por cédula."""
        for persona in self._personas:
            if persona.cedula == cedula:
                return persona
        return None

    def prestar_libro(self, isbn: str, cedula: str,
                      fecha_prestamo: str, fecha_devolucion: str) -> str:
        
        libro = self._buscar_libro(isbn)
        if libro is None:
            return f"  ✗ Error: No se encontró el libro con ISBN {isbn}"

        persona = self._buscar_persona(cedula) # <-- Usamos _buscar_persona
        if persona is None:
            return f"  ✗ Error: No se encontró el usuario con cédula {cedula}"

        if not libro.disponible:
            return f"  ✗ Error: El libro '{libro.titulo}' no está disponible"

        libro.prestar()
        # Creamos el préstamo pasándole la 'persona'
        prestamo = Prestamo(libro, persona, fecha_prestamo, fecha_devolucion)
        self._prestamos.append(prestamo)
        return f"  ✓ Préstamo registrado: '{libro.titulo}' → {persona.nombre}"

    def devolver_libro(self, isbn: str, cedula: str) -> str:
        for prestamo in self._prestamos:
            # <-- CAMBIO: Comparamos usando prestamo.persona.cedula
            if (prestamo.libro.isbn == isbn and
                prestamo.persona.cedula == cedula and 
                prestamo.activo):
                prestamo.registrar_devolucion()
                return f"  ✓ Devolución registrada: '{prestamo.libro.titulo}'"

        return "  ✗ Error: No se encontró un préstamo activo con esos datos"

    def consultar_prestamos_activos(self, cedula: str) -> list:
        activos = []
        for prestamo in self._prestamos:
             # <-- CAMBIO: Comparamos usando prestamo.persona.cedula
            if prestamo.persona.cedula == cedula and prestamo.activo:
                activos.append(prestamo)
        return activos

    def __str__(self) -> str:
        return (f"Biblioteca '{self._nombre}' | "
                f"Libros: {len(self._libros)} | "
                f"Usuarios: {len(self._personas)} | " 
                f"Préstamos: {len(self._prestamos)}")