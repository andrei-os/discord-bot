import discord

def append_ends(keys):
    tokens = [ ' ', ',', '.', '?', '!' ]
    
    for key in keys:
        for token in tokens:
            yield token + key + token
            yield token + key
            yield key + token

def contains_element(text, keys):
    for key in append_ends(keys):
        if ' ' + key + ' ' in text: 
            return True

    return False


# predstavlja vezu s discordom
client = discord.Client()

# nakon logina
@client.event
async def on_ready():
    print('Ready!')
    await client.change_presence(activity=discord.Game(name='Signals and Sytems'))

# za svaku poruku
@client.event
async def on_message(message):
    # ignoriraj vlastite poruke
    if message.author == client.user: return

    user_msg = ' ' + message.content.lower() + ' '

    # izdominiraj kolegu
    if contains_element(user_msg, [ 'šteta', 'steta', 'stvarno' ]): 
        await message.channel.send('Šteta kolega šteta šteta stvarno šteta.')

    elif contains_element(user_msg, [ 'ne kužim', 'ne kuzim' ]):
        await message.channel.send('Sve se vidi.')

# samo token se nalazi u token.txt
with open('token.txt', 'r') as file:
    token = file.read().strip('\n\r ')

# obavezno zadnja naredba - event loop - blocking
client.run(token)
