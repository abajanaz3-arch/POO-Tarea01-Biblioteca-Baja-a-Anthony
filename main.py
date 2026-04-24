# main.py
from modelo.libro import Libro
from modelo.estudiante import Estudiante
from modelo.profesor import Profesor  # <-- Importamos la nueva clase Profesor
from modelo.biblioteca import Biblioteca


def main():
    # ─── Crear la biblioteca ───
    print("=" * 60)
    print("  SISTEMA DE GESTIÓN DE BIBLIOTECA UNEMI")
    print("=" * 60)

    biblioteca = Biblioteca("Biblioteca Central UNEMI")
    print(f"\n{biblioteca}\n")

    # ─── Registrar libros (RF-01) ───
    print("── Registrando libros ──")
    libro1 = Libro("978-0-13-468599-1", "El Principito", "Antoine de Saint-Exupéry")
    libro2 = Libro("978-0-06-112008-4", "Cien Años de Soledad", "Gabriel García Márquez")
    libro3 = Libro("978-84-376-0494-7", "Don Quijote de la Mancha", "Miguel de Cervantes")
    libro4 = Libro("978-0-201-83595-3", "Patrones de Diseño", "Erich Gamma") # <-- Libro extra para el profesor

    biblioteca.registrar_libro(libro1)
    biblioteca.registrar_libro(libro2)
    biblioteca.registrar_libro(libro3)
    biblioteca.registrar_libro(libro4)

    # ─── Registrar usuarios (RF-02 adaptado) ───
    print("\n── Registrando usuarios (Estudiantes y Profesores) ──")
    est1 = Estudiante("0926400615", "María", "López", "Ingeniería en Sistemas")
    est2 = Estudiante("0912345678", "Carlos", "Ramírez", "Ingeniería Industrial")
    prof1 = Profesor("0998765432", "Roberto", "Gómez", "Ciencias de la Computación") # <-- Nuevo profesor

    # Usamos registrar_persona en lugar de registrar_estudiante
    biblioteca.registrar_persona(est1)
    biblioteca.registrar_persona(est2)
    biblioteca.registrar_persona(prof1)

    # ─── Estado actual ───
    print(f"\n{biblioteca}\n")

    # ─── Realizar préstamos (RF-03 y RF-04) ───
    print("── Realizando préstamos a Estudiantes ──")
    resultado = biblioteca.prestar_libro(
        "978-0-13-468599-1", "0926400615", "2026-04-15", "2026-04-29"
    )
    print(resultado)

    resultado = biblioteca.prestar_libro(
        "978-0-06-112008-4", "0926400615", "2026-04-15", "2026-05-01"
    )
    print(resultado)

    resultado = biblioteca.prestar_libro(
        "978-84-376-0494-7", "0912345678", "2026-04-15", "2026-04-22"
    )
    print(resultado)

    # ─── Préstamo a Profesor ───
    print("\n── Realizando préstamo a Profesor ──")
    resultado = biblioteca.prestar_libro(
        "978-0-201-83595-3", "0998765432", "2026-04-24", "2026-05-10"
    )
    print(resultado)

    # ─── Intentar prestar un libro ya prestado (RF-04: validación) ───
    print("\n── Intentando prestar libro ya prestado ──")
    resultado = biblioteca.prestar_libro(
        "978-0-13-468599-1", "0912345678", "2026-04-16", "2026-04-30"
    )
    print(resultado)

    # ─── Consultar préstamos activos (RF-06) ───
    print("\n── Préstamos activos de María López ──")
    prestamos_maria = biblioteca.consultar_prestamos_activos("0926400615")
    for prestamo in prestamos_maria:
        print(f"  → {prestamo}")

    # ─── Devolver un libro (RF-05) ───
    print("\n── Devolviendo un libro ──")
    resultado = biblioteca.devolver_libro("978-0-13-468599-1", "0926400615")
    print(resultado)

    # ─── Verificar que el libro está disponible nuevamente ───
    print(f"\n── Estado del libro devuelto ──")
    print(f"  {libro1}")

    # ─── Consultar préstamos activos después de devolución ───
    print("\n── Préstamos activos de María López (después de devolución) ──")
    prestamos_maria = biblioteca.consultar_prestamos_activos("0926400615")
    if prestamos_maria:
        for prestamo in prestamos_maria:
            print(f"  → {prestamo}")
    else:
        print("  (Sin préstamos activos)")

    # ─── Ahora el libro puede prestarse de nuevo ───
    print("\n── Prestando el libro devuelto a otro estudiante ──")
    resultado = biblioteca.prestar_libro(
        "978-0-13-468599-1", "0912345678", "2026-04-16", "2026-04-30"
    )
    print(resultado)

    # ─── Estado final ───
    print(f"\n{'=' * 60}")
    print(f"  {biblioteca}")
    print(f"{'=' * 60}")


if __name__ == "__main__":
    main()