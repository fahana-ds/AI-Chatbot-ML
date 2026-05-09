import json
import random
import pickle

# Load data
with open("intents.json") as file:
    data = json.load(file)

model = pickle.load(open("model.pkl", "rb"))
vectorizer = pickle.load(open("vectorizer.pkl", "rb"))

def chatbot_response(user_input):
    X = vectorizer.transform([user_input])
    predicted_tag = model.predict(X)[0]

    for intent in data["intents"]:
        if intent["tag"] == predicted_tag:
            return random.choice(intent["responses"])

    return "Sorry, I didn't understand."

# Chat loop
while True:
    message = input("You: ")

    if message.lower() == "exit":
        print("Bot: Goodbye!")
        break

    print("Bot:", chatbot_response(message))