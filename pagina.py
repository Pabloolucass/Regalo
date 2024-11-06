import streamlit as st
import time
from streamlit_option_menu import option_menu
from datetime import datetime
import pandas as pd
import pydeck as pdk
from PIL import ImageFilter, Image

# Contraseña de acceso
PASSWORD = "mirando las estrellas me acordé de ti"

clave = PASSWORD.split()
# Ubicación
lat, lon = 39.56939, 2.65024  # Zielo de levante

# Fecha y hora objetivo (14 de noviembre a las 00:00)
target_date = datetime(2024, 11, 14, 0, 0, 0)

# image, col_menu = st.columns((0.2,0.8))

pistas = ['Inicio', "Cuenta", "MLEMADT", "..."]

cant = 1.41

pis1 = False

movimientos = {
    'Vuelo Valencia_Mallorca': -15.00,
    'Autobús Alicante_Granada - 02/07/2024': -3.72,
    'Hotel Zielo de Levante - 05/02/2024': -40.00,
    'Ryanair Valencia_Viena - 15/12/2023': -98.00,
    'Renfe Alicante_Valencia - 05/09/2023': -20.00,
    'Amanecer - 15/07/2023': -0.0,
    'Fuegos artificiales - 25/07/2023' : -5.5,
    'Autobús hogueras - 24/06/2023': -1.45,
    'Copity PAU - 08/06/2023': -6.00,
    'Ruta del bacalao - 29/12/2022': -5.5
}

#difuminar imagen
def load_and_blur_image(image_path, blur_radius=5):
    image = Image.open(image_path)
    blurred_image = image.filter(ImageFilter.GaussianBlur(radius=blur_radius))
    return blurred_image

def main():
    with st.sidebar:
        selected = option_menu(
            menu_title="",
            options= pistas,
            icons=['tic',"money", "tic", "tic"],
            menu_icon= 'tic',
            default_index=0
        )
    if selected == pistas[0]:
        # Título de la cuenta regresiva y texto adicional
        st.markdown("<h1 style='text-align: center;'>2005 (MLEMADT)</h1>", unsafe_allow_html=True)

        # Crear un contenedor para la cuenta regresiva
        countdown_container = st.empty()
        st.subheader('')

        left_co, cent_co,last_co = st.columns(3)
        with cent_co:
            st.image('luna 22% buena.png', caption= '22%')
        st.title('')

        cara1, cara2 = st.columns(2)

        with cara1:
                    # Muestra la imagen difuminada
            st.image(load_and_blur_image('2.png', blur_radius=156), use_column_width=True)
        with cara2:
            st.image(load_and_blur_image('3.png', blur_radius=156), use_column_width=True)
        
        while True:
            now = datetime.now()
            time_left = target_date - now

            if time_left.total_seconds() > 0:
                # Calcula días, horas, minutos y segundos restantes
                days, seconds = divmod(time_left.total_seconds(), 86400)
                hours, seconds = divmod(seconds, 3600)
                minutes, seconds = divmod(seconds, 60)

                # Muestra la cuenta regresiva con el formato y estilo deseados
                countdown_container.markdown(
                    f"""
                    <div style='display: flex; justify-content: center; font-size: 80px; color: black;'>
                        <div style='text-align: center; margin: 0 20px;'>
                            <div>{int(days):02}</div>
                            <small style='font-size: 24px;'>días</small>
                        </div>
                        <div>:</div>
                        <div style='text-align: center; margin: 0 20px;'>
                            <div>{int(hours):02}</div>
                            <small style='font-size: 24px;'>horas</small>
                        </div>
                        <div>:</div>
                        <div style='text-align: center; margin: 0 20px;'>
                            <div>{int(minutes):02}</div>
                            <small style='font-size: 24px;'>minutos</small>
                        </div>
                        <div>:</div>
                        <div style='text-align: center; margin: 0 20px;'>
                            <div>{int(seconds):02}</div>
                            <small style='font-size: 24px;'>segundos</small>
                        </div>
                    </div>
                    <h3 style='text-align: center;'>14 de noviembre de 2024</h3>
                    """,
                    unsafe_allow_html=True
                )

                time.sleep(1)


            else:
                countdown_container.markdown("<h1 style='text-align: center; color: green;'>¡La cuenta regresiva ha terminado!</h1>", unsafe_allow_html=True)
                break
    
    if selected == pistas[1]:
        # CSS para estilo personalizado
        st.markdown(
        """
        <style>
            .header {
                text-align: center;
                font-size: 24px;
                font-weight: bold;
                margin-bottom: 20px;
            }
            .balance-container {
                text-align: center;
                font-size: 36px;
                font-weight: bold;
                color: black;
                margin: 10px 0;
            }
            .amount {
                text-align: center;
                font-size: 40px;
                color: #000;
            }
            .icon-container {
                text-align: right;
                margin-top: -50px;
                margin-right: 10px;
            }
            .icon {
                font-size: 24px;
                margin-left: 5px;
                color: #888;
            }
        </style>
        """,
        unsafe_allow_html=True
        )

        # Mostrar la cabecera
        st.markdown("<div class='header'>Saldo</div>", unsafe_allow_html=True)

        # Mostrar el nombre del titular y el saldo
        st.markdown("<div class='balance-container'>SARA RIPOLL</div>", unsafe_allow_html=True)
        st.markdown('---')
        st.markdown(f"<div class='amount'>{cant} €</div>", unsafe_allow_html=True)
        st.markdown('---')
                
        st.markdown("<div class='header'>Movimientos</div>", unsafe_allow_html=True)
        st.markdown('---')
        for mov, dinero in movimientos.items():
            st.subheader(mov)
            st.subheader(f'{dinero} €')
            st.markdown('---')

    if selected == pistas[2]:
        
        m= st.text_input('M')
        l= st.text_input('L')
        e= st.text_input('E')
        me= st.text_input(' M')
        a= st.text_input('A')
        d= st.text_input('D')
        t= st.text_input('T')

        if st.button('ingresar'):
            if m == clave[0] and l == clave[1] and e == clave[2] and me == clave[3] and a == clave[4] and d == clave[5] and t == clave[6]:
                # cara1, cara2 = st.columns(2)

                # with cara1:
                #     # Muestra la imagen difuminada
                #     st.image(load_and_blur_image('2.png', blur_radius=150), use_column_width=True)
                # with cara2:
                #     st.image(load_and_blur_image('3.png', blur_radius=150), use_column_width=True)
                left_co, cent,last_co = st.columns(3)
                with cent:
                    st.image(load_and_blur_image('qr.png', blur_radius=0))             
                
                left_co, cen,last_co = st.columns(3)
                with cen:
                    st.subheader("fbdm'h nhsfjaz")
                map_data = pd.DataFrame({"lat": [lat], "lon": [lon]})
                st.pydeck_chart(pdk.Deck(
                    map_style="mapbox://styles/mapbox/satellite-streets-v11",  # Mapa satélite con etiquetas
                    initial_view_state=pdk.ViewState(
                        latitude=lat,
                        longitude=lon,
                        zoom=9,
                        pitch=0,
                    ),
                    layers=[
                        pdk.Layer(
                            "ScatterplotLayer",
                            data=map_data,
                            get_position="[lon, lat]",
                            get_color="[0, 0, 0, 0]",
                            get_radius=600,
                        ),
                        pdk.Layer(
                            "IconLayer",
                            data=map_data,
                            get_icon="pin",
                            get_size=4,
                            get_position=["lon", "lat"],
                            pickable=True,
                            icon_atlas="https://raw.githubusercontent.com/visgl/deck.gl-data/master/website/icon-atlas.png",
                            icon_mapping={
                                "pin": {
                                    "x": 0,
                                    "y": 0,
                                    "width": 128,
                                    "height": 128,
                                    "anchorY": 128,
                                }
                            },
                        )
                    ],
                ))
                left_co, ce,last_co = st.columns(3)
                with ce:
                    st.markdown('Donde todo empieza')

    if selected == pistas[3]:
        st.title('??????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????')

# def login():
#     st.title("Acceso a la página")
#     password = st.text_input("Ingresa la contraseña:", type="password")
    
#     # Botón para confirmar la contraseña
#     if st.button("Ingresar"):
#         if password == PASSWORD:
#             st.session_state["acceso"] = True
#             # st.rerun()  # Recarga la página para mostrar el contenido
#         else:
#             st.error("Contraseña incorrecta. Inténtalo de nuevo.")

# Verifica si el usuario ha ingresado correctamente la contraseña
main()  # Muestra la página principal si la contraseña es correcta
# else:
#     login()  # Solicita la contraseña
