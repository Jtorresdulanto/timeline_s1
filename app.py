import streamlit as st

st.set_page_config(page_title="Timeline con Slider", layout="centered")

st.title("Timeline con Slider (5 puntos)")

# URLs de las imágenes almacenadas en tu repositorio de GitHub.
# IMPORTANTE: Reemplaza "TU_USUARIO", "TU_REPO", y las imágenes correspondientes.
img_urls = {
    1: "https://raw.githubusercontent.com/TU_USUARIO/TU_REPO/main/timeline_images/imagen1.png",
    2: "https://raw.githubusercontent.com/TU_USUARIO/TU_REPO/main/timeline_images/imagen2.png",
    3: "https://raw.githubusercontent.com/TU_USUARIO/TU_REPO/main/timeline_images/imagen3.png",
    4: "https://raw.githubusercontent.com/TU_USUARIO/TU_REPO/main/timeline_images/imagen4.png",
    5: "https://raw.githubusercontent.com/TU_USUARIO/TU_REPO/main/timeline_images/imagen5.png",
}

# Slider con 5 puntos
punto = st.slider(
    "Selecciona un punto de la línea del tiempo",
    min_value=1,
    max_value=5,
    step=1
)

# Mostrar imagen correspondiente
st.image(img_urls[punto], use_column_width=True)
