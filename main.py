# -*- coding: utf-8 -*-
"""
Proyecto Final: Asistente virtual en Python para orientar trámites universitarios
                y organizar el tiempo de estudio.
Universidad Nacional Federico Villarreal - FIIS - Ingeniería de Sistemas
"""

from modulo_chatbot import ejecutar_chatbot
from modulo_planificador import ejecutar_planificador

def mostrar_banner():
    print("\n" + "=" * 68)
    print("   UNIVERSIDAD NACIONAL FEDERICO VILLARREAL - INGENIERÍA DE SISTEMAS")
    print("   ASISTENTE VIRTUAL ACADÉMICO Y GESTOR DE TIEMPO EN PYTHON")
    print("=" * 68)

def menu_principal():
    mostrar_banner()
    while True:
        print("\nMENÚ PRINCIPAL:")
        print("1. Consultar trámites universitarios (Chatbot Inteligente)")
        print("2. Organizar tiempo y generar horario de estudio")
        print("3. Acerca del sistema")
        print("4. Salir")

        opcion = input("\nElige una opción (1-4): ").strip()

        if opcion == "1":
            ejecutar_chatbot()
        elif opcion == "2":
            ejecutar_planificador()
        elif opcion == "3":
            print("\n[INFO] Sistema desarrollado en Python 3 con arquitectura modular,")
            print("       procesamiento difuso de consultas y persistencia en JSON.")
        elif opcion == "4":
            print("\n¡Éxitos en tus estudios! Cerrando el asistente virtual...")
            break
        else:
            print("[!] Opción no válida. Por favor ingresa un número del 1 al 4.")

if __name__ == "__main__":
    menu_principal()
