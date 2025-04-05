import discord
from discord.ext import commands
from bot.commands.manual_input import handle_manual_input
from bot.commands.external_input import handle_external_input
from bot.utils.calculations import calculate_total_value, calculate_category_totals
from bot.utils.data_handler import load_data, save_data
from bot.config.settings import TOKEN, PREFIX

intents = discord.Intents.default()
bot = commands.Bot(command_prefix=PREFIX, intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name} - {bot.user.id}')
    print('------')

@bot.command(name='manual')
async def manual(ctx, *, input_data):
    result = handle_manual_input(input_data)
    await ctx.send(result)

@bot.command(name='external')
async def external(ctx, *, source):
    result = handle_external_input(source)
    await ctx.send(result)

@bot.command(name='total')
async def total(ctx):
    total_value = calculate_total_value()
    await ctx.send(f'Total value of items: {total_value}')

@bot.command(name='category_totals')
async def category_totals(ctx):
    totals = calculate_category_totals()
    await ctx.send(f'Category totals: {totals}')

if __name__ == '__main__':
    load_data()
    bot.run(TOKEN)