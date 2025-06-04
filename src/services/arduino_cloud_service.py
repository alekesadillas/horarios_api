import os
import requests

# Variables de entorno
ARDUINO_CLIENT_ID = os.environ.get('ARDUINO_CLIENT_ID')
ARDUINO_CLIENT_SECRET = os.environ.get('ARDUINO_CLIENT_SECRET')

# Validar que las variables de entorno estén configuradas
if not ARDUINO_CLIENT_ID or not ARDUINO_CLIENT_SECRET:
    raise EnvironmentError("Faltan ARDUINO_CLIENT_ID o ARDUINO_CLIENT_SECRET en el entorno.")

THING_ID = '1b3d7355-ef20-4ef1-a3db-4a63978a44a6'
VARIABLE_NAME = 'Status'  # Asegúrate de que esté exactamente igual que en Arduino Cloud

def actualizar_status_en_arduino_cloud(nuevo_estado):
    # Paso 1: Obtener el token
    auth_url = 'https://api2.arduino.cc/iot/v1/clients/token'
    auth_data = {
        'grant_type': 'client_credentials',
        'client_id': ARDUINO_CLIENT_ID,
        'client_secret': ARDUINO_CLIENT_SECRET,
        'audience': 'https://api2.arduino.cc/iot'
    }

    try:
        auth_response = requests.post(auth_url, json=auth_data, timeout=5)
        auth_response.raise_for_status()
    except requests.RequestException as e:
        raise RuntimeError(f"Error autenticando con Arduino Cloud: {e}")

    access_token = auth_response.json().get('access_token')
    if not access_token:
        raise RuntimeError("No se pudo obtener token de acceso de Arduino Cloud.")

    # Paso 2: Enviar el nuevo estado
    headers = {
        'Authorization': f'Bearer {access_token}',
        'Content-Type': 'application/json'
    }

    try:
        variable_url = f'https://api2.arduino.cc/iot/v2/things/{THING_ID}/properties'
        propiedades_response = requests.get(variable_url, headers=headers, timeout=5)
        propiedades_response.raise_for_status()
    except requests.RequestException as e:
        raise RuntimeError(f"Error obteniendo propiedades del thing: {e}")

    propiedades = propiedades_response.json()
    propiedad_status = next((p for p in propiedades if p['name'] == VARIABLE_NAME), None)

    if not propiedad_status:
        raise RuntimeError(f"No se encontró la propiedad '{VARIABLE_NAME}' en el thing.")

    propiedad_id = propiedad_status['id']
    patch_url = f'https://api2.arduino.cc/iot/v2/things/{THING_ID}/properties/{propiedad_id}/publish'
    body = {'value': nuevo_estado.lower() == 't'}


    try:
        patch_resp = requests.put(patch_url, headers=headers, json=body, timeout=5)
        patch_resp.raise_for_status()
    except requests.RequestException as e:
        raise RuntimeError(f"Error al actualizar variable status: {e}")
