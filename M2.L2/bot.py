import discord
from discord.ext import commands
import random

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

descripcion = "Un bot de contaminación"

bot = commands.Bot(command_prefix="!", intents=intents, description=descripcion)

#Listas que usare más adelante en las preguntas interactivas con el usuario
consejos = [
    "Usa bicicleta o transporte público en vez de un automóvil.",
    "Apaga las luces y aparatos electrónicos cuando no los uses.",
    "Reduce el consumo de carne y prefiere productos locales.",
    "Recicla y reutiliza materiales para disminuir residuos.",
    "Planta árboles y cuida áreas verdes en tu comunidad."
]

soluciones = [
    "Evita el exceso de plásticos, lleva tus propias bolsas reutilizables.",
    "Usa botellas reutilizables en lugar de botellas de plástico desechables.",
    "Desconecta cargadores cuando no estén en uso.",
    "Aprovecha la luz natural en vez de encender focos.",
    "Comparte viajes en auto para reducir emisiones."
]

@bot.event
async def on_ready():
    print(f"Bot conectado como {bot.user}")

@bot.command
async def on_message(message):
    if message.author == bot.user:
        return
    if message.content.lower() == "!imagen":
        with open("planeta.png", "rb") as f:
            picture = discord.File(f)
            await message.channel.send(content = ".", file=picture)

@bot.command()
async def imagen(ctx):
    await ctx.send("Aquí tienes una imagen del planeta del objetivo que todos buscamos:")
    await ctx.send("https://pin.it/42Ux0fK9D")

@bot.command()
async def imagen(ctx):
    await ctx.send("Aquí tienes una imagen del planeta si no intervenimos a mejorar:")
    await ctx.send("https://pin.it/kJWwapbkT")

#Este comando se asemeja a un comando interactivo que utilizo en mi bot, el comando "lucky"
@bot.command()
async def consejos_bot(ctx, eleccion: str = None):
    """Elige "gases" o "soluciones" para obtener la información"""
    if eleccion is None:
        await ctx.send("Elige 'gases' o 'soluciones'")

        def check(m):
            return m.author == ctx.author and m.channel == ctx.channel

        msg = await bot.wait_for("message", check=check)
        eleccion = msg.content.lower()
    else:
        eleccion = eleccion.lower()

    if eleccion not in ("gases", "soluciones"):
        await ctx.send("Debes escribir `gases` o `soluciones`.")
        return

    if eleccion == "gases":
        mensaje = "Consejos para reducir gases de efecto invernadero:\n\n"
        for c in consejos:
            mensaje += f"- {c}\n"
        await ctx.send(mensaje)

    elif eleccion == "soluciones":
        mensaje = "Posibles soluciones para ayudar al medio ambiente:\n\n"
        for s in soluciones:
            mensaje += f"- {s}\n"
        await ctx.send(mensaje)

bot.run("TU_TOKEN_AQUI")