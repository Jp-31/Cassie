# Create a new config.py or rename this to config.py file in same dir and import, then extend this class.
import json
import os


def get_user_list(config, key):
    with open('{}/SaitamaRobot/{}'.format(os.getcwd(), config),
              'r') as json_file:
        return json.load(json_file)[key]


# Create a new config.py or rename this to config.py file in same dir and import, then extend this class.
class Config(object):
    LOGGER = True
    # REQUIRED
    #Login to https://my.telegram.org and fill in these slots with the details given by it

    API_ID = 1700483  # integer value, dont use ""
    API_HASH = "d86557e2e223db978dc823559a2d5349"
    TOKEN = "1317491419:AAFUxWFa8VvqG6PilWngRutcy4bq5HvEJ7k"  #This var used to be API_KEY but it is now TOKEN, adjust accordingly.
    OWNER_ID = 638711063  # If you dont know, run the bot and do /id in your private chat with it, also an integer
    OWNER_USERNAME = "Jeeeypi"
    SUPPORT_CHAT = 'cassie_support'  #Your own group for support, do not add the @
    JOIN_LOGGER = -1001410683162  #Prints any new group the bot is added to, prints just the name and ID.
    EVENT_LOGS = -1001190806654  #Prints information like gbans, sudo promotes, AI enabled disable states that may help in debugging and shit

    #RECOMMENDED
    SQLALCHEMY_DATABASE_URI = 'postgres://spcsfvaabcbzfj:0a9fa8c6734b93033d143c8b8eb3eeb40a9ee91a92c0f11b805f995843a69c48@ec2-52-21-0-111.compute-1.amazonaws.com:5432/d2sj13jk1lpdjr'  # needed for any database modules
    LOAD = []
    NO_LOAD = ['rss', 'cleaner', 'connection', 'math']
    WEBHOOK = False
    INFOPIC = True
    URL = None
    SPAMWATCH_API = "gEM6jn~hn5RGnCiLOw6q9vca__RYP9BlRWerPKrBLOjKfwEh5kITT61y6WnEvXut"  # go to support.spamwat.ch to get key
    SPAMWATCH_SUPPORT_CHAT = "@SpamWatchSupport"

    #OPTIONAL
    ##List of id's -  (not usernames) for users which have sudo access to the bot.
    SUDO_USERS = get_user_list('elevated_users.json', 'sudos')
    ##List of id's - (not usernames) for developers who will have the same perms as the owner
    DEV_USERS = get_user_list('elevated_users.json', 'devs')
    ##List of id's (not usernames) for users which are allowed to gban, but can also be banned.
    SUPPORT_USERS = get_user_list('elevated_users.json', 'supports')
    #List of id's (not usernames) for users which WONT be banned/kicked by the bot.
    TIGER_USERS = get_user_list('elevated_users.json', 'tigers')
    WHITELIST_USERS = get_user_list('elevated_users.json', 'whitelists')
    DONATION_LINK = None  # EG, paypal
    CERT_PATH = None
    PORT = 5000
    DEL_CMDS = True  #Delete commands that users dont have access to, like delete /ban if a non admin uses it.
    STRICT_GBAN = True
    WORKERS = 8  # Number of subthreads to use. Set as number of threads your processor uses
    BAN_STICKER = ''  # banhammer marie sticker id, the bot will send this sticker before banning or kicking a user in chat.
    ALLOW_EXCL = True  # Allow ! commands as well as / (Leave this to true so that blacklist can work)
    CASH_API_KEY = '795SYGXSY93LNIB5'  # Get your API key from https://www.alphavantage.co/support/#api-key
    TIME_API_KEY = 'V90H61RWLCQB'  # Get your API key from https://timezonedb.com/api
    WALL_API = '89d63f9947e9a72a5b34c16de03ba1a6'  #For wallpapers, get one from https://wall.alphacoders.com/api.php
    AI_API_KEY = '8816413e4ee076088cafbade01851d326ed384607e5773b23ddcab692736d9b6bf1b69a215ce46dc3b31db3eda5085f04edd5c5d99727bac4ba0c9707a8f6d9b'  #For chatbot, get one from https://coffeehouse.intellivoid.net/dashboard
    BL_CHATS = []  # List of groups that you want blacklisted.
    SPAMMERS = None


class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
