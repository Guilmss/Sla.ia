import os
from dotenv import load_dotenv
from groq import Groq  # Certifique-se de que esta linha está presente
import streamlit as st

# Carrega as variáveis de ambiente do arquivo .env
load_dotenv()

# Verifica se a chave foi carregada
api_key = os.environ.get("GROQ_API_KEY")
if not api_key:
    st.error("A chave de API não foi encontrada. Configure a variável de ambiente 'GROQ_API_KEY' no arquivo '.env'.")
    st.stop()

# Configuração do cliente Groq
client = Groq(
    api_key=api_key,
)

# Configuração da interface Streamlit
st.image("SLA.png", width=500)  # Substitua "logo.png" pelo caminho da sua imagem
st.write("💬Digite sua mensagem abaixo para interagir com o modelo.💬")

# Campo de entrada do usuário
user_input = st.text_input("Você:", placeholder="Digite sua mensagem aqui...")

# Botão para enviar a mensagem
if st.button("Enviar"):
    if user_input.strip() == "":
        st.warning("Por favor, digite uma mensagem antes de enviar.")
    else:
        try:
            # Envia a entrada do usuário para o modelo
            chat_completion = client.chat.completions.create(
                messages=[
                    {
                        "role": "user",
                        "content": user_input,
                    }
                ],
                model="llama-3.3-70b-versatile",
            )

            # Exibe a resposta do modelo
            response = chat_completion.choices[0].message.content
            st.success(f"SLA Bot diz: {response}")
        except Exception as e:
            st.error(f"Ocorreu um erro: {e}")

st.markdown("---")
st.markdown("Desenvolvido por [Guilmss.Dev](https://github.com/Guilmss).")
