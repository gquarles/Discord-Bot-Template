import discord
import json
import os

client = discord.Client()

with open('token.json', 'r') as file:  # Load token from token.json
    TOKEN = json.load(file)
    TOKEN = TOKEN['token']

commands = []  # Initialize commands


class Command:
    def __init__(self, command, channel, output, batch):
        self.command = command
        self.channel = channel
        self.output = output
        self.batch = batch
        commands.append(self)  # Add command to commands list

    def run(self):
        os.system('start cmd /c {}'.format(self.batch))  # Run command
        return self.output


# Add commands below
Command('!test', 'discord-channel', 'The command works!', 'test.bat')


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    for command in commands:
        if message.content == command.command and str(message.channel) == command.channel:
            msg = command.run()
            msg = msg.format(message)
            await client.send_message(message.channel, msg)


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run(TOKEN)
