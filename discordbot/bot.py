from discord.ext import commands

from discordbot.config import config

bot = commands.Bot(command_prefix=[p.strip() for p in str(config.get('Bot', 'command_prefixes')).split(',')],
                   case_insensitive=True)
