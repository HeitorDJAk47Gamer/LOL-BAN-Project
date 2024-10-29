import json, disnake, asyncio, datetime
from disnake.ext import commands, tasks
from disnake.ext.commands import cooldown, has_permissions, MissingPermissions, BucketType 

with open('config.json') as e:
    infos = json.load(e)
    TOKEN = infos['token']
    prefix = infos['prefixo']

ban = commands.Bot(command_prefix=commands.when_mentioned_or(prefix), case_insensitive=True, intents=disnake.Intents.all())

@ban.event
async def on_ready():
    print(f'O bot {ban.user} está pronto!')

@ban.event
async def on_presence_update(before, after):
    # Verifica se o usuário começou a jogar algo
    if not before.activities and after.activities:
        for activity in after.activities:
            # Verifica se o nome do jogo é "League of Legends"
            try:
                await after.kick(reason="Jogando League of Legends")
                print(f"{after.display_name} foi expulso por jogar League of Legends.")
            except disnake.Forbidden:
                print(f"Não foi possível expulsar {after.display_name}. Verifique as permissões do bot.")
            except disnake.HTTPException as e:
                print(f"Ocorreu um erro ao tentar expulsar {after.display_name}: {e}")


ban.run(TOKEN)
