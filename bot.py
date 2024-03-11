import nltk
from nltk.chat.util import Chat, reflections

# Definir pares de patrón-respuesta
pares = [
    [
        r"mi nombre es (.*)",
        ["Hola %1, ¿cómo puedo ayudarte hoy?",]
    ],
    [
        r"cual es tu nombre?",
        ["Mi nombre es ChatBot y estoy aquí para ayudarte.",]
    ],
    [
        r"como estas ?",
        ["Estoy bien, gracias! ¿Y tú?",]
    ],
    [
        r"disculpa (.*)",
        ["No hay problema", "No pasa nada :)",]
    ],
    [
        r"(.*) edad (.*)",
        ["Soy un programa de computadora, así que no tengo edad.",]
    ],
    [
        r"salir",
        ["Hasta luego. ¡Que tengas un buen día!",]
    ],
]

# Crear un objeto Chat a partir de los pares definidos
chatbot = Chat(pares, reflections)

def chat():
    print("¡Hola! Soy un chatbot. ¿En qué puedo ayudarte hoy?")
    while True:
        user_input = input("Tú: ")
        if user_input.lower() == "salir":
            break
        else:
            print(chatbot.respond(user_input))

# Iniciar el chat
if __name__ == "__main__":
    nltk.download('punkt')  # Descargar datos necesarios para tokenización
    chat()