import json, disnake, asyncio, datetime, random
from disnake.ext import commands, tasks
from disnake.ext.commands import cooldown, has_permissions, MissingPermissions, BucketType 

with open('config.json') as e:
    infos = json.load(e)
    TOKEN = infos['token']
    prefix = infos['prefixo']

ban = commands.Bot(command_prefix=commands.when_mentioned_or(prefix), case_insensitive=True, intents=disnake.Intents.all())

@ban.event
async def on_ready():
    calc = ban.latency * 1000
    pong = round(calc)
    print(f'O bot {ban.user} está pronto!')
    print(f'Atualmente meu ping é de {pong} ms')
    stats.start()

@tasks.loop(minutes=30)
async def stats():
    await ban.change_presence(activity=disnake.Activity(type=disnake.ActivityType.playing, name=f'Tudo menos LOL'))
    await asyncio.sleep(15 * 60)
    await ban.change_presence(activity=disnake.Activity(type=disnake.ActivityType.watching, name=f'ANTI_LOL LIGADO!'))

@ban.event
async def on_presence_update(before, after):
    # Verifica se o usuário começou a jogar algo
    if not before.activities and after.activities:
        for activity in after.activities:
            # Verifica se o nome do jogo é "League of Legends"
            try:
                await after.ban(reason="Jogando League of Legends")
                print(f"{after.display_name} foi banido por jogar League of Legends.")
            except disnake.Forbidden:
                print(f"Não foi possível banir {after.display_name}. Verifique as permissões do bot.")
            except disnake.HTTPException as e:
                print(f"Ocorreu um erro ao tentar banir {after.display_name}: {e}")


ban.run(TOKEN)
