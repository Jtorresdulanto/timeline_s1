import streamlit as st
import os

# --- Configuración de la Página ---
st.set_page_config(
    page_title="Visor de Línea de Tiempo",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Título principal de la aplicación
st.title("Línea de Tiempo Interactiva ⏳")
st.markdown("Utiliza el deslizador para navegar por los 5 puntos clave.")

# --- Mapeo de Valores del Slider a Rutas de Imagen ---
# IMPORTANTE: Asegúrate de que los nombres de los archivos en tu carpeta
# 'timeline_images' coincidan con los nombres utilizados aquí.
# Si tus archivos tienen nombres diferentes (por ejemplo, 'fase1.png'),
# debes modificar las rutas en este diccionario.
IMAGE_PATHS = {
    1: "timeline_images/image_1.png",
    2: "timeline_images/image_2.png",
    3: "timeline_images/image_3.png",
    4: "timeline_images/image_4.png",
    5: "timeline_images/image_5.png",
}

# Diccionario para descripciones de los puntos de la línea de tiempo (opcional)
DESCRIPTIONS = {
    1: "Punto 1: El Inicio del Proyecto",
    2: "Punto 2: Desarrollo de la Fase Alpha",
    3: "Punto 3: Lanzamiento de la Versión Beta",
    4: "Punto 4: Optimización y Feedback",
    5: "Punto 5: Lanzamiento Final y Éxito",
}

# --- Slider con 5 Puntos ---
# El valor mínimo es 1, el máximo es 5, y el valor por defecto es 1.
# step=1 asegura que solo se seleccionen números enteros.
selected_point = st.slider(
    "Selecciona un punto en la Línea de Tiempo:",
    min_value=1,
    max_value=5,
    value=1,
    step=1,
    key="timeline_slider"
)

# --- Carga y Muestra de la Imagen Correspondiente ---
if selected_point in IMAGE_PATHS:
    image_path = IMAGE_PATHS[selected_point]

    # Verificar si el archivo existe (útil para pruebas locales)
    if os.path.exists(image_path):
        st.header(DESCRIPTIONS[selected_point])
        # Mostrar la imagen
        st.image(image_path, caption=f"Vista del Punto {selected_point}", use_column_width=True)
    else:
        # Mensaje de error si la ruta es incorrecta o la imagen falta
        st.error(
            f"Error: No se encontró la imagen para el punto {selected_point} en la ruta esperada: `{image_path}`. "
            f"Asegúrate de que la carpeta `timeline_images` exista en tu repositorio y que los archivos PNG estén allí."
        )
else:
    st.warning("Selección inválida en el deslizador.")

# Información de Depuración (opcional, puedes removerla)
st.sidebar.info(f"Punto seleccionado actualmente: {selected_point}")
