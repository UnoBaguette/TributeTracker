import sys, os
import atexit
import discord
from discord.ext import commands
from commands.manual_input import perform_manual_tribute_input
from utils.data_handler import load_data, save_data
from config.settings import TOKEN, PREFIX, ITEMS_DATA_FILE
from dotenv import load_dotenv
import datetime as dt

load_dotenv()
global current_data
current_data: dict = {}

intents = discord.Intents.all()
bot = commands.Bot(
    command_prefix=PREFIX,  # Use your prefix from settings
    intents=intents,
    help_command=None  # Disable default help to avoid conflicts
)

@bot.event
async def on_ready():
    print(f'✅ {bot.user} is online!')
    print('🔄 Syncing commands...')
    await bot.tree.sync()  # Sync slash commands
    print('🔹 Registered commands:', [cmd.name for cmd in bot.commands])
    await bot.change_presence(activity=discord.Game(name="Tracking tributes"))

# Add this error handler
@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send("Command not found. Try !help")
    else:
        print(f"Error: {error}")

@bot.command()
async def ping(ctx):
    """Check if bot is responsive"""
    await ctx.send('🏓 Pong! Latency: {:.2f}ms'.format(bot.latency * 1000))

@bot.command(
    name="tribute",
    description="Record a tribute payment from a user. If there is no @user, assigns tribute amount to the user running the command.",
    usage="!tribute <amount> [@user]",
    aliases=["t"]
)
async def tribute(ctx, amount: str, user: discord.User = None):
    """
    Records a tribute payment in the system.
    
    Parameters:
    -----------
    ctx: commands.Context
        The command context
    amount: str
        The tribute amount (can include currency symbol, defaults to USD)
    user: discord.User (optional)
        The user who sent the tribute (defaults to command author)
        
    Examples:
    --------
    !tribute 100 @User
    !tribute £50
    """
    if amount is None:
        await ctx.send("❌ No amount given. Usage: `!tribute <amount> [@user]`")
        return
    global current_data
    user = user or ctx.author
    month_number = dt.datetime.now().month
    current_data = perform_manual_tribute_input(amount, user, month_number, current_data)
    
    string_month = dt.datetime(year=dt.datetime.now().year, month=month_number, day=1).strftime("%B")
    await ctx.send(
        f"✅ Tribute of {amount} received from {user.mention}\n"+
        get_tribute_info(user)
    )

@bot.command()
async def check(ctx: discord.Interaction, user: discord.User = None):
    global current_data
    user = user or ctx.author
    await ctx.send(
        get_tribute_info(user)
    )


def save_on_exit():
    global current_data
    """Save data when bot shuts down"""
    print("\n🛑 Bot shutting down - saving data...")
    save_data(ITEMS_DATA_FILE, current_data)
    print("💾 Data saved successfully")

@bot.event
async def on_disconnect():
    """Triggered when bot disconnects"""
    save_on_exit()

def get_tribute_info(user: discord.User) -> str:
    global current_data
    user_info = current_data[str(user.id)]
    grand_total = sum(user_info)
    month_string = dt.datetime.now().strftime("%B")
    return f"{user.mention} Current Month Total For {month_string} = ${user_info[dt.datetime.now().month-1]}\nGrand Total = ${grand_total}"

# Register shutdown handler
atexit.register(save_on_exit)

if __name__ == '__main__':
    current_data = load_data(ITEMS_DATA_FILE)
    try:
        bot.run(os.getenv(TOKEN))
    except discord.LoginFailure:
        print("⚠️ ERROR: Invalid token!")
    except Exception as e:
        print(f"⚠️ ERROR: {e}")