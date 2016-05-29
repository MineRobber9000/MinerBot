import praw,logging;
from prawoauth2 import PrawOAuth2Mini as OAuth2Helper;
from config import *;

r = praw.Reddit(user_agent=USER_AGENT);
helper = OAuth2Helper(r, app_key=APP_ID,
                      app_secret=APP_SECRET, access_token=None,
                      scopes=SCOPES, refresh_token=REFRESH_TOKEN)
logging.basicConfig(filename='minerbot.log',level=logging.DEBUG)

def reply(c,msg):
	c.reply(msg+"\n\n*This account is a bot. If I have done something wrong, [let me know.](/r/minerbot)*")
	logging.info("Replied \"%s\" to \"/u/%s\":\"%s\";",msg,c.author.name,str(c))

def loop():
	for c in r.get_comments('all'):
		if c.body.find('/u/'+USERNAME) == 0:
			print("/u/"+c.author.name+" mentioned /u/"+USERNAME+"!")
			body = c.body[len('/u/'+USERNAME):]
			if body.find("hello") == 0:
				reply(c,"Hello!");

while True:
	try:
		loop()
		sleep(60)
	except praw.errors.OAuthInvalidToken:
		# token expired, refresh 'em!
		oauth_helper.refresh()