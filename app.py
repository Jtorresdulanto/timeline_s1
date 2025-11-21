import streamlit as st
import os

# --- Configuración de la página ---
st.set_page_config(
    page_title="Línea de Tiempo Interactiva",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Título de la aplicación
st.title("🗺️ Línea de Tiempo Visual")
st.markdown("Utiliza el control deslizante para navegar a través de los diferentes puntos de la línea de tiempo y ver la imagen correspondiente.")

# --- Definición de las imágenes y sus rutas ---
# Se define un diccionario que mapea el valor del slider (1 a 5) a la ruta de la imagen
# La ruta es relativa a la carpeta 'timeline_images' que debe estar en el mismo nivel que 'app.py'
IMAGE_MAP = {
    1: "timeline_images/1.PNG",
    2: "timeline_images/2.PNG",
    3: "timeline_images/3.PNG",
    4: "timeline_images/4.PNG",
    5: "timeline_images/5.PNG",
}

# Definición de etiquetas descriptivas para cada punto
IMAGE_LABELS = {
    1: "Punto 1: El Inicio del Proyecto",
    2: "Punto 2: Desarrollo Intermedio",
    3: "Punto 3: Hito Importante Alcanzado",
    4: "Punto 4: Fase de Pruebas",
    5: "Punto 5: Lanzamiento Final",
}


# --- Control Deslizante (Slider) ---
# Creamos el slider con solo 5 puntos, forzando valores enteros
selected_point = st.slider(
    "Selecciona un Punto en la Línea de Tiempo",
    min_value=1,
    max_value=5,
    value=1, # Valor inicial
    step=1,
    key="timeline_slider"
)

# --- Lógica de Visualización ---
# Obtener la ruta de la imagen y la etiqueta basadas en la selección del slider
image_path = IMAGE_MAP.get(selected_point)
image_label = IMAGE_LABELS.get(selected_point, "Descripción no disponible")

st.header(image_label)
st.write(f"Cargando imagen desde: `{image_path}`")

# Verificar si el archivo existe antes de intentar cargarlo
if os.path.exists(image_path):
    # Cargar y mostrar la imagen
    st.image(
        image_path,
        caption=image_label,
        use_column_width=True # Ajusta la imagen al ancho de la columna
    )
else:
    # Mensaje de error si la imagen no se encuentra
    st.error(f"""
        ⚠️ Error al cargar la imagen. El archivo no se encuentra en la ruta: `{image_path}`.

        Asegúrate de que:
        1. La carpeta `timeline_images` exista en la raíz de tu repositorio.
        2. Los archivos dentro de la carpeta se llamen `1.jpg`, `2.jpg`, etc. (o ajusta los nombres en el código).
        3. La extensión del archivo (`.jpg` en este ejemplo) sea la correcta.
    """)

# --- Pie de página informativo (opcional) ---
st.sidebar.info("Esta aplicación se ejecuta en Streamlit y carga recursos desde un repositorio de GitHub.")
