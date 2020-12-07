# APACHE LICENSE
# Copyright 2020 Stuart Paterson
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


# External Packages
import os
import discord
from dotenv import load_dotenv

# Local Files
import utils

# Create the bot
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
client = discord.Client()


@client.event
async def on_ready():
    # Triggered when starting up the bot
    print(f'{client.user} has connected to Discord!')


@client.event
async def on_member_update(before, after):
    if str(before.status) == "offline" and str(after.status) == "online":
        # When a user comes online
        channel = utils.get_channel_by_name(client, after.guild, 'general')
        try:
            # Send your message when a user comes online here!
            pass
        except discord.errors.Forbidden:
            pass


@client.event
async def on_message(message):
    if message.author == client.user:
        # Ignore messages this bot sends
        return

    current_channel = message.channel

    if message.content and len(message.content) > 1 and message.content[0] == '!':
        # First we extract the message after the ! then split it on spaces to
        # get a list or the arguments the user gave
        message_text = message.content[1:]
        split_message = message_text.split(" ")
        command = split_message[0]

        if command == "test":
            response = "test successful"
            await current_channel.send(response)
		elif command == "stop":
            await client.logout()
        # elif command == "foo":
        #     # Add your extra commands in blocks like this!
        #     pass

# Run the bot
client.run(TOKEN)
