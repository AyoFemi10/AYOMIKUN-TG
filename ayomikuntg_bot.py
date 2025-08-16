python
import telebot

# Define the token for your bot (replace 'YOUR_BOT_TOKEN' with the API token obtained from BotFather)
TOKEN = "8268530224:AAG1jBPM0nd__weRTrAXhlQm703oRqcXp00"

# Create an instance of the telebot.TeleBot class
bot = telebot.TeleBot(TOKEN)

# Define the bot owner
bot_owner = {
    "name": "Ayomikun Feranmi",
    "username": "mikunistheemperor"
}

# Define the commands and menus
fun_menu = ["rizz", "motivation", "jokes", "riddle"]
admin_commands = ["block user", "unblock user", "clear chat", "view once"]
holy_menu = ["bible verse", "Quran verse"]
games_menu = ["wcg", "tic-tac-toe"]
group_menu = ["kick user", "clear all admins", "make admin", "delete channel", "mute channel", "mute user", "ban words in channel", "changepfp", "change bio"]
bot_commands = ["ping", "runtime", "start"]

# Handle /start command
@bot.message_handler(commands=['start'])
def handle_start(message):
    bot.send_message(message.chat.id, "Welcome to AYOMIKUN TG bot! Made by Ayomikun Feranmi.If you have any problem dm @mikunistheemperor")

# Handle fun menu commands
@bot.message_handler(func=lambda message: message.text in fun_menu)
def handle_fun_menu(message):
    bot.send_message(message.chat.id, f"Fun menu command: {message.text}")

# Handle admin commands
@bot.message_handler(func=lambda message: message.text in admin_commands)
def handle_admin_commands(message):
    bot.send_message(message.chat.id, f"Admin command: {message.text}")

# Handle holy menu commands
@bot.message_handler(func=lambda message: message.text in holy_menu)
def handle_holy_menu(message):
    bot.send_message(message.chat.id, f"Holy menu command: {message.text}")

# Handle games menu commands
@bot.message_handler(func=lambda message: message.text in games_menu)
def handle_games_menu(message):
    bot.send_message(message.chat.id, f"Games menu command: {message.text}")

# Handle group menu commands
@bot.message_handler(func=lambda message: message.text in group_menu)
def handle_group_menu(message):
    bot.send_message(message.chat.id, f"Group menu command: {message.text}")

# Handle bot commands
@bot.message_handler(func=lambda message: message.text in bot_commands)
def handle_bot_commands(message):
    bot.send_message(message.chat.id, f"Bot command: {message.text}")

# Polling for new messages
bot.polling()