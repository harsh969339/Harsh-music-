from PrinceMusic.core.bot import PRINCE
from PrinceMusic.core.dir import dirr
from PrinceMusic.core.git import git
from PrinceMusic.core.userbot import Userbot
from PrinceMusic.misc import dbb, heroku

from SafoneAPI import SafoneAPI
from .logging import LOGGER

dirr()
git()
dbb()
heroku()

app = PRINCE()
api = SafoneAPI()
userbot = Userbot()


from .platforms import *

Apple = AppleAPI()
Carbon = CarbonAPI()
SoundCloud = SoundAPI()
Spotify = SpotifyAPI()
Resso = RessoAPI()
Telegram = TeleAPI()
YouTube = YouTubeAPI()
