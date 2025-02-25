# Create a new config.py or rename this to config.py file in same dir and import, then extend this class.
import json
import os


def get_user_list(config, key):
    with open('{}/ZeusXRobot/{}'.format(os.getcwd(), config),
              'r') as json_file:
        return json.load(json_file)[key]


# Create a new config.py or rename this to config.py file in same dir and import, then extend this class.
class Config(object):
    LOGGER = True
    # REQUIRED
    #Login to https://my.telegram.org and fill in these slots with the details given by it

    API_ID = 4759912  # integer value, dont use ""
    API_HASH = "5bcc548f108e30a913a339a4f97f315c"
    TOKEN = "5059068789:AAG1p9zixkDPEUZCjlKOz1g-OjPWaH1Xx0g"  #This var used to be API_KEY but it is now TOKEN, adjust accordingly.
    OWNER_ID = 1323719429  # If you dont know, run the bot and do /id in your private chat with it, also an integer
    OWNER_USERNAME = "Aryanjawale"
    SUPPORT_CHAT = 'trainer_zone'  #Your own group for support, do not add the @
    UPDATES_CHANNEL = 'ZeusUpdates' #Your own channel for Updates of bot, Do not add @
    JOIN_LOGGER = -1001197394366  #Prints any new group the bot is added to, prints just the name and ID.
    REM_BG_API_KEY = "dxsh728mZMDmj4ijSZCNPZig"
    TEMP_DOWNLOAD_DIRECTORY = "./"
    EVENT_LOGS = -1001197394366  #Prints information like gbans, sudo promotes, AI enabled disable states that may help in debugging and shit
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:qm59vitoitrQmUbndk82@containers-us-west-13.railway.app:6646/railway' #do you hub your old heroku app database_URL then put here, most use 25days ago sql
    LOAD = [] #try to kang this db ur big mothersfuckers i know your noob so only kanging my db
    NO_LOAD = ['rss', 'cleaner', 'connection', 'math']
    WEBHOOK = None
    INFOPIC = True
    URL = None
    SPAMWATCH_API = "M7r11AlyDZGvFh2F9U6umCS96iVvyMC~Bo9khw2cKMcYvRBYyDOUNJ7FLQqEEwgP"  # go to support.spamwat.ch to get key
    SPAMWATCH_SUPPORT_CHAT = "@SpamWatchSupport"
    BOT_USERNAME = "HawkMoth_rbot"
    BOT_ID = "5059068789"
    
    DRAGONS = get_user_list('elevated_users.json', 'sudos')

    DEV_USERS = get_user_list('elevated_users.json', 'devs')
    ##List of id's (not usernames) for users which are allowed to gban, but can also be banned.
    DEMONS = get_user_list('elevated_users.json', 'supports')
    #List of id's (not usernames) for users which WONT be banned/kicked by the bot.
    TIGERS = get_user_list('elevated_users.json', 'tigers')
    WOLVES = get_user_list('elevated_users.json', 'whitelists')
    DONATION_LINK = None  # EG, paypal
    CERT_PATH = None
    PORT = 5000
    DEL_CMDS = True  #Delete commands that users dont have access to, like delete /ban if a non admin uses it.
    STRICT_GBAN = True
    STRICT_GMUTE = True
    WORKERS = 8  # Number of subthreads to use. Set as number of threads your processor uses
    BAN_STICKER = ''  # banhammer marie sticker id, the bot will send this sticker before banning or kicking a user in chat.
    ALLOW_EXCL = True  # Allow ! commands as well as / (Leave this to true so that blacklist can work)
    ARQ_API_URL = "https://thearq.tech"
    ARQ_API_KEY = "VPGDCM-JFWZOY-OQQHWN-OLIIMI-ARQ"
    CASH_API_KEY = '24IWG7JGXMR46QEE'  # Get your API key from https://www.alphavantage.co/support/#api-key
    TIME_API_KEY = 'YGTK7XPATUHK'  # Get your API key from https://timezonedb.com/api
    OPENWEATHERMAP_ID = 'e8c43576833a8867d24a4e6785349e20'
    WALL_API = 'awoo'  #For wallpapers, get one from https://wall.alphacoders.com/api.php
    AI_API_KEY = 'awoo'  #For chatbot, get one from https://coffeehouse.intellivoid.net/dashboard
    BL_CHATS = []  # List of groups that you want blacklisted.
    SPAMMERS = None


class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
