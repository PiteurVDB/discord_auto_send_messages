import requests
import time
import random
import sys

# Discord Token
USER_TOKEN = 'MjIwNTY3ODUzNjY3OTc1MTY4.G_JjZR.8M3-9mladwI7A56Y3NvvydPxVWJkYMKHVKfufM'
# ID of the discord channel
CHANNEL_ID = '1078813252433231922'

# Random messages
messages = [
    "Salut tout le monde!",
    "Comment ça va ?",
    "Ce jeu à l'air insane!",
    "Insane!",
    "De ouf.",
    "d'accord...",
    "ok, ça marche",
    "Ouais, je suis bien d'accord",
    "ahahahahha, t'as trop raison"
]

def send_and_delete_message():
    send_message_url = f'https://discord.com/api/v10/channels/{CHANNEL_ID}/messages'
    headers = {
        'Authorization': USER_TOKEN,
        'Content-Type': 'application/json'
    }
    data = {
        'content': random.choice(messages)
    }

    response = requests.post(send_message_url, headers=headers, json=data)
    message_data = response.json()

    delete_message_url = f'https://discord.com/api/v10/channels/{CHANNEL_ID}/messages/{message_data["id"]}'
    response = requests.delete(delete_message_url, headers=headers)

    if response.status_code == 204:
        print("Message sent and deleted successfully.")
    else:
        print("Failed to delete the message.")

# loop
while True:
    send_and_delete_message()
    interval = random.randint(90, 180)  # Wait for 60 seconds before sending the next message
    print(f"Next message in {interval} seconds...")

    for remaining_time in range(interval, 0, -1):
        sys.stdout.write("\r" + "Time remaining: " +str(remaining_time) + " seconds.")
        time.sleep(1)

    print(" " * 50, end="\r")  # Clear the timer line