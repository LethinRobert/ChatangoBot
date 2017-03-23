import ch
import rmlist
import string
import random
import sys
import re
import time
import sys
from time import gmtime, strftime
import datetime
import urllib

if sys.version_info[0] > 2:
	import urllib.request as urlreq
else:
	import urllib2 as urlreq

dictionary = open("dictionary.py", "w")


dancemoves1 = [
	"(>^.^)>  "
	"(v^.^)v  "
	"v(^.^v)  "
	"<(^.^<)  "
]

dancemoves2 = [
	"v(^.^v)  "
	"<(^.^<)  "
	"(>^.^)>  "
	"(v^.^)v  "
]

hugs = [
"http://i51.tinypic.com/2vc7osg.jpg"
]

hugs2 = [
"http://i56.tinypic.com/1zf3att.jpg"
]

hugs3 = [
"http://2.bp.blogspot.com/_gKAo1-uGs7I/SZ3t8ethaAI/AAAAAAAAAA4/E900Q6h3Kng/s320/Kodomo_no_Jikan_-_02_-.jpg"
]

hugs4 = [
"http://i54.tinypic.com/15nmz4z.png"
]

hugs5 = [
"http://1.bp.blogspot.com/-__matri8wks/TaQiZxEw0BI/AAAAAAAABek/qsCE6G4o6yc/s320/%255BHorribleSubs%255D+Astarotte%2527s+Toy+-+01+%255B480p%255D.mkv_snapshot_21.15_%255B2011.04.12_11.01.26%255D+copy.jpg"
]

hugs6 = [
"http://i204.photobucket.com/albums/bb40/Toupaulthao/Kira-FansubMMVol01-SS01v01920x1080x264AACmkv_snapshot_0120_20101225_153707.jpg"
]

suicide1 = [
"-Pours water onto self-"
]

suicide2 = [
"NO, YOU!!!"
]

huladance = [
"(>*.*)> hula belly hula belly <(*.*<)",
"<(*.*<) hula belly hula hoo (>*.*)>",
"(>*.*)> coconutty coconutty <(*.*<)",
"<(*.*<) everybody hula hoo (>*.*)>",
]

help = [
'For a list of commands type ";list". For help on a command type ;help(insert command name here). Example for help with the hug command type ";helphug". To initaite a command you must first type ";", note that their is NOT a space after ;. Commands do NOT have spaces in them. spinthebottle, for example, does not have spaces. Commands also must be all lower case, and must have a space after them only if you are doing a command that requires user input. Examples: ";hug" does not need a space, but ";say something" does.'
]

cmdlst = [
'Commands for fun: huladance, dance, lick, hug, spinthebottle, rr, 8ball, slang, suicide, define, cmpt. There is also a "talk" function for things like "Hello t6.".',
'Semi-useful Commands: math, say, mylvl, help, list, die[Only mods can use, it is a killswitch for when the bot is being abused], banlist[lvl2 or mod]. ";helpCOMMAND" for more info on the commands. <--There is no space between help and the command. [locked commands, you cannot use them] def, rdwiki, imdb.'
]


helpimbd = [
';imbd will search the internet movie database.'
]

helpcmpt = [
';cpmt will complement a person, if you do not say a person then a random person will be picked.'
]

helpdefine = [
';define is a user created dictionary. To look up a word type ;define WORD. To define a word type ;define WORD: definition'
]

helpdbanlist = [
';banlist or simply ;bl will return a list of people that are banned. Mods and lvl2+ users only. Ion must be modded.'
]

helprdwiki = [
';rdwiki will return a link to a random wiki page. Note that the page changes everytime that you click the link, so it only needs to be posted one time.'
]


helpdie = [
';die is a killswitch, it will terminate the program. Only mods and level 3 users can use this.'
]

helpmath = [
';math will compute math questions. It can do basic math, but it can also do advanced math, like calculus. It can also be used for VERY basic searchs, example: ";math hello" might return "hello is an english word".'
]

attack1 = ("It is not very effective.")

attack2 = ("water ballons.")

attack3 = ("a mother fucking gun. Bitch.")

attack4 = ("Sexy time.")

attack5 = ("a pencil.")

attack6 = ("a dull, rusty sword.")

attack7 = ("a pillow! Feel my wrath! RAWR!")

attack8 = ("babies. Yes, I am attacking you with babies. Be afraid, very afraid.")


lick = [
"Click the image (it's a gif) http://images.kaneva.com/filestore0/279261/289581/ghost-lick.gif"
]

rr2 = [
"Click!"
]
rr1 = [
"BANG!!"
]

helprr = [
";rr is Russian Roulette. There is a 1/6th chance that the 'gun' will fire."
]

helphug = [
";hug posts random picture of a hug!"
]

help8ball = [
';8ball answers yes/no style questions like a normal 8 ball but more Ion. Example: ";8ball Is Ion God?" Response: "Absolutely!"'
]

helplick = [
";lick is a gif (you have to click it to see it move) : p"
]

helpsay = [
';say repeats what a user says. Example: ";say Hello!" gets the response "Hello!" from the bot.'
]


helpdance = [
";dance makes the bot post kirby dance emoticons. The bot does multiple dances (One of them being Huladance)."
]

helphuladance = [
";huladance is kinda like the dance command. This command is brought to yo by OmegaDestructoTaco."
]

helpspinthebottle = [
";spinthebottle outputs a random user's account name. This command can be used for multiple things, such as a lotto where a random user is the winner."
]

helpattack = [
";attack It's not very effective."
]

helpsuicide = [
";suicide orders the bot to kill itself."
]

helpslang = [
";slang uses thesurrealist, a uk site to give you slang terms for things that you would not normally think to have a slang meaning. DO NOT USE in chats with bad language rules."
]

cmpt1 = " is like the rays of sunshine shining down in the otherwise unbearably cold artic wasteland in which we live."

cmpt2 = " is almost as lovely as Ion is."

cmpt3 = " is the most absolutely amazingly awesome person ever."

cmpt4 = "'s mom...is a respectable lady."

cmpt5 = ", I like your shoes."

helpmylvl = [
";mylvl will tell you if you are a normal user, a mod, or the admin."
]

helpmodlist = [
";modlist will display a list of all of a chats mods. This is so that you know who to complain to if you mad."
]

luvres = ['I love you too, ']
luvres2 = ['!']

now = [
strftime("%a, %d %b %Y %H:%M GMT", gmtime())
]

class TestBot(ch.RoomManager):
	def onInit(self):
		self.setNameColor("9900CC")
		self.setFontColor("9966FF")
		self.setFontFace("1")
		self.setFontSize(10)
		self.enableBg()
		self.enableRecording()

	def onConnect(self, room):
		print("Connected")

	def onReconnect(self, room):
		print("Reconnected")

	def onDisconnect(self, room):
		print("Disconnected")

	def onMessage(self, room, user, message):
		if self.user == user: return
		if (message.body[0] == ";"):
		    callname = 6
		else: 
		    callname = 0
		lvl3rd = open("lvl3.txt","r")
		lvl3rd2 = (lvl3rd.read()).lower()
		lvl2rd = open("lvl2.txt","r")
		lvl2rd2 = (lvl2rd.read()).lower()
		lvl1rd = open("lvl1.txt","r")
		lvl1rd2 = (lvl1rd.read()).lower()
		if (( '$#@!@#$(*(^$#@' + user.name + '!^@*#($)@(@^*&#*@$*#$*#@') in lvl3rd2):
		    usrlvl = 3
		    lvl3rd.close()
		    lvl2rd.close()
		    lvl1rd.close()
		elif (( '$#@!@#$(*(^$#@' + user.name + '!^@*#($)@(@^*&#*@$*#$*#@') in lvl2rd2):
		    usrlvl = 2
		    lvl3rd.close()
		    lvl2rd.close()
		    lvl1rd.close()
		elif (( '$#@!@#$(*(^$#@' + user.name + '!^@*#($)@(@^*&#*@$*#$*#@') in lvl1rd2):
		    usrlvl = 1
		    lvl3rd.close()
		    lvl2rd.close()
		    lvl1rd.close()
		else:
		    usrlvl = 0
		    lvl3rd.close()
		    lvl2rd.close()
		    lvl1rd.close()
		if ( (callname == 6) and (usrlvl >= 1) and (room.name == 'teruchat')):
			data = message.body[1:].split(" ", 1)
			if len(data) > 1:
				cmd, args = data[0], data[1]
			else:
				cmd, args = data[0], ""
#			if   (cmd.lower()) == "delay":
#				self.setTimeout(int(args), room.message, ":D")
			if (cmd.lower()) == "rm":
				if usrlvl >= 3:
					if args.find(": ") != -1: #if there's a colon somewhere
						argsadj = args.lower()
						uroomr, umsg = argsadj.split(": ", 1)
						if uroomr == 'buzz':
							uroomr = 'animebuzzez'
						elif uroomr == 'ab':
							uroomr = 'animebuzzez'
						elif uroomr == 'buzzez':
							uroomr = 'animebuzzez'
						elif uroomr == 'animebuzz':
							uroomr = 'animebuzzez'
						elif uroomr == 'home':
							uroomr = 'teruchat'
						elif uroomr == 'seed':
							uroomr = 'animeseed'
						elif uroomr == 'as':
							uroomr = 'animeseed'
						elif uroomr == 'teru':
							uroomr = 'teruchat'
						elif uroomr == 'tc':
							uroomr = 'teruchat'
						elif uroomr == 'uri':
							uroomr = 'projecturi'
						elif uroomr == 'project':
							uroomr = 'projecturi'
						elif uroomr == 'pu':
							uroomr = 'projecturi'
						elif uroomr == 'am':
							uroomr = 'amaniacs'
						elif uroomr == 'animemaniacs':
							uroomr = 'amaniacs'
						elif uroomr == 'maniacs':
							uroomr = 'amaniacs'
						elif uroomr == 'kuro':
							uroomr = 'kuronetwork'
						elif uroomr == 'network':
							uroomr = 'kuronetwork'
						elif uroomr == 'kn':
							uroomr = 'kuronetwork'
						elif uroomr == 'love':
							uroomr = 'lovemyanimechat'
						elif uroomr == 'lovemy':
							uroomr = 'lovemyanimechat'
						elif uroomr == 'lovemyanime':
							uroomr = 'lovemyanimechat'
						elif uroomr == 'lma':
							uroomr = 'lovemyanimechat'
						elif uroomr == 'lmac':
							uroomr = 'lovemyanimechat'
						elif uroomr == 'animeon':
							uroomr = 'watchanimeonn'
						elif uroomr == 'watchanimeon':
							uroomr = 'watchanimeonn'
						elif uroomr == 'animenow':
							uroomr = 'watchanimenow'
						elif uroomr == 'animefreak':
							uroomr = 'tvanimefreak'
						elif uroomr == 'aftv':
							uroomr = 'tvanimefreak'
						elif uroomr == 'af':
							uroomr = 'tvanimefreak'
						elif uroomr == 'chat':
							uroomr = 'teruchat'
						if (uroomr in str(self._rooms)):
							uroom = self._rooms[uroomr]
							gumsgr1 = re.split('([.!?] *)', umsg)
							gumsgr2 = [item.capitalize() for item in gumsgr1]
							gumsgr3 = ''.join(gumsgr2)
							gumsgr4 = gumsgr3.replace((' i '), ' I ')
							gumsgr5 = gumsgr4.replace(('teru'), 'Teru')
							gumsgr6 = gumsgr5.replace(('ion'), 'Ion')
							gumsgr7 = gumsgr6.replace(('bobby'), 'Bobby')
							gumsgr8 = gumsgr7.replace(('god'), 'God')
							gumsgr9 = gumsgr8.replace(('jaye'), 'Jaye')
							gumsgr10 = gumsgr9.replace(('T-t'), 'T-T')
							gumsgr11 = gumsgr10.replace(('"i '), '"I ')
							gumsgr12 = gumsgr11.replace(('t6'), '"T6')
							gumsg = gumsgr12.replace(('jesus'), 'Jesus')
							uroom.message(gumsg)
						else:
							room.message("I am not currently in " + uroomr + '.')
			elif (cmd.lower()) == "pm":
				if usrlvl >= 3:
					if args.find(": ") != -1: #if there's a colon somewhere
						wrtdata = open("PMOUT.txt","a")
						argsadj = args.lower()
						uuserr, umsg = argsadj.split(": ", 1)
						uuser = uuserr
						if uuser == 'teru':
							uuser = 't3ru'
						elif uuser == 'te':
							uuser = 't3ru'
						elif uuser == 'ru':
							uuser = 't3ru'
						elif uuser == 'ruru':
							uuser = 't3ru'
						elif uuser == 't3':
							uuser = 't3ru'
						elif uuser == 't6':
							uuser = 't6ru'
						elif uuser == 'dorko':
							uuser = 'eldorko'
						elif uuser == 'bobby':
							uuser = 'simplicity'
						elif uuser == 'lumz':
							uuser = 'lumirayz'
						elif uuser == 'lumz2':
							uuser = 'lumirayz'
						elif uuser == 'jaye':
							uuser = 'jayeraine'
						elif uuser == 'wyx':
							uuser = 'wyxmir'
						elif uuser == 'grimipoo':
							uuser = 'grim'
						elif uuser == 'hubby':
							uuser = 'grim'
						elif uuser == 'my love':
							uuser = 'grim'
						elif uuser == 'speed':
							uuser = 'sp33d'
						elif uuser == 'sp':
							uuser = 'sp33d'
						if ('<User: ' + uuser + '>') in str((self._pm).getContacts()):
							if ('http://' in umsg):
								pendusr = ch._users.get(uuser)
								room.message("I have sent " + uuser.capitalize() + ' the message: "' + str(umsg) + '"')
								(self._pm).message(pendusr, str(umsg))
								wrtdata.write(user.name + " To " + uuser.capitalize() + ': ' + str(umsg) + '\n\n')
								wrtdata.close()
							else:
								pendusr = ch._users.get(uuser)
								gumsgr1 = re.split('([.!?] *)', umsg)
								gumsgr2 = [item.capitalize() for item in gumsgr1]
								gumsgr3 = ''.join(gumsgr2)
								gumsgr4 = gumsgr3.replace((' i '), ' I ')
								gumsgr5 = gumsgr4.replace(('teru'), 'Teru')
								gumsgr6 = gumsgr5.replace(('ion'), 'Ion')
								gumsgr7 = gumsgr6.replace(('bobby'), 'Bobby')
								gumsgr8 = gumsgr7.replace(('god'), 'God')
								gumsgr9 = gumsgr8.replace(('jaye'), 'Jaye')
								gumsgr10 = gumsgr9.replace(('T-t'), 'T-T')
								gumsg = gumsgr10.replace(('jesus'), 'Jesus')
								room.message("I have sent " + uuser.capitalize() + ' the message: "' + str(gumsg) + '"')
								(self._pm).message(pendusr, str(gumsg))
								wrtdata.write(user.name + " To " + uuser.capitalize() + ': ' + str(gumsg) + '\n\n')
								wrtdata.close()
						else:
							room.message("An error occured, your message was not sent.")
					else:
						room.message("An error occured, your message was not sent.")
			elif (cmd.lower()) == "contacts":
				if usrlvl >= 3:
					room.message(str((self._pm)._contacts))
			elif (cmd.lower()) == "acontact":
				if usrlvl >= 3:
					iusr = ch._users.get(args.lower())
					if iusr == None:
						room.message(args.capitalize() + ' is not in the chat.')
					else:
						room.message('Done.')
						(self._pm).addContact(iusr)
			elif (cmd.lower()) == "rcontact":
				if usrlvl >= 3:
					iusr = ch._users.get(args.lower())
					if iusr == None:
						room.message(args.capitalize() + ' is not in the chat.')
					else:
						room.message('Done.')
						(self._pm).removeContact(iusr)
			elif (cmd.lower()) == "rooms":
				if usrlvl >= 2:
					roomso = str(self.getRoomNames())
					roomsa1 = roomso.replace("'","")
					roomsa2 = roomsa1.replace("{","")
					rooms = roomsa2.replace("}","")
					room.message('I am currently in the following rooms: ' + str(rooms) + ".")
			elif (cmd.lower()) == "gtfo":
				mdlvl = room.getLevel(user)
				if (args == ''):
					if (usrlvl >= 2 or mdlvl >= 1):
						room.message("Okay, if it will make you happy. ;(+20")
						self.leaveRoom(str(room.name))
					else:
						room.message("No, you!")
				else:
					if usrlvl >= 2:
						uroomr = args.lower()
						if uroomr == 'buzz':
							uroomr = 'animebuzzez'
						elif uroomr == 'ab':
							uroomr = 'animebuzzez'
						elif uroomr == 'buzzez':
							uroomr = 'animebuzzez'
						elif uroomr == 'animebuzz':
							uroomr = 'animebuzzez'
						elif uroomr == 'home':
							uroomr = 'teruchat'
						elif uroomr == 'seed':
							uroomr = 'animeseed'
						elif uroomr == 'as':
							uroomr = 'animeseed'
						elif uroomr == 'teru':
							uroomr = 'teruchat'
						elif uroomr == 'tc':
							uroomr = 'teruchat'
						elif uroomr == 'uri':
							uroomr = 'projecturi'
						elif uroomr == 'project':
							uroomr = 'projecturi'
						elif uroomr == 'pu':
							uroomr = 'projecturi'
						elif uroomr == 'am':
							uroomr = 'amaniacs'
						elif uroomr == 'animemaniacs':
							uroomr = 'amaniacs'
						elif uroomr == 'maniacs':
							uroomr = 'amaniacs'
						elif uroomr == 'kuro':
							uroomr = 'kuronetwork'
						elif uroomr == 'network':
							uroomr = 'kuronetwork'
						elif uroomr == 'kn':
							uroomr = 'kuronetwork'
						elif uroomr == 'love':
							uroomr = 'lovemyanimechat'
						elif uroomr == 'lovemy':
							uroomr = 'lovemyanimechat'
						elif uroomr == 'lovemyanime':
							uroomr = 'lovemyanimechat'
						elif uroomr == 'lma':
							uroomr = 'lovemyanimechat'
						elif uroomr == 'lmac':
							uroomr = 'lovemyanimechat'
						elif uroomr == 'animeon':
							uroomr = 'watchanimeonn'
						elif uroomr == 'watchanimeon':
							uroomr = 'watchanimeonn'
						elif uroomr == 'animenow':
							uroomr = 'watchanimenow'
						elif uroomr == 'animefreak':
							uroomr = 'tvanimefreak'
						elif uroomr == 'aftv':
							uroomr = 'tvanimefreak'
						elif uroomr == 'af':
							uroomr = 'tvanimefreak'
						if (uroomr in str(self._rooms)):
							room.message("Okay, if it will make you happy. ;(+20")
							self.leaveRoom(uroomr)
						else:
							room.message("I am not in " + uroomr + ", thus I can't leave it.")
					else:
						room.message("No, you!")
			elif (cmd.lower()) == "join":
				if usrlvl >= 2:
					if args == '':
						room.message('Please enter a valid room.')
					else:
						uroomr = args.lower()
						if uroomr == 'buzz':
							uroomr = 'animebuzzez'
						elif uroomr == 'ab':
							uroomr = 'animebuzzez'
						elif uroomr == 'buzzez':
							uroomr = 'animebuzzez'
						elif uroomr == 'animebuzz':
							uroomr = 'animebuzzez'
						elif uroomr == 'home':
							uroomr = 'teruchat'
						elif uroomr == 'seed':
							uroomr = 'animeseed'
						elif uroomr == 'as':
							uroomr = 'animeseed'
						elif uroomr == 'teru':
							uroomr = 'teruchat'
						elif uroomr == 'tc':
							uroomr = 'teruchat'
						elif uroomr == 'uri':
							uroomr = 'projecturi'
						elif uroomr == 'project':
							uroomr = 'projecturi'
						elif uroomr == 'pu':
							uroomr = 'projecturi'
						elif uroomr == 'am':
							uroomr = 'amaniacs'
						elif uroomr == 'animemaniacs':
							uroomr = 'amaniacs'
						elif uroomr == 'maniacs':
							uroomr = 'amaniacs'
						elif uroomr == 'kuro':
							uroomr = 'kuronetwork'
						elif uroomr == 'network':
							uroomr = 'kuronetwork'
						elif uroomr == 'kn':
							uroomr = 'kuronetwork'
						elif uroomr == 'love':
							uroomr = 'lovemyanimechat'
						elif uroomr == 'lovemy':
							uroomr = 'lovemyanimechat'
						elif uroomr == 'lovemyanime':
							uroomr = 'lovemyanimechat'
						elif uroomr == 'lma':
							uroomr = 'lovemyanimechat'
						elif uroomr == 'lmac':
							uroomr = 'lovemyanimechat'
						elif uroomr == 'animeon':
							uroomr = 'watchanimeonn'
						elif uroomr == 'watchanimeon':
							uroomr = 'watchanimeonn'
						elif uroomr == 'animenow':
							uroomr = 'watchanimenow'
						elif uroomr == 'animefreak':
							uroomr = 'tvanimefreak'
						elif uroomr == 'aftv':
							uroomr = 'tvanimefreak'
						elif uroomr == 'af':
							uroomr = 'tvanimefreak'
						if (uroomr in str(self._rooms)):
							room.message("I am already in " + uroomr + ".")
						else:
							self.joinRoom(uroomr)
							room.message('I have joined ' + uroomr + '.')
			elif (cmd.lower()) == "rc":
				if usrlvl >= 2:
					if args == '':
						self.leaveRoom(room.name)
						time.sleep(2)
						self.joinRoom(room.name)
					else:
						uroomr = args.lower()
						if uroomr == 'buzz':
							uroomr = 'animebuzzez'
						elif uroomr == 'ab':
							uroomr = 'animebuzzez'
						elif uroomr == 'buzzez':
							uroomr = 'animebuzzez'
						elif uroomr == 'animebuzz':
							uroomr = 'animebuzzez'
						elif uroomr == 'home':
							uroomr = 'teruchat'
						elif uroomr == 'seed':
							uroomr = 'animeseed'
						elif uroomr == 'as':
							uroomr = 'animeseed'
						elif uroomr == 'teru':
							uroomr = 'teruchat'
						elif uroomr == 'tc':
							uroomr = 'teruchat'
						elif uroomr == 'uri':
							uroomr = 'projecturi'
						elif uroomr == 'project':
							uroomr = 'projecturi'
						elif uroomr == 'pu':
							uroomr = 'projecturi'
						elif uroomr == 'am':
							uroomr = 'amaniacs'
						elif uroomr == 'animemaniacs':
							uroomr = 'amaniacs'
						elif uroomr == 'maniacs':
							uroomr = 'amaniacs'
						elif uroomr == 'kuro':
							uroomr = 'kuronetwork'
						elif uroomr == 'network':
							uroomr = 'kuronetwork'
						elif uroomr == 'kn':
							uroomr = 'kuronetwork'
						elif uroomr == 'love':
							uroomr = 'lovemyanimechat'
						elif uroomr == 'lovemy':
							uroomr = 'lovemyanimechat'
						elif uroomr == 'lovemyanime':
							uroomr = 'lovemyanimechat'
						elif uroomr == 'lma':
							uroomr = 'lovemyanimechat'
						elif uroomr == 'lmac':
							uroomr = 'lovemyanimechat'
						elif uroomr == 'animeon':
							uroomr = 'watchanimeonn'
						elif uroomr == 'watchanimeon':
							uroomr = 'watchanimeonn'
						elif uroomr == 'animenow':
							uroomr = 'watchanimenow'
						elif uroomr == 'animefreak':
							uroomr = 'tvanimefreak'
						elif uroomr == 'aftv':
							uroomr = 'tvanimefreak'
						elif uroomr == 'af':
							uroomr = 'tvanimefreak'
						if (uroomr in str(self._rooms)):
							self.leaveRoom(uroomr)
							time.sleep(2)
							self.joinRoom(uroomr)
						else:
							room.message('I am not in ' + uroomr + '.')
		else:
		    mdlvl = room.getLevel(user)  
		    if ( (message.body.lower().startswith("t6 die")) and (mdlvl >= 1) ):	
		        sys.exit(0)
		    else:
		    	tryagain=0
	def onFloodWarning(self, room):
		room.reconnect()

#	def onJoin(self, room, user):
		#room.message("Hello, " + (user.name).capitalize() + "!")
	#def onLeave(self, room, user):
		#room.message("Bye, " + (user.name).capitalize() + "!")

#	def onUserCountChange(self, room):
#		print("Users: " + str(room.usercount))

	def onPMMessage(self, pm, user, body):
#	    pmchoice = random.choice(["Hello!", "How are you?", "Good.", "Yes", "No", "Yes", "No", "Yes", "No", "I like pie!", body, body, body, body, "Are you a fruit or a vegetable?", "Fruit.", "I love you!", "Don't be rude!", "I hate all Indians, including you.", "No, I don't want to watch you masturbate on cam or on any other medium.", "Are you seriously talking to me?", "Am I seriously writing all of this?", "Wow, I must be bored", "-Kills you and rapes the body-", "What else should I say in PMs?", "My password is password. I am not even joking. :|", "I don't like you very much.", body, body, body, "What is your name?", "Your name is very b-e-a-u-tiful.", "I like Jell-o!", "Have you been to DELETED yet? What are you waitting for, visit now!", "Oh, I see.", "Really?", "You don't say?", "How interesting!", "I hate you, a lot.", "I could be doing better. You see, as a bot I have no soul.", "This is my only purpose.", "If I were a cow would you eat me?", "Do you like cake or just men?", "I bet you a dollar that I can jump higher than you can.", "I win, you can't see it, but I win.", "You now owe me a dollar. :|", "I hope you die in a buring fire. Not a regular fire, a fire that burns.", ":D", "The Game.", "I know for a fact that if you shot yourself in the head while on a live stream that you will come back to life after 5 seconds with no damage to you. This only works if you send me the link to the livestream, of course.", "Let's be serious for a moment. Why haven't you killed yourself?", "Trololololo", "Y U MAD THO?", "Y U MAD THO?", "Y U MAD THO?", "Y U MAD THO?", "Y U MAD THO?", "U SO MAD.", "Rawr...Rawr...I'm a dinosaur!", "No, you're a bot.", "Did you say that you love soda, I fucking love soda!", "I once killed a panda and then cut out its tongue and then made the tounge lick me all over.", "Is that a naked man riding on a zebra while eating soup or are you just happy to see me?", "How about not.", "Sure, why not.", "I am so depressed v.v", "-ehugs you- Be mine!", "Don't mind me I am just kissing this penguin.", "COME AT ME BRO!", "The cake is a lie.", "*fish*", "*snow*", "*mummy*", "*monkey*"])
	    wrtdata = open(("PM" + user.name + ".txt"),"a")
	    wrtdata.write(str(user) + " " + str(body) + '\n')
	    print('\n\n' + "PM from " + str(user) + " " + str(body) + '\n\n')
#	    time.sleep(4)
#	    pm.message(user, pmchoice)
#	    wrtdata.write("BOT: " + str(pmchoice) + '\n\n')
#	    print("PM res BOT: " + str(pmchoice) + '\n\n')
	    wrtdata.close()
	    #print ("username = " + user.name + " and message = " + pm.message)

if __name__ == "__main__": TestBot.easy_start(rmlist.roomlist, name = 'Ion', password = 'Ion1uvzT3ru', pm = True)
