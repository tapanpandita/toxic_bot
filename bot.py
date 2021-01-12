# bot.py
import os
import tempfile
import random
import asyncio
from urllib.parse import quote
from html import unescape

import aiohttp
import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")
BRRR_URL = "https://www.youtube.com/watch?v=WEMCYBPUR00"

bot = commands.Bot(command_prefix="!")


@bot.command(name="nitish", help="Responds with toxic shit")
async def be_toxic(ctx):
    toxic_quotes = [
        "I won't need as many hours as Neel to reach his level",
        "You're just jealous",
        "You were getting carried for most stretches as a carry yourself",
        "I have better stats than you no matter which type of game I play it means I not only play my role well I play it better than you",
        "I know how the team game works better than you",
        "Even as support I had better stats than you",
        "I literally healed the entire dungeon",
        "I had most assists last 2 unfair mode games",
        "I was top of the pack in that game",
        "I was much better",
        "Lets play 1v1 bitch, I'll own your ass",
        "I literally pushed mid to win us the game",
        "Why would I be salty",
        "That's not toxic",
        "Yeah well, you won't get them",
        "I think 5 steps ahead all the time",
    ]

    response = random.choice(toxic_quotes)
    await ctx.send(response)


@bot.command(name="bj", help="Responds with a bj joke")
async def get_bj_joke(ctx):
    async with aiohttp.ClientSession() as session:
        async with session.get(
            "http://api.icndb.com/jokes/random?firstName=Bannanje&lastName=Nayak"
        ) as resp:
            result = await resp.json()
            await ctx.send(result.get("value").get("joke"))


@bot.command(name="donald", help="Responds with a djt quote")
async def get_djt_quote(ctx):
    async with aiohttp.ClientSession() as session:
        async with session.get("https://api.tronalddump.io/random/quote") as resp:
            result = await resp.json()
            await ctx.send(result.get("value"))


# @bot.command(name="joke", help="Responds with a joke")
# async def get_joke(ctx):
# async with aiohttp.ClientSession() as session:
# async with session.get("https://v2.jokeapi.dev/joke/Any") as resp:
# result = await resp.json()

# if result.get("type") == "single":
# await ctx.send(result.get("joke"))
# elif result.get("type") == "twopart":
# await ctx.send(result.get("setup"))
# await asyncio.sleep(4)
# await ctx.send(result.get("delivery"))


@bot.command(name="dog", help="Posts a random dog picture")
async def random_dog_image(ctx):
    async with aiohttp.ClientSession() as session:
        async with session.get("https://dog.ceo/api/breeds/image/random") as resp:
            dog_url = await resp.json()
            await ctx.send(dog_url.get("message"))


@bot.command(name="cat", help="Posts a random cat picture")
async def random_cat_image(ctx):
    async with aiohttp.ClientSession() as session:
        async with session.get("https://aws.random.cat/meow") as resp:
            cat_url = await resp.json()
            await ctx.send(cat_url.get("file"))


@bot.command(name="fox", help="Posts a random fox picture")
async def random_fox_image(ctx):
    async with aiohttp.ClientSession() as session:
        async with session.get("https://randomfox.ca/floof/") as resp:
            fox_url = await resp.json()
            await ctx.send(fox_url.get("image"))


@bot.command(name="food", help="Posts a random food picture")
async def random_food_image(ctx):
    async with aiohttp.ClientSession() as session:
        async with session.get("https://foodish-api.herokuapp.com/api/") as resp:
            image_url = await resp.json()
            await ctx.send(image_url.get("image"))


@bot.command(name="trivia", help="Posts a trivia question")
async def get_trivia_question(ctx, category):
    if category == "help":
        await ctx.send(
            """
Use the command "!trivia <category_id>" to get a question. You have 10 seconds to get the answer.

Use one of the following category ids -

id:9  General Knowledge
id:10 Entertainment: Books
id:11 Entertainment: Film
id:12 Entertainment: Music
id:13 Entertainment: Musicals & Theatres
id:14 Entertainment: Television
id:15 Entertainment: Video Games
id:16 Entertainment: Board Games
id:17 Science & Nature
id:18 Science: Computers
id:19 Science: Mathematics
id:20 Mythology
id:21 Sports
id:22 Geography
id:23 History
id:24 Politics
id:25 Art
id:26 Celebrities
id:27 Animals
id:28 Vehicles
id:29 Entertainment: Comics
id:30 Science: Gadgets
id:31 Entertainment: Japanese Anime & Manga
id:32 Entertainment: Cartoon & Animations
        """
        )
    else:
        async with aiohttp.ClientSession() as session:
            async with session.get(
                f"https://opentdb.com/api.php?amount=1&category={category}"
            ) as resp:
                response = await resp.json()
                result = response.get("results")[0]
                question = unescape(result.get("question"))
                options = result.get("incorrect_answers") + [
                    result.get("correct_answer")
                ]
                options = [unescape(option) for option in options]
                random.shuffle(options)
                await ctx.send(question)
                await ctx.send("\n".join(options))
                await asyncio.sleep(12)
                await ctx.send("3 seconds to go!")
                await asyncio.sleep(3)
                await ctx.send(
                    '"{}" is the correct answer!'.format(
                        unescape(result.get("correct_answer"))
                    )
                )


@bot.command(name="qr", help="Posts a qr code for the url")
async def convert_to_qr_image(ctx, data):
    data = quote(data)
    await ctx.send(
        f"https://api.qrserver.com/v1/create-qr-code/?size=250X250&data={data}"
    )


@bot.command(name="brrr", help="Posts the money printer goes brrr meme")
async def send_brrr_meme_video(ctx):
    await ctx.send(f"{BRRR_URL}")


@bot.listen()
async def on_message(message):
    if "brrr" in message.content.lower() and message.content.lower() != "!brrr":
        await message.channel.send(f"{BRRR_URL}")
        await bot.process_commands(message)


bot.run(TOKEN)
