# Consulta de dni de un cliente (Perú)
## Fines Educativos
API REST hecha en Flask, realiza scraping a una web de consultas y obtiene el nombre y apellidos del dni

1. Genera el entorno virtual
    ```bash
    virtualenv venv

2. Inicia el entorno virtual
    ```bash
    venv\Scripts\activate

3. Instala las dependencias
    ```bash
    pip install -r requirements.txt

4. Inicia el app.py
    ```bash
    py app.py

Prueba la API
```json
{
    "dni": "xxxxxxxx"
}
```

Example response
```json
{
  "nombre": "JUAN JOSE RODRIGUEZ MENDEZ",
  "status": "success"
}
```

Use la url de prueba
```bash
curl -X POST https://search-name-client.vercel.app/consulta_dni \
    -H "Content-Type: application/json" \
    -d '{"dni": "xxxxxxxx"}'
