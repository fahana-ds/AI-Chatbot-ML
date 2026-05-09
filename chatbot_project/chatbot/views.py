import json
import random
import pickle
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

# Load files
with open("chatbot/intents.json") as file:
    data = json.load(file)

model = pickle.load(open("chatbot/model.pkl", "rb"))
vectorizer = pickle.load(open("chatbot/vectorizer.pkl", "rb"))

@csrf_exempt
def chatbot_api(request):
    if request.method == "POST":
        user_input = request.POST.get("message")

        X = vectorizer.transform([user_input])
        predicted_tag = model.predict(X)[0]

        for intent in data["intents"]:
            if intent["tag"] == predicted_tag:
                return JsonResponse({
                    "response": random.choice(intent["responses"])
                })

        return JsonResponse({"response": "Sorry, I didn't understand."})