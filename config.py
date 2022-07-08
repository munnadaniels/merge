import os

class Config(object):
	API_HASH = os.getenv('API_HASH','97abf9b730e7fae3d7e9c5dd240885c1')
	BOT_TOKEN = os.getenv('BOT_TOKEN','5100078702:AAHveHDTRCubIg-ALCm93QDKeVANF1V2BWs')
	API_ID = int(os.getenv('API_ID','7963542'))
	OWNER = int(os.environ.get('OWNER','1807485738'))
	OWNER_USERNAME = os.getenv('OWNER_USERNAME','vanajakshi69')
	PASSWORD = os.getenv('PASSWORD','thatha')
	DATABASE_URL=os.environ.get("DATABASE_URL","mongodb+srv://vanajakshi:pravalika@cluster0.t2dgo.mongodb.net/?retryWrites=true&w=majority")
	FLAG = int(os.getenv('FLAG',1))		# Dont Change this(unfinished feature!!) or else bot will stop working
	LOGCHANNEL = os.getenv('LOGCHANNEL') or None # Add channel id with -100 /\or/\ channel user name without @
