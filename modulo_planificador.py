# -*- coding: utf-8 -*-
"""
Módulo: modulo_planificador.py
Descripción: Permite registrar cursos/tareas y genera un horario de estudio
personalizado priorizando fechas límite, dificultad y horas disponibles.
"""

from datetime import datetime
from base_conocimiento import cargar_tareas, guardar_tareas

def calcular_indice_prioridad(tarea):
    """Calcula un puntaje numérico de urgencia basado en fecha y dificultad."""
    hoy = datetime.now().date()
    try:
        fecha_entrega = datetime.strptime(tarea["fecha_entrega"], "%Y-%m-%d").date()
        dias_restantes = (fecha_entrega - hoy).days
    except ValueError:
        dias_restantes = 7

    factor_urgencia = 100 if dias_restantes <= 0 else (30 / dias_restantes)
    return round(factor_urgencia + (tarea["dificultad"] * 2.5), 2)

def registrar_actividad(tareas):
    """Solicita datos validados de una nueva tarea o examen."""
    print("\n--- REGISTRAR NUEVA ACTIVIDAD ACADÉMICA ---")
    curso = input("Nombre del curso (ej. Fundamentos de Programación): ").strip()
    actividad = input("Descripción (ej. Proyecto Final / Examen Parcial): ").strip()

    if not curso or not actividad:
        print("[!] Error: El curso y la descripción no pueden estar vacíos.")
        return

    while True:
        fecha_str = input("Fecha de entrega (Formato AAAA-MM-DD, ej. 2026-11-25): ").strip()
        try:
            datetime.strptime(fecha_str, "%Y-%m-%d")
            break
        except ValueError:
            print("[!] Formato inválido. Usa AAAA-MM-DD (ejemplo: 2026-11-25).")

    while True:
        try:
            dificultad = int(input("Nivel de dificultad (1 = Baja, 2 = Media, 3 = Alta): "))
            if dificultad in [1, 2, 3]:
                break
            print("[!] Ingresa 1, 2 o 3.")
        except ValueError:
            print("[!] Ingresa un número entero válido.")

    while True:
        try:
            horas_req = float(input("Horas estimadas necesarias para completarla (ej. 4.5): "))
            if horas_req > 0:
                break
            print("[!] Las horas deben ser mayores a 0.")
        except ValueError:
            print("[!] Ingresa un número válido.")

    nueva_tarea = {
        "curso": curso,
        "actividad": actividad,
        "fecha_entrega": fecha_str,
        "dificultad": dificultad,
        "horas_estimadas": horas_req,
        "completada": False
    }
    tareas.append(nueva_tarea)
    guardar_tareas(tareas)
    print(f"[OK] Actividad '{actividad}' registrada y guardada correctamente.\n")

def listar_actividades(tareas):
    """Muestra las actividades ordenadas por índice de prioridad."""
    pendientes = [t for t in tareas if not t["completada"]]
    if not pendientes:
        print("\n[i] No tienes tareas pendientes registradas.\n")
        return []

    ordenadas = sorted(pendientes, key=calcular_indice_prioridad, reverse=True)
    print("\n" + "=" * 78)
    print(f"{'N°':<4} {'CURSO':<22} {'ACTIVIDAD':<22} {'ENTREGA':<12} {'HORAS':<7} {'PRIORIDAD'}")
    print("=" * 78)
    for idx, t in enumerate(ordenadas, 1):
        prio = calcular_indice_prioridad(t)
        etiqueta = "ALTA" if prio >= 12 else ("MEDIA" if prio >= 8 else "NORMAL")
        print(f"{idx:<4} {t['curso'][:20]:<22} {t['actividad'][:20]:<22} {t['fecha_entrega']:<12} {t['horas_estimadas']:<7} {etiqueta} ({prio})")
    print("=" * 78 + "\n")
    return ordenadas

def generar_horario_estudio(tareas):
    """Distribuye las horas de estudio diarias según disponibilidad del alumno."""
    pendientes = [t for t in tareas if not t["completada"]]
    if not pendientes:
        print("\n[i] Agrega primero tus tareas o exámenes para generar un horario.\n")
        return

    try:
        horas_dia = float(input("\n¿Cuántas horas libres tienes al día para estudiar? (ej. 3): "))
        dias_plan = int(input("¿Para cuántos días deseas planificar tu horario? (ej. 5): "))
        if horas_dia <= 0 or dias_plan <= 0:
            print("[!] Los valores deben ser mayores a cero.")
            return
    except ValueError:
        print("[!] Entrada numérica inválida.")
        return

    cola_tareas = [
        {
            "curso": t["curso"],
            "actividad": t["actividad"],
            "horas_restantes": t["horas_estimadas"],
            "prioridad": calcular_indice_prioridad(t)
        }
        for t in sorted(pendientes, key=calcular_indice_prioridad, reverse=True)
    ]

    print("\n" + "*" * 70)
    print("        CRONOGRAMA DE ESTUDIO PERSONALIZADO GENERADO")
    print("*" * 70)

    for dia in range(1, dias_plan + 1):
        capacidad_dia = horas_dia
        print(f"\nDÍA {dia} (Disponibilidad: {horas_dia} hrs):")
        asignado_hoy = False

        for item in cola_tareas:
            if capacidad_dia <= 0:
                break
            if item["horas_restantes"] > 0:
                bloque = min(capacidad_dia, item["horas_restantes"])
                item["horas_restantes"] = round(item["horas_restantes"] - bloque, 2)
                capacidad_dia = round(capacidad_dia - bloque, 2)
                asignado_hoy = True
                estado = "FINALIZADO" if item["horas_restantes"] == 0 else f"faltan {item['horas_restantes']}h"
                print(f"  -> {bloque:.1f} hrs | {item['curso']} - {item['actividad']} ({estado})")

        if not asignado_hoy:
            print("  -> ¡Todas las tareas planificadas han sido cubiertas! Tiempo libre para repaso.")

    print("\n" + "*" * 70 + "\n")

def marcar_completada(tareas):
    """Permite marcar una actividad como concluida."""
    ordenadas = listar_actividades(tareas)
    if not ordenadas:
        return
    try:
        num = int(input("Ingresa el N° de la actividad completada (0 para cancelar): "))
        if num == 0:
            return
        seleccionada = ordenadas[num - 1]
        for t in tareas:
            if t == seleccionada:
                t["completada"] = True
                break
        guardar_tareas(tareas)
        print("[OK] Actividad marcada como completada.\n")
    except (ValueError, IndexError):
        print("[!] Número de actividad no válido.\n")

def ejecutar_planificador():
    """Submenú del módulo organizador de tiempo."""
    tareas = cargar_tareas()
    while True:
        print("\n--- ORGANIZADOR DE TIEMPO Y HORARIOS DE ESTUDIO ---")
        print("1. Registrar nueva tarea o examen")
        print("2. Ver actividades ordenadas por prioridad")
        print("3. Generar horario de estudio personalizado")
        print("4. Marcar actividad como completada")
        print("5. Volver al menú principal")

        op = input("Selecciona una opción (1-5): ").strip()
        if op == "1":
            registrar_actividad(tareas)
        elif op == "2":
            listar_actividades(tareas)
        elif op == "3":
            generar_horario_estudio(tareas)
        elif op == "4":
            marcar_completada(tareas)
        elif op == "5":
            break
        else:
            print("[!] Opción inválida.")
