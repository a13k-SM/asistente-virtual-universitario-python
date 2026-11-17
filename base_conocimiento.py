# -*- coding: utf-8 -*-
"""
Módulo: base_conocimiento.py
Descripción: Almacena la base de conocimiento de trámites universitarios (UNFV)
y gestiona la persistencia de tareas y horarios en archivos JSON.
"""

import json
import os

ARCHIVO_TAREAS = "tareas_estudiante.json"

BASE_TRAMITES = [
    {
        "id": "TR-01",
        "categoria": "Matrícula",
        "titulo": "Matrícula Regular y Extemporánea",
        "keywords": ["matricula", "inscripcion", "cursos", "creditos", "rectificacion", "extemporanea"],
        "respuesta": (
            "1. Verifica estar al día en tus pagos y no tener deudas en tesorería.\n"
            "   2. Ingresa al portal académico en la fecha asignada según tu promedio ponderado.\n"
            "   3. Selecciona tus asignaturas respetando el límite de 22 créditos regulares.\n"
            "   4. Descarga tu constancia de matrícula en PDF. Si perdiste la fecha, solicita rectificación dentro de los primeros 5 días hábiles."
        ),
        "tiempo_estimado": "24 a 48 horas (validación en sistema)"
    },
    {
        "id": "TR-02",
        "categoria": "Identificación",
        "titulo": "Carné Universitario (Nuevo o Duplicado)",
        "keywords": ["carne", "carnet", "identificacion", "duplicado", "perdida", "robo", "ocracc"],
        "respuesta": (
            "1. Realiza el pago por derecho de trámite en el Banco de la Nación o agente autorizado.\n"
            "   2. En caso de pérdida o robo, adjunta la denuncia policial digital.\n"
            "   3. Presenta tu solicitud mediante Mesa de Partes Virtual dirigida a OCRACC adjuntando foto tamaño pasaporte con fondo blanco y comprobante de pago."
        ),
        "tiempo_estimado": "15 a 20 días hábiles"
    },
    {
        "id": "TR-03",
        "categoria": "Certificados",
        "titulo": "Constancia de Estudios y Récord Académico",
        "keywords": ["constancia", "certificado", "notas", "record", "academico", "historial"],
        "respuesta": (
            "1. Cancela la tasa administrativa correspondiente en caja o banco autorizado.\n"
            "   2. Ingresa a la plataforma de trámites documentarios con tu código de estudiante.\n"
            "   3. Adjunta el voucher escaneado y selecciona 'Constancia de Estudios' o 'Récord Académico'.\n"
            "   4. El documento firmado digitalmente llegará a tu correo institucional."
        ),
        "tiempo_estimado": "3 a 5 días hábiles"
    },
    {
        "id": "TR-04",
        "categoria": "Bienestar",
        "titulo": "Comedor Universitario y Atención Médica",
        "keywords": ["comedor", "almuerzo", "beca", "medico", "salud", "bienestar", "psicologia"],
        "respuesta": (
            "1. Acércate a la Oficina de Bienestar Universitario o revisa la convocatoria semestral en redes oficiales.\n"
            "   2. Presenta tu ficha socioeconómica, copia de DNI y constancia de matrícula vigente.\n"
            "   3. Para atención médica o psicológica gratuita, acude al tópico de tu facultad con tu código de alumno."
        ),
        "tiempo_estimado": "Inmediato (tópico) / Semestral (comedor)"
    },
    {
        "id": "TR-05",
        "categoria": "Académico",
        "titulo": "Reserva de Matrícula y Retiro de Curso",
        "keywords": ["reserva", "retiro", "dejar", "curso", "ciclo", "suspender"],
        "respuesta": (
            "1. El retiro de curso solo procede hasta la semana 8 del semestre académico vigente.\n"
            "   2. Presenta una solicitud dirigida al Director de Escuela explicando los motivos.\n"
            "   3. Para reserva de matrícula, el trámite debe realizarse antes de culminar el proceso de matrícula regular."
        ),
        "tiempo_estimado": "5 a 7 días hábiles"
    }
]

def cargar_tareas():
    """Carga la lista de tareas desde el archivo JSON local si existe."""
    if not os.path.exists(ARCHIVO_TAREAS):
        return []
    try:
        with open(ARCHIVO_TAREAS, "r", encoding="utf-8") as archivo:
            return json.load(archivo)
    except (json.JSONDecodeError, IOError):
        return []

def guardar_tareas(lista_tareas):
    """Guarda la lista actualizada de tareas en el archivo JSON."""
    with open(ARCHIVO_TAREAS, "w", encoding="utf-8") as archivo:
        json.dump(lista_tareas, archivo, indent=4, ensure_ascii=False)
