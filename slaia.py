from dotenv import load_dotenv
import os
from groq import Groq  # Certifique-se de que esta linha está presente

# Carrega as variáveis de ambiente do arquivo .env
load_dotenv()

# Verifica se a chave foi carregada
api_key = os.environ.get("GROQ_API_KEY")
print(f"API Key carregada: {api_key}")  # Para depuração

if not api_key:
    raise ValueError("A chave de API não foi encontrada. Configure a variável de ambiente 'GROQ_API_KEY' no arquivo '.env'.")

# Configuração do cliente Groq
client = Groq(
    api_key=api_key,
)

# Exemplo de uso do cliente
chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": "como fazer uma pizza",
        }
    ],
    model="llama-3.3-70b-versatile",
)

print(chat_completion.choices[0].message.content)