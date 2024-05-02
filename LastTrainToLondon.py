import streamlit as st
import webbrowser
import matplotlib.pyplot as plt
import pandas as pd # Importacion estandar de la libreria Pandas
import numpy  as np # Importacion estandar de la libreria NumPy
import matplotlib.pyplot as plt
from PIL import Image
import folium
from streamlit_folium import folium_static as st_folium

st.set_page_config(
    page_title="LONDON GPON",
    page_icon="🤓",
)

st.write("# :red[Despliegue de fibra en Londres] ")

st.sidebar.success("¿Sí ven que sí sirve?")

st.markdown("""<p style='text-align: justify;'>En el contexto de una ciudad como Londres, donde la conectividad digital es crucial, 
    el despliegue de una red GPON en lugares emblemáticos como el Aeropuerto de Gatwick, el Puente de la Torre, la Catedral de San Pablo, 
    el Museo Británico, el Palacio de Kensington, el Palacio de Buckingham y el Big Ben, representa una solución tecnológica avanzada para 
    satisfacer la creciente demanda de ancho de banda y conectividad confiable. Esta infraestructura de fibra óptica ofrece velocidades de 
    Internet ultra rápidas, baja latencia y una base sólida para la innovación tecnológica y el desarrollo económico. Además de mejorar la 
    calidad de vida de los residentes, esta red GPON impulsa la productividad y la competitividad de las empresas al proporcionar una 
    infraestructura de comunicaciones de alta calidad y alta capacidad.<br></br></p>""",unsafe_allow_html=True)

st.write("# ¿Que es una red GPON?")
st.markdown("""<p style='text-align:justify;'> Es una arquitectura de red de fibra óptica que utiliza tecnología de división de longitud de onda 
    para proporcionar conectividad de alta velocidad a través de una infraestructura óptica pasiva. En una red GPON, la transmisión de 
    datos se realiza a través de pulsos de luz que viajan a través de cables de fibra óptica.</p>""",unsafe_allow_html=True)

st.subheader(" :blue[**Implementación de la fibra óptica en Inglaterra**]")
st.markdown("""<p style='text-align:justify;'> La implementación de la fibra óptica en Inglaterra ha sido un proceso continuo y progresivo, 
    impulsado por la creciente demanda de conectividad de alta velocidad en todo el país. En los últimos años, se ha observado un aumento 
    significativo en la extensión de la red de fibra óptica, con un enfoque particular en áreas urbanas y suburbanas densamente pobladas. 
    Esta expansión ha sido respaldada por inversiones tanto del sector privado como del gobierno, con el objetivo de mejorar la infraestructura 
    de comunicaciones y promover la competitividad económica.</p>""",unsafe_allow_html=True)

images = ['Gatwick.jpg',
          'TowerBridge.jpg',
          'StPauls.jpg',
          'BritishMuseum.jpg',
          'Kensington.jpg',
          'Buckingham.jpg',
          'BigBen.jpg']

# Mostrar las imágenes en una disposición en mosaico
image_index = st.slider('Sedes en donde se desplegara el servicio', 0, len(images)-1)

# Mostrar la imagen seleccionada
st.image(images[image_index], use_column_width=True)
            

# Crear un mapa de Folium
m = folium.Map(location=[51.359865, -0.118092], zoom_start=10)

st.markdown("""<p style='text-align: justify;'>Graficamente se puede observar en el 
            siguiente mapa el despliegue, la cobertura que tendra el servicio,
            los componentes utilizados y la posible ruta que tomara la fibra optica
            a las diferentes sedes<br></br></p>""",unsafe_allow_html=True)

# Definir información de las sedes
sedes = [
    {
        "Punto": "Gatwick Airport",
        "Lat": 51.1537,
        "Lon": -0.1821,
        "Componentes": [
            "Nodo central de fibra óptica : 8 puertos GPON : Tp-link",
            "Splitters de fibra óptica : Splitter-1x16 : Huawei",
            "Cables de fibra óptica : Cable-Fibra-Optica-10G-Monomodo : Huawei",
        ],
    },
    {
        "Punto": "Tower Bridge",
        "Lat": 51.5055,
        "Lon": -0.0754,
        "Componentes": [
            "Nodo central de fibra óptica : OLT-GPON-8 : Tp-link",
            "Splitters de fibra óptica : Splitter-1x8 : Huawei",
            "Cables de fibra óptica : Cable-Fibra-Optica-10G-Monomodo : Corning",
        ],
    },
    {
        "Punto": "St. Paul's Cathedral",
        "Lat": 51.5138,
        "Lon": -0.0984,
        "Componentes": [
            "Nodo central de fibra óptica : OLT-GPON-8 : Tp-link",
            "Splitters de fibra óptica : Splitter-1x4 : Huawei",
            "Cables de fibra óptica : Cable-Fibra-Optica-10G-Monomodo : Corning",
        ],
    },
    {
        "Punto": "British Museum",
        "Lat": 51.5194,
        "Lon": -0.1270,
        "Componentes": [
            "Nodo central de fibra óptica : OLT-GPON-8 : Tp-link",
            "Splitters de fibra óptica : Splitter-1x8 : Huawei",
            "Cables de fibra óptica : Cable-Fibra-Optica-10G-Monomodo : Corning",
        ],
    },
    {
        "Punto": "Kensington Palace",
        "Lat": 51.5051,
        "Lon": -0.1876,
        "Componentes": [
            "Nodo central de fibra óptica : OLT-GPON-8 : Tp-link",
            "Splitters de fibra óptica : Splitter-1x8 : Huawei",
            "Cables de fibra óptica : Cable-Fibra-Optica-10G-Monomodo : Corning",
        ],
    },
    {
        "Punto": "Buckingham Palace",
        "Lat": 51.5014,
        "Lon": -0.1419,
        "Componentes": [
            "Nodo central de fibra óptica : OLT-GPON-8 : Tp-link",
            "Splitters de fibra óptica : Splitter-1x4 : Huawei",
            "Cables de fibra óptica : Cable-Fibra-Optica-10G-Monomodo : Corning",
        ],
    },
    {
        "Punto": "Big Ben",
        "Lat": 51.5007,
        "Lon": -0.1246,
        "Componentes": [
            "Nodo central de fibra óptica : OLT-GPON-8 : Tp-link",
            "Splitters de fibra óptica : Splitter-1x4 : Huawei",
            "Cables de fibra óptica : Cable-Fibra-Optica-10G-Monomodo : Corning",
        ],
    },
]

# Coordenadas de la ruta de la fibra óptica (Gatwick -> T Bridge -> St Paul's -> British M -> Kensington P -> Buckingham P -> Big Ben)
fibra_optica_route = [(51.1537, -0.1821),
                      (51.5055, -0.0754),
                      (51.5138, -0.0984),
                      (51.5194, -0.1270),
                      (51.5051, -0.1876),
                      (51.5014, -0.1419),
                      (51.5007, -0.1246)]

cell_tower = {

    'coverage_radius': 1000,  # Radio de cobertura en metros
    'num_sides': 6,  # Número de lados del polígono (forma de panal)
    'border_color': 'purple',  # Color del borde del marcador
    'fill_color': 'green',  # Color del relleno del marcador
    'fill_opacity': 0.2  # Opacidad del relleno del marcador
}

for sede in sedes:
    sede_html = f"<b>{sede['Punto']}</b><br>"
    for componente in sede['Componentes']:
        sede_html += f"- {componente}<br>"
    
    folium.Marker(
        location=[sede['Lat'], sede['Lon']],
        icon=folium.Icon(color='red'),  # Cambiar el color del marcador a naranja
        popup=folium.Popup(sede_html, max_width=300),
        tooltip=sede['Punto']
    ).add_to(m)


for coord in fibra_optica_route:
    folium.Circle(
        location=coord,
        radius=cell_tower['coverage_radius'],  # Radio de cobertura
        number_of_sides=cell_tower['num_sides'],  # Número de lados (forma de panal)
        color=cell_tower['border_color'],  # Color del borde del marcador
        fill_color=cell_tower['fill_color'],  # Color del relleno del marcador
        fill_opacity=cell_tower['fill_opacity']  # Opacidad del relleno del marcador
    ).add_to(m)

# Trazar la ruta de la fibra óptica en el mapa
folium.PolyLine(locations=fibra_optica_route, color='blue', weight=3).add_to(m)

# Llamar a la función para renderizar el mapa de Folium en Streamlit
st_data = st_folium(m, width=700)

st.write("# :red[COMPONENTES NECESARIOS]", align="center", style={"background-color": "#FF8C00"})

st.markdown("""<p style='text-align: justify;'> El proyecto implica el despliegue de fibra óptica desde el nodo central, ubicado en el 
    Aeropuerto de Gatwick, hasta los distintos puntos de interés de Londres. La red se organizará en células para facilitar la gestión y 
    el mantenimiento, asegurando así una conectividad eficiente y confiable en cada ubicación emblemática</p>""",unsafe_allow_html=True)

st.subheader("**Equipos necesarios:**")
st.markdown("""<p>
            🔴 Nodo central de fibra óptica<br></br>
            🟢 Splitters de fibra óptica<br></br>
            🟡 Cables de fibra óptica<br></br>
            🟣 Herramientas de instalación
            </p>
            """,unsafe_allow_html=True)

st.subheader(" :blue[**Nodo central de fibra óptica**]")

st.markdown("""<p style='text-align: justify;'> Este es un dispositivo que actúa como punto de conexión primario para la red de fibra óptica. 
    El nodo central del proyecto, ubicado en el Aeropuerto de Gatwick, está diseñado para soportar hasta 16 puertos de entrada y salida, lo 
    que facilitará la conexión de hasta 16 splitters de fibra óptica.

Para este proyecto específico de despliegue de fibra óptica en los diferentes puntos de interés de Londres, se recomienda utilizar una 
OLT con capacidad para 8 puertos. Esta cantidad de puertos permitirá conectar los splitters de fibra óptica necesarios y aún dejar un 
número de puertos adicionales para futuras expansiones o reservas.

La OLT GPON DeltaStream de 8 puertos PON será la elección ideal para este proyecto. Se ubicará estratégicamente en el Aeropuerto de Gatwick, 
sirviendo como el punto central de conexión para los diversos puntos de interés en Londres. Esta ubicación central garantizará un rendimiento 
óptimo de la red y facilitará la gestión y el mantenimiento de la infraestructura de fibra óptica en toda la ciudad.</p>""",unsafe_allow_html=True)

image = Image.open('OLT.png')
st.image(image, caption='GPON Optical Line Terminal')

st.subheader(":orange[**Splitters de fibra óptica**]")

st.markdown("""<p style='text-align: justify;'>Los splitters de fibra óptica son componentes que dividen la señal de fibra óptica en 
            varias señales más pequeñas. Se utilizan para conectar múltiples usuarios a la red de fibra óptica<br>
            Los splitters de fibra óptica se dividirán de la siguiente manera:<br><br>
                Punto Aeropuerto Gatwick: 1 splitter de 1x16 (16 salidas)<br><br>
                Punto Tower Bridge: 1 splitter de 1x8 (8 salidas)<br><br>
                Punto San Pablo: 1 splitters de 1x4 (4 salidas)<br><br>
                Punto British Museum: 1 splitter de 1x8 (8 salidas)<br><br>
                Punto Kensington Palace: 1 splitter de 1x8 (8 salidas)<br><br>
                Punto Buckingham Palace: 1 splitter de 1x4 (4 salidas)<br><br>
                Punto Big Ben: 1 splitter de 1x4 (4 salidas)</p>""",unsafe_allow_html=True)

splitter = Image.open('splitter.png')
st.image(splitter, caption='Splitter 1x16')