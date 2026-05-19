from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-2.5-flash")

chat_history = []

while True:
    user_input = input("You: ")

    if user_input.lower() in ["exit", "quit"]:
        print("Exiting chat...")
        break
    
    chat_history.append({"role": "user", "content": user_input})
    
    response = model.invoke(chat_history)
    print(f"Bot: {response.content}")
    
    chat_history.append({"role": "assistant", "content": response.content})