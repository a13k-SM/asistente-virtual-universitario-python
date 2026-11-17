# -*- coding: utf-8 -*-
"""
Módulo: modulo_chatbot.py
Descripción: Procesa consultas en lenguaje natural del estudiante mediante
normalización de texto, coincidencia de palabras clave y similitud difusa.
"""

import unicodedata
from difflib import SequenceMatcher
from base_conocimiento import BASE_TRAMITES

def normalizar_texto(texto):
    """Elimina tildes, signos de puntuación y convierte a minúsculas."""
    texto = texto.lower().strip()
    texto = "".join(
        c for c in unicodedata.normalize("NFD", texto)
        if unicodedata.category(c) != "Mn"
    )
    for signo in ["¿", "?", "¡", "!", ".", ",", ";", ":"]:
        texto = texto.replace(signo, "")
    return texto

def buscar_respuesta_tramite(consulta_usuario):
    """Evalúa la consulta y devuelve el trámite más relevante o sugerencias."""
    consulta_norm = normalizar_texto(consulta_usuario)
    palabras_usuario = set(consulta_norm.split())

    mejor_tramite = None
    mayor_puntaje = 0.0

    for tramite in BASE_TRAMITES:
        puntaje = 0.0
        for kw in tramite["keywords"]:
            if kw in palabras_usuario:
                puntaje += 2.0
            elif kw in consulta_norm:
                puntaje += 1.5
            else:
                for palabra in palabras_usuario:
                    similitud = SequenceMatcher(None, palabra, kw).ratio()
                    if similitud >= 0.82:
                        puntaje += similitud

        if puntaje > mayor_puntaje:
            mayor_puntaje = puntaje
            mejor_tramite = tramite

    if mayor_puntaje >= 1.2 and mejor_tramite:
        return mejor_tramite
    return None

def ejecutar_chatbot():
    """Interfaz interactiva en consola para el módulo de consultas."""
    print("\n" + "=" * 65)
    print("   ASISTENTE VIRTUAL DE TRÁMITES UNIVERSITARIOS (MODO CHAT)")
    print("=" * 65)
    print("Escribe tu consulta (ej. '¿Cómo saco mi carné?' o 'info matrícula')")
    print("Escribe 'lista' para ver todos los temas o 'salir' para volver.\n")

    while True:
        pregunta = input("Estudiante > ").strip()
        if not pregunta:
            continue

        cmd = normalizar_texto(pregunta)
        if cmd in ["salir", "volver", "menu", "0"]:
            print("Asistente > Regresando al menú principal...\n")
            break

        if cmd in ["lista", "temas", "ayuda"]:
            print("\nAsistente > Temas disponibles en mi base de conocimiento:")
            for t in BASE_TRAMITES:
                print(f"  [{t['id']}] {t['titulo']} ({t['categoria']})")
            print()
            continue

        resultado = buscar_respuesta_tramite(pregunta)
        if resultado:
            print(f"\nAsistente > Encontré información sobre: {resultado['titulo'].upper()}")
            print("-" * 65)
            print(f"   {resultado['respuesta']}")
            print(f"   Tiempo estimado de atención: {resultado['tiempo_estimado']}")
            print("-" * 65 + "\n")
        else:
            print("\nAsistente > No identifiqué el trámite exacto. Intenta usar palabras como:")
            print("            'matrícula', 'carné', 'constancia', 'comedor' o 'retiro'.\n")
