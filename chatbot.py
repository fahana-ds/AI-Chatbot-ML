import json
import random

# Load JSON file
with open("intents.json") as file:
    data = json.load(file)

# Function to get response
def chatbot_response(user_input):
    user_input = user_input.lower()

    for intent in data["intents"]:
        for pattern in intent["patterns"]:
            if pattern in user_input:
                return random.choice(intent["responses"])

    return "Sorry, I didn't understand that."

# Chat loop
while True:
    message = input("You: ")
    
    if message.lower() == "exit":
        print("Bot: Goodbye!")
        break

    response = chatbot_response(message)
    print("Bot:", response)
    