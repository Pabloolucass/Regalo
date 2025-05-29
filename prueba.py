cant = 1.41
blur1 = 90
blur2 = 35
id_cheque = '76696e696c6f'
beneficiario = 'sara ripoll moreno'
dinero = 40
usado = True
email_sender = 'mlemadtexpress@gmail.com'
password = 'mltp jfbx rxwy nlkg'
ID = '74652071756965726f'
gmail = 'sararipoll@icloud.com'
cargado = False
done = False
shipping_history = [
                        # {"date": "14/11/2024", "time": "00:00", "status": "Paquete en destino", "location": "ALICANTE, ESPAÑA", "icon": "✅", "image": "granada.jpg"},
                        {"date": "14/11/2024", "time": "17:00", "status": "Paquete próximo a destino", "location": "GUARDAMAR, ESPAÑA", "icon": "🚚", "image": "guardamar.jpg"},
                        {"date": "13/11/2024", "time": "21:00", "status": "Paquete en tránsito hacia destino", "location": "MURCIA, ESPAÑA", "icon": "🚚", "image": "granada.jpg"},
                        {"date": "13/11/2024", "time": "15:00", "status": "Paquete llegado a territorio nacional", "location": "GRANADA, ESPAÑA", "icon": "🚚", "image": "granada.jpg"},
                        {"date": "12/11/2024", "time": "21:00", "status": "Pedido enviado a destino", "location": "VIENA, AUSTRIA", "icon": "🚚", "image": "viena 4.jpg"},                        
                        {"date": "12/11/2024", "time": "19:00", "status": "Preparando pedido para el envío", "location": "VIENA, AUSTRIA", "icon": "📦", "image": "viena 3.png"},
                    ]
new_entry = {
    "date": "13/11/2024",
    "time": "22:45",
    "status": "Paquete en reparto",
    "location": "ALICANTE, ESPAÑA",
    "icon": "🚚",
    "image": "alicante 1.jpg"
}

movimientos = {
    'Enfoque imagen PHOTO RESTORATION - 07/11/2024': -40.00,
    'Cheque COM - 07/11/2024': '+40.0',
    'Vuelo Valencia_Mallorca - 04/10/2024': -15.00,
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

count = 0
body_oferta = '''
    <html>
    <head>
        <meta charset="UTF-8">
        <title>Información importante de MLEMADT Express</title>
    </head>
    <body style="font-family: Arial, sans-serif; background-color: #f8f8f8; padding: 20px;">
        <table width="100%" cellspacing="0" cellpadding="0" style="max-width: 600px; margin: auto; background-color: #ffffff; border-radius: 8px; overflow: hidden;">
            <tr>
                <td style="padding: 30px; text-align: center;">
                    <h2 style="color: #2f84d3;">Hola,</h2>
                    <p style="font-size: 16px; color: #333;">
                        Queremos informarte sobre una novedad disponible en nuestra plataforma. Puedes acceder a más detalles a través del siguiente enlace:
                    </p>
                    <a href="https://mlemadt.streamlit.app" target="_blank"
                        style="display: inline-block; margin-top: 20px; padding: 12px 24px; background-color: #2f84d3; color: #fff; text-decoration: none; border-radius: 5px; font-weight: bold;">
                        Acceder a la plataforma
                    </a>
                    <p style="font-size: 14px; color: #666; margin-top: 30px;">
                        Si tienes alguna pregunta, no dudes en responder a este correo.
                    </p>
                    <p style="font-size: 14px; color: #666;">Gracias por confiar en MLEMADT Express.</p>
                </td>
            </tr>
        </table>
    </body>
    </html>
'''
subject_oferta = 'Hola cliente, tenemos una noticia que quizá te pueda interesar'

body_qr='''
<html>
<head>
    <meta charset="UTF-8">
    <title>Tu vale exclusivo de MLEMADT Express</title>
</head>
<body style="font-family: Arial, sans-serif; background-color: #f8f8f8; padding: 20px;">
    <table width="100%" cellspacing="0" cellpadding="0" style="max-width: 600px; margin: auto; background-color: #ffffff; border-radius: 8px; overflow: hidden;">
        <tr>
            <td style="padding: 30px; text-align: center;">
                <h2 style="color: #2f84d3;">¡Tu vale exclusivo ha llegado!</h2>
                <p style="font-size: 16px; color: #333;">
                    Aquí tienes tu vale para canjear hoy, <strong>29 de mayo de 2025</strong>.
                </p>
                <p style="font-size: 14px; color: #666; margin-top: 30px;">
                    Recuerda que es válido solo para hoy, así que no pierdas la oportunidad.
                </p>
                <p style="font-size: 14px; color: #666;">
                    Si tienes alguna pregunta, estamos aquí para ayudarte.
                </p>
                <p style="font-size: 14px; color: #666;">Gracias por confiar en <strong>MLEMADT Express</strong>.</p>
            </td>
        </tr>
    </table>
</body>
</html>
'''
