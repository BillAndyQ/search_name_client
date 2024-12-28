import re
import json
from flask import Flask, jsonify, request
import requests

app = Flask(__name__)

@app.route('/consulta_dni', methods=['POST'])
def consulta_dni():
    # Obtener el número de DNI desde el JSON enviado en la solicitud
    dni = request.json.get('dni', None)

    if not dni:
        return jsonify({'error': 'DNI no proporcionado'}), 400

    # URL del endpoint
    url = "https://dniperu.com/querySelector"

    # Datos que se envían en la solicitud POST (ajustado al formulario)
    data = {
        'dni4': dni,  # Número de DNI proporcionado en el cuerpo de la solicitud
        'buscar_dni': 'Buscar'  # El nombre del botón en el formulario, aunque generalmente no es necesario
    }

    # Encabezados necesarios para la solicitud (simula un navegador real)
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
        'Accept': '*/*',
        'Accept-Encoding': 'gzip, deflate, br, zstd',
        'Accept-Language': 'es-419,es;q=0.9',
        'Origin': 'https://dniperu.com',
        'Referer': 'https://dniperu.com/buscar-dni-nombres-apellidos/',
        'Content-Type': 'application/x-www-form-urlencoded',  # Cambié a application/x-www-form-urlencoded
        'X-Content-Type-Options': 'nosniff',
        'X-Frame-Options': 'DENY',
        'X-XSS-Protection': '1; mode=block',
        'Cookie': 'PHPSESSID=8e742c219d48e1fc96c24495db7e68a6'  # Si la cookie es necesaria
    }

    try:
        # Realizar la solicitud POST
        response = requests.post(url, data=data, headers=headers)

        data = json.loads(response.text)

        # Extraer el valor de 'mensaje'
        mensaje = data['mensaje']

        # Extraer los valores correctos utilizando los delimitadores
        nombre = mensaje.split('Nombres: ')[1].split('\n')[0]  # Obtener 'BILL ANDY'
        apellido_paterno = mensaje.split('Apellido Paterno: ')[1].split('\n')[0]  # Obtener 'QUISPE'
        apellido_materno = mensaje.split('Apellido Materno: ')[1].split('\n')[0]  # Obtener 'MARTINEZ'

        # Almacenar los valores en el diccionario 'data'
        nombre = apellido_paterno + " " + apellido_materno + " "  + nombre

        # Si la respuesta es exitosa, devolver el contenido
        if response.status_code == 200:
            return jsonify({'status': 'success', 'nombre': nombre}), 200
        else:
            return jsonify({'error': 'Error al hacer la solicitud', 'status_code': response.status_code}), response.status_code

    except requests.exceptions.RequestException as e:
        # Manejar cualquier error en la solicitud
        return jsonify({'error': str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True)
