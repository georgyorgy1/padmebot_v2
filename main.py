import discord
import asyncio
import padshitpostlib
import padmathlib
import padphysicslib
import padloglib
import padgamelib

class Main:
    bot = discord.Client()
    shitpost = padshitpostlib.Shitpost
    math = padmathlib.Mathematics
    physics = padphysicslib.Physics
    game = padgamelib.Game
    logger = padloglib.Printer

    def log_string(command, author, author_id, channel, server_name):
        return command + ' command engaged by ' + str(author) + ' (ID: ' + str(author_id) + ') in #' + str(channel) + ' @ ' + str(server_name)

    @bot.event
    async def on_message(message):
        try:
            if message.content.startswith('$checkem'):
                string = Main.shitpost.check_em()
                await Main.bot.send_message(message.channel, string)
                Main.logger.say(Main.log_string('$checkem', message.author, message.author.id, message.channel, message.server))

            if message.content.startswith('$daisy'):
                string = Main.shitpost.daisy()
                await Main.bot.send_message(message.channel, string)
                Main.logger.say(Main.log_string('$daisy', message.author, message.author.id, message.channel, message.server))

            if 'big guy' in message.content:
                string = Main.shitpost.big_guy()
                await Main.bot.send_message(message.channel, string)
                Main.logger.say(Main.log_string('big guy', message.author, message.author.id, message.channel, message.server))

            if message.content.startswith('garlic'):
                string = Main.shitpost.garlic()
                await Main.bot.send_message(message.channel, string)
                Main.logger.say(Main.log_string('garlic', message.author, message.author.id, message.channel, message.server))

            if message.content.startswith('anakin'):
                string = Main.shitpost.anakin()
                await Main.bot.send_message(message.channel, string)
                Main.logger.say(Main.log_string('anakin', message.author, message.author.id, message.channel, message.server))

            if message.content.startswith('$rand32') or '$random' in message.content:
                string = Main.math.generate_32bit()
                await Main.bot.send_message(message.channel, string)
                Main.logger.say(Main.log_string('$rand32/$random', message.author, message.author.id, message.channel, message.server))

            if message.content.startswith('$rand64'):
                string = Main.math.generate_64bit()
                await Main.bot.send_message(message.channel, string)
                Main.logger.say(Main.log_string('$rand64', message.author, message.author.id, message.channel, message.server))

            if message.content.startswith('$sin'):
                number = message.content[len('$sin'):].strip()
                string = Main.math.get_sin(number)
                await Main.bot.send_message(message.channel, string)
                Main.logger.say(Main.log_string('$sin', message.author, message.author.id, message.channel, message.server))

            if message.content.startswith('$cos'):
                number = message.content[len('$cos'):].strip()
                string = Main.math.get_cos(number)
                await Main.bot.send_message(message.channel, string)
                Main.logger.say(Main.log_string('$cos', message.author, message.author.id, message.channel, message.server))

            if message.content.startswith('$tan'):
                number = message.content[len('$tan'):].strip()
                string = Main.math.get_tan(number)
                await Main.bot.send_message(message.channel, string)
                Main.logger.say(Main.log_string('$tan', message.author, message.author.id, message.channel, message.server))

            if message.content.startswith('$weight'):
                number = message.content[len('$weight'):].strip()
                string = str(Main.physics.get_weight(number))
                await Main.bot.send_message(message.channel, string)
                Main.logger.say(Main.log_string('$weight', message.author, message.author.id, message.channel, message.server))


        except Exception as e:
            Main.logger.say(str(e))
            await Main.bot.send_message(message.channel, 'Whoops, something went wrong. Tell the bot owner to check the logs for more information!')

    @bot.event
    async def on_ready():
        await Main.bot.change_presence(game=discord.Game(name='PadmeBot v2.1 alpha test'))
        Main.logger.say('PadmeBot is ready!')

    def main():
        Main.logger.say('Starting PadmeBot.....')
        token_file = open('cred.txt', 'r')
        cred = token_file.read()
        token_file.close()

        try:
            Main.bot.run(str(cred))
            cred = ''

        except discord.errors.LoginFailure:
            error_string = 'Login failed. Your token is either invalid or empty. Please check cred.txt if your token is valid or not empty'
            Main.logger.say(error_string)

Main.main()
