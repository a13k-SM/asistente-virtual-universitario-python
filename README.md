# 🎓 Asistente Virtual Universitario y Gestor de Tiempo en Python

Proyecto final del curso **Fundamentos de Programación I** — Escuela Profesional de Ingeniería de Sistemas, **Universidad Nacional Federico Villarreal (UNFV)**.

## 📌 Descripción del Proyecto
Este sistema en consola desarrollado en **Python 3** resuelve dos problemáticas frecuentes de la vida universitaria:
1. **Orientación inmediata de trámites universitarios:** Un módulo conversacional (*chatbot*) capaz de interpretar consultas escritas en lenguaje natural (con tolerancia a errores tipográficos y ausencia de tildes) sobre matrícula, carné universitario (OCRACC), constancias de estudio, comedor universitario y retiro de cursos.
2. **Organización del tiempo y horarios de estudio:** Un planificador académico que calcula un **índice dinámico de prioridad** según la fecha límite y el nivel de dificultad de cada actividad, generando cronogramas diarios personalizados y guardando la información de forma persistente en formato **JSON**.

## 🗂️ Arquitectura Modular del Repositorio
```text
asistente-virtual-universitario-python/
│
├── main.py                   # Módulo principal y menú de navegación
├── base_conocimiento.py      # Base de datos de trámites y persistencia JSON
├── modulo_chatbot.py         # Motor de búsqueda con normalización y coincidencia difusa
├── modulo_planificador.py    # Algoritmo de priorización y generador de horarios
└── README.md                 # Documentación técnica del repositorio
```

## 🚀 Requisitos y Ejecución
* **Requisitos:** Python 3.8 o superior (no requiere instalar librerías externas; utiliza exclusivamente módulos estándar: `json`, `os`, `unicodedata`, `difflib`, `datetime`).
* **Ejecución en terminal:**
```bash
git clone https://github.com/TU-USUARIO/asistente-virtual-universitario-python.git
cd asistente-virtual-universitario-python
python main.py
```

## 👥 Autores (Grupo de Trabajo)
* Integrante 1 — Módulo Principal (`main.py`)
* Integrante 2 — Base de Conocimiento (`base_conocimiento.py`)
* Integrante 3 — Módulo Chatbot (`modulo_chatbot.py`)
* Integrante 4 — Módulo Planificador (`modulo_planificador.py`)
* Integrante 5 — Pruebas y Documentación

**Docente:** Ing. Ivan Carlo Petrlik Azabache — Lima, Perú (2026).
