import requests

url = "http://127.0.0.1:8000/api/chat/"

while True:
    message = input("You: ")

    if message == "exit":
        break

    response = requests.post(url, data={"message": message})
    print("Bot:", response.json()["response"])