# 🧠 Predicción del Alzheimer mediante un Juego Interactivo

Este proyecto es una plataforma desarrollada con Django que busca detectar patrones cognitivos asociados al Alzheimer mediante la interacción del usuario con mini-juegos. Combina tecnología, ciencia y participación ciudadana para construir un sistema predictivo y adaptativo.

---

## 🎯 Objetivo

Diseñar una aplicación accesible y entretenida que permita a los usuarios:
- Realizar mini-juegos que evalúan funciones cognitivas clave
- Recoger métricas de tiempo de reacción, precisión, memoria, etc.
- Generar una predicción del riesgo de Alzheimer (modelo ML)
- Ofrecer recomendaciones personalizadas en base a los resultados
- Contribuir de forma anónima a la investigación científica

---

## 🧩 Componentes principales

### 1. Módulo de juegos interactivos
- Juegos de memoria visual, atención, lógica y lenguaje
- Registro automático del rendimiento y evolución

### 2. Módulo de perfil de usuario
- Registro de datos personales relevantes (edad, antecedentes, etc.)
- Historial de juegos y predicciones anteriores

### 3. Módulo de predicción
- Aplicación de un modelo de Machine Learning entrenado con métricas cognitivas
- Probabilidad estimada de deterioro cognitivo

### 4. Módulo de recomendaciones
- Sugerencias personalizadas (alimentación, estimulación cognitiva, hábitos)
- Seguimiento de progreso y evolución

---

## ⚙️ Tecnologías utilizadas

- **Backend**: Python + Django
- **Frontend**: HTML5, CSS3, JavaScript
- **Base de datos**: SQLite (fase inicial), PostgreSQL (opcional)
- **ML**: scikit-learn (modelo simple)
- **Gráficos**: Chart.js
- **Admin y pruebas**: Django Admin, Django Test

---

## 🚀 Estado del proyecto

- [x] Estructura base del proyecto Django
- [x] App `core` creada y registrada
- [ ] Modelos definidos: UsuarioPaciente, ResultadoMiniJuego, Predicción
- [ ] Mini-juegos en desarrollo (JS o framework)
- [ ] Carga de datos y entrenamiento del modelo
- [ ] Visualización y feedback personalizado

---

## 🧪 ¿De dónde salen los datos?

1. **Inicialmente**: Carga manual desde el panel de administración para testear la lógica
2. **Posteriormente**:
   - Datos recolectados desde los juegos
   - Datos de prueba generados con Faker
   - Dataset público para entrenamiento de modelo (como ADNI, OASIS, o similares adaptados)

---

## 👩‍💻 Desarrollado por

Beatriz Lamiquiz  
Proyecto final del curso  
**Certificado de Formación Avanzada Backend: Python, Flask y Django**  
Fundae + IBM

---

## 🔒 Aviso legal

Esta aplicación es solo con fines educativos y de investigación. No reemplaza diagnóstico clínico ni asesoramiento médico. Se prohíbe su uso con fines terapéuticos sin validación científica adecuada.
