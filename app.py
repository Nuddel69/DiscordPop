import interactions
import json

token = json.load(open('secret.json'))["token"]

bot = interactions.Client(token=token)


bot.start()
