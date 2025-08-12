📄 resumen_openai
Aplicación de prueba técnica que utiliza la API de OpenAI para generar resúmenes automáticos de textos.
El proyecto está desarrollado con Node.js y Express, y expone un endpoint que recibe texto y devuelve un resumen procesado por IA.

🚀 Características
🧠 Genera resúmenes automáticos usando OpenAI API.

🌐 API REST construida con Node.js + Express.

⚡ Respuestas rápidas y precisas.

📦 Código limpio y fácil de entender.

🛠️ Tecnologías utilizadas
Node.js

Express

OpenAI API

📥 Instalación y uso
Clonar el repositorio

bash
Copiar
Editar
git clone https://github.com/tu-usuario/resumen_openai.git
cd resumen_openai
Instalar dependencias

bash
Copiar
Editar
npm install
Configurar variables de entorno
Crea un archivo .env en la raíz con:

env
Copiar
Editar
OPENAI_API_KEY=tu_api_key_aqui
PORT=3000
Iniciar el servidor

bash
Copiar
Editar
npm start
El servidor se ejecutará en http://localhost:3000.

📡 Endpoint disponible
POST /resumen
Recibe un texto y devuelve su resumen.

Ejemplo de request:

json
Copiar
Editar
{
  "texto": "Aquí va el texto largo que quieres resumir..."
}
Ejemplo de respuesta:

json
Copiar
Editar
{
  "resumen": "Este es el resumen generado por la IA."
}
📌 Notas
Es necesario contar con una API Key de OpenAI.

Se recomienda no enviar textos extremadamente extensos debido a las limitaciones de tokens de la API
