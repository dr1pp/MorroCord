import asyncio
import discord
import interactions
import random as rand

from interactions import Option, OptionType, SelectMenu, SelectOption, ActionRow, ButtonStyle, Button, TextInput, Modal
from discord.ui import Select, View
from discord.ext import commands
from token_secret import TOKEN
from classes import PLAYER_ATTRIBUTES
from components import *

GUILD_ID = 332927745044774914

bot = interactions.Client(TOKEN)


@bot.event
async def on_ready():
    print("MorroCord online!")
    emojis = await discord.utils.get(bot.guilds, name="MorroCord Emojis").get_all_emoji()
    for emoji in emojis:
        if emoji.name.startswith("attribute"):
            for attribute in PLAYER_ATTRIBUTES:
                if emoji.name.endswith(emoji.name):
                    attribute.emoji = emoji
        else:
            pass


@bot.command(name="prophecy",
             description="Begin your journey into Vvardenfell",
             scope=GUILD_ID)
async def create_character(ctx):
    await ctx.popup(name_form)


@bot.modal("character_name_form")
async def character_name_form_response(ctx, response: str):
    await ctx.send(f"Welcome to Vvardenfell, {response}!\n", components=race_select, ephemeral=True)


@bot.component(race_select)
async def race_select_response(ctx, selection: str):
    race = selection[0]
    await ctx.edit(
        f"Of course, a{'n ' if race[0].lower() in 'aeiou' else ' '}{race}! Now, how do you approach your battles?",
        components=specialization_row)

@bot.component("combat_selected")
async def combat_selected(ctx):
    pass


@bot.component("magic_selected")
async def magic_selected(ctx):
    pass


@bot.component("stealth_selected")
async def stealth_selected(ctx):
    pass


bot.start()