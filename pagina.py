import streamlit as st
import time
from streamlit_option_menu import option_menu
from datetime import datetime
import pandas as pd
import pydeck as pdk
from PIL import ImageFilter, Image
import prueba

# Contraseña de acceso
PASSWORD = "mirando las estrellas me acordé de ti"

clave = PASSWORD.split()
# Ubicación
lat, lon = 39.56939, 2.65024  # Zielo de levante

# Fecha y hora objetivo (14 de noviembre a las 00:00)
target_date = datetime(2024, 11, 14, 21, 30, 0)

# image, col_menu = st.columns((0.2,0.8))

pistas = ['Inicio', "M.L.E.M.A.D.T. BANK",'PHOTO RESTORATION', "MLEMADT", '...']

tienda = {
    'Enfocar imagen 50%': 40,
    'Enfocar imagen 100%': 70,
    'Restaurar foto antigua': 100,
    'Retoque fotográfico': 65,
    'Pasar imagen a color': 46
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
            icons=['tic',"money", "tic", "tic", 'tic'],
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
            st.image('luna 32% buena.png', caption= '32%')
        st.title('')

        cara1, cara2 = st.columns(2)

        with cara1:
                    # Muestra la imagen difuminada
            st.image(load_and_blur_image('foto granada.png', blur_radius=prueba.blur1), use_column_width=True)
        with cara2:
            st.image(load_and_blur_image('qr bonito.png', blur_radius=prueba.blur2), use_column_width=True)
        
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
        st.image('banco.png') 
        page = st.radio("Selecciona una opción:", ['Inicio', "Saldo y movimientos", "Reclamar cheque"])

        if page == "Reclamar cheque":
            st.subheader("Formulario para reclamar cheque")

            # Ingresar ID y nombre de la persona
            id_cheque = st.text_input("Ingresa el ID del cheque")
            nombre_persona = st.text_input("Ingresa el nombre del beneficiario (Nombre y apellidos)").lower()

            if st.button("Enviar reclamo"):
                if (id_cheque == prueba.id_cheque) and (nombre_persona == prueba.beneficiario) and(prueba.usado == False):
                    st.success(f"Cheque de {prueba.dinero}€ reclamado con éxito por {nombre_persona} (ID: {id_cheque}).")
                    prueba.cant += prueba.dinero
                    prueba.movimientos['Cheque COM - 07/11/2024'] =  prueba.dinero
                    prueba.usado = True
                else:
                    st.error("Por favor, revisa que la información sea correcta.")
        elif page == 'Inicio':
            pass
            
        elif page == 'Saldo y movimientos':
            # Mostrar la cabecera
            st.markdown("<div class='header'>Saldo</div>", unsafe_allow_html=True)

            # Mostrar el nombre del titular y el saldo
            st.markdown("<div class='balance-container'>SARA RIPOLL</div>", unsafe_allow_html=True)
            st.markdown('---')
            st.markdown(f"<div class='amount'>{prueba.cant:.2f} €</div>", unsafe_allow_html=True)
            st.markdown('---')
                    
            st.markdown("<div class='header'>Movimientos</div>", unsafe_allow_html=True)
            st.markdown('---')
            if prueba.pago_hecho:
                st.subheader('Enfoque imagen PHOTO RESTORATION - 07/11/2024')
                st.subheader('-40.0 €')
                st.markdown('---')
            if prueba.usado:
                st.subheader('Cheque COM - 07/11/2024')
                st.subheader('+40.0 €')
                st.markdown('---')
            for mov, dinero in prueba.movimientos.items():
                st.subheader(mov)
                st.subheader(f'{dinero} €')
                st.markdown('---')

    if selected == pistas[3]:
        
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
                
                with cent:
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
                with cent:
                    st.markdown('Dónde todo empieza')

    if selected == pistas[2]:
        left_co, middle,last_co = st.columns(3)
        with left_co:
            st.image('rest fotos logo.png', width= 580,)
        st.markdown('---')

        st.markdown(f"<div class='subtitulo'>Servicios</div>", unsafe_allow_html=True)

        for producto, precio in tienda.items():
            
            st.markdown('---')

            st.markdown(
            """
            <style>
                .subtitulo {
                    text-align: center;
                    font-size: 34px;
                    font-weight: bold;
                    margin-bottom: 10px;
                    margin-right: 175px;
                }
                .header {
                    text-align: center;
                    font-size: 24px;
                    font-weight: bold;
                    margin-bottom: 10px;
                    margin-right: 175px;
                }
                hr {
                    border: 0;
                    height: 5px; /* Grosor de la línea */
                    background-color: #000; /* Color de la línea */
                    width: 78%; /* Ocupa todo el ancho */
                }
            </style>
            """, unsafe_allow_html= True)
            st.markdown(f"<div class='header'>{producto}</div>", unsafe_allow_html=True)

            left_c, c,last_co = st.columns(3)
            with c:
                if st.button(f'💳 {precio} €'):
                    if prueba.cant >= precio:
                        st.success('Se ha realizado el pago correctamente')
                        prueba.cant -= precio
                        prueba.blur2 = 30
                        prueba.blur1 = 90
                        prueba.pago_hecho = True

                    else:
                        st.error('No tienes dinero suficiente')
        st.title('')
        s1,s2,s3,s4,s5, s6, s7, s8, s9 = st.columns(9)

        with s1:
            st.button('Pag 1')
        with s2:
            st.button('Pag 2')
        with s3:
            st.button('Pag 3')
        with s4:
            st.subheader('........')
        with s5:
            st.subheader('........')
        with s6:
            st.subheader('.......')
        with s7:
            st.button('Pag 9')


    if selected == pistas[4]:
        
        pass
            

    if selected == pistas[4]:
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
