import os
from openai import OpenAI
from dotenv import load_dotenv
from colorama import Fore

load_dotenv()
MODEL_NAME = "gpt-4o"
SYSTEM_MESSAGE = "You are a helpful assistant"
messages = [{"role": "system", "content": SYSTEM_MESSAGE}]

client = OpenAI(
    api_key=os.getenv("GITHUB_TOKEN"),
    base_url=os.getenv("ENDPOINT")
)

def generate_chat_completion(user_input=""):
    messages.append({"role": "user", "content": user_input})
    response = client.chat.completions.create(
        model=MODEL_NAME,
        messages=messages,
        temperature=0.7,
        max_tokens=200
    )
    response_message = response.choices[0].message.content
    messages.append({"role": "assistant", "content": response_message})
    print(Fore.GREEN + "AI: " + response_message.replace("\n", ""))

def start_chat():
    print("to end chat, type 'x'")
    print("\n")
    print("      NEW CHAT       ")
    print("---------------------")
    generate_chat_completion()

    while True:
        user_input = input(Fore.WHITE + "You: ")

        if user_input.lower() == "x":
            main()
            break
        else:
            generate_chat_completion(user_input)

def main():
    while True:
        print("\n")
        print("----------------------------------------\n")
        print(" *** WELCOME TO THE AI-CHATBOT🤖 *** ")
        print("\n----------------------------------------")
        print("\n================* MENU *================\n")
        print("[1]- Start Chat")
        print("[2]- Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            start_chat()
        elif choice == "2":
            exit()
        else:
            print("Invalid choice")



if __name__ == "__main__":
    main()