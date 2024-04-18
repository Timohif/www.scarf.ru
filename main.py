import discord
from discord.ext import commands
import random
import os
intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)
facts_list = ['1. ГЛОБАЛЬНОЕ ПОТЕПЛЕНИЕ СУЩЕСТВУЕТ',
         '2. СОВРЕМЕННОЕ ПОТЕПЛЕНИЕ СВЯЗАНО С ПАРНИКОВЫМИ ГАЗАМИ',
         '3. РОССИЯ СИЛЬНЕЕ ОЩУЩАЕТ ИЗМЕНЕНИЕ КЛИМАТА',
         '4. ИЗМЕНЕНИЕ КЛИМАТА ВОЛНУЕТ УЧЁНЫХ НЕ ОДНО ДЕСЯТИЛЕТИЕ',
         '5. НА ИЗМЕНЕНИЕ КЛИМАТА ВЛИЯЕТ НЕ ТОЛЬКО ЭНЕРГЕТИКА И ПРОМЫШЛЕННОСТЬ, НО И СЕЛЬСКОЕ ХОЗЯЙСТВО']

advice_list = ['Чаще пользоваться общественным транспортомэ',
          'Экономить энергию',
          'Сократить потребление мяса',
          'Утилизировать отходы, использовать вторсырье, даже воду',
          'Информировать и обучать']
@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Привет! Я бот {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def fact(ctx):
    fact = random.choice(facts_list)
    await ctx.send(fact)
    
@bot.command()
async def advice(ctx):
    advice = random.choice(advice_list)
    await ctx.send(advice)

