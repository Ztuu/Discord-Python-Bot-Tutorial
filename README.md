# Discord Bot in Python Tutorial
A simple discord bot as a teaching exercise for learning Python and Discord.py.
This exercise is aimed at beginner programmers who have some experience with python
but want a simple project to practice their skills on. It's also suitable for anyone
who wants to start a discord bot using discord.py!

You can view a completed version of this project [here](https://github.com/Ztuu/Discord-Python-Bot-Model-Answer)
which I have created as a model answer.

## Before You Start
Before you start with the tasks below you will have to create a bot within the Discord developer portal.

Follow [this tutorial](https://realpython.com/how-to-make-a-discord-bot-python/)
to create your discord application and bot.
Once you have created your discord application and bot you can fork this repository
to get a copy downloaded to your machine for working on.

You will need to edit the .env file included in this project with your discord bot
token as described in the tutorial above.
(Normally .env files should not be committed to repositories but in this case a
blank version has been included for simplicity. Make sure you do not commit your
token to your own repository if you commit one. Edit the .gitignore and look for
the line with .env. Remove the # to uncomment this line and make sure you do not
commit the file to your repo.)

## Once Your Bot is Running
Once you have the bot running on your server you can use the !test command to check
if it is functioning correctly. The bot should reply with a message in the same
channel saying "test successful". Open up the bot.py file and take a look over the
code, try to understand what each section does and use the comments to help you.

Take a look at the code responsible for the test command(line 64).
You will mimic this code when creating your own commands. You will see there is
also a stop command for
stopping the bot from running. This is a useful development tool I added as
exiting the bot from the command line can have a significant delay.
Make sure to remove this if you publish your bot!

- - - -

## Tasks
1. When a user types "!hello" the bot should send a message in that channel saying "Hello World!".

2. Update the previous code so that when a user types "!hello" the bot sends a message saying "Hello *@username*!". *(hint: You can get the user who sent the command by using message.author.mention)*.

3. When a user types "!compliment" the bot sends a message saying "You look nice today *@username*".

4. Update the previous command to send a random compliment from a list of compliments you define.

5. When a user comes online send them a message saying "Hello *@username*!" *(hint: The code to handle detecting when a user comes online has been done for you, you just need to add in sending a message to the channel!)*.

6. Adjust the previous code by adding a random compliment after greeting the user.
*(hint: don't copy your compliment code from earlier, create a get_compliment function you can use for the !compliment command and when users come online)*

7. We're going to make a random number guessing game. When the user types "!guess X" (where X is a number) the bot should generate a random number from 1 to 100 and send a message based on whether the user's number and the bot's number match. If they match say "That's a match!" otherwise say "Sorry, you guessed X but I was thinking of Y" (where Y is the random number the bot came up with). *(hint: this is the first task that requires you to take more than one argument in the user's command. The arguments have already been loaded for you into split_message.)*

8. Does the "!guess" command you wrote in the previous part handle if the user enters an invalid command? For example what if they type "!guess foo" or "!guess". Test your code and edit it so that you can handle non-integer arguments, or the user not entering a guess at all.

9. If you haven't already, add a different error message if the user guesses a number not between 1 and 100.

10. Add a cat image to your project in the same folder as bot.py. When a user types "!meow" send an this image embedded in a message.
*(hint: here is the [discord.py documentation for creating a file object](https://discordpy.readthedocs.io/en/latest/api.html?highlight=file#discord.File). The simplest way is to create a file with my_file = discord.File(filename). The file object can then be sent to a channel by adding a file argument to a message `channel.send(response, file=my_file)`. Remember to add the image to the same folder as bot.py!)*

11. Add several cat images to your project and create a list with all the filenames. Modify the "!meow" command to send a random image.

12. Having our filenames hardcoded in a list doesn't seem like a great idea If someone changes a filename our program could break, and every time we add a photo we'll have to manually add the filename to our list. To improve this change your code so that when the bot starts up it loads all your image filenames into our list instead. First put all your cat images in a folder in the same directory as the bot.py script called "cat_photos", then in your code loop over the filenames in this folder and add them to our list. *(hint: You can use [os.listdir(path)](https://docs.python.org/3/library/os.html#os.listdir) to get a list of the filenames in a directory, which you can then iterate over in your code! If you named your folder and put it in the correct place try `for filename in os.listdir('cat_photos'). You will also have to modify the code for creating your discord file object as you have to load the photo from a folder. We can use filepath = os.path.join(folder_name, filename) to connect our folder and filename and create our file with discord.File(filepath).`)*.

 - - - -
## Useful Stuff
* [Discord.py docs](https://discordpy.readthedocs.io/en/latest/ "Discord.py docs")
* [Discord.py FAQS](https://discordpy.readthedocs.io/en/latest/faq.html "Discord.py faqs")
* ["How to Make a Discord Bot in Python"](https://realpython.com/how-to-make-a-discord-bot-python/#responding-to-events, "How to Make a Discord Bot in Python") - The tutorial I used for the initial bot setup.
* [Discord Developer Portal](https://discord.com/developers/applications, "Discord Developer Portal")
* [Python Docs](https://docs.python.org/3/contents.html "Python Docs") - The full Python documentation.
* [Python OS Module](https://docs.python.org/3/library/os.html) - Useful for browsing files/directories and managing filepaths.
* [Model Answer](https://github.com/Ztuu/Discord-Python-Bot-Model-Answer) -  A model answer repository I created by completing the tasks myself.



Copyright 2020 Stuart Paterson

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    [http://www.apache.org/licenses/LICENSE-2.0](http://www.apache.org/licenses/LICENSE-2.0)

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
