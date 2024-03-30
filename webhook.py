import requests
import discord
USE_WEBHOOK = True
webhook = 1
from discord_webhook import DiscordWebhook  # Try to import discord_webhook
url = "webhook adress"
if webhook is not None:
        DiscordWebhook(  # Let the user know it has started logging the ids
            url=url,
            content=f"```Your message```").execute()
