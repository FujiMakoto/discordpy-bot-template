from discordbot.config import config
from discordbot.discordbot import bot

bot.run(config.get('Discord', 'token'))
