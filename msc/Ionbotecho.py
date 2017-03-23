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
		tcroom = self._rooms['teruchat']
		if room.name == 'teruchat':
			ignore = True
		elif user.name == ('gayookami'):
			ignore = True
		elif user.name == ('lucion'):
			ignore = True
		elif user.name == ('narcassist'):
			ignore = True
		elif user.name == ('soda'):
			ignore = True
		elif user.name == ('wei'):
			ignore = True
		elif user.name == ('uri'):
			ignore = True
		elif user.name == ('tesfallout'):
			ignore = True
		elif user.name == ('t6ru'):
			ignore = True
		elif user.name == ('ion'):
			ignore = True
		else:
			if message.body.startswith(';'):
				wrtdata = open("usage.txt","a")
				wrtdata.write(str(room.name + ': ' + user.name + ': ' + message.body + '\n'))
				wrtdata.close()
				tcroom.message(room.name + ' --> ' + user.name + ': ' + message.body)
			elif user.name == 'grim':
				wrtdata = open("grimhistory.txt","a")
				wrtdata.write(str(room.name + ': ' + user.name + ': ' + message.body + '\n'))
				wrtdata.close()
				tcroom.message(room.name + ' --> ' + user.name + ': ' + message.body)
			else:
				tcroom.message(room.name + ' --> ' + user.name + ': ' + message.body)
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
			if (cmd.lower()) == "spinthebottle":
				room.message(random.choice(room.usernames))
			elif (cmd.lower()) == "die":
			    mdlvl = room.getLevel(user)
			    if (usrlvl == 3):
				    sys.exit(0)
			    elif (mdlvl >= 1):
				    sys.exit(0)
			    else:
				    nicetry = 0
			elif (cmd.lower()) == "d":
				mdlvl = room.getLevel(user)
				if ((usrlvl >=3) or (mdlvl >= 1)):
					if args == "":
						room.clearUser(user)
					else:
						args2 = args.lower()
						endusr = ch._users.get(args2)
						if endusr == None:
							room.message(args.capitalize() + ' is not in the chat.')
						else:
							room.message(args.capitalize() + ' STFU please, k thx.')
							room.clearUser(endusr)
			elif (cmd.lower()) == "delete":
				mdlvl = room.getLevel(user)
				if ((usrlvl >=3) or (mdlvl >= 1)):
					if args == "":
						room.clearUser(user)
					else:
						args2 = args.lower()
						endusr = ch._users.get(args2)
						if endusr == None:
							room.message(args.capitalize() + ' is not in the chat.')
						else:
							room.message(args.capitalize() + ' STFU please, k thx.')
							room.clearUser(endusr)
			elif (cmd.lower()) == "kill":
				mdlvl = room.getLevel(user)
				if ((usrlvl >=3) or (mdlvl >= 1)):
					if args == "":
						room.message('Enter a valid user')
					else:
						args2 = args.lower()
						endusr = ch._users.get(args2)
						if endusr == None:
							room.message(args.capitalize() + ' is not in the chat.')
						else:
							room.message('I have killed ' + args.capitalize() + '.')
							room.banUser(endusr)
			elif (cmd.lower()) == "defib":
				mdlvl = room.getLevel(user)
				if ((usrlvl >=3) or (mdlvl >= 1)):
					if args == "":
						room.unban(user)
					else:
						args2 = args.lower()
						endusr = ch._users.get(args2)
						if endusr == None:
							room.message(args.capitalize() + ' is not in the chat.')
						else:
							room.message("Clear...Bzzz... I've got a pulse, it looks like " + args.capitalize() + ' will be ok.')
							room.unban(endusr)
			elif (cmd.lower()) == "n":
				mdlvl = room.getLevel(user)
				if ((usrlvl >=3) or (mdlvl >= 1)):
					room.clearall()
					for n in (room.getUserlist(mode = None, unique = None, memory = None)):
						room.clearUser(n)
			elif (cmd.lower()) == "nuke":
				mdlvl = room.getLevel(user)
				if ((usrlvl >=3) or (mdlvl >= 1)):
					room.clearall()
					for n in (room.getUserlist(mode = None, unique = None, memory = None)):
						room.clearUser(n)
			elif (cmd.lower()) == "amod":
				mdlvl = room.getLevel(user)
				if ((usrlvl >=3) or (mdlvl >= 1)):
					if args == "":
						room.addMod(user)
					else:
						args2 = args.lower()
						endusr = ch._users.get(args2)
						if endusr == None:
							room.message(args.capitalize() + ' is not in the chat.')
						else:
							room.message(args.capitalize() + ' is now ONE OF US! ONE OF US!')
							room.addMod(endusr)
			elif (cmd.lower()) == "rmod":
				mdlvl = room.getLevel(user)
				if ((usrlvl >=3) or (mdlvl >= 1)):
					if args != "":
						args2 = args.lower()
						endusr = ch._users.get(args2)
						if endusr == None:
							room.message(args.capitalize() + ' is not in the chat.')
						else:
							room.message(args.capitalize() + ' is no longer a moderator.')
							room.removeMod(endusr)
			elif (cmd.lower()) == "reset":
			    mdlvl = room.getLevel(user)
			    if usrlvl >=3:
			            room.reconnect()
			    elif mdlvl >= 1:
			            room.reconnect()
			    else:
				    nicetry = 0
			elif (cmd.lower()) == "wl":
				lvl3rd = open("lvl3.txt","r")
				lvl3rd2 = (lvl3rd.read()).lower()
				lvl2rd = open("lvl2.txt","r")
				lvl2rd2 = (lvl2rd.read()).lower()
				lvl1rd = open("lvl1.txt","r")
				lvl1rd2 = (lvl1rd.read()).lower()
				lvl0rd = open("lvl0.txt","r")
				lvl0rd2 = (lvl0rd.read()).lower()
				argsadj = args.lower()
				argssec = '$#@!@#$(*(^$#@' + argsadj + '!^@*#($)@(@^*&#*@$*#$*#@'
				if (usrlvl >=3):
					if args.find(":") != -1: #if there's a colon somewhere
						uuser, ulvl = argsadj.split(": ", 1)
						if ulvl == '3':
							wrtdata = open("lvl3.txt","a")
							room.message(uuser + " is now a level 3! -Set by " + (user.name).capitalize() + '.')
							wrtdata.write('$#@!@#$(*(^$#@' + uuser + '!^@*#($)@(@^*&#*@$*#$*#@' + '$#&@*&$*^' + user.name +  '#$@*' + uuser + '$@#^&*@!' + '\n')
							wrtdata.close()
							if (('$#@!@#$(*(^$#@' + uuser + '!^@*#($)@(@^*&#*@$*#$*#@') in lvl2rd2):
								wrtdata = open("lvl2.txt","w")
								indexs = lvl2rd2.find(('$#@!@#$(*(^$#@' + uuser + '!^@*#($)@(@^*&#*@$*#$*#@') + '$#&@*&$*^')
								indexe = lvl2rd2.find('#$@*' + uuser + '$@#^&*@!')
								rawout = lvl2rd2[(int(indexs)):(int(indexe))]
								newdata = str(lvl2rd2).replace((rawout + '#$@*' + uuser + '$@#^&*@!'), "")
								wrtdata.write(newdata)
								wrtdata.close()
								lvl3rd.close()
								lvl2rd.close()
								lvl1rd.close()
								lvl0rd.close()
							elif (('$#@!@#$(*(^$#@' + uuser + '!^@*#($)@(@^*&#*@$*#$*#@') in lvl1rd2):
								wrtdata = open("lvl1.txt","w")
								indexs = lvl1rd2.find(('$#@!@#$(*(^$#@' + uuser + '!^@*#($)@(@^*&#*@$*#$*#@') + '$#&@*&$*^')
								indexe = lvl1rd2.find('#$@*' + uuser + '$@#^&*@!')
								rawout = lvl1rd2[(int(indexs)):(int(indexe))]
								newdata = str(lvl1rd2).replace((rawout + '#$@*' + uuser + '$@#^&*@!'), "")
								wrtdata.write(newdata)
								wrtdata.close()
								lvl3rd.close()
								lvl2rd.close()
								lvl1rd.close()
								lvl0rd.close()
							elif (('$#@!@#$(*(^$#@' + uuser + '!^@*#($)@(@^*&#*@$*#$*#@') in lvl0rd2):
								wrtdata = open("lvl0.txt","w")
								indexs = lvl0rd2.find(('$#@!@#$(*(^$#@' + uuser + '!^@*#($)@(@^*&#*@$*#$*#@') + '$#&@*&$*^')
								indexe = lvl0rd2.find('#$@*' + uuser + '$@#^&*@!')
								rawout = lvl0rd2[(int(indexs)):(int(indexe))]
								newdata = str(lvl0rd2).replace((rawout + '#$@*' + uuser + '$@#^&*@!'), "")
								wrtdata.write(newdata)
								wrtdata.close()
								lvl3rd.close()
								lvl2rd.close()
								lvl1rd.close()
								lvl0rd.close()
						elif ulvl == '2':
							wrtdata = open("lvl2.txt","a")
							room.message(uuser + " is now a level 2! -Set by " + (user.name).capitalize() + '.')
							wrtdata.write('$#@!@#$(*(^$#@' + uuser + '!^@*#($)@(@^*&#*@$*#$*#@' + '$#&@*&$*^' + user.name +  '#$@*' + uuser + '$@#^&*@!' + '\n')
							wrtdata.close()
							if (('$#@!@#$(*(^$#@' + uuser + '!^@*#($)@(@^*&#*@$*#$*#@') in lvl3rd2):
								wrtdata = open("lvl3.txt","w")



								indexs = lvl3rd2.find(('$#@!@#$(*(^$#@' + uuser + '!^@*#($)@(@^*&#*@$*#$*#@') + '$#&@*&$*^')
								indexe = lvl3rd2.find('#$@*' + uuser + '$@#^&*@!')
								rawout = lvl3rd2[(int(indexs)):(int(indexe))]
								newdata = str(lvl3rd2).replace((rawout + '#$@*' + uuser + '$@#^&*@!'), "")
								wrtdata.write(newdata)
								wrtdata.close()
								lvl3rd.close()
								lvl2rd.close()
								lvl1rd.close()
								lvl0rd.close()
							elif (('$#@!@#$(*(^$#@' + uuser + '!^@*#($)@(@^*&#*@$*#$*#@') in lvl1rd2):
								wrtdata = open("lvl1.txt","w")
								indexs = lvl1rd2.find(('$#@!@#$(*(^$#@' + uuser + '!^@*#($)@(@^*&#*@$*#$*#@') + '$#&@*&$*^')
								indexe = lvl1rd2.find('#$@*' + uuser + '$@#^&*@!')
								rawout = lvl1rd2[(int(indexs)):(int(indexe))]
								newdata = str(lvl1rd2).replace((rawout + '#$@*' + uuser + '$@#^&*@!'), "")
								wrtdata.write(newdata)
								wrtdata.close()
								lvl3rd.close()
								lvl2rd.close()
								lvl1rd.close()
								lvl0rd.close()
							elif (('$#@!@#$(*(^$#@' + uuser + '!^@*#($)@(@^*&#*@$*#$*#@') in lvl0rd2):
								wrtdata = open("lvl0.txt","w")
								indexs = lvl0rd2.find(('$#@!@#$(*(^$#@' + uuser + '!^@*#($)@(@^*&#*@$*#$*#@') + '$#&@*&$*^')
								indexe = lvl0rd2.find('#$@*' + uuser + '$@#^&*@!')
								rawout = lvl0rd2[(int(indexs)):(int(indexe))]
								newdata = str(lvl0rd2).replace((rawout + '#$@*' + uuser + '$@#^&*@!'), "")
								wrtdata.write(newdata)
								wrtdata.close()
								lvl3rd.close()
								lvl2rd.close()
								lvl1rd.close()
								lvl0rd.close()
						elif ulvl == '1':
							wrtdata = open("lvl1.txt","a")
							room.message(uuser + " is now a level 1! -Set by " + (user.name).capitalize() + '.')
							wrtdata.write('$#@!@#$(*(^$#@' + uuser + '!^@*#($)@(@^*&#*@$*#$*#@' + '$#&@*&$*^' + user.name +  '#$@*' + uuser + '$@#^&*@!' + '\n')
							wrtdata.close()
							if (('$#@!@#$(*(^$#@' + uuser + '!^@*#($)@(@^*&#*@$*#$*#@') in lvl3rd2):
								wrtdata = open("lvl3.txt","w")
								indexs = lvl3rd2.find(('$#@!@#$(*(^$#@' + uuser + '!^@*#($)@(@^*&#*@$*#$*#@') + '$#&@*&$*^')
								indexe = lvl3rd2.find('#$@*' + uuser + '$@#^&*@!')
								rawout = lvl3rd2[(int(indexs)):(int(indexe))]
								newdata = str(lvl3rd2).replace((rawout + '#$@*' + uuser + '$@#^&*@!'), "")
								wrtdata.write(newdata)
								wrtdata.close()
								lvl3rd.close()
								lvl2rd.close()
								lvl1rd.close()
								lvl0rd.close()
							elif (('$#@!@#$(*(^$#@' + uuser + '!^@*#($)@(@^*&#*@$*#$*#@') in lvl2rd2):
								wrtdata = open("lvl2.txt","w")
								indexs = lvl2rd2.find(('$#@!@#$(*(^$#@' + uuser + '!^@*#($)@(@^*&#*@$*#$*#@') + '$#&@*&$*^')
								indexe = lvl2rd2.find('#$@*' + uuser + '$@#^&*@!')
								rawout = lvl2rd2[(int(indexs)):(int(indexe))]
								newdata = str(lvl2rd2).replace((rawout + '#$@*' + uuser + '$@#^&*@!'), "")
								wrtdata.write(newdata)
								wrtdata.close()
								lvl3rd.close()
								lvl2rd.close()
								lvl1rd.close()
								lvl0rd.close()
							elif (('$#@!@#$(*(^$#@' + uuser + '!^@*#($)@(@^*&#*@$*#$*#@') in lvl0rd2):
								wrtdata = open("lvl0.txt","w")
								indexs = lvl0rd2.find(('$#@!@#$(*(^$#@' + uuser + '!^@*#($)@(@^*&#*@$*#$*#@') + '$#&@*&$*^')
								indexe = lvl0rd2.find('#$@*' + uuser + '$@#^&*@!')
								rawout = lvl0rd2[(int(indexs)):(int(indexe))]
								newdata = str(lvl0rd2).replace((rawout + '#$@*' + uuser + '$@#^&*@!'), "")
								wrtdata.write(newdata)
								wrtdata.close()
								lvl3rd.close()
								lvl2rd.close()
								lvl1rd.close()
								lvl0rd.close()
						elif ulvl == '0':
							wrtdata = open("lvl0.txt","a")
							room.message(uuser + " is now a level 0! -Set by " + (user.name).capitalize() + '.')
							wrtdata.write('$#@!@#$(*(^$#@' + uuser + '!^@*#($)@(@^*&#*@$*#$*#@' + '$#&@*&$*^' + user.name +  '#$@*' + uuser + '$@#^&*@!' + '\n')
							wrtdata.close()
							if (('$#@!@#$(*(^$#@' + uuser + '!^@*#($)@(@^*&#*@$*#$*#@') in lvl3rd2):
								wrtdata = open("lvl3.txt","w")
								indexs = lvl3rd2.find(('$#@!@#$(*(^$#@' + uuser + '!^@*#($)@(@^*&#*@$*#$*#@') + '$#&@*&$*^')
								indexe = lvl3rd2.find('#$@*' + uuser + '$@#^&*@!')
								rawout = lvl3rd2[(int(indexs)):(int(indexe))]
								newdata = str(lvl3rd2).replace((rawout + '#$@*' + uuser + '$@#^&*@!'), "")
								wrtdata.write(newdata)
								wrtdata.close()
								lvl3rd.close()
								lvl2rd.close()
								lvl1rd.close()
								lvl0rd.close()
							elif (('$#@!@#$(*(^$#@' + uuser + '!^@*#($)@(@^*&#*@$*#$*#@') in lvl2rd2):
								wrtdata = open("lvl2.txt","w")
								indexs = lvl2rd2.find(('$#@!@#$(*(^$#@' + uuser + '!^@*#($)@(@^*&#*@$*#$*#@') + '$#&@*&$*^')
								indexe = lvl2rd2.find('#$@*' + uuser + '$@#^&*@!')
								rawout = lvl2rd2[(int(indexs)):(int(indexe))]
								newdata = str(lvl2rd2).replace((rawout + '#$@*' + uuser + '$@#^&*@!'), "")
								wrtdata.write(newdata)
								wrtdata.close()
								lvl3rd.close()
								lvl2rd.close()
								lvl1rd.close()
								lvl0rd.close()
							elif (('$#@!@#$(*(^$#@' + uuser + '!^@*#($)@(@^*&#*@$*#$*#@') in lvl1rd2):
								wrtdata = open("lvl1.txt","w")
								indexs = lvl1rd2.find(('$#@!@#$(*(^$#@' + uuser + '!^@*#($)@(@^*&#*@$*#$*#@') + '$#&@*&$*^')
								indexe = lvl1rd2.find('#$@*' + uuser + '$@#^&*@!')
								rawout = lvl1rd2[(int(indexs)):(int(indexe))]
								newdata = str(lvl1rd2).replace((rawout + '#$@*' + uuser + '$@#^&*@!'), "")
								wrtdata.write(newdata)
								wrtdata.close()
								lvl3rd.close()
								lvl2rd.close()
								lvl1rd.close()
								lvl0rd.close()
					else:
						if (argssec in lvl3rd2):
							indexs = lvl3rd2.find(argssec + '$#&@*&$*^')
							indexe = lvl3rd2.find(argsadj + '$@#^&*@!')
							rawout = lvl3rd2[(int(indexs)):(int(indexe))]
							rawout2 = rawout.replace((argssec + '$#&@*&$*^'), "")
							out = rawout2.replace(('#$@*'), "")
							room.message(args.capitalize() + ' is <b>my Mistress</b>.' + ' - Loved by ' + out, html = True)
							lvl3rd.close()
							lvl2rd.close()
							lvl1rd.close()
							lvl0rd.close()
						elif (argssec in lvl2rd2):
							indexs = lvl2rd2.find(argssec + '$#&@*&$*^')
							indexe = lvl2rd2.find(argsadj + '$@#^&*@!')
							rawout = lvl2rd2[(int(indexs)):(int(indexe))]
							rawout2 = rawout.replace((argssec + '$#&@*&$*^'), "")
							out = rawout2.replace(('#$@*'), "")
							room.message(args.capitalize() + ' is slighty <i>special</i>' + ' - Loved by ' + out, html = True)
							lvl3rd.close()
							lvl2rd.close()
							lvl1rd.close()
							lvl0rd.close()
						elif (argssec in lvl1rd2):
							indexs = lvl1rd2.find(argssec + '$#&@*&$*^')
							indexe = lvl1rd2.find(argsadj + '$@#^&*@!')
							rawout = lvl1rd2[(int(indexs)):(int(indexe))]
							rawout2 = rawout.replace((argssec + '$#&@*&$*^'), "")
							out = rawout2.replace(('#$@*'), "")
							room.message(args.capitalize() + ' is a <b>normal user</b>.' + ' - Loved by ' + out, html = True)
							lvl3rd.close()
							lvl2rd.close()
							lvl1rd.close()
							lvl0rd.close()
						elif (args == ""):
							argssec = '$#@!@#$(*(^$#@' + user.name + '!^@*#($)@(@^*&#*@$*#$*#@'
							if (argssec in lvl3rd2):
								indexs = lvl3rd2.find(argssec + '$#&@*&$*^')
								indexe = lvl3rd2.find(user.name + '$@#^&*@!')
								rawout = lvl3rd2[(int(indexs)):(int(indexe))]
								rawout2 = rawout.replace((argssec + '$#&@*&$*^'), "")
								out = rawout2.replace(('#$@*'), "")
								room.message((user.name).capitalize() + ' is <b>my Mistress</b>.' + ' - Loved by ' + out, html = True)
								lvl3rd.close()
								lvl2rd.close()
								lvl1rd.close()
								lvl0rd.close()
							elif (argssec in lvl2rd2):
								indexs = lvl2rd2.find(argssec + '$#&@*&$*^')
								indexe = lvl2rd2.find(user.name + '$@#^&*@!')
								rawout = lvl2rd2[(int(indexs)):(int(indexe))]
								rawout2 = rawout.replace((argssec + '$#&@*&$*^'), "")
								out = rawout2.replace(('#$@*'), "")
								room.message((user.name).capitalize() + ' is slighty <i>special</i>' + ' - Loved by ' + out, html = True)
								lvl3rd.close()
								lvl2rd.close()
								lvl1rd.close()
								lvl0rd.close()
							elif (argssec in lvl1rd2):
								indexs = lvl1rd2.find(argssec + '$#&@*&$*^')
								indexe = lvl1rd2.find(user.name + '$@#^&*@!')
								rawout = lvl1rd2[(int(indexs)):(int(indexe))]
								rawout2 = rawout.replace((argssec + '$#&@*&$*^'), "")
								out = rawout2.replace(('#$@*'), "")
								room.message((user.name).capitalize() + ' is a <b>normal user</b>.' + ' - Loved by ' + out, html = True)
								lvl3rd.close()
								lvl2rd.close()
								lvl1rd.close()
								lvl0rd.close()
							else:
								room.message("We'll just assume that I have not met " + (user.name).capitalize() + " yet.")
								lvl3rd.close()
								lvl2rd.close()
								lvl1rd.close()
								lvl0rd.close()
						else:
							room.message("We'll just assume that I have not met " + args.capitalize() + " yet.")
							lvl3rd.close()
							lvl2rd.close()
							lvl1rd.close()
							lvl0rd.close()
				else:
					if args.find(":") != -1: #if there's a colon somewhere
						room.message("Lol, no.")
						lvl3rd.close()
						lvl2rd.close()
						lvl1rd.close()
						lvl0rd.close()
					else:
						if (argssec in lvl3rd2):
							indexs = lvl3rd2.find(argssec + '$#&@*&$*^')
							indexe = lvl3rd2.find(argsadj + '$@#^&*@!')
							rawout = lvl3rd2[(int(indexs)):(int(indexe))]
							rawout2 = rawout.replace((argssec + '$#&@*&$*^'), "")
							out = rawout2.replace(('#$@*'), "")
							room.message(args.capitalize() + ' is <b>my Mistress</b>.' + ' - Loved by ' + out, html = True)
							lvl3rd.close()
							lvl2rd.close()
							lvl1rd.close()
							lvl0rd.close()
						elif (argssec in lvl2rd2):
							indexs = lvl2rd2.find(argssec + '$#&@*&$*^')
							indexe = lvl2rd2.find(argsadj + '$@#^&*@!')
							rawout = lvl2rd2[(int(indexs)):(int(indexe))]
							rawout2 = rawout.replace((argssec + '$#&@*&$*^'), "")
							out = rawout2.replace(('#$@*'), "")
							room.message(args.capitalize() + ' is slighty <i>special</i>' + ' - Loved by ' + out, html = True)
							lvl3rd.close()
							lvl2rd.close()
							lvl1rd.close()
							lvl0rd.close()
						elif (argssec in lvl1rd2):
							indexs = lvl1rd2.find(argssec + '$#&@*&$*^')
							indexe = lvl1rd2.find(argsadj + '$@#^&*@!')
							rawout = lvl1rd2[(int(indexs)):(int(indexe))]
							rawout2 = rawout.replace((argssec + '$#&@*&$*^'), "")
							out = rawout2.replace(('#$@*'), "")
							room.message(args.capitalize() + ' is a <b>normal user</b>.' + ' - Loved by ' + out, html = True)
							lvl3rd.close()
							lvl2rd.close()
							lvl1rd.close()
							lvl0rd.close()
						elif (args == ""):
							argssec = '$#@!@#$(*(^$#@' + user.name + '!^@*#($)@(@^*&#*@$*#$*#@'
							if (argssec in lvl3rd2):
								indexs = lvl3rd2.find(argssec + '$#&@*&$*^')
								indexe = lvl3rd2.find(user.name + '$@#^&*@!')
								rawout = lvl3rd2[(int(indexs)):(int(indexe))]
								rawout2 = rawout.replace((argssec + '$#&@*&$*^'), "")
								out = rawout2.replace(('#$@*'), "")
								room.message((user.name).capitalize() + ' is <b>my Mistress</b>.' + ' - Loved by ' + out, html = True)
								lvl3rd.close()
								lvl2rd.close()
								lvl1rd.close()
								lvl0rd.close()
							elif (argssec in lvl2rd2):
								indexs = lvl2rd2.find(argssec + '$#&@*&$*^')
								indexe = lvl2rd2.find(user.name + '$@#^&*@!')
								rawout = lvl2rd2[(int(indexs)):(int(indexe))]
								rawout2 = rawout.replace((argssec + '$#&@*&$*^'), "")
								out = rawout2.replace(('#$@*'), "")
								room.message((user.name).capitalize() + ' is slighty <i>special</i>' + ' - Loved by ' + out.capitalize(), html = True)
								lvl3rd.close()
								lvl2rd.close()
								lvl1rd.close()
								lvl0rd.close()
							elif (argssec in lvl1rd2):
								indexs = lvl1rd2.find(argssec + '$#&@*&$*^')
								indexe = lvl1rd2.find(user.name + '$@#^&*@!')
								rawout = lvl1rd2[(int(indexs)):(int(indexe))]
								rawout2 = rawout.replace((argssec + '$#&@*&$*^'), "")
								out = rawout2.replace(('#$@*'), "")
								room.message((user.name).capitalize() + ' is a <b>normal user</b>.' + ' - Loved by ' + out.capitalize(), html = True)
								lvl3rd.close()
								lvl2rd.close()
								lvl1rd.close()
								lvl0rd.close()
							else:
								room.message("We'll just assume that I have not met " + (user.name).capitalize() + " yet.")
								lvl3rd.close()
								lvl2rd.close()
								lvl1rd.close()
								lvl0rd.close()
						else:
							room.message("We'll just assume that I have not met " + args.capitalize() + " yet.")
							lvl3rd.close()
							lvl2rd.close()
							lvl1rd.close()
							lvl0rd.close()
#			elif (cmd.lower()) == "ival":
#			    self.setInterval(int(500), room.message, args)
			elif (cmd.lower()) == "mylvl":
			    mdst = room.getLevel(user)
			    if mdst == 0:
			        room.message("You are a regular user.")
			    elif mdst == 1:
			        room.message("You are a chat moderator.")
			    elif mdst == 2:
			        room.message("You are the head boss.")
			    else:
			        room.message("Your mod level: %i" %(room.getLevel(user)))
			elif (cmd.lower()) == "rr":
			    rrr = random.choice([rr1, rr2, rr2, rr2, rr2, rr1])
			    for i, msg in enumerate(rrr):
			        self.setTimeout(i / 2, room.message, msg)
			elif (cmd.lower()) == "suicide":
				mdlvl = room.getLevel(user)
				if (usrlvl >= 2 or mdlvl >= 1):
				    for i, msg in enumerate(suicide1):
				        self.setTimeout(i / 2, room.message, msg)
			elif (cmd.lower()) == "stfu":
				mdlvl = room.getLevel(user)
				if (usrlvl >= 2 or mdlvl >= 1):
					if args == "":
						croom = room.name
						time.sleep(.2)
						self.leaveRoom(str(room.name))
						time.sleep(300)
						self.joinRoom(room)
					else:
						if (('a' in args.lower()) or ('b' in args.lower()) or ('c' in args.lower()) or ('d' in args.lower()) or ('e' in args.lower()) or ('f' in args.lower()) or ('g' in args.lower()) or ('h' in args.lower()) or ('i' in args.lower()) or ('j' in args.lower()) or ('k' in args.lower()) or ('l' in args.lower()) or ('m' in args.lower()) or ('n' in args.lower()) or ('o' in args.lower()) or ('p' in args.lower()) or ('q' in args.lower()) or ('r' in args.lower()) or ('s' in args.lower()) or ('t' in args.lower()) or ('u' in args.lower()) or ('v' in args.lower()) or ('!' in args.lower()) or ('@' in args.lower()) or ('#' in args.lower()) or ('%' in args.lower()) or ('^' in args.lower()) or ('&' in args.lower()) or ('*' in args.lower()) or ('(' in args.lower()) or (')' in args.lower()) or ('-' in args.lower()) or ('+' in args.lower()) or ('_' in args.lower()) or ('=' in args.lower()) or ('w' in args.lower()) or ('x' in args.lower()) or ('y' in args.lower()) or ('z' in args.lower()) ):
							room.message('Enter a valid number of seconds.')
						elif int(args) > 500:
							croom = room.name
							room.message('The max timeout is 500 seconds. Because you seem to hate me, I will stay in timeout for the max amount of time.')
							time.sleep(.2)
							self.leaveRoom(str(room.name))
							time.sleep(500)
							self.joinRoom(croom)
						else:
							croom = room.name
							timeout = int(args)
							room.message('I am sorry for being bad T-T. I will go to timeout for ' + args + ' seconds.')
							time.sleep(.2)
							self.leaveRoom(str(room.name))
							time.sleep(timeout)
							self.joinRoom(croom)
			elif (cmd.lower()) == "timeout":
				mdlvl = room.getLevel(user)
				if (usrlvl >= 2 or mdlvl >= 1):
					if args == "":
						croom = room.name
						time.sleep(.2)
						self.leaveRoom(str(room.name))
						time.sleep(300)
						self.joinRoom(room)
					else:
						if (('a' in args.lower()) or ('b' in args.lower()) or ('c' in args.lower()) or ('d' in args.lower()) or ('e' in args.lower()) or ('f' in args.lower()) or ('g' in args.lower()) or ('h' in args.lower()) or ('i' in args.lower()) or ('j' in args.lower()) or ('k' in args.lower()) or ('l' in args.lower()) or ('m' in args.lower()) or ('n' in args.lower()) or ('o' in args.lower()) or ('p' in args.lower()) or ('q' in args.lower()) or ('r' in args.lower()) or ('s' in args.lower()) or ('t' in args.lower()) or ('u' in args.lower()) or ('v' in args.lower()) or ('!' in args.lower()) or ('@' in args.lower()) or ('#' in args.lower()) or ('%' in args.lower()) or ('^' in args.lower()) or ('&' in args.lower()) or ('*' in args.lower()) or ('(' in args.lower()) or (')' in args.lower()) or ('-' in args.lower()) or ('+' in args.lower()) or ('_' in args.lower()) or ('=' in args.lower()) or ('w' in args.lower()) or ('x' in args.lower()) or ('y' in args.lower()) or ('z' in args.lower()) ):
							room.message('Enter a valid number of seconds.')
						elif int(args) > 500:
							croom = room.name
							room.message('The max timeout is 500 seconds. Because you seem to hate me, I will stay in timeout for the max amount of time.')
							time.sleep(.2)
							self.leaveRoom(str(room.name))
							time.sleep(500)
							self.joinRoom(croom)
						else:
							croom = room.name
							timeout = int(args)
							room.message('I am sorry for being bad T-T. I will go to timeout for ' + args + ' seconds.')
							time.sleep(.2)
							self.leaveRoom(str(room.name))
							time.sleep(timeout)
							self.joinRoom(croom)
				else:
				    rcide = random.choice([suicide1, suicide2, suicide2, suicide2, suicide2, suicide2, suicide2, suicide2, suicide2, suicide2, suicide2,])
				    for i, msg in enumerate(rcide):
				        self.setTimeout(i / 2, room.message, msg)
				    if rcide == suicide1:
				    	time.sleep(0)
			elif (cmd.lower()) == "modlist":
				if usrlvl >= 2:
					room.message(", ".join(room.modnames + [room.ownername]))
			elif (cmd.lower()) == "nope":
			    print (", ".join(room.modnames + [room.ownername]))
			    wrtdata2 = open("mods.txt","a")
			    wrtdata2.write('\n' + (", ".join(room.modnames + [room.ownername])) )
			    wrtdata2.close()
			elif (cmd.lower()) == "o.o":
			    print (", ".join(room.modnames + [room.ownername]))
			    wrtdata2 = open("mods.txt","a")
			    wrtdata2.write('\n' + (", ".join(room.modnames + [room.ownername])) )
			    wrtdata2.close()
			elif (cmd.lower()) == "yep":
			    print (", ".join(room.banlist))
			elif (cmd.lower()) == "banlist":
				mdlvl = room.getLevel(user)
				if ((usrlvl >=2) or (mdlvl >= 1)):
					banlistr1 = str(room.banlist).replace("[", "")
					banlistr2 = banlistr1.replace("[", "")
					banlistr3 = banlistr2.replace("]", "")
					banlistr4 = banlistr3.replace("[", "")
					banlistr5 = banlistr4.replace("<User: ", "")
					banlistr6 = banlistr5.replace(">", "")
					banlist = banlistr6 + ' is/are currently banned.'
					room.message(banlist)
				else:
					room.message("Haha. Nice try. 2/10 for effort.")
			elif (cmd.lower()) == "bl":
				mdlvl = room.getLevel(user)
				if ((usrlvl >=2) or (mdlvl >= 1)):
					banlistr1 = str(room.banlist).replace("[", "")
					banlistr2 = banlistr1.replace("[", "")
					banlistr3 = banlistr2.replace("]", "")
					banlistr4 = banlistr3.replace("[", "")
					banlistr5 = banlistr4.replace("<User: ", "")
					banlistr6 = banlistr5.replace(">", "")
					banlist = banlistr6 + ' is/are currently banned.'
					room.message(banlist)
				else:
					room.message("Haha. Nice try. 2/10 for effort.")
			elif (cmd.lower()) == "huladance":
				if ((usrlvl >=2) or (mdlvl >= 1)):
					time.sleep(0)
					for i, msg in enumerate(huladance):
						self.setTimeout(i / 2, room.message, msg)
				else:
					room.message("Not going to happen.")
			elif (cmd.lower()) == "lick":
			    time.sleep(0)
			    for i, msg in enumerate(lick):
			        self.setTimeout(i / 2, room.message, msg)
			elif (cmd.lower()) == "fish":
			    if usrlvl >= 2:
			    	time.sleep(0)
			    	room.message("><>")
			elif (cmd.lower()) == "fishes":
			    if usrlvl >= 2:
			    	time.sleep(0)
			    	room.message("><>")
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
			elif (cmd.lower()) == "goml":
			    if usrlvl >= 2:
			    	time.sleep(0)
			    	rgoml = (random.choice(['http://i63.photobucket.com/albums/h139/babyxoxghurl/quotes%20and%20sayings/6d0htts.jpg','http://typophile.com/files/ryan%20get%20on%20my%20level.jpg','http://rlv.zcache.co.uk/get_on_my_level_poster-r8661161397c644918177cdfaac59700a_w2q_400.jpg','http://fc08.deviantart.net/fs71/f/2011/228/2/b/get_on_my_level_by_sabertoothedolivia-d46ucri.jpg','http://i305.photobucket.com/albums/nn222/InsanitySmiles/get-on-my-level.jpg']))
			    	room.message(rgoml)
			elif (cmd.lower()) == "attack":
			    rattack = (random.choice([attack1, attack2, attack3, attack4, attack5, attack6, attack7, attack8]))
			    aau = random.choice(room.usernames)
			    word = str(args)
			    if word == "":
			        if rattack == attack1:
			            time.sleep(1)
			            room.message(rattack)
			        else:
			            aar = (("Attacks ") + aau + (" with ") + rattack)
			            time.sleep(1)
			            room.message(aar)
			    else:
			        if rattack == attack1:
			            time.sleep(1)
			            room.message(rattack)
			        else:
			            aar = (("Attacks ") + word + (" with ") + rattack)
			            time.sleep(1)
			            room.message(aar)
			elif (cmd.lower()) == "tableflip":
				if usrlvl >= 1:
					flipped = random.choice(["Soup flies across the room!", "A fork flies up in the air and pokes you in the eye", "Sammiches, sammiches everywhere.", "The table does a 360 and nothing even moves from its place of the table.", "Meatballs and noodles splatter the wall in the shape of Jesus.", "Good job, you just broke your mother's good china.", "In hindsight, you probably should have taken your computer off of the table before you flipped it.", "Juice spills on the floor and stains your cat a dark redish-purple color.", "The table goes through your window and lands on an old lady, killing her in the process. You better hide the body."])
					time.sleep(1)
					room.message(flipped)
			elif (cmd.lower()) == "help":
				room.message('<a href="http://t6ru.chatango.com/" target="_blank">For help and the list of commands click here.</a>', html = True)
#			elif (cmd.lower()) == "helphug":
#			    for i, msg in enumerate(helphug):
#			        self.setTimeout(i / 2, room.message, msg)
#			elif (cmd.lower()) == "helpdance":
#			    for i, msg in enumerate(helpdance):
#			        self.setTimeout(i / 2, room.message, msg)
#			elif (cmd.lower()) == "helprr":
#			    for i, msg in enumerate(helprr):
#			        self.setTimeout(i / 2, room.message, msg)
#			elif (cmd.lower()) == "helpmylvl":
#			    for i, msg in enumerate(helpmylvl):
#			        self.setTimeout(i / 2, room.message, msg)
#			elif (cmd.lower()) == "helpdie":
#			    for i, msg in enumerate(helpdie):
#			        self.setTimeout(i / 2, room.message, msg)
#			elif (cmd.lower()) == "helpbanlist":
#			    for i, msg in enumerate(helpbanlist):
#			        self.setTimeout(i / 2, room.message, msg)
#			elif (cmd.lower()) == "helpbl":
#			    for i, msg in enumerate(helpbanlist):
#			        self.setTimeout(i / 2, room.message, msg)
#			elif (cmd.lower()) == "helpcmpt":
#			    for i, msg in enumerate(helpcmpt):
#			        self.setTimeout(i / 2, room.message, msg)
#			elif (cmd.lower()) == "helpdefine":
#			    for i, msg in enumerate(helpdefine):
#			        self.setTimeout(i / 2, room.message, msg)
#			elif (cmd.lower()) == "helpmath":
#			    for i, msg in enumerate(helpmath):
#			        self.setTimeout(i / 2, room.message, msg)
#			elif (cmd.lower()) == "helpwotd":
#			    for i, msg in enumerate(helpwotd):
#			        self.setTimeout(i / 2, room.message, msg)
#			elif (cmd.lower()) == "helprdwiki":
#			    for i, msg in enumerate(helprdwiki):
#			        self.setTimeout(i / 2, room.message, msg)
#			elif (cmd.lower()) == "helpimdb":
#			    for i, msg in enumerate(helpimdb):
#			        self.setTimeout(i / 2, room.message, msg)
#			elif (cmd.lower()) == "help1ch":
#			    for i, msg in enumerate(help1ch):
#			        self.setTimeout(i / 2, room.message, msg)
#			elif (cmd.lower()) == "helpdef":
#			    for i, msg in enumerate(helpdef):
#			        self.setTimeout(i / 2, room.message, msg)
#			elif (cmd.lower()) == "helpmodlist":
#			    for i, msg in enumerate(helpmodlist):
#			        self.setTimeout(i / 2, room.message, msg)
#			elif (cmd.lower()) == "helpslang":
#			    for i, msg in enumerate(helpslang):
#			        self.setTimeout(i / 2, room.message, msg)
#			elif (cmd.lower()) == "helplick":
#			    for i, msg in enumerate(helplick):
#			        self.setTimeout(i / 2, room.message, msg)
#			elif (cmd.lower()) == "helphuladance":
#			    for i, msg in enumerate(helphuladance):
#			        self.setTimeout(i / 2, room.message, msg)
#			elif (cmd.lower()) == "helpspinthebottle":
#			    for i, msg in enumerate(helpspinthebottle):
#			        self.setTimeout(i / 2, room.message, msg)
#			elif (cmd.lower()) == "helpsay":
#			    for i, msg in enumerate(helpsay):
#			        self.setTimeout(i / 2, room.message, msg)
#			elif (cmd.lower()) == "helpsuicide":
#			    for i, msg in enumerate(helpsuicide):
#			        self.setTimeout(i / 2, room.message, msg)
#			elif (cmd.lower()) == "commands":
#			    for i, msg in enumerate(cmdlst):
#			        self.setTimeout(i / 2, room.message, msg)
#			elif (cmd.lower()) == "list":
#			    for i, msg in enumerate(cmdlst):
#			        self.setTimeout(i / 2, room.message, msg)
#			elif (cmd.lower()) == "cd":
#			    room.message("3")
#			    self.sleep(1)
#			    room.message("2")
#			    self.sleep(1)
#			    room.message("1")
#			    self.sleep(1)
#			    room.message("Go!")
#			    self.sleep(1)
#			elif (cmd.lower()) == "commandlist":
#			    for i, msg in enumerate(cmdlst):
#			        self.setTimeout(i / 2, room.message, msg)
			elif (cmd.lower()) == "uptime":
#strftime("%a, %d %b %Y %H:%M:%S GMT", gmtime())
			    time.sleep(1)
			    room.message("I connected at " + (str(now).replace("['", "")).replace("']", ""))
			elif (cmd.lower()) == "say":
			    if usrlvl>=1:
			    	time.sleep(1)
			    	room.message(args, html = True)
			elif (cmd.lower()) == "":
			    nameres = 'Yes, '
			    nameres2 = '?'
			    fnameres = nameres + (user.name).capitalize() + nameres2
			    time.sleep(2)
			    room.message(fnameres)
			elif (cmd.lower()) == "cmpt":
			    rcmpt = random.choice([cmpt1, cmpt2,cmpt3, cmpt4, cmpt5])
			    fcmpt = args.capitalize() + str(rcmpt)
			    time.sleep(1)
			    room.message(fcmpt)
			elif (cmd.lower()) == "poker":
				if usrlvl >= 0:
					rpgpr = open("pgp.txt","r")
					rpgp = (rpgpr.read()).lower()
					cindexs = rpgp.find('*#&$^#cards = ')
					cindexe = rpgp.find('#&#@$($#')
					crawout = rpgp[(int(cindexs)):(int(cindexe))]
					crawout2 = crawout.replace(('*#&$^#cards = '), "")
					cardsstr = crawout2.replace(('#&#@$($#'), "")
					cardsprep = re.split(', ', cardsstr)
					cards = [item.lower() for item in cardsprep]
					def cdt(cards):
						return random.choice(cards)
					if ((args.lower() == '><>') and (user.name == 'ion')):
						indexs = rpgp.find('^$&*available = ')
						indexe = rpgp.find(' *)!#')
						rawout = rpgp[(int(indexs)):(int(indexe))]
						rawout2 = rawout.replace(('^$&*available = '), "")
						available = rawout2.replace((' *)!#'), "")
						if available == '0':
							wrtset1 = open("pgp.txt", "w")
							wrtset1.write('*$#^!players = 2 &^$*\n^$&*available = 2 *)!#\n##$*!@turn = 1@*&(*\n')
							wrtset1.close()
						elif user.name in rpgp:
							room.message("You have already drawn for this game.")
						else:
							card1 = 'Ace of spades'
							card2 = 'King of spades'
							card3 = 'IceQueen of spades'
							card4 = 'Jack of spades'
							card5 = '10 of spades'
							handpoints = 1000
							highcard = 14
							availableir = int(available)
							availablei = availableir - 1
							availblenew = '^$&*available = ' + str(availablei) + ' *)!#'
							pgpnew = rpgp.replace(('^$&*available = ' + available + ' *)!#'), str(availblenew))
							wrtdata2 = open("pgp.txt", "w")
							secnames = '#$!*&^!@' + available + user.name + '&&*)^$#@!'
							secnamef = ')(&$&$#@' + available + user.name + '!@&@$@^&'
							highnames = '!!@*^$&' + available + user.name + '**^&$$#!('
							highnamef = '&(#*$%!)^' + available + user.name + '(*&$@@#!'
							wrtdata2.write(pgpnew + '\n' + secnames + ("handpointp%d = %d" %(availableir, handpoints)) + secnamef + '\n' + highnames + ("highcardp%d = %d" %(availableir, highcard)) + highnamef + '\n' )
							wrtdata2.close()
							rpgpr.close()
							pgpfr = open("pgp.txt","r")
							pgpf = (pgpfr.read()).lower()
							room.message(str("The cards you drew are: " + card1 + ", " + card2 + ", " + card3 + ", " + card4 + ", " + card5 + "."))
							if availablei == 0:
								indexsp1 = pgpf.find('&&*)^$#@!handpointp1 = ')
								indexep1 = pgpf.find(')(&$&$#@1')
								rawoutp1 = pgpf[(int(indexsp1)):(int(indexep1))]
								rawout2p1 = rawoutp1.replace(('&&*)^$#@!handpointp1 = '), "")
								pointsrp1 = rawout2p1.replace((')(&$&$#@1'), "")
								pointsp1 = int(pointsrp1)
								indexsp2 = pgpf.find('&&*)^$#@!handpointp2 = ')
								indexep2 = pgpf.find(')(&$&$#@2')
								rawoutp2 = pgpf[(int(indexsp2)):(int(indexep2))]
								rawout2p2 = rawoutp2.replace(('&&*)^$#@!handpointp2 = '), "")
								pointsrp2 = rawout2p2.replace((')(&$&$#@2'), "")
								pointsp2 = int(pointsrp2)
								indexshp1 = pgpf.find('**^&$$#!(highcardp1 = ')
								indexehp1 = pgpf.find('&(#*$%!)^1')
								rawouthp1 = pgpf[(int(indexshp1)):(int(indexehp1))]
								rawout2hp1 = rawouthp1.replace(('**^&$$#!(highcardp1 = '), "")
								pointsrhp1 = rawout2hp1.replace(('&(#*$%!)^1'), "")
								pointshp1 = int(pointsrhp1)
								indexshp2 = pgpf.find('**^&$$#!(highcardp2 = ')
								indexehp2 = pgpf.find('&(#*$%!)^2')
								rawouthp2 = pgpf[(int(indexshp2)):(int(indexehp2))]
								rawout2hp2 = rawouthp2.replace(('**^&$$#!(highcardp2 = '), "")
								pointsrhp2 = rawout2hp2.replace(('&(#*$%!)^2'), "")
								pointshp2 = int(pointsrhp2)
								if (pointsp1 > pointsp2):
									indexsw = pgpf.find('#$!*&^!@1')
									indexew = pgpf.find(')(&$&$#@1')
									rawoutw = pgpf[(int(indexsw)):(int(indexew))]
									rawout2w = rawoutw.replace(('#$!*&^!@1'), "")
									victorrw = rawout2w.replace(('&&*)^$#@!handpointp1 = ' + pointsrp1), "")
									victorw = victorrw.replace((')(&$&$#@1'), "")
									room.message(victorw.capitalize() + " wins the match!")
									pgpfr.close()
									wrtset1 = open("pgp.txt", "w")
									wrtset1.write("*$#^!players = 2 &^$*\n^$&*available = 2 *)!#\n##$*!@turn = 1@*&(*\n*#&$^#cards = #&!2 of hearts, #&!3 of hearts, #&!4 of hearts, #&!5 of hearts, #&!6 of hearts, #&!7 of hearts, #&!8 of hearts, #&!9 of hearts, #&!10 of hearts, #&!Jack of hearts, #&!IceQueen of hearts, #&!King of hearts, #&!Ace of hearts, #&!2 of diamonds, #&!3 of diamonds, #&!4 of diamonds, #&!5 of diamonds, #&!6 of diamonds, #&!7 of diamonds, #&!8 of diamonds, #&!9 of diamonds, #&!10 of diamonds, #&!Jack of diamonds, #&!IceQueen of diamonds, #&!King of diamonds, #&!Ace of diamonds, #&!2 of clubs, #&!3 of clubs, #&!4 of clubs, #&!5 of clubs, #&!6 of clubs, #&!7 of clubs, #&!8 of clubs, #&!9 of clubs, #&!10 of clubs, #&!Jack of clubs, #&!IceQueen of clubs, #&!King of clubs, #&!Ace of clubs, #&!2 of spades, #&!3 of spades, #&!4 of spades, #&!5 of spades, #&!6 of spades, #&!7 of spades, #&!8 of spades, #&!9 of spades, #&!10 of spades, #&!Jack of spades, #&!IceQueen of spades, #&!King of spades, #&!Ace of spades#&#@$($#\n")
									wrtset1.close()
								elif (pointsp2 > pointsp1):
									indexsw = pgpf.find('#$!*&^!@2')
									indexew = pgpf.find(')(&$&$#@2')
									rawoutw = pgpf[(int(indexsw)):(int(indexew))]
									rawout2w = rawoutw.replace(('#$!*&^!@2'), "")
									victorrw = rawout2w.replace(('&&*)^$#@!handpointp2 = ' + pointsrp2), "")
									victorw = victorrw.replace((')(&$&$#@2'), "")
									room.message(victorw.capitalize() + " wins the match!")
									pgpfr.close()
									wrtset1 = open("pgp.txt", "w")
									wrtset1.write("*$#^!players = 2 &^$*\n^$&*available = 2 *)!#\n##$*!@turn = 1@*&(*\n*#&$^#cards = #&!2 of hearts, #&!3 of hearts, #&!4 of hearts, #&!5 of hearts, #&!6 of hearts, #&!7 of hearts, #&!8 of hearts, #&!9 of hearts, #&!10 of hearts, #&!Jack of hearts, #&!IceQueen of hearts, #&!King of hearts, #&!Ace of hearts, #&!2 of diamonds, #&!3 of diamonds, #&!4 of diamonds, #&!5 of diamonds, #&!6 of diamonds, #&!7 of diamonds, #&!8 of diamonds, #&!9 of diamonds, #&!10 of diamonds, #&!Jack of diamonds, #&!IceQueen of diamonds, #&!King of diamonds, #&!Ace of diamonds, #&!2 of clubs, #&!3 of clubs, #&!4 of clubs, #&!5 of clubs, #&!6 of clubs, #&!7 of clubs, #&!8 of clubs, #&!9 of clubs, #&!10 of clubs, #&!Jack of clubs, #&!IceQueen of clubs, #&!King of clubs, #&!Ace of clubs, #&!2 of spades, #&!3 of spades, #&!4 of spades, #&!5 of spades, #&!6 of spades, #&!7 of spades, #&!8 of spades, #&!9 of spades, #&!10 of spades, #&!Jack of spades, #&!IceQueen of spades, #&!King of spades, #&!Ace of spades#&#@$($#\n")
									wrtset1.close()
								elif (pointsp2 == pointsp1):
									if (pointshp1 > pointshp2):
										indexsw = pgpf.find('#$!*&^!@1')
										indexew = pgpf.find(')(&$&$#@1')
										rawoutw = pgpf[(int(indexsw)):(int(indexew))]
										rawout2w = rawoutw.replace(('#$!*&^!@1'), "")
										victorrw = rawout2w.replace(('&&*)^$#@!handpointp1 = ' + pointsrp1), "")
										victorw = victorrw.replace((')(&$&$#@1'), "")
										room.message(victorw.capitalize() + " wins the match!")
										pgpfr.close()
										wrtset1 = open("pgp.txt", "w")
										wrtset1.write("*$#^!players = 2 &^$*\n^$&*available = 2 *)!#\n##$*!@turn = 1@*&(*\n*#&$^#cards = #&!2 of hearts, #&!3 of hearts, #&!4 of hearts, #&!5 of hearts, #&!6 of hearts, #&!7 of hearts, #&!8 of hearts, #&!9 of hearts, #&!10 of hearts, #&!Jack of hearts, #&!IceQueen of hearts, #&!King of hearts, #&!Ace of hearts, #&!2 of diamonds, #&!3 of diamonds, #&!4 of diamonds, #&!5 of diamonds, #&!6 of diamonds, #&!7 of diamonds, #&!8 of diamonds, #&!9 of diamonds, #&!10 of diamonds, #&!Jack of diamonds, #&!IceQueen of diamonds, #&!King of diamonds, #&!Ace of diamonds, #&!2 of clubs, #&!3 of clubs, #&!4 of clubs, #&!5 of clubs, #&!6 of clubs, #&!7 of clubs, #&!8 of clubs, #&!9 of clubs, #&!10 of clubs, #&!Jack of clubs, #&!IceQueen of clubs, #&!King of clubs, #&!Ace of clubs, #&!2 of spades, #&!3 of spades, #&!4 of spades, #&!5 of spades, #&!6 of spades, #&!7 of spades, #&!8 of spades, #&!9 of spades, #&!10 of spades, #&!Jack of spades, #&!IceQueen of spades, #&!King of spades, #&!Ace of spades#&#@$($#\n")
										wrtset1.close()
									elif (pointshp2 > pointshp1):
										indexsw = pgpf.find('#$!*&^!@2')
										indexew = pgpf.find(')(&$&$#@2')
										rawoutw = pgpf[(int(indexsw)):(int(indexew))]
										rawout2w = rawoutw.replace(('#$!*&^!@2'), "")
										victorrw = rawout2w.replace(('&&*)^$#@!handpointp2 = ' + pointsrp2), "")
										victorw = victorrw.replace((')(&$&$#@2'), "")
										room.message(victorw.capitalize() + " wins the match!")
										pgpfr.close()
										wrtset1 = open("pgp.txt", "w")
										wrtset1.write("*$#^!players = 2 &^$*\n^$&*available = 2 *)!#\n##$*!@turn = 1@*&(*\n*#&$^#cards = #&!2 of hearts, #&!3 of hearts, #&!4 of hearts, #&!5 of hearts, #&!6 of hearts, #&!7 of hearts, #&!8 of hearts, #&!9 of hearts, #&!10 of hearts, #&!Jack of hearts, #&!IceQueen of hearts, #&!King of hearts, #&!Ace of hearts, #&!2 of diamonds, #&!3 of diamonds, #&!4 of diamonds, #&!5 of diamonds, #&!6 of diamonds, #&!7 of diamonds, #&!8 of diamonds, #&!9 of diamonds, #&!10 of diamonds, #&!Jack of diamonds, #&!IceQueen of diamonds, #&!King of diamonds, #&!Ace of diamonds, #&!2 of clubs, #&!3 of clubs, #&!4 of clubs, #&!5 of clubs, #&!6 of clubs, #&!7 of clubs, #&!8 of clubs, #&!9 of clubs, #&!10 of clubs, #&!Jack of clubs, #&!IceQueen of clubs, #&!King of clubs, #&!Ace of clubs, #&!2 of spades, #&!3 of spades, #&!4 of spades, #&!5 of spades, #&!6 of spades, #&!7 of spades, #&!8 of spades, #&!9 of spades, #&!10 of spades, #&!Jack of spades, #&!IceQueen of spades, #&!King of spades, #&!Ace of spades#&#@$($#\n")
										wrtset1.close()
									elif (pointshp2 == pointshp1):
										room.message("It is a draw!")
										pgpfr.close()
										wrtset1 = open("pgp.txt", "w")
										wrtset1.write("*$#^!players = 2 &^$*\n^$&*available = 2 *)!#\n##$*!@turn = 1@*&(*\n*#&$^#cards = #&!2 of hearts, #&!3 of hearts, #&!4 of hearts, #&!5 of hearts, #&!6 of hearts, #&!7 of hearts, #&!8 of hearts, #&!9 of hearts, #&!10 of hearts, #&!Jack of hearts, #&!IceQueen of hearts, #&!King of hearts, #&!Ace of hearts, #&!2 of diamonds, #&!3 of diamonds, #&!4 of diamonds, #&!5 of diamonds, #&!6 of diamonds, #&!7 of diamonds, #&!8 of diamonds, #&!9 of diamonds, #&!10 of diamonds, #&!Jack of diamonds, #&!IceQueen of diamonds, #&!King of diamonds, #&!Ace of diamonds, #&!2 of clubs, #&!3 of clubs, #&!4 of clubs, #&!5 of clubs, #&!6 of clubs, #&!7 of clubs, #&!8 of clubs, #&!9 of clubs, #&!10 of clubs, #&!Jack of clubs, #&!IceQueen of clubs, #&!King of clubs, #&!Ace of clubs, #&!2 of spades, #&!3 of spades, #&!4 of spades, #&!5 of spades, #&!6 of spades, #&!7 of spades, #&!8 of spades, #&!9 of spades, #&!10 of spades, #&!Jack of spades, #&!IceQueen of spades, #&!King of spades, #&!Ace of spades#&#@$($#\n")
										wrtset1.close()
					else:
						indexs = rpgp.find('^$&*available = ')
						indexe = rpgp.find(' *)!#')
						rawout = rpgp[(int(indexs)):(int(indexe))]
						rawout2 = rawout.replace(('^$&*available = '), "")
						available = rawout2.replace((' *)!#'), "")
						if available == '0':
							wrtset1 = open("pgp.txt", "w")
							wrtset1.write('*$#^!players = 2 &^$*\n^$&*available = 2 *)!#\n##$*!@turn = 1@*&(*\n')
							wrtset1.close()
						elif user.name in rpgp:
							room.message("You have already drawn for this game.")
						else:
							card1r = cdt(cards)
							card1 = card1r.replace("#&!", "")
							cs2r1 = str(cards).replace("[", "")
							cs2r2 = cs2r1.replace("]", "")
							cs2r3 = cs2r2.replace(" '#&!", "#&!")
							cs2r4 = cs2r3.replace("'", "")
							cardset2rr = cs2r4.replace(str(card1) + ',', "")
							cardset2r = cardset2rr.replace("#&!#&!", "#&!")
							cardset2 = ([n for n in cardset2r.split(",")])
							card2r = cdt(cardset2)
							card2 = card2r.replace("#&!", "")
							cs3r1 = str(cardset2).replace("[", "")
							cs3r2 = cs3r1.replace("]", "")
							cs3r3 = cs3r2.replace(" '#&!", "#&!")
							cs3r4 = cs3r3.replace("'", "")
							cardset3rr = cs3r4.replace((str(card2) + ','), '')
							cardset3r = cardset3rr.replace("#&!#&!", "#&!")
							cardset3 = ([n for n in cardset3r.split(',')])
							card3r = cdt(cardset3)
							card3 = card3r.replace("#&!", "")
							cs4r1 = str(cardset3).replace("[", "")
							cs4r2 = cs4r1.replace("]", "")
							cs4r3 = cs4r2.replace(" '#&!", "#&!")
							cs4r4 = cs4r3.replace("'", "")
							cardset4rr = cs4r4.replace((str(card3) + ','), '')
							cardset4r = cardset4rr.replace("#&!#&!", "#&!")
							cardset4 = ([n for n in cardset4r.split(',')])
							card4r = cdt(cardset4)
							card4 = card4r.replace("#&!", "")
							cs5r1 = str(cardset4).replace("[", "")
							cs5r2 = cs5r1.replace("]", "")
							cs5r3 = cs5r2.replace(" '#&!", "#&!")
							cs5r4 = cs5r3.replace("'", "")
							cardset5rr = cs5r4.replace((str(card4) + ','), '')
							cardset5r = cardset5rr.replace("#&!#&!", "#&!")
							cardset5 = ([n for n in cardset5r.split(',')])
							card5r = cdt(cardset5)
							card5 = card5r.replace("#&!", "")
							csfr1 = str(cardset5).replace("[", "")
							csfr2 = csfr1.replace("]", "")
							csfr3 = csfr2.replace(" '#&!", "#&!")
							csfr4 = csfr3.replace("'", "")
							cardsetfrr = csfr4.replace((str(card5) + ','), '')
							cardsetfr = cardsetfrr.replace("#&!#&!", "#&!")
							cardsetf = ([n for n in cardsetfr.split(',')])
							fcsfr1 = str(cardsetf).replace("[", "")
							fcsfr2 = fcsfr1.replace("]", "")
							fcsfr3 = fcsfr2.replace("'#&!", "#&!")
							fcsfr4 = fcsfr3.replace("'", "")
							fcs2r1 = str(cards).replace("[", "")
							fcs2r2 = fcs2r1.replace("]", "")
							fcs2r3 = fcs2r2.replace("'#&!", "#&!")
							fcs2r4 = fcs2r3.replace("'", "")
							pgpnewcd = rpgp.replace(fcs2r4, fcsfr4)
							wrtnewcd = open("pgp.txt", "w")
							wrtnewcd.write(pgpnewcd)
							wrtnewcd.close()
							rpgpr.close()
							pgpr = open("pgp.txt","r")
							pgp = (pgpr.read()).lower()
							handstrr = card1 + "," + card2 + "," + card3 + "," + card4 + "," + card5
							handli = handstrr.lower()
							#handli = ([n for n in handstr.split(',')])
							cvp2f = handli.count('2')
							cvp3f = handli.count('3')
							cvp4f = handli.count('4')
							cvp5f = handli.count('5')
							cvp6f = handli.count('6')
							cvp7f = handli.count('7')
							cvp8f = handli.count('8')
							cvp9f = handli.count('9')
							cvp10f = handli.count('10')
							cvpjf = handli.count('jack')
							cvpqf = handli.count('icequeen')
							cvpkf = handli.count('king')
							cvpaf = handli.count('ace')
							svpcf = handli.count('clubs')
							svpsf = handli.count('spades')
							svphf = handli.count('hearts')
							svpdf = handli.count('diamonds')
							if cvp2f == 1:
								pointv21 = 2
								highcard = 2
								pointv20 = 0
								pointv22 = 0
								pointv23 = 0
								pointv24 = 0
							elif cvp2f == 2:
								pointv22 = 2
								highcard = 2
								pointv20 = 0
								pointv21 = 0
								pointv23 = 0
								pointv24 = 0
							elif cvp2f == 3:
								pointv23 = 2
								highcard = 2
								pointv20 = 0
								pointv21 = 0
								pointv22 = 0
								pointv24 = 0
							elif cvp2f == 4:
								pointv24 = 2
								highcard = 2
								pointv20 = 0
								pointv21 = 0
								pointv22 = 0
								pointv23 = 0
							elif cvp2f == 0:
								pointv20 = 0
								pointv21 = 0
								pointv22 = 0
								pointv23 = 0
								pointv24 = 0
							if cvp3f == 1:
								pointv31 = 3
								highcard = 3
								pointv30 = 0
								pointv32 = 0
								pointv33 = 0
								pointv34 = 0
							elif cvp3f == 2:
								pointv32 = 3
								highcard = 3
								pointv30 = 0
								pointv31 = 0
								pointv33 = 0
								pointv34 = 0
							elif cvp3f == 3:
								pointv33 = 3
								highcard = 3
								pointv30 = 0
								pointv31 = 0
								pointv32 = 0
								pointv34 = 0
							elif cvp3f == 4:
								pointv34 = 3
								highcard = 3
								pointv30 = 0
								pointv31 = 0
								pointv32 = 0
								pointv33 = 0
							elif cvp3f == 0:
								pointv30 = 0
								pointv31 = 0
								pointv32 = 0
								pointv33 = 0
								pointv34 = 0
							if cvp4f == 1:
								pointv41 = 4
								highcard = 4
								pointv40 = 0
								pointv42 = 0
								pointv43 = 0
								pointv44 = 0
							elif cvp4f == 2:
								pointv42 = 4
								highcard = 4
								pointv40 = 0
								pointv41 = 0
								pointv43 = 0
								pointv44 = 0
							elif cvp4f == 3:
								pointv43 = 4
								pointv40 = 0
								pointv41 = 0
								pointv42 = 0
								pointv44 = 0
							elif cvp4f == 4:
								pointv44 = 4
								pointv40 = 0
								pointv41 = 0
								pointv42 = 0
								pointv43 = 0
							elif cvp4f == 0:

								pointv40 = 0
								pointv41 = 0
								pointv42 = 0
								pointv43 = 0
								pointv44 = 0
							if cvp5f == 1:
								pointv51 = 5
								highcard = 5
								pointv50 = 0
								pointv52 = 0
								pointv53 = 0
								pointv54 = 0
							elif cvp5f == 2:
								pointv52 = 5
								highcard = 5
								pointv50 = 0
								pointv51 = 0
								pointv53 = 0
								pointv54 = 0
							elif cvp5f == 3:
								pointv53 = 5
								highcard = 5
								pointv50 = 0
								pointv51 = 0
								pointv52 = 0
								pointv54 = 0
							elif cvp5f == 4:
								pointv54 = 5
								highcard = 5
								pointv50 = 0
								pointv51 = 0
								pointv52 = 0
								pointv53 = 0
							elif cvp5f == 0:
								pointv50 = 0
								pointv51 = 0
								pointv52 = 0
								pointv53 = 0
								pointv54 = 0
							if cvp6f == 1:
								pointv61 = 6
								highcard = 6
								pointv60 = 0
								pointv62 = 0
								pointv63 = 0
								pointv64 = 0
							elif cvp6f == 2:
								pointv62 = 6
								highcard = 6
								pointv60 = 0
								pointv61 = 0
								pointv63 = 0
								pointv64 = 0
							elif cvp6f == 3:
								pointv63 = 6
								highcard = 6
								pointv60 = 0
								pointv61 = 0
								pointv62 = 0
								pointv64 = 0
							elif cvp6f == 4:
								pointv64 = 6
								highcard = 6
								pointv60 = 0
								pointv61 = 0
								pointv62 = 0
								pointv63 = 0
							elif cvp6f == 0:
								pointv60 = 0
								pointv61 = 0
								pointv62 = 0
								pointv63 = 0
								pointv64 = 0
							if cvp7f == 1:
								pointv71 = 7
								highcard = 7
								pointv70 = 0
								pointv72 = 0
								pointv73 = 0
								pointv74 = 0
							elif cvp7f == 2:
								pointv72 = 7
								highcard = 7
								pointv70 = 0
								pointv71 = 0
								pointv73 = 0
								pointv74 = 0
							elif cvp7f == 3:
								pointv73 = 7
								highcard = 7
								pointv70 = 0
								pointv71 = 0
								pointv72 = 0
								pointv74 = 0
							elif cvp7f == 4:
								pointv74 = 7
								highcard = 7
								pointv70 = 0
								pointv71 = 0
								pointv72 = 0
								pointv73 = 0
							elif cvp7f == 0:
								pointv70 = 0
								pointv71 = 0
								pointv72 = 0
								pointv73 = 0
								pointv74 = 0
							if cvp8f == 1:
								pointv81 = 8
								highcard = 8
								pointv80 = 0
								pointv82 = 0
								pointv83 = 0
								pointv84 = 0
							elif cvp8f == 2:
								pointv82 = 8
								highcard = 8
								pointv80 = 0
								pointv81 = 0
								pointv83 = 0
								pointv84 = 0
							elif cvp8f == 3:
								pointv83 = 8
								highcard = 8
								pointv80 = 0
								pointv81 = 0
								pointv82 = 0
								pointv84 = 0
							elif cvp8f == 4:
								pointv84 = 8
								highcard = 8
								pointv80 = 0
								pointv81 = 0
								pointv82 = 0
								pointv83 = 0
							elif cvp8f == 0:
								pointv80 = 0
								pointv81 = 0
								pointv82 = 0
								pointv83 = 0
								pointv84 = 0
							if cvp9f == 1:
								pointv91 = 9
								highcard = 9
								pointv90 = 0
								pointv92 = 0
								pointv93 = 0
								pointv94 = 0
							elif cvp9f == 2:
								pointv92 = 9
								highcard = 9
								pointv90 = 0
								pointv91 = 0
								pointv93 = 0
								pointv94 = 0
							elif cvp9f == 3:
								pointv93 = 9
								highcard = 9
								pointv90 = 0
								pointv91 = 0
								pointv92 = 0
								pointv94 = 0
							elif cvp9f == 4:
								pointv94 = 9
								highcard = 9
								pointv90 = 0
								pointv91 = 0
								pointv92 = 0
								pointv93 = 0
							elif cvp9f == 0:
								pointv90 = 0
								pointv91 = 0
								pointv92 = 0
								pointv93 = 0
								pointv94 = 0
							if cvp10f == 1:
								pointv101 = 10
								highcard = 10
								pointv100 = 0
								pointv102 = 0
								pointv103 = 0
								pointv104 = 0
							elif cvp10f == 2:
								pointv102 = 10
								highcard = 10
								pointv100 = 0
								pointv101 = 0
								pointv103 = 0
								pointv104 = 0
							elif cvp10f == 3:
								pointv103 = 10
								highcard = 10
								pointv100 = 0
								pointv101 = 0
								pointv102 = 0
								pointv104 = 0
							elif cvp10f == 4:
								pointv104 = 10
								highcard = 10
								pointv100 = 0
								pointv101 = 0
								pointv102 = 0
								pointv103 = 0
							elif cvp10f == 0:
								pointv100 = 0
								pointv101 = 0
								pointv102 = 0
								pointv103 = 0
								pointv104 = 0
							if cvpjf == 1:
								pointvj1 = 11
								highcard = 11
								pointvj0 = 0
								pointvj2 = 0
								pointvj3 = 0
								pointvj4 = 0
							elif cvpjf == 2:
								pointvj2 = 11
								highcard = 11
								pointvj0 = 0
								pointvj1 = 0
								pointvj3 = 0
								pointvj4 = 0
							elif cvpjf == 3:
								pointvj3 = 11
								highcard = 11
								pointvj0 = 0
								pointvj1 = 0
								pointvj2 = 0
								pointvj4 = 0
							elif cvpjf == 4:
								pointvj4 = 11
								highcard = 11
								pointvj0 = 0
								pointvj1 = 0
								pointvj2 = 0
								pointvj3 = 0
							elif cvpjf == 0:
								pointvj0 = 0
								pointvj1 = 0
								pointvj2 = 0
								pointvj3 = 0
								pointvj4 = 0
							if cvpqf == 1:
								pointvq1 = 12
								highcard = 12
								pointvq0 = 0

								pointvq2 = 0
								pointvq3 = 0
								pointvq4 = 0
							elif cvpqf == 2:
								pointvq2 = 12
								highcard = 12
								pointvq0 = 0
								pointvq1 = 0
								pointvq3 = 0
								pointvq4 = 0
							elif cvpqf == 3:
								pointvq3 = 12
								highcard = 12
								pointvq0 = 0
								pointvq1 = 0
								pointvq2 = 0
								pointvq4 = 0
							elif cvpqf == 4:
								pointvq4 = 12
								highcard = 12
								pointvq0 = 0
								pointvq1 = 0
								pointvq2 = 0
								pointvq3 = 0
							elif cvpqf == 0:
								pointvq0 = 0
								pointvq1 = 0
								pointvq2 = 0
								pointvq3 = 0
								pointvq4 = 0
							if cvpkf == 1:
								pointvk1 = 13
								highcard = 13
								pointvk0 = 0
								pointvk2 = 0
								pointvk3 = 0
								pointvk4 = 0
							elif cvpkf == 2:
								pointvk2 = 13
								highcard = 13
								pointvk0 = 0
								pointvk1 = 0
								pointvk3 = 0
								pointvk4 = 0
							elif cvpkf == 3:
								pointvk3 = 13
								highcard = 13
								pointvk0 = 0
								pointvk1 = 0
								pointvk2 = 0
								pointvk4 = 0
							elif cvpkf == 4:
								pointvk4 = 13
								highcard = 13
								pointvk0 = 0
								pointvk1 = 0
								pointvk2 = 0
								pointvk3 = 0
							elif cvpkf == 0:
								pointvk0 = 0
								pointvk1 = 0
								pointvk2 = 0
								pointvk3 = 0
								pointvk4 = 0
							if cvpaf == 1:
								pointva1 = 14
								highcard = 14
								pointva0 = 0
								pointva2 = 0
								pointva3 = 0
								pointva4 = 0
							elif cvpaf == 2:
								pointva2 = 14
								highcard = 14
								pointva0 = 0
								pointva1 = 0
								pointva3 = 0
								pointva4 = 0
							elif cvpaf == 3:
								pointva3 = 14
								highcard = 14
								pointva0 = 0
								pointva1 = 0
								pointva2 = 0
								pointva4 = 0
							elif cvpaf == 4:
								pointva4 = 14
								highcard = 14
								pointva0 = 0
								pointva1 = 0
								pointva2 = 0
								pointva3 = 0
							elif cvpaf == 0:
								pointva0 = 0
								pointva1 = 0
								pointva2 = 0
								pointva3 = 0
								pointva4 = 0
							if svpdf == 1:
								pointvd = 0
							elif svpdf == 2:
								pointvd = 0
							elif svpdf == 3:
								pointvd = 0
							elif svpdf == 4:
								pointvd = 0
							elif svpdf == 5:
								pointvd = 1
							elif svpdf == 0:
								pointvd = 0
							if svphf == 1:
								pointvh = 0
							elif svphf == 2:
								pointvh = 0
							elif svphf == 3:
								pointvh = 0
							elif svphf == 4:
								pointvh = 0
							elif svphf == 5:
								pointvh = 1
							elif svphf == 0:
								pointvh = 0
							if svpsf == 1:
								pointvs = 0
							elif svpsf == 2:
								pointvs = 0
							elif svpsf == 3:
								pointvs = 0
							elif svpsf == 4:
								pointvs = 0
							elif svpsf == 5:
								pointvs = 1
							elif svpsf == 0:
								pointvs = 0
							if svpcf == 1:
								pointvc = 0
							elif svpcf == 2:
								pointvc = 0
							elif svpcf == 3:
								pointvc = 0
							elif svpcf == 4:
								pointvc = 0
							elif svpcf == 5:
								pointvc = 1
							elif svpcf == 0:
								pointvc = 0
							if ( (cvp10f == 1) and (cvpjf == 1) and (cvpqf == 1) and (cvpkf == 1) and (cvpaf == 1) and ((svpcf == 5) or(svpsf == 5) or(svphf == 5) or(svpdf == 5))):
								handpoints = 1000
							elif ( (cvp10f == 1) and (cvpjf == 1) and (cvpqf == 1) and (cvpkf == 1) and (cvp9f == 1) and ((svpcf == 5) or(svpsf == 5) or(svphf == 5) or(svpdf == 5))):
								handpoints = 999
							elif ( (cvp10f == 1) and (cvpjf == 1) and (cvpqf == 1) and (cvp8f == 1) and (cvp9f == 1) and ((svpcf == 5) or(svpsf == 5) or(svphf == 5) or(svpdf == 5))):
								handpoints = 998
							elif ( (cvp10f == 1) and (cvpjf == 1) and (cvp7f == 1) and (cvp8f == 1) and (cvp9f == 1) and ((svpcf == 5) or(svpsf == 5) or(svphf == 5) or(svpdf == 5))):
								handpoints = 997
							elif ( (cvp10f == 1) and (cvp6f == 1) and (cvp7f == 1) and (cvp8f == 1) and (cvp9f == 1) and ((svpcf == 5) or(svpsf == 5) or(svphf == 5) or(svpdf == 5))):
								handpoints = 996
							elif ( (cvp5f == 1) and (cvp6f == 1) and (cvp7f == 1) and (cvp8f == 1) and (cvp9f == 1) and ((svpcf == 5) or(svpsf == 5) or(svphf == 5) or(svpdf == 5))):
								handpoints = 995
							elif ( (cvp5f == 1) and (cvp6f == 1) and (cvp7f == 1) and (cvp8f == 1) and (cvp4f == 1) and ((svpcf == 5) or(svpsf == 5) or(svphf == 5) or(svpdf == 5))):
								handpoints = 994
							elif ( (cvp5f == 1) and (cvp6f == 1) and (cvp7f == 1) and (cvp3f == 1) and (cvp4f == 1) and ((svpcf == 5) or(svpsf == 5) or(svphf == 5) or(svpdf == 5))):
								handpoints = 993
							elif ( (cvp5f == 1) and (cvp6f == 1) and (cvp2f == 1) and (cvp3f == 1) and (cvp4f == 1) and ((svpcf == 5) or(svpsf == 5) or(svphf == 5) or(svpdf == 5))):
								handpoints = 992
							elif ( (cvp5f == 1) and (cvpaf == 1) and (cvp2f == 1) and (cvp3f == 1) and (cvp4f == 1) and ((svpcf == 5) or(svpsf == 5) or(svphf == 5) or(svpdf == 5))):
								handpoints = 991
							elif ( (cvp2f == 4) or (cvp3f == 4) or (cvp4f == 4) or (cvp5f == 4) or (cvp6f == 4) or (cvp7f == 4) or (cvp8f == 4) or (cvp9f == 4) or (cvp10f == 4) or (cvpjf == 4) or (cvpqf == 4) or (cvpkf == 4) or (cvpaf == 4) ):
								handpoints = 976 + pointva4 + pointvk4 + pointvq4 + pointvj4 + pointv104 + pointv94 + pointv84 + pointv74 + pointv64 + pointv54 + pointv44 + pointv34 + pointv24
							elif ( (cvpaf == 3) and ( (cvp2f == 2) or (cvp3f == 2) or (cvp4f == 2) or (cvp5f == 2) or (cvp6f == 2) or (cvp7f == 2) or (cvp8f == 2) or (cvp9f == 2) or (cvp10f == 2) or (cvpjf == 2) or (cvpqf == 2) or (cvpkf == 2) or (cvpaf == 2)) ):
								handpoints = 963 + pointva2 + pointvk2 + pointvq2 + pointvj2 + pointv102 + pointv92 + pointv82 + pointv72 + pointv62 + pointv52 + pointv42 + pointv32 + pointv22
							elif ( (cvpkf == 3) and ( (cvp2f == 2) or (cvp3f == 2) or (cvp4f == 2) or (cvp5f == 2) or (cvp6f == 2) or (cvp7f == 2) or (cvp8f == 2) or (cvp9f == 2) or (cvp10f == 2) or (cvpjf == 2) or (cvpqf == 2) or (cvpkf == 2) or (cvpaf == 2)) ):
								handpoints = 948 + pointva2 + pointvk2 + pointvq2 + pointvj2 + pointv102 + pointv92 + pointv82 + pointv72 + pointv62 + pointv52 + pointv42 + pointv32 + pointv22
							elif ( (cvpqf == 3) and ( (cvp2f == 2) or (cvp3f == 2) or (cvp4f == 2) or (cvp5f == 2) or (cvp6f == 2) or (cvp7f == 2) or (cvp8f == 2) or (cvp9f == 2) or (cvp10f == 2) or (cvpjf == 2) or (cvpqf == 2) or (cvpkf == 2) or (cvpaf == 2)) ):
								handpoints = 933 + pointva2 + pointvk2 + pointvq2 + pointvj2 + pointv102 + pointv92 + pointv82 + pointv72 + pointv62 + pointv52 + pointv42 + pointv32 + pointv22
							elif ( (cvpjf == 3) and ( (cvp2f == 2) or (cvp3f == 2) or (cvp4f == 2) or (cvp5f == 2) or (cvp6f == 2) or (cvp7f == 2) or (cvp8f == 2) or (cvp9f == 2) or (cvp10f == 2) or (cvpjf == 2) or (cvpqf == 2) or (cvpkf == 2) or (cvpaf == 2)) ):
								handpoints = 918 + pointva2 + pointvk2 + pointvq2 + pointvj2 + pointv102 + pointv92 + pointv82 + pointv72 + pointv62 + pointv52 + pointv42 + pointv32 + pointv22
							elif ( (cvp10f == 3) and ( (cvp2f == 2) or (cvp3f == 2) or (cvp4f == 2) or (cvp5f == 2) or (cvp6f == 2) or (cvp7f == 2) or (cvp8f == 2) or (cvp9f == 2) or (cvp10f == 2) or (cvpjf == 2) or (cvpqf == 2) or (cvpkf == 2) or (cvpaf == 2)) ):
								handpoints = 903 + pointva2 + pointvk2 + pointvq2 + pointvj2 + pointv102 + pointv92 + pointv82 + pointv72 + pointv62 + pointv52 + pointv42 + pointv32 + pointv22
							elif ( (cvp9f == 3) and ( (cvp2f == 2) or (cvp3f == 2) or (cvp4f == 2) or (cvp5f == 2) or (cvp6f == 2) or (cvp7f == 2) or (cvp8f == 2) or (cvp9f == 2) or (cvp10f == 2) or (cvpjf == 2) or (cvpqf == 2) or (cvpkf == 2) or (cvpaf == 2)) ):
								handpoints = 888 + pointva2 + pointvk2 + pointvq2 + pointvj2 + pointv102 + pointv92 + pointv82 + pointv72 + pointv62 + pointv52 + pointv42 + pointv32 + pointv22
							elif ( (cvp8f == 3) and ( (cvp2f == 2) or (cvp3f == 2) or (cvp4f == 2) or (cvp5f == 2) or (cvp6f == 2) or (cvp7f == 2) or (cvp8f == 2) or (cvp9f == 2) or (cvp10f == 2) or (cvpjf == 2) or (cvpqf == 2) or (cvpkf == 2) or (cvpaf == 2)) ):
								handpoints = 873 + pointva2 + pointvk2 + pointvq2 + pointvj2 + pointv102 + pointv92 + pointv82 + pointv72 + pointv62 + pointv52 + pointv42 + pointv32 + pointv22
							elif ( (cvp7f == 3) and ( (cvp2f == 2) or (cvp3f == 2) or (cvp4f == 2) or (cvp5f == 2) or (cvp6f == 2) or (cvp7f == 2) or (cvp8f == 2) or (cvp9f == 2) or (cvp10f == 2) or (cvpjf == 2) or (cvpqf == 2) or (cvpkf == 2) or (cvpaf == 2)) ):
								handpoints = 858 + pointva2 + pointvk2 + pointvq2 + pointvj2 + pointv102 + pointv92 + pointv82 + pointv72 + pointv62 + pointv52 + pointv42 + pointv32 + pointv22
							elif ( (cvp6f == 3) and ( (cvp2f == 2) or (cvp3f == 2) or (cvp4f == 2) or (cvp5f == 2) or (cvp6f == 2) or (cvp7f == 2) or (cvp8f == 2) or (cvp9f == 2) or (cvp10f == 2) or (cvpjf == 2) or (cvpqf == 2) or (cvpkf == 2) or (cvpaf == 2)) ):
								handpoints = 843 + pointva2 + pointvk2 + pointvq2 + pointvj2 + pointv102 + pointv92 + pointv82 + pointv72 + pointv62 + pointv52 + pointv42 + pointv32 + pointv22
							elif ( (cvp5f == 3) and ( (cvp2f == 2) or (cvp3f == 2) or (cvp4f == 2) or (cvp5f == 2) or (cvp6f == 2) or (cvp7f == 2) or (cvp8f == 2) or (cvp9f == 2) or (cvp10f == 2) or (cvpjf == 2) or (cvpqf == 2) or (cvpkf == 2) or (cvpaf == 2)) ):
								handpoints = 828 + pointva2 + pointvk2 + pointvq2 + pointvj2 + pointv102 + pointv92 + pointv82 + pointv72 + pointv62 + pointv52 + pointv42 + pointv32 + pointv22
							elif ( (cvp4f == 3) and ( (cvp2f == 2) or (cvp3f == 2) or (cvp4f == 2) or (cvp5f == 2) or (cvp6f == 2) or (cvp7f == 2) or (cvp8f == 2) or (cvp9f == 2) or (cvp10f == 2) or (cvpjf == 2) or (cvpqf == 2) or (cvpkf == 2) or (cvpaf == 2)) ):
								handpoints = 813 + pointva2 + pointvk2 + pointvq2 + pointvj2 + pointv102 + pointv92 + pointv82 + pointv72 + pointv62 + pointv52 + pointv42 + pointv32 + pointv22
							elif ( (cvp3f == 3) and ( (cvp2f == 2) or (cvp3f == 2) or (cvp4f == 2) or (cvp5f == 2) or (cvp6f == 2) or (cvp7f == 2) or (cvp8f == 2) or (cvp9f == 2) or (cvp10f == 2) or (cvpjf == 2) or (cvpqf == 2) or (cvpkf == 2) or (cvpaf == 2)) ):
								handpoints = 798 + pointva2 + pointvk2 + pointvq2 + pointvj2 + pointv102 + pointv92 + pointv82 + pointv72 + pointv62 + pointv52 + pointv42 + pointv32 + pointv22
							elif ( (cvp2f == 3) and ( (cvp2f == 2) or (cvp3f == 2) or (cvp4f == 2) or (cvp5f == 2) or (cvp6f == 2) or (cvp7f == 2) or (cvp8f == 2) or (cvp9f == 2) or (cvp10f == 2) or (cvpjf == 2) or (cvpqf == 2) or (cvpkf == 2) or (cvpaf == 2)) ):
								handpoints = 783 + pointva2 + pointvk2 + pointvq2 + pointvj2 + pointv102 + pointv92 + pointv82 + pointv72 + pointv62 + pointv52 + pointv42 + pointv32 + pointv22
							elif ( (svpcf == 5) or (svpsf ==5) or (svphf ==5) or (svpdf ==5) ):
								handpoints = 782
							elif ( (cvp10f == 1) and (cvpjf == 1) and (cvpqf == 1) and (cvpkf == 1) and (cvpaf == 1)):
								handpoints = 781
							elif ( (cvp10f == 1) and (cvpjf == 1) and (cvpqf == 1) and (cvpkf == 1) and (cvp9f == 1)):
								handpoints = 780
							elif ( (cvp10f == 1) and (cvpjf == 1) and (cvpqf == 1) and (cvp8f == 1) and (cvp9f == 1)):
								handpoints = 779
							elif ( (cvp10f == 1) and (cvpjf == 1) and (cvp7f == 1) and (cvp8f == 1) and (cvp9f == 1)):
								handpoints = 778
							elif ( (cvp10f == 1) and (cvp6f == 1) and (cvp7f == 1) and (cvp8f == 1) and (cvp9f == 1)):
								handpoints = 776
							elif ( (cvp5f == 1) and (cvp6f == 1) and (cvp7f == 1) and (cvp8f == 1) and (cvp9f == 1)):
								handpoints = 775
							elif ( (cvp5f == 1) and (cvp6f == 1) and (cvp7f == 1) and (cvp8f == 1) and (cvp4f == 1)):
								handpoints = 774
							elif ( (cvp5f == 1) and (cvp6f == 1) and (cvp7f == 1) and (cvp3f == 1) and (cvp4f == 1)):
								handpoints = 773
							elif ( (cvp5f == 1) and (cvp6f == 1) and (cvp2f == 1) and (cvp3f == 1) and (cvp4f == 1)):
								handpoints = 772
							elif ( (cvp5f == 1) and (cvpaf == 1) and (cvp2f == 1) and (cvp3f == 1) and (cvp4f == 1)):
								handpoints = 771
							elif ( (cvp2f == 3) or (cvp3f == 3) or (cvp4f == 3) or (cvp5f == 3) or (cvp6f == 3) or (cvp7f == 3) or (cvp8f == 3) or (cvp9f == 3) or (cvp10f == 3) or (cvpjf == 3) or (cvpqf == 3) or (cvpkf == 3) or (cvpaf == 3) ):
								handpoints = 756 + pointva3 + pointvk3 + pointvq3 + pointvj3 + pointv103 + pointv93 + pointv83 + pointv73 + pointv63 + pointv53 + pointv43 + pointv33 + pointv23
							elif ( (cvpaf == 2) and ( (cvp2f == 2) or (cvp3f == 2) or (cvp4f == 2) or (cvp5f == 2) or (cvp6f == 2) or (cvp7f == 2) or (cvp8f == 2) or (cvp9f == 2) or (cvp10f == 2) or (cvpjf == 2) or (cvpqf == 2) or (cvpkf == 2)) ):
								handpoints = 741 + pointvk2 + pointvq2 + pointvj2 + pointv102 + pointv92 + pointv82 + pointv72 + pointv62 + pointv52 + pointv42 + pointv32 + pointv22
							elif ( (cvpkf == 2) and ( (cvp2f == 2) or (cvp3f == 2) or (cvp4f == 2) or (cvp5f == 2) or (cvp6f == 2) or (cvp7f == 2) or (cvp8f == 2) or (cvp9f == 2) or (cvp10f == 2) or (cvpjf == 2) or (cvpqf == 2) or (cvpaf == 2)) ):
								handpoints = 726 + pointva2 + pointvq2 + pointvj2 + pointv102 + pointv92 + pointv82 + pointv72 + pointv62 + pointv52 + pointv42 + pointv32 + pointv22
							elif ( (cvpqf == 2) and ( (cvp2f == 2) or (cvp3f == 2) or (cvp4f == 2) or (cvp5f == 2) or (cvp6f == 2) or (cvp7f == 2) or (cvp8f == 2) or (cvp9f == 2) or (cvp10f == 2) or (cvpjf == 2) or (cvpkf == 2) or (cvpaf == 2)) ):
								handpoints = 711 + pointva2 + pointvk2 + pointvj2 + pointv102 + pointv92 + pointv82 + pointv72 + pointv62 + pointv52 + pointv42 + pointv32 + pointv22
							elif ( (cvpjf == 2) and ( (cvp2f == 2) or (cvp3f == 2) or (cvp4f == 2) or (cvp5f == 2) or (cvp6f == 2) or (cvp7f == 2) or (cvp8f == 2) or (cvp9f == 2) or (cvp10f == 2) or (cvpqf == 2) or (cvpkf == 2) or (cvpaf == 2)) ):
								handpoints = 696 + pointva2 + pointvk2 + pointvq2 + pointv102 + pointv92 + pointv82 + pointv72 + pointv62 + pointv52 + pointv42 + pointv32 + pointv22
							elif ( (cvp10f == 2) and ( (cvp2f == 2) or (cvp3f == 2) or (cvp4f == 2) or (cvp5f == 2) or (cvp6f == 2) or (cvp7f == 2) or (cvp8f == 2) or (cvp9f == 2) or (cvpjf == 2) or (cvpqf == 2) or (cvpkf == 2) or (cvpaf == 2)) ):
								handpoints = 681 + pointva2 + pointvk2 + pointvq2 + pointvj2 + pointv92 + pointv82 + pointv72 + pointv62 + pointv52 + pointv42 + pointv32 + pointv22
							elif ( (cvp9f == 2) and ( (cvp2f == 2) or (cvp3f == 2) or (cvp4f == 2) or (cvp5f == 2) or (cvp6f == 2) or (cvp7f == 2) or (cvp8f == 2) or (cvp10f == 2) or (cvpjf == 2) or (cvpqf == 2) or (cvpkf == 2) or (cvpaf == 2)) ):
								handpoints = 666 + pointva2 + pointvk2 + pointvq2 + pointvj2 + pointv102 + pointv82 + pointv72 + pointv62 + pointv52 + pointv42 + pointv32 + pointv22
							elif ( (cvp8f == 2) and ( (cvp2f == 2) or (cvp3f == 2) or (cvp4f == 2) or (cvp5f == 2) or (cvp6f == 2) or (cvp7f == 2) or (cvp9f == 2) or (cvp10f == 2) or (cvpjf == 2) or (cvpqf == 2) or (cvpkf == 2) or (cvpaf == 2)) ):
								handpoints = 651 + pointva2 + pointvk2 + pointvq2 + pointvj2 + pointv102 + pointv92 + pointv72 + pointv62 + pointv52 + pointv42 + pointv32 + pointv22
							elif ( (cvp7f == 2) and ( (cvp2f == 2) or (cvp3f == 2) or (cvp4f == 2) or (cvp5f == 2) or (cvp6f == 2) or (cvp8f == 2) or (cvp9f == 2) or (cvp10f == 2) or (cvpjf == 2) or (cvpqf == 2) or (cvpkf == 2) or (cvpaf == 2)) ):
								handpoints = 636 + pointva2 + pointvk2 + pointvq2 + pointvj2 + pointv102 + pointv92 + pointv82 + pointv62 + pointv52 + pointv42 + pointv32 + pointv22
							elif ( (cvp6f == 2) and ( (cvp2f == 2) or (cvp3f == 2) or (cvp4f == 2) or (cvp5f == 2) or (cvp7f == 2) or (cvp8f == 2) or (cvp9f == 2) or (cvp10f == 2) or (cvpjf == 2) or (cvpqf == 2) or (cvpkf == 2) or (cvpaf == 2)) ):
								handpoints = 621 + pointva2 + pointvk2 + pointvq2 + pointvj2 + pointv102 + pointv92 + pointv82 + pointv72 + pointv52 + pointv42 + pointv32 + pointv22
							elif ( (cvp5f == 2) and ( (cvp2f == 2) or (cvp3f == 2) or (cvp4f == 2) or (cvp6f == 2) or (cvp7f == 2) or (cvp8f == 2) or (cvp9f == 2) or (cvp10f == 2) or (cvpjf == 2) or (cvpqf == 2) or (cvpkf == 2) or (cvpaf == 2)) ):
								handpoints = 606 + pointva2 + pointvk2 + pointvq2 + pointvj2 + pointv102 + pointv92 + pointv82 + pointv72 + pointv62 + pointv42 + pointv32 + pointv22
							elif ( (cvp4f == 2) and ( (cvp2f == 2) or (cvp3f == 2) or (cvp5f == 2) or (cvp6f == 2) or (cvp7f == 2) or (cvp8f == 2) or (cvp9f == 2) or (cvp10f == 2) or (cvpjf == 2) or (cvpqf == 2) or (cvpkf == 2) or (cvpaf == 2)) ):
								handpoints = 591 + pointva2 + pointvk2 + pointvq2 + pointvj2 + pointv102 + pointv92 + pointv82 + pointv72 + pointv62 + pointv52 + pointv32 + pointv22
							elif ( (cvp3f == 2) and ( (cvp2f == 2) or (cvp4f == 2) or (cvp5f == 2) or (cvp6f == 2) or (cvp7f == 2) or (cvp8f == 2) or (cvp9f == 2) or (cvp10f == 2) or (cvpjf == 2) or (cvpqf == 2) or (cvpkf == 2) or (cvpaf == 2)) ):
								handpoints = 576 + pointva2 + pointvk2 + pointvq2 + pointvj2 + pointv102 + pointv92 + pointv82 + pointv72 + pointv62 + pointv52 + pointv42 + pointv22
							elif ( (cvp2f == 2) and ((cvp3f == 2) or (cvp4f == 2) or (cvp5f == 2) or (cvp6f == 2) or (cvp7f == 2) or (cvp8f == 2) or (cvp9f == 2) or (cvp10f == 2) or (cvpjf == 2) or (cvpqf == 2) or (cvpkf == 2) or (cvpaf == 2)) ):
								handpoints = 561 + pointva2 + pointvk2 + pointvq2 + pointvj2 + pointv102 + pointv92 + pointv82 + pointv72 + pointv62 + pointv52 + pointv42 + pointv32
							elif ( (cvp2f == 2) or (cvp3f == 2) or (cvp4f == 2) or (cvp5f == 2) or (cvp6f == 2) or (cvp7f == 2) or (cvp8f == 2) or (cvp9f == 2) or (cvp10f == 2) or (cvpjf == 2) or (cvpqf == 2) or (cvpkf == 2) or (cvpaf == 2) ):
								handpoints = 546 + pointva2 + pointvk2 + pointvq2 + pointvj2 + pointv102 + pointv92 + pointv82 + pointv72 + pointv62 + pointv52 + pointv42 + pointv32 + pointv22
							else:
								handpoints = 500
							availableir = int(available)
							availablei = availableir - 1
							availblenew = '^$&*available = ' + str(availablei) + ' *)!#'
							pgpnew = pgp.replace(('^$&*available = ' + available + ' *)!#'), str(availblenew))
							wrtdata2 = open("pgp.txt", "w")
							secnames = '#$!*&^!@' + available + user.name + '&&*)^$#@!'
							secnamef = ')(&$&$#@' + available + user.name + '!@&@$@^&'
							highnames = '!!@*^$&' + available + user.name + '**^&$$#!('
							highnamef = '&(#*$%!)^' + available + user.name + '(*&$@@#!'
							wrtdata2.write(pgpnew + '\n' + secnames + ("handpointp%d = %d" %(availableir, handpoints)) + secnamef + '\n' + highnames + ("highcardp%d = %d" %(availableir, highcard)) + highnamef + '\n' )
							wrtdata2.close()
							pgpr.close()
							pgpfr = open("pgp.txt","r")
							pgpf = (pgpfr.read()).lower()
							room.message(str("The cards you drew are: " + card1 + ", " + card2 + ", " + card3 + ", " + card4 + ", " + card5 + "."))
							#room.message(str("Your points for this hand are: " + str(handpoints) + ". Your high card is " + str(highcard) + "."))
							if availablei == 0:
								indexsp1 = pgpf.find('&&*)^$#@!handpointp1 = ')
								indexep1 = pgpf.find(')(&$&$#@1')
								rawoutp1 = pgpf[(int(indexsp1)):(int(indexep1))]
								rawout2p1 = rawoutp1.replace(('&&*)^$#@!handpointp1 = '), "")
								pointsrp1 = rawout2p1.replace((')(&$&$#@1'), "")
								pointsp1 = int(pointsrp1)
								indexsp2 = pgpf.find('&&*)^$#@!handpointp2 = ')
								indexep2 = pgpf.find(')(&$&$#@2')
								rawoutp2 = pgpf[(int(indexsp2)):(int(indexep2))]
								rawout2p2 = rawoutp2.replace(('&&*)^$#@!handpointp2 = '), "")
								pointsrp2 = rawout2p2.replace((')(&$&$#@2'), "")
								pointsp2 = int(pointsrp2)
								indexshp1 = pgpf.find('**^&$$#!(highcardp1 = ')
								indexehp1 = pgpf.find('&(#*$%!)^1')
								rawouthp1 = pgpf[(int(indexshp1)):(int(indexehp1))]
								rawout2hp1 = rawouthp1.replace(('**^&$$#!(highcardp1 = '), "")
								pointsrhp1 = rawout2hp1.replace(('&(#*$%!)^1'), "")
								pointshp1 = int(pointsrhp1)
								indexshp2 = pgpf.find('**^&$$#!(highcardp2 = ')
								indexehp2 = pgpf.find('&(#*$%!)^2')
								rawouthp2 = pgpf[(int(indexshp2)):(int(indexehp2))]
								rawout2hp2 = rawouthp2.replace(('**^&$$#!(highcardp2 = '), "")
								pointsrhp2 = rawout2hp2.replace(('&(#*$%!)^2'), "")
								pointshp2 = int(pointsrhp2)
								if (pointsp1 > pointsp2):
									indexsw = pgpf.find('#$!*&^!@1')
									indexew = pgpf.find(')(&$&$#@1')
									rawoutw = pgpf[(int(indexsw)):(int(indexew))]
									rawout2w = rawoutw.replace(('#$!*&^!@1'), "")
									victorrw = rawout2w.replace(('&&*)^$#@!handpointp1 = ' + pointsrp1), "")
									victorw = victorrw.replace((')(&$&$#@1'), "")
									room.message(victorw.capitalize() + " wins the match!")
									pgpfr.close()
									wrtset1 = open("pgp.txt", "w")
									wrtset1.write("*$#^!players = 2 &^$*\n^$&*available = 2 *)!#\n##$*!@turn = 1@*&(*\n*#&$^#cards = #&!2 of hearts, #&!3 of hearts, #&!4 of hearts, #&!5 of hearts, #&!6 of hearts, #&!7 of hearts, #&!8 of hearts, #&!9 of hearts, #&!10 of hearts, #&!Jack of hearts, #&!IceQueen of hearts, #&!King of hearts, #&!Ace of hearts, #&!2 of diamonds, #&!3 of diamonds, #&!4 of diamonds, #&!5 of diamonds, #&!6 of diamonds, #&!7 of diamonds, #&!8 of diamonds, #&!9 of diamonds, #&!10 of diamonds, #&!Jack of diamonds, #&!IceQueen of diamonds, #&!King of diamonds, #&!Ace of diamonds, #&!2 of clubs, #&!3 of clubs, #&!4 of clubs, #&!5 of clubs, #&!6 of clubs, #&!7 of clubs, #&!8 of clubs, #&!9 of clubs, #&!10 of clubs, #&!Jack of clubs, #&!IceQueen of clubs, #&!King of clubs, #&!Ace of clubs, #&!2 of spades, #&!3 of spades, #&!4 of spades, #&!5 of spades, #&!6 of spades, #&!7 of spades, #&!8 of spades, #&!9 of spades, #&!10 of spades, #&!Jack of spades, #&!IceQueen of spades, #&!King of spades, #&!Ace of spades#&#@$($#\n")
									wrtset1.close()
								elif (pointsp2 > pointsp1):
									indexsw = pgpf.find('#$!*&^!@2')
									indexew = pgpf.find(')(&$&$#@2')
									rawoutw = pgpf[(int(indexsw)):(int(indexew))]
									rawout2w = rawoutw.replace(('#$!*&^!@2'), "")
									victorrw = rawout2w.replace(('&&*)^$#@!handpointp2 = ' + pointsrp2), "")
									victorw = victorrw.replace((')(&$&$#@2'), "")
									room.message(victorw.capitalize() + " wins the match!")
									pgpfr.close()
									wrtset1 = open("pgp.txt", "w")
									wrtset1.write("*$#^!players = 2 &^$*\n^$&*available = 2 *)!#\n##$*!@turn = 1@*&(*\n*#&$^#cards = #&!2 of hearts, #&!3 of hearts, #&!4 of hearts, #&!5 of hearts, #&!6 of hearts, #&!7 of hearts, #&!8 of hearts, #&!9 of hearts, #&!10 of hearts, #&!Jack of hearts, #&!IceQueen of hearts, #&!King of hearts, #&!Ace of hearts, #&!2 of diamonds, #&!3 of diamonds, #&!4 of diamonds, #&!5 of diamonds, #&!6 of diamonds, #&!7 of diamonds, #&!8 of diamonds, #&!9 of diamonds, #&!10 of diamonds, #&!Jack of diamonds, #&!IceQueen of diamonds, #&!King of diamonds, #&!Ace of diamonds, #&!2 of clubs, #&!3 of clubs, #&!4 of clubs, #&!5 of clubs, #&!6 of clubs, #&!7 of clubs, #&!8 of clubs, #&!9 of clubs, #&!10 of clubs, #&!Jack of clubs, #&!IceQueen of clubs, #&!King of clubs, #&!Ace of clubs, #&!2 of spades, #&!3 of spades, #&!4 of spades, #&!5 of spades, #&!6 of spades, #&!7 of spades, #&!8 of spades, #&!9 of spades, #&!10 of spades, #&!Jack of spades, #&!IceQueen of spades, #&!King of spades, #&!Ace of spades#&#@$($#\n")
									wrtset1.close()
								elif (pointsp2 == pointsp1):
									if (pointshp1 > pointshp2):
										indexsw = pgpf.find('#$!*&^!@1')
										indexew = pgpf.find(')(&$&$#@1')
										rawoutw = pgpf[(int(indexsw)):(int(indexew))]
										rawout2w = rawoutw.replace(('#$!*&^!@1'), "")
										victorrw = rawout2w.replace(('&&*)^$#@!handpointp1 = ' + pointsrp1), "")
										victorw = victorrw.replace((')(&$&$#@1'), "")
										room.message(victorw.capitalize() + " wins the match!")
										pgpfr.close()
										wrtset1 = open("pgp.txt", "w")
										wrtset1.write("*$#^!players = 2 &^$*\n^$&*available = 2 *)!#\n##$*!@turn = 1@*&(*\n*#&$^#cards = #&!2 of hearts, #&!3 of hearts, #&!4 of hearts, #&!5 of hearts, #&!6 of hearts, #&!7 of hearts, #&!8 of hearts, #&!9 of hearts, #&!10 of hearts, #&!Jack of hearts, #&!IceQueen of hearts, #&!King of hearts, #&!Ace of hearts, #&!2 of diamonds, #&!3 of diamonds, #&!4 of diamonds, #&!5 of diamonds, #&!6 of diamonds, #&!7 of diamonds, #&!8 of diamonds, #&!9 of diamonds, #&!10 of diamonds, #&!Jack of diamonds, #&!IceQueen of diamonds, #&!King of diamonds, #&!Ace of diamonds, #&!2 of clubs, #&!3 of clubs, #&!4 of clubs, #&!5 of clubs, #&!6 of clubs, #&!7 of clubs, #&!8 of clubs, #&!9 of clubs, #&!10 of clubs, #&!Jack of clubs, #&!IceQueen of clubs, #&!King of clubs, #&!Ace of clubs, #&!2 of spades, #&!3 of spades, #&!4 of spades, #&!5 of spades, #&!6 of spades, #&!7 of spades, #&!8 of spades, #&!9 of spades, #&!10 of spades, #&!Jack of spades, #&!IceQueen of spades, #&!King of spades, #&!Ace of spades#&#@$($#\n")
										wrtset1.close()
									elif (pointshp2 > pointshp1):
										indexsw = pgpf.find('#$!*&^!@2')
										indexew = pgpf.find(')(&$&$#@2')
										rawoutw = pgpf[(int(indexsw)):(int(indexew))]
										rawout2w = rawoutw.replace(('#$!*&^!@2'), "")
										victorrw = rawout2w.replace(('&&*)^$#@!handpointp2 = ' + pointsrp2), "")
										victorw = victorrw.replace((')(&$&$#@2'), "")
										room.message(victorw.capitalize() + " wins the match!")
										pgpfr.close()
										wrtset1 = open("pgp.txt", "w")
										wrtset1.write("*$#^!players = 2 &^$*\n^$&*available = 2 *)!#\n##$*!@turn = 1@*&(*\n*#&$^#cards = #&!2 of hearts, #&!3 of hearts, #&!4 of hearts, #&!5 of hearts, #&!6 of hearts, #&!7 of hearts, #&!8 of hearts, #&!9 of hearts, #&!10 of hearts, #&!Jack of hearts, #&!IceQueen of hearts, #&!King of hearts, #&!Ace of hearts, #&!2 of diamonds, #&!3 of diamonds, #&!4 of diamonds, #&!5 of diamonds, #&!6 of diamonds, #&!7 of diamonds, #&!8 of diamonds, #&!9 of diamonds, #&!10 of diamonds, #&!Jack of diamonds, #&!IceQueen of diamonds, #&!King of diamonds, #&!Ace of diamonds, #&!2 of clubs, #&!3 of clubs, #&!4 of clubs, #&!5 of clubs, #&!6 of clubs, #&!7 of clubs, #&!8 of clubs, #&!9 of clubs, #&!10 of clubs, #&!Jack of clubs, #&!IceQueen of clubs, #&!King of clubs, #&!Ace of clubs, #&!2 of spades, #&!3 of spades, #&!4 of spades, #&!5 of spades, #&!6 of spades, #&!7 of spades, #&!8 of spades, #&!9 of spades, #&!10 of spades, #&!Jack of spades, #&!IceQueen of spades, #&!King of spades, #&!Ace of spades#&#@$($#\n")
										wrtset1.close()
									elif (pointshp2 == pointshp1):
										room.message("It is a draw!")
										pgpfr.close()
										wrtset1 = open("pgp.txt", "w")
										wrtset1.write("*$#^!players = 2 &^$*\n^$&*available = 2 *)!#\n##$*!@turn = 1@*&(*\n*#&$^#cards = #&!2 of hearts, #&!3 of hearts, #&!4 of hearts, #&!5 of hearts, #&!6 of hearts, #&!7 of hearts, #&!8 of hearts, #&!9 of hearts, #&!10 of hearts, #&!Jack of hearts, #&!IceQueen of hearts, #&!King of hearts, #&!Ace of hearts, #&!2 of diamonds, #&!3 of diamonds, #&!4 of diamonds, #&!5 of diamonds, #&!6 of diamonds, #&!7 of diamonds, #&!8 of diamonds, #&!9 of diamonds, #&!10 of diamonds, #&!Jack of diamonds, #&!IceQueen of diamonds, #&!King of diamonds, #&!Ace of diamonds, #&!2 of clubs, #&!3 of clubs, #&!4 of clubs, #&!5 of clubs, #&!6 of clubs, #&!7 of clubs, #&!8 of clubs, #&!9 of clubs, #&!10 of clubs, #&!Jack of clubs, #&!IceQueen of clubs, #&!King of clubs, #&!Ace of clubs, #&!2 of spades, #&!3 of spades, #&!4 of spades, #&!5 of spades, #&!6 of spades, #&!7 of spades, #&!8 of spades, #&!9 of spades, #&!10 of spades, #&!Jack of spades, #&!IceQueen of spades, #&!King of spades, #&!Ace of spades#&#@$($#\n")
										wrtset1.close()
			elif (cmd.lower()) == "pokerstart":
				if usrlvl >= 0:
					if args == "2":
						players = 2
						def id_gen(size=5, chars=string.ascii_uppercase + string.digits):
							return ''.join(random.choice(chars) for x in range(size))
						gidn = id_gen()
						gid = gidn + '2'
						wrtset1 = open((gid + ".txt"), "w")
						wrtset1.write("*$#^!players = %d &^$*\n^$&*available = %d *)!#\n*#&^tradestatus = %d )#(#*&\n##$*!@turn = 1@*&(*\n\n*#&$^#cards = #&!2 of hearts, #&!3 of hearts, #&!4 of hearts, #&!5 of hearts, #&!6 of hearts, #&!7 of hearts, #&!8 of hearts, #&!9 of hearts, #&!10 of hearts, #&!Jack of hearts, #&!IceQueen of hearts, #&!King of hearts, #&!Ace of hearts, #&!2 of diamonds, #&!3 of diamonds, #&!4 of diamonds, #&!5 of diamonds, #&!6 of diamonds, #&!7 of diamonds, #&!8 of diamonds, #&!9 of diamonds, #&!10 of diamonds, #&!Jack of diamonds, #&!IceQueen of diamonds, #&!King of diamonds, #&!Ace of diamonds, #&!2 of clubs, #&!3 of clubs, #&!4 of clubs, #&!5 of clubs, #&!6 of clubs, #&!7 of clubs, #&!8 of clubs, #&!9 of clubs, #&!10 of clubs, #&!Jack of clubs, #&!IceQueen of clubs, #&!King of clubs, #&!Ace of clubs, #&!2 of spades, #&!3 of spades, #&!4 of spades, #&!5 of spades, #&!6 of spades, #&!7 of spades, #&!8 of spades, #&!9 of spades, #&!10 of spades, #&!Jack of spades, #&!IceQueen of spades, #&!King of spades, #&!Ace of spades#&#@$($#\n" %(players, players, players))
						wrtset1.close()
						wrtlist2 = open(("glist.txt"), "a")
						wrtlist2.write('*$^&@($#@!*$#' + gid + '$*#$$*&&@^#\n')
						wrtlist2.close()
						room.message("Your game has been created. The game id is: " + gid + ". The number of players selected is " + str(players) + ". To draw a hand type ;pokerdraw " + gid)
					elif args == "3":
						players = 3
						def id_gen(size=5, chars=string.ascii_uppercase + string.digits):
							return ''.join(random.choice(chars) for x in range(size))
						gidn = id_gen()
						gid = gidn + '3'
						wrtset1 = open((gid + ".txt"), "w")
						wrtset1.write("*$#^!players = %d &^$*\n^$&*available = %d *)!#\n*#&^tradestatus = %d )#(#*&\n##$*!@turn = 1@*&(*\n\n*#&$^#cards = #&!2 of hearts, #&!3 of hearts, #&!4 of hearts, #&!5 of hearts, #&!6 of hearts, #&!7 of hearts, #&!8 of hearts, #&!9 of hearts, #&!10 of hearts, #&!Jack of hearts, #&!IceQueen of hearts, #&!King of hearts, #&!Ace of hearts, #&!2 of diamonds, #&!3 of diamonds, #&!4 of diamonds, #&!5 of diamonds, #&!6 of diamonds, #&!7 of diamonds, #&!8 of diamonds, #&!9 of diamonds, #&!10 of diamonds, #&!Jack of diamonds, #&!IceQueen of diamonds, #&!King of diamonds, #&!Ace of diamonds, #&!2 of clubs, #&!3 of clubs, #&!4 of clubs, #&!5 of clubs, #&!6 of clubs, #&!7 of clubs, #&!8 of clubs, #&!9 of clubs, #&!10 of clubs, #&!Jack of clubs, #&!IceQueen of clubs, #&!King of clubs, #&!Ace of clubs, #&!2 of spades, #&!3 of spades, #&!4 of spades, #&!5 of spades, #&!6 of spades, #&!7 of spades, #&!8 of spades, #&!9 of spades, #&!10 of spades, #&!Jack of spades, #&!IceQueen of spades, #&!King of spades, #&!Ace of spades#&#@$($#\n" %(players, players, players))
						wrtset1.close()
						wrtlist2 = open(("glist.txt"), "a")
						wrtlist2.write('*$^&@($#@!*$#' + gid + '$*#$$*&&@^#\n')
						wrtlist2.close()
						room.message("Your game has been created. The game id is: " + gid + ". The number of players selected is " + str(players) + ". To draw a hand type ;pokerdraw " + gid)
					elif args == "4":
						players = 4
						def id_gen(size=5, chars=string.ascii_uppercase + string.digits):
							return ''.join(random.choice(chars) for x in range(size))
						gidn = id_gen()
						gid = gidn + '4'
						wrtset1 = open((gid + ".txt"), "w")
						wrtset1.write("*$#^!players = %d &^$*\n^$&*available = %d *)!#\n*#&^tradestatus = %d )#(#*&\n##$*!@turn = 1@*&(*\n\n*#&$^#cards = #&!2 of hearts, #&!3 of hearts, #&!4 of hearts, #&!5 of hearts, #&!6 of hearts, #&!7 of hearts, #&!8 of hearts, #&!9 of hearts, #&!10 of hearts, #&!Jack of hearts, #&!IceQueen of hearts, #&!King of hearts, #&!Ace of hearts, #&!2 of diamonds, #&!3 of diamonds, #&!4 of diamonds, #&!5 of diamonds, #&!6 of diamonds, #&!7 of diamonds, #&!8 of diamonds, #&!9 of diamonds, #&!10 of diamonds, #&!Jack of diamonds, #&!IceQueen of diamonds, #&!King of diamonds, #&!Ace of diamonds, #&!2 of clubs, #&!3 of clubs, #&!4 of clubs, #&!5 of clubs, #&!6 of clubs, #&!7 of clubs, #&!8 of clubs, #&!9 of clubs, #&!10 of clubs, #&!Jack of clubs, #&!IceQueen of clubs, #&!King of clubs, #&!Ace of clubs, #&!2 of spades, #&!3 of spades, #&!4 of spades, #&!5 of spades, #&!6 of spades, #&!7 of spades, #&!8 of spades, #&!9 of spades, #&!10 of spades, #&!Jack of spades, #&!IceQueen of spades, #&!King of spades, #&!Ace of spades#&#@$($#\n" %(players, players, players))
						wrtset1.close()
						wrtlist2 = open(("glist.txt"), "a")
						wrtlist2.write('*$^&@($#@!*$#' + gid + '$*#$$*&&@^#\n')
						wrtlist2.close()
						room.message("Your game has been created. The game id is: " + gid + ". The number of players selected is " + str(players) + ". To draw a hand type ;pokerdraw " + gid)
					elif args == "5":
						players = 5
						def id_gen(size=5, chars=string.ascii_uppercase + string.digits):
							return ''.join(random.choice(chars) for x in range(size))
						gidn = id_gen()
						gid = gidn + '5'
						wrtset1 = open((gid + ".txt"), "w")
						wrtset1.write("*$#^!players = %d &^$*\n^$&*available = %d *)!#\n*#&^tradestatus = %d )#(#*&\n##$*!@turn = 1@*&(*\n\n*#&$^#cards = #&!2 of hearts, #&!3 of hearts, #&!4 of hearts, #&!5 of hearts, #&!6 of hearts, #&!7 of hearts, #&!8 of hearts, #&!9 of hearts, #&!10 of hearts, #&!Jack of hearts, #&!IceQueen of hearts, #&!King of hearts, #&!Ace of hearts, #&!2 of diamonds, #&!3 of diamonds, #&!4 of diamonds, #&!5 of diamonds, #&!6 of diamonds, #&!7 of diamonds, #&!8 of diamonds, #&!9 of diamonds, #&!10 of diamonds, #&!Jack of diamonds, #&!IceQueen of diamonds, #&!King of diamonds, #&!Ace of diamonds, #&!2 of clubs, #&!3 of clubs, #&!4 of clubs, #&!5 of clubs, #&!6 of clubs, #&!7 of clubs, #&!8 of clubs, #&!9 of clubs, #&!10 of clubs, #&!Jack of clubs, #&!IceQueen of clubs, #&!King of clubs, #&!Ace of clubs, #&!2 of spades, #&!3 of spades, #&!4 of spades, #&!5 of spades, #&!6 of spades, #&!7 of spades, #&!8 of spades, #&!9 of spades, #&!10 of spades, #&!Jack of spades, #&!IceQueen of spades, #&!King of spades, #&!Ace of spades#&#@$($#\n" %(players, players, players))
						wrtset1.close()
						wrtlist2 = open(("glist.txt"), "a")
						wrtlist2.write('*$^&@($#@!*$#' + gid + '$*#$$*&&@^#\n')
						wrtlist2.close()
						room.message("Your game has been created. The game id is: " + gid + ". The number of players selected is " + str(players) + ". To draw a hand type ;pokerdraw " + gid)
					elif args == "6":
						players = 6
						def id_gen(size=5, chars=string.ascii_uppercase + string.digits):
							return ''.join(random.choice(chars) for x in range(size))
						gidn = id_gen()
						gid = gidn + '6'
						wrtset1 = open((gid + ".txt"), "w")
						wrtset1.write("*$#^!players = %d &^$*\n^$&*available = %d *)!#\n*#&^tradestatus = %d )#(#*&\n##$*!@turn = 1@*&(*\n\n*#&$^#cards = #&!2 of hearts, #&!3 of hearts, #&!4 of hearts, #&!5 of hearts, #&!6 of hearts, #&!7 of hearts, #&!8 of hearts, #&!9 of hearts, #&!10 of hearts, #&!Jack of hearts, #&!IceQueen of hearts, #&!King of hearts, #&!Ace of hearts, #&!2 of diamonds, #&!3 of diamonds, #&!4 of diamonds, #&!5 of diamonds, #&!6 of diamonds, #&!7 of diamonds, #&!8 of diamonds, #&!9 of diamonds, #&!10 of diamonds, #&!Jack of diamonds, #&!IceQueen of diamonds, #&!King of diamonds, #&!Ace of diamonds, #&!2 of clubs, #&!3 of clubs, #&!4 of clubs, #&!5 of clubs, #&!6 of clubs, #&!7 of clubs, #&!8 of clubs, #&!9 of clubs, #&!10 of clubs, #&!Jack of clubs, #&!IceQueen of clubs, #&!King of clubs, #&!Ace of clubs, #&!2 of spades, #&!3 of spades, #&!4 of spades, #&!5 of spades, #&!6 of spades, #&!7 of spades, #&!8 of spades, #&!9 of spades, #&!10 of spades, #&!Jack of spades, #&!IceQueen of spades, #&!King of spades, #&!Ace of spades#&#@$($#\n" %(players, players, players))
						wrtset1.close()
						wrtlist2 = open(("glist.txt"), "a")
						wrtlist2.write('*$^&@($#@!*$#' + gid + '$*#$$*&&@^#\n')
						wrtlist2.close()
						room.message("Your game has been created. The game id is: " + gid + ". The number of players selected is " + str(players) + ". To draw a hand type ;pokerdraw " + gid)
					elif args == "7":
						players = 7
						def id_gen(size=5, chars=string.ascii_uppercase + string.digits):
							return ''.join(random.choice(chars) for x in range(size))
						gidn = id_gen()
						gid = gidn + '7'
						wrtset1 = open((gid + ".txt"), "w")
						wrtset1.write("*$#^!players = %d &^$*\n^$&*available = %d *)!#\n*#&^tradestatus = %d )#(#*&\n##$*!@turn = 1@*&(*\n\n*#&$^#cards = #&!2 of hearts, #&!3 of hearts, #&!4 of hearts, #&!5 of hearts, #&!6 of hearts, #&!7 of hearts, #&!8 of hearts, #&!9 of hearts, #&!10 of hearts, #&!Jack of hearts, #&!IceQueen of hearts, #&!King of hearts, #&!Ace of hearts, #&!2 of diamonds, #&!3 of diamonds, #&!4 of diamonds, #&!5 of diamonds, #&!6 of diamonds, #&!7 of diamonds, #&!8 of diamonds, #&!9 of diamonds, #&!10 of diamonds, #&!Jack of diamonds, #&!IceQueen of diamonds, #&!King of diamonds, #&!Ace of diamonds, #&!2 of clubs, #&!3 of clubs, #&!4 of clubs, #&!5 of clubs, #&!6 of clubs, #&!7 of clubs, #&!8 of clubs, #&!9 of clubs, #&!10 of clubs, #&!Jack of clubs, #&!IceQueen of clubs, #&!King of clubs, #&!Ace of clubs, #&!2 of spades, #&!3 of spades, #&!4 of spades, #&!5 of spades, #&!6 of spades, #&!7 of spades, #&!8 of spades, #&!9 of spades, #&!10 of spades, #&!Jack of spades, #&!IceQueen of spades, #&!King of spades, #&!Ace of spades#&#@$($#\n" %(players, players, players))
						wrtset1.close()
						wrtlist2 = open(("glist.txt"), "a")
						wrtlist2.write('*$^&@($#@!*$#' + gid + '$*#$$*&&@^#\n')
						wrtlist2.close()
						room.message("Your game has been created. The game id is: " + gid + ". The number of players selected is " + str(players) + ". To draw a hand type ;pokerdraw " + gid)
					elif args == "8":
						players = 8
						def id_gen(size=5, chars=string.ascii_uppercase + string.digits):
							return ''.join(random.choice(chars) for x in range(size))
						gidn = id_gen()
						gid = gidn + '8'
						wrtset1 = open((gid + ".txt"), "w")
						wrtset1.write("*$#^!players = %d &^$*\n^$&*available = %d *)!#\n*#&^tradestatus = %d )#(#*&\n##$*!@turn = 1@*&(*\n\n*#&$^#cards = #&!2 of hearts, #&!3 of hearts, #&!4 of hearts, #&!5 of hearts, #&!6 of hearts, #&!7 of hearts, #&!8 of hearts, #&!9 of hearts, #&!10 of hearts, #&!Jack of hearts, #&!IceQueen of hearts, #&!King of hearts, #&!Ace of hearts, #&!2 of diamonds, #&!3 of diamonds, #&!4 of diamonds, #&!5 of diamonds, #&!6 of diamonds, #&!7 of diamonds, #&!8 of diamonds, #&!9 of diamonds, #&!10 of diamonds, #&!Jack of diamonds, #&!IceQueen of diamonds, #&!King of diamonds, #&!Ace of diamonds, #&!2 of clubs, #&!3 of clubs, #&!4 of clubs, #&!5 of clubs, #&!6 of clubs, #&!7 of clubs, #&!8 of clubs, #&!9 of clubs, #&!10 of clubs, #&!Jack of clubs, #&!IceQueen of clubs, #&!King of clubs, #&!Ace of clubs, #&!2 of spades, #&!3 of spades, #&!4 of spades, #&!5 of spades, #&!6 of spades, #&!7 of spades, #&!8 of spades, #&!9 of spades, #&!10 of spades, #&!Jack of spades, #&!IceQueen of spades, #&!King of spades, #&!Ace of spades#&#@$($#\n" %(players, players, players))
						wrtset1.close()
						wrtlist2 = open(("glist.txt"), "a")
						wrtlist2.write('*$^&@($#@!*$#' + gid + '$*#$$*&&@^#\n')
						wrtlist2.close()
						room.message("Your game has been created. The game id is: " + gid + ". The number of players selected is " + str(players) + ". To draw a hand type ;pokerdraw " + gid)
					else:
						players = 3
						def id_gen(size=5, chars=string.ascii_uppercase + string.digits):
							return ''.join(random.choice(chars) for x in range(size))
						gidn = id_gen()
						gid = gidn + '3'
						wrtset1 = open((gid + ".txt"), "w")
						wrtset1.write("*$#^!players = %d &^$*\n^$&*available = %d *)!#\n*#&^tradestatus = %d )#(#*&\n##$*!@turn = 1@*&(*\n\n*#&$^#cards = #&!2 of hearts, #&!3 of hearts, #&!4 of hearts, #&!5 of hearts, #&!6 of hearts, #&!7 of hearts, #&!8 of hearts, #&!9 of hearts, #&!10 of hearts, #&!Jack of hearts, #&!IceQueen of hearts, #&!King of hearts, #&!Ace of hearts, #&!2 of diamonds, #&!3 of diamonds, #&!4 of diamonds, #&!5 of diamonds, #&!6 of diamonds, #&!7 of diamonds, #&!8 of diamonds, #&!9 of diamonds, #&!10 of diamonds, #&!Jack of diamonds, #&!IceQueen of diamonds, #&!King of diamonds, #&!Ace of diamonds, #&!2 of clubs, #&!3 of clubs, #&!4 of clubs, #&!5 of clubs, #&!6 of clubs, #&!7 of clubs, #&!8 of clubs, #&!9 of clubs, #&!10 of clubs, #&!Jack of clubs, #&!IceQueen of clubs, #&!King of clubs, #&!Ace of clubs, #&!2 of spades, #&!3 of spades, #&!4 of spades, #&!5 of spades, #&!6 of spades, #&!7 of spades, #&!8 of spades, #&!9 of spades, #&!10 of spades, #&!Jack of spades, #&!IceQueen of spades, #&!King of spades, #&!Ace of spades#&#@$($#\n" %(players, players, players))
						wrtset1.close()
						wrtlist2 = open(("glist.txt"), "a")
						wrtlist2.write('*$^&@($#@!*$#' + gid + '$*#$$*&&@^#\n')
						wrtlist2.close()
						room.message("Your game has been created. The game id is: " + gid + ". The number of players selected is " + str(players) + ". To draw a hand type ;pokerdraw " + gid)
			elif (cmd.lower()) == "pokerdraw":
				if usrlvl >= 0:
					glistr = open("glist.txt","r")
					glist = (glistr.read()).upper()
					if ('*$^&@($#@!*$#' + args.upper() + '$*#$$*&&@^#') in glist:
						gid = args
						rgsetr = open(gid + ".txt","r")
						rgset = (rgsetr.read()).lower()
						cindexs = rgset.find('*#&$^#cards = ')
						cindexe = rgset.find('#&#@$($#')
						crawout = rgset[(int(cindexs)):(int(cindexe))]
						crawout2 = crawout.replace(('*#&$^#cards = '), "")
						cardsstr = crawout2.replace(('#&#@$($#'), "")
						cardsprep = re.split(', ', cardsstr)
						cards = [item.lower() for item in cardsprep]
						def cdt(cards):
							return random.choice(cards)
						indexs = rgset.find('^$&*available = ')
						indexe = rgset.find(' *)!#')
						rawout = rgset[(int(indexs)):(int(indexe))]
						rawout2 = rawout.replace(('^$&*available = '), "")
						available = rawout2.replace((' *)!#'), "")
						if ('##$*!@turn = 1@*&(*' not in rgset):
							indexst = rgset.find('##$*!@turn = ')
							indexet = rgset.find('@*&(*')
							rawoutt = rgset[(int(indexst)):(int(indexet))]
							rawout2t = rawoutt.replace(('##$*!@turn = '), "")
							turn = rawout2t.replace(('@*&(*'), "")
							if turn == '2':
								room.message('This game is in the trade phase, to trade your unwanted cards for new cards type ;pokertrade ' + gid.upper() + ': [CARD NAME], [CARD NAME], [CARD NAME], etc...')
							elif turn == '3':
								room.message('No Turn 3 yet.')
							elif turn == '4':
								room.message('No turn 4 yet.')
						elif user.name in rgset:
							room.message("You have already drawn for this game.")
						elif available == '0':
							room.message("This game is full, no new people can join.")
						else:
							card1r = cdt(cards)
							card1 = card1r.replace("#&!", "")
							cs2r1 = str(cards).replace("[", "")
							cs2r2 = cs2r1.replace("]", "")
							cs2r3 = cs2r2.replace(" '#&!", "#&!")
							cs2r4 = cs2r3.replace("'", "")
							cardset2rr = cs2r4.replace(str(card1) + ',', "")
							cardset2r = cardset2rr.replace("#&!#&!", "#&!")
							cardset2 = ([n for n in cardset2r.split(",")])
							card2r = cdt(cardset2)
							card2 = card2r.replace("#&!", "")
							cs3r1 = str(cardset2).replace("[", "")
							cs3r2 = cs3r1.replace("]", "")
							cs3r3 = cs3r2.replace(" '#&!", "#&!")
							cs3r4 = cs3r3.replace("'", "")
							cardset3rr = cs3r4.replace((str(card2) + ','), '')
							cardset3r = cardset3rr.replace("#&!#&!", "#&!")
							cardset3 = ([n for n in cardset3r.split(',')])
							card3r = cdt(cardset3)
							card3 = card3r.replace("#&!", "")
							cs4r1 = str(cardset3).replace("[", "")
							cs4r2 = cs4r1.replace("]", "")
							cs4r3 = cs4r2.replace(" '#&!", "#&!")
							cs4r4 = cs4r3.replace("'", "")
							cardset4rr = cs4r4.replace((str(card3) + ','), '')
							cardset4r = cardset4rr.replace("#&!#&!", "#&!")
							cardset4 = ([n for n in cardset4r.split(',')])
							card4r = cdt(cardset4)
							card4 = card4r.replace("#&!", "")
							cs5r1 = str(cardset4).replace("[", "")
							cs5r2 = cs5r1.replace("]", "")
							cs5r3 = cs5r2.replace(" '#&!", "#&!")
							cs5r4 = cs5r3.replace("'", "")
							cardset5rr = cs5r4.replace((str(card4) + ','), '')
							cardset5r = cardset5rr.replace("#&!#&!", "#&!")
							cardset5 = ([n for n in cardset5r.split(',')])
							card5r = cdt(cardset5)
							card5 = card5r.replace("#&!", "")
							csfr1 = str(cardset5).replace("[", "")
							csfr2 = csfr1.replace("]", "")
							csfr3 = csfr2.replace(" '#&!", "#&!")
							csfr4 = csfr3.replace("'", "")
							cardsetfrr = csfr4.replace((str(card5) + ','), '')
							cardsetfr = cardsetfrr.replace("#&!#&!", "#&!")
							cardsetf = ([n for n in cardsetfr.split(',')])
							fcsfr1 = str(cardsetf).replace("[", "")
							fcsfr2 = fcsfr1.replace("]", "")
							fcsfr3 = fcsfr2.replace("'#&!", "#&!")
							fcsfr4 = fcsfr3.replace("'", "")
							fcs2r1 = str(cards).replace("[", "")
							fcs2r2 = fcs2r1.replace("]", "")
							fcs2r3 = fcs2r2.replace("'#&!", "#&!")
							fcs2r4 = fcs2r3.replace("'", "")
							gsetnewcd = rgset.replace(fcs2r4, fcsfr4)
							wrtnewcd = open(gid + ".txt","w")
							wrtnewcd.write(gsetnewcd)
							wrtnewcd.close()
							rgsetr.close()
							gsetr = open(gid + ".txt","r")
							gset = (gsetr.read()).lower()
							handstrr = card1 + "," + card2 + "," + card3 + "," + card4 + "," + card5
							handli = handstrr.lower()
							#handli = ([n for n in handstr.split(',')])
							cvp2f = handli.count('2')
							cvp3f = handli.count('3')
							cvp4f = handli.count('4')
							cvp5f = handli.count('5')
							cvp6f = handli.count('6')
							cvp7f = handli.count('7')
							cvp8f = handli.count('8')
							cvp9f = handli.count('9')
							cvp10f = handli.count('10')
							cvpjf = handli.count('jack')
							cvpqf = handli.count('icequeen')
							cvpkf = handli.count('king')
							cvpaf = handli.count('ace')
							svpcf = handli.count('clubs')
							svpsf = handli.count('spades')
							svphf = handli.count('hearts')
							svpdf = handli.count('diamonds')
							if cvp2f == 1:
								pointv21 = 2
								highcard = 2
								pointv20 = 0
								pointv22 = 0
								pointv23 = 0
								pointv24 = 0
							elif cvp2f == 2:
								pointv22 = 2
								highcard = 2
								pointv20 = 0
								pointv21 = 0
								pointv23 = 0
								pointv24 = 0
							elif cvp2f == 3:
								pointv23 = 2
								highcard = 2
								pointv20 = 0
								pointv21 = 0
								pointv22 = 0
								pointv24 = 0
							elif cvp2f == 4:
								pointv24 = 2
								highcard = 2
								pointv20 = 0
								pointv21 = 0
								pointv22 = 0
								pointv23 = 0
							elif cvp2f == 0:
								pointv20 = 0
								pointv21 = 0
								pointv22 = 0
								pointv23 = 0
								pointv24 = 0
							if cvp3f == 1:
								pointv31 = 3
								highcard = 3
								pointv30 = 0
								pointv32 = 0
								pointv33 = 0
								pointv34 = 0
							elif cvp3f == 2:
								pointv32 = 3
								highcard = 3
								pointv30 = 0
								pointv31 = 0
								pointv33 = 0
								pointv34 = 0
							elif cvp3f == 3:
								pointv33 = 3
								highcard = 3
								pointv30 = 0
								pointv31 = 0
								pointv32 = 0
								pointv34 = 0
							elif cvp3f == 4:
								pointv34 = 3
								highcard = 3
								pointv30 = 0
								pointv31 = 0
								pointv32 = 0
								pointv33 = 0
							elif cvp3f == 0:
								pointv30 = 0
								pointv31 = 0
								pointv32 = 0
								pointv33 = 0
								pointv34 = 0
							if cvp4f == 1:
								pointv41 = 4
								highcard = 4
								pointv40 = 0
								pointv42 = 0
								pointv43 = 0
								pointv44 = 0
							elif cvp4f == 2:
								pointv42 = 4
								highcard = 4
								pointv40 = 0
								pointv41 = 0
								pointv43 = 0
								pointv44 = 0
							elif cvp4f == 3:
								pointv43 = 4
								pointv40 = 0
								pointv41 = 0
								pointv42 = 0
								pointv44 = 0
							elif cvp4f == 4:
								pointv44 = 4
								pointv40 = 0
								pointv41 = 0
								pointv42 = 0
								pointv43 = 0
							elif cvp4f == 0:
								pointv40 = 0
								pointv41 = 0
								pointv42 = 0
								pointv43 = 0
								pointv44 = 0
							if cvp5f == 1:
								pointv51 = 5
								highcard = 5
								pointv50 = 0
								pointv52 = 0
								pointv53 = 0
								pointv54 = 0
							elif cvp5f == 2:
								pointv52 = 5
								highcard = 5
								pointv50 = 0
								pointv51 = 0
								pointv53 = 0
								pointv54 = 0
							elif cvp5f == 3:
								pointv53 = 5
								highcard = 5
								pointv50 = 0
								pointv51 = 0
								pointv52 = 0
								pointv54 = 0
							elif cvp5f == 4:
								pointv54 = 5
								highcard = 5
								pointv50 = 0
								pointv51 = 0
								pointv52 = 0
								pointv53 = 0
							elif cvp5f == 0:
								pointv50 = 0
								pointv51 = 0
								pointv52 = 0
								pointv53 = 0
								pointv54 = 0
							if cvp6f == 1:
								pointv61 = 6
								highcard = 6
								pointv60 = 0
								pointv62 = 0
								pointv63 = 0
								pointv64 = 0
							elif cvp6f == 2:
								pointv62 = 6
								highcard = 6
								pointv60 = 0
								pointv61 = 0
								pointv63 = 0
								pointv64 = 0
							elif cvp6f == 3:
								pointv63 = 6
								highcard = 6
								pointv60 = 0
								pointv61 = 0
								pointv62 = 0
								pointv64 = 0
							elif cvp6f == 4:
								pointv64 = 6
								highcard = 6
								pointv60 = 0
								pointv61 = 0
								pointv62 = 0
								pointv63 = 0
							elif cvp6f == 0:
								pointv60 = 0
								pointv61 = 0
								pointv62 = 0
								pointv63 = 0
								pointv64 = 0
							if cvp7f == 1:
								pointv71 = 7
								highcard = 7
								pointv70 = 0
								pointv72 = 0
								pointv73 = 0
								pointv74 = 0
							elif cvp7f == 2:
								pointv72 = 7
								highcard = 7
								pointv70 = 0
								pointv71 = 0
								pointv73 = 0
								pointv74 = 0
							elif cvp7f == 3:
								pointv73 = 7
								highcard = 7
								pointv70 = 0
								pointv71 = 0
								pointv72 = 0
								pointv74 = 0
							elif cvp7f == 4:
								pointv74 = 7
								highcard = 7
								pointv70 = 0
								pointv71 = 0
								pointv72 = 0
								pointv73 = 0
							elif cvp7f == 0:
								pointv70 = 0
								pointv71 = 0
								pointv72 = 0
								pointv73 = 0
								pointv74 = 0
							if cvp8f == 1:
								pointv81 = 8
								highcard = 8
								pointv80 = 0
								pointv82 = 0
								pointv83 = 0
								pointv84 = 0
							elif cvp8f == 2:
								pointv82 = 8
								highcard = 8
								pointv80 = 0
								pointv81 = 0
								pointv83 = 0
								pointv84 = 0
							elif cvp8f == 3:
								pointv83 = 8
								highcard = 8
								pointv80 = 0
								pointv81 = 0
								pointv82 = 0
								pointv84 = 0
							elif cvp8f == 4:
								pointv84 = 8
								highcard = 8
								pointv80 = 0
								pointv81 = 0
								pointv82 = 0
								pointv83 = 0
							elif cvp8f == 0:
								pointv80 = 0
								pointv81 = 0
								pointv82 = 0
								pointv83 = 0
								pointv84 = 0
							if cvp9f == 1:
								pointv91 = 9
								highcard = 9
								pointv90 = 0
								pointv92 = 0
								pointv93 = 0
								pointv94 = 0
							elif cvp9f == 2:
								pointv92 = 9
								highcard = 9
								pointv90 = 0
								pointv91 = 0
								pointv93 = 0
								pointv94 = 0
							elif cvp9f == 3:
								pointv93 = 9
								highcard = 9
								pointv90 = 0
								pointv91 = 0
								pointv92 = 0
								pointv94 = 0
							elif cvp9f == 4:
								pointv94 = 9
								highcard = 9
								pointv90 = 0
								pointv91 = 0
								pointv92 = 0
								pointv93 = 0
							elif cvp9f == 0:
								pointv90 = 0
								pointv91 = 0
								pointv92 = 0
								pointv93 = 0
								pointv94 = 0
							if cvp10f == 1:
								pointv101 = 10
								highcard = 10
								pointv100 = 0
								pointv102 = 0
								pointv103 = 0
								pointv104 = 0
							elif cvp10f == 2:
								pointv102 = 10
								highcard = 10
								pointv100 = 0
								pointv101 = 0
								pointv103 = 0
								pointv104 = 0
							elif cvp10f == 3:
								pointv103 = 10
								highcard = 10
								pointv100 = 0
								pointv101 = 0
								pointv102 = 0
								pointv104 = 0
							elif cvp10f == 4:
								pointv104 = 10
								highcard = 10
								pointv100 = 0
								pointv101 = 0
								pointv102 = 0
								pointv103 = 0
							elif cvp10f == 0:
								pointv100 = 0
								pointv101 = 0
								pointv102 = 0
								pointv103 = 0
								pointv104 = 0
							if cvpjf == 1:
								pointvj1 = 11
								highcard = 11
								pointvj0 = 0
								pointvj2 = 0
								pointvj3 = 0
								pointvj4 = 0
							elif cvpjf == 2:
								pointvj2 = 11
								highcard = 11
								pointvj0 = 0
								pointvj1 = 0
								pointvj3 = 0
								pointvj4 = 0
							elif cvpjf == 3:
								pointvj3 = 11
								highcard = 11
								pointvj0 = 0
								pointvj1 = 0
								pointvj2 = 0
								pointvj4 = 0
							elif cvpjf == 4:
								pointvj4 = 11
								highcard = 11
								pointvj0 = 0
								pointvj1 = 0
								pointvj2 = 0
								pointvj3 = 0
							elif cvpjf == 0:
								pointvj0 = 0
								pointvj1 = 0
								pointvj2 = 0
								pointvj3 = 0
								pointvj4 = 0
							if cvpqf == 1:
								pointvq1 = 12
								highcard = 12
								pointvq0 = 0
								pointvq2 = 0
								pointvq3 = 0
								pointvq4 = 0
							elif cvpqf == 2:
								pointvq2 = 12
								highcard = 12
								pointvq0 = 0
								pointvq1 = 0
								pointvq3 = 0
								pointvq4 = 0
							elif cvpqf == 3:
								pointvq3 = 12
								highcard = 12
								pointvq0 = 0
								pointvq1 = 0
								pointvq2 = 0
								pointvq4 = 0
							elif cvpqf == 4:
								pointvq4 = 12
								highcard = 12
								pointvq0 = 0
								pointvq1 = 0
								pointvq2 = 0
								pointvq3 = 0
							elif cvpqf == 0:
								pointvq0 = 0
								pointvq1 = 0
								pointvq2 = 0
								pointvq3 = 0
								pointvq4 = 0
							if cvpkf == 1:
								pointvk1 = 13
								highcard = 13
								pointvk0 = 0
								pointvk2 = 0
								pointvk3 = 0
								pointvk4 = 0
							elif cvpkf == 2:
								pointvk2 = 13
								highcard = 13
								pointvk0 = 0
								pointvk1 = 0
								pointvk3 = 0
								pointvk4 = 0
							elif cvpkf == 3:
								pointvk3 = 13
								highcard = 13
								pointvk0 = 0
								pointvk1 = 0
								pointvk2 = 0
								pointvk4 = 0
							elif cvpkf == 4:
								pointvk4 = 13
								highcard = 13
								pointvk0 = 0
								pointvk1 = 0
								pointvk2 = 0
								pointvk3 = 0
							elif cvpkf == 0:
								pointvk0 = 0
								pointvk1 = 0
								pointvk2 = 0
								pointvk3 = 0
								pointvk4 = 0
							if cvpaf == 1:
								pointva1 = 14
								highcard = 14
								pointva0 = 0
								pointva2 = 0
								pointva3 = 0
								pointva4 = 0
							elif cvpaf == 2:
								pointva2 = 14
								highcard = 14
								pointva0 = 0
								pointva1 = 0
								pointva3 = 0
								pointva4 = 0
							elif cvpaf == 3:
								pointva3 = 14
								highcard = 14
								pointva0 = 0
								pointva1 = 0
								pointva2 = 0
								pointva4 = 0
							elif cvpaf == 4:
								pointva4 = 14
								highcard = 14
								pointva0 = 0
								pointva1 = 0
								pointva2 = 0
								pointva3 = 0
							elif cvpaf == 0:
								pointva0 = 0
								pointva1 = 0
								pointva2 = 0
								pointva3 = 0
								pointva4 = 0
							if svpdf == 1:
								pointvd = 0
							elif svpdf == 2:
								pointvd = 0
							elif svpdf == 3:
								pointvd = 0
							elif svpdf == 4:
								pointvd = 0
							elif svpdf == 5:
								pointvd = 1
							elif svpdf == 0:
								pointvd = 0
							if svphf == 1:
								pointvh = 0
							elif svphf == 2:
								pointvh = 0
							elif svphf == 3:
								pointvh = 0
							elif svphf == 4:
								pointvh = 0
							elif svphf == 5:
								pointvh = 1
							elif svphf == 0:
								pointvh = 0
							if svpsf == 1:
								pointvs = 0
							elif svpsf == 2:
								pointvs = 0
							elif svpsf == 3:
								pointvs = 0
							elif svpsf == 4:
								pointvs = 0
							elif svpsf == 5:
								pointvs = 1
							elif svpsf == 0:
								pointvs = 0
							if svpcf == 1:
								pointvc = 0
							elif svpcf == 2:
								pointvc = 0
							elif svpcf == 3:
								pointvc = 0
							elif svpcf == 4:
								pointvc = 0
							elif svpcf == 5:
								pointvc = 1
							elif svpcf == 0:
								pointvc = 0
							if ( (cvp10f == 1) and (cvpjf == 1) and (cvpqf == 1) and (cvpkf == 1) and (cvpaf == 1) and ((svpcf == 5) or(svpsf == 5) or(svphf == 5) or(svpdf == 5))):
								handpoints = 1000
							elif ( (cvp10f == 1) and (cvpjf == 1) and (cvpqf == 1) and (cvpkf == 1) and (cvp9f == 1) and ((svpcf == 5) or(svpsf == 5) or(svphf == 5) or(svpdf == 5))):
								handpoints = 999
							elif ( (cvp10f == 1) and (cvpjf == 1) and (cvpqf == 1) and (cvp8f == 1) and (cvp9f == 1) and ((svpcf == 5) or(svpsf == 5) or(svphf == 5) or(svpdf == 5))):
								handpoints = 998
							elif ( (cvp10f == 1) and (cvpjf == 1) and (cvp7f == 1) and (cvp8f == 1) and (cvp9f == 1) and ((svpcf == 5) or(svpsf == 5) or(svphf == 5) or(svpdf == 5))):
								handpoints = 997
							elif ( (cvp10f == 1) and (cvp6f == 1) and (cvp7f == 1) and (cvp8f == 1) and (cvp9f == 1) and ((svpcf == 5) or(svpsf == 5) or(svphf == 5) or(svpdf == 5))):
								handpoints = 996
							elif ( (cvp5f == 1) and (cvp6f == 1) and (cvp7f == 1) and (cvp8f == 1) and (cvp9f == 1) and ((svpcf == 5) or(svpsf == 5) or(svphf == 5) or(svpdf == 5))):
								handpoints = 995
							elif ( (cvp5f == 1) and (cvp6f == 1) and (cvp7f == 1) and (cvp8f == 1) and (cvp4f == 1) and ((svpcf == 5) or(svpsf == 5) or(svphf == 5) or(svpdf == 5))):
								handpoints = 994
							elif ( (cvp5f == 1) and (cvp6f == 1) and (cvp7f == 1) and (cvp3f == 1) and (cvp4f == 1) and ((svpcf == 5) or(svpsf == 5) or(svphf == 5) or(svpdf == 5))):
								handpoints = 993
							elif ( (cvp5f == 1) and (cvp6f == 1) and (cvp2f == 1) and (cvp3f == 1) and (cvp4f == 1) and ((svpcf == 5) or(svpsf == 5) or(svphf == 5) or(svpdf == 5))):
								handpoints = 992
							elif ( (cvp5f == 1) and (cvpaf == 1) and (cvp2f == 1) and (cvp3f == 1) and (cvp4f == 1) and ((svpcf == 5) or(svpsf == 5) or(svphf == 5) or(svpdf == 5))):
								handpoints = 991
							elif ( (cvp2f == 4) or (cvp3f == 4) or (cvp4f == 4) or (cvp5f == 4) or (cvp6f == 4) or (cvp7f == 4) or (cvp8f == 4) or (cvp9f == 4) or (cvp10f == 4) or (cvpjf == 4) or (cvpqf == 4) or (cvpkf == 4) or (cvpaf == 4) ):
								handpoints = 976 + pointva4 + pointvk4 + pointvq4 + pointvj4 + pointv104 + pointv94 + pointv84 + pointv74 + pointv64 + pointv54 + pointv44 + pointv34 + pointv24
							elif ( (cvpaf == 3) and ( (cvp2f == 2) or (cvp3f == 2) or (cvp4f == 2) or (cvp5f == 2) or (cvp6f == 2) or (cvp7f == 2) or (cvp8f == 2) or (cvp9f == 2) or (cvp10f == 2) or (cvpjf == 2) or (cvpqf == 2) or (cvpkf == 2) or (cvpaf == 2)) ):
								handpoints = 963 + pointva2 + pointvk2 + pointvq2 + pointvj2 + pointv102 + pointv92 + pointv82 + pointv72 + pointv62 + pointv52 + pointv42 + pointv32 + pointv22
							elif ( (cvpkf == 3) and ( (cvp2f == 2) or (cvp3f == 2) or (cvp4f == 2) or (cvp5f == 2) or (cvp6f == 2) or (cvp7f == 2) or (cvp8f == 2) or (cvp9f == 2) or (cvp10f == 2) or (cvpjf == 2) or (cvpqf == 2) or (cvpkf == 2) or (cvpaf == 2)) ):
								handpoints = 948 + pointva2 + pointvk2 + pointvq2 + pointvj2 + pointv102 + pointv92 + pointv82 + pointv72 + pointv62 + pointv52 + pointv42 + pointv32 + pointv22
							elif ( (cvpqf == 3) and ( (cvp2f == 2) or (cvp3f == 2) or (cvp4f == 2) or (cvp5f == 2) or (cvp6f == 2) or (cvp7f == 2) or (cvp8f == 2) or (cvp9f == 2) or (cvp10f == 2) or (cvpjf == 2) or (cvpqf == 2) or (cvpkf == 2) or (cvpaf == 2)) ):
								handpoints = 933 + pointva2 + pointvk2 + pointvq2 + pointvj2 + pointv102 + pointv92 + pointv82 + pointv72 + pointv62 + pointv52 + pointv42 + pointv32 + pointv22
							elif ( (cvpjf == 3) and ( (cvp2f == 2) or (cvp3f == 2) or (cvp4f == 2) or (cvp5f == 2) or (cvp6f == 2) or (cvp7f == 2) or (cvp8f == 2) or (cvp9f == 2) or (cvp10f == 2) or (cvpjf == 2) or (cvpqf == 2) or (cvpkf == 2) or (cvpaf == 2)) ):
								handpoints = 918 + pointva2 + pointvk2 + pointvq2 + pointvj2 + pointv102 + pointv92 + pointv82 + pointv72 + pointv62 + pointv52 + pointv42 + pointv32 + pointv22
							elif ( (cvp10f == 3) and ( (cvp2f == 2) or (cvp3f == 2) or (cvp4f == 2) or (cvp5f == 2) or (cvp6f == 2) or (cvp7f == 2) or (cvp8f == 2) or (cvp9f == 2) or (cvp10f == 2) or (cvpjf == 2) or (cvpqf == 2) or (cvpkf == 2) or (cvpaf == 2)) ):
								handpoints = 903 + pointva2 + pointvk2 + pointvq2 + pointvj2 + pointv102 + pointv92 + pointv82 + pointv72 + pointv62 + pointv52 + pointv42 + pointv32 + pointv22
							elif ( (cvp9f == 3) and ( (cvp2f == 2) or (cvp3f == 2) or (cvp4f == 2) or (cvp5f == 2) or (cvp6f == 2) or (cvp7f == 2) or (cvp8f == 2) or (cvp9f == 2) or (cvp10f == 2) or (cvpjf == 2) or (cvpqf == 2) or (cvpkf == 2) or (cvpaf == 2)) ):
								handpoints = 888 + pointva2 + pointvk2 + pointvq2 + pointvj2 + pointv102 + pointv92 + pointv82 + pointv72 + pointv62 + pointv52 + pointv42 + pointv32 + pointv22
							elif ( (cvp8f == 3) and ( (cvp2f == 2) or (cvp3f == 2) or (cvp4f == 2) or (cvp5f == 2) or (cvp6f == 2) or (cvp7f == 2) or (cvp8f == 2) or (cvp9f == 2) or (cvp10f == 2) or (cvpjf == 2) or (cvpqf == 2) or (cvpkf == 2) or (cvpaf == 2)) ):
								handpoints = 873 + pointva2 + pointvk2 + pointvq2 + pointvj2 + pointv102 + pointv92 + pointv82 + pointv72 + pointv62 + pointv52 + pointv42 + pointv32 + pointv22
							elif ( (cvp7f == 3) and ( (cvp2f == 2) or (cvp3f == 2) or (cvp4f == 2) or (cvp5f == 2) or (cvp6f == 2) or (cvp7f == 2) or (cvp8f == 2) or (cvp9f == 2) or (cvp10f == 2) or (cvpjf == 2) or (cvpqf == 2) or (cvpkf == 2) or (cvpaf == 2)) ):
								handpoints = 858 + pointva2 + pointvk2 + pointvq2 + pointvj2 + pointv102 + pointv92 + pointv82 + pointv72 + pointv62 + pointv52 + pointv42 + pointv32 + pointv22
							elif ( (cvp6f == 3) and ( (cvp2f == 2) or (cvp3f == 2) or (cvp4f == 2) or (cvp5f == 2) or (cvp6f == 2) or (cvp7f == 2) or (cvp8f == 2) or (cvp9f == 2) or (cvp10f == 2) or (cvpjf == 2) or (cvpqf == 2) or (cvpkf == 2) or (cvpaf == 2)) ):
								handpoints = 843 + pointva2 + pointvk2 + pointvq2 + pointvj2 + pointv102 + pointv92 + pointv82 + pointv72 + pointv62 + pointv52 + pointv42 + pointv32 + pointv22
							elif ( (cvp5f == 3) and ( (cvp2f == 2) or (cvp3f == 2) or (cvp4f == 2) or (cvp5f == 2) or (cvp6f == 2) or (cvp7f == 2) or (cvp8f == 2) or (cvp9f == 2) or (cvp10f == 2) or (cvpjf == 2) or (cvpqf == 2) or (cvpkf == 2) or (cvpaf == 2)) ):
								handpoints = 828 + pointva2 + pointvk2 + pointvq2 + pointvj2 + pointv102 + pointv92 + pointv82 + pointv72 + pointv62 + pointv52 + pointv42 + pointv32 + pointv22
							elif ( (cvp4f == 3) and ( (cvp2f == 2) or (cvp3f == 2) or (cvp4f == 2) or (cvp5f == 2) or (cvp6f == 2) or (cvp7f == 2) or (cvp8f == 2) or (cvp9f == 2) or (cvp10f == 2) or (cvpjf == 2) or (cvpqf == 2) or (cvpkf == 2) or (cvpaf == 2)) ):
								handpoints = 813 + pointva2 + pointvk2 + pointvq2 + pointvj2 + pointv102 + pointv92 + pointv82 + pointv72 + pointv62 + pointv52 + pointv42 + pointv32 + pointv22
							elif ( (cvp3f == 3) and ( (cvp2f == 2) or (cvp3f == 2) or (cvp4f == 2) or (cvp5f == 2) or (cvp6f == 2) or (cvp7f == 2) or (cvp8f == 2) or (cvp9f == 2) or (cvp10f == 2) or (cvpjf == 2) or (cvpqf == 2) or (cvpkf == 2) or (cvpaf == 2)) ):
								handpoints = 798 + pointva2 + pointvk2 + pointvq2 + pointvj2 + pointv102 + pointv92 + pointv82 + pointv72 + pointv62 + pointv52 + pointv42 + pointv32 + pointv22
							elif ( (cvp2f == 3) and ( (cvp2f == 2) or (cvp3f == 2) or (cvp4f == 2) or (cvp5f == 2) or (cvp6f == 2) or (cvp7f == 2) or (cvp8f == 2) or (cvp9f == 2) or (cvp10f == 2) or (cvpjf == 2) or (cvpqf == 2) or (cvpkf == 2) or (cvpaf == 2)) ):
								handpoints = 783 + pointva2 + pointvk2 + pointvq2 + pointvj2 + pointv102 + pointv92 + pointv82 + pointv72 + pointv62 + pointv52 + pointv42 + pointv32 + pointv22
							elif ( (svpcf == 5) or (svpsf ==5) or (svphf ==5) or (svpdf ==5) ):
								handpoints = 782
							elif ( (cvp10f == 1) and (cvpjf == 1) and (cvpqf == 1) and (cvpkf == 1) and (cvpaf == 1)):
								handpoints = 781
							elif ( (cvp10f == 1) and (cvpjf == 1) and (cvpqf == 1) and (cvpkf == 1) and (cvp9f == 1)):
								handpoints = 780
							elif ( (cvp10f == 1) and (cvpjf == 1) and (cvpqf == 1) and (cvp8f == 1) and (cvp9f == 1)):
								handpoints = 779
							elif ( (cvp10f == 1) and (cvpjf == 1) and (cvp7f == 1) and (cvp8f == 1) and (cvp9f == 1)):
								handpoints = 778
							elif ( (cvp10f == 1) and (cvp6f == 1) and (cvp7f == 1) and (cvp8f == 1) and (cvp9f == 1)):
								handpoints = 776
							elif ( (cvp5f == 1) and (cvp6f == 1) and (cvp7f == 1) and (cvp8f == 1) and (cvp9f == 1)):
								handpoints = 775
							elif ( (cvp5f == 1) and (cvp6f == 1) and (cvp7f == 1) and (cvp8f == 1) and (cvp4f == 1)):
								handpoints = 774
							elif ( (cvp5f == 1) and (cvp6f == 1) and (cvp7f == 1) and (cvp3f == 1) and (cvp4f == 1)):
								handpoints = 773
							elif ( (cvp5f == 1) and (cvp6f == 1) and (cvp2f == 1) and (cvp3f == 1) and (cvp4f == 1)):
								handpoints = 772
							elif ( (cvp5f == 1) and (cvpaf == 1) and (cvp2f == 1) and (cvp3f == 1) and (cvp4f == 1)):
								handpoints = 771
							elif ( (cvp2f == 3) or (cvp3f == 3) or (cvp4f == 3) or (cvp5f == 3) or (cvp6f == 3) or (cvp7f == 3) or (cvp8f == 3) or (cvp9f == 3) or (cvp10f == 3) or (cvpjf == 3) or (cvpqf == 3) or (cvpkf == 3) or (cvpaf == 3) ):
								handpoints = 756 + pointva3 + pointvk3 + pointvq3 + pointvj3 + pointv103 + pointv93 + pointv83 + pointv73 + pointv63 + pointv53 + pointv43 + pointv33 + pointv23
							elif ( (cvpaf == 2) and ( (cvp2f == 2) or (cvp3f == 2) or (cvp4f == 2) or (cvp5f == 2) or (cvp6f == 2) or (cvp7f == 2) or (cvp8f == 2) or (cvp9f == 2) or (cvp10f == 2) or (cvpjf == 2) or (cvpqf == 2) or (cvpkf == 2)) ):
								handpoints = 741 + pointvk2 + pointvq2 + pointvj2 + pointv102 + pointv92 + pointv82 + pointv72 + pointv62 + pointv52 + pointv42 + pointv32 + pointv22
							elif ( (cvpkf == 2) and ( (cvp2f == 2) or (cvp3f == 2) or (cvp4f == 2) or (cvp5f == 2) or (cvp6f == 2) or (cvp7f == 2) or (cvp8f == 2) or (cvp9f == 2) or (cvp10f == 2) or (cvpjf == 2) or (cvpqf == 2) or (cvpaf == 2)) ):
								handpoints = 726 + pointva2 + pointvq2 + pointvj2 + pointv102 + pointv92 + pointv82 + pointv72 + pointv62 + pointv52 + pointv42 + pointv32 + pointv22
							elif ( (cvpqf == 2) and ( (cvp2f == 2) or (cvp3f == 2) or (cvp4f == 2) or (cvp5f == 2) or (cvp6f == 2) or (cvp7f == 2) or (cvp8f == 2) or (cvp9f == 2) or (cvp10f == 2) or (cvpjf == 2) or (cvpkf == 2) or (cvpaf == 2)) ):
								handpoints = 711 + pointva2 + pointvk2 + pointvj2 + pointv102 + pointv92 + pointv82 + pointv72 + pointv62 + pointv52 + pointv42 + pointv32 + pointv22
							elif ( (cvpjf == 2) and ( (cvp2f == 2) or (cvp3f == 2) or (cvp4f == 2) or (cvp5f == 2) or (cvp6f == 2) or (cvp7f == 2) or (cvp8f == 2) or (cvp9f == 2) or (cvp10f == 2) or (cvpqf == 2) or (cvpkf == 2) or (cvpaf == 2)) ):
								handpoints = 696 + pointva2 + pointvk2 + pointvq2 + pointv102 + pointv92 + pointv82 + pointv72 + pointv62 + pointv52 + pointv42 + pointv32 + pointv22
							elif ( (cvp10f == 2) and ( (cvp2f == 2) or (cvp3f == 2) or (cvp4f == 2) or (cvp5f == 2) or (cvp6f == 2) or (cvp7f == 2) or (cvp8f == 2) or (cvp9f == 2) or (cvpjf == 2) or (cvpqf == 2) or (cvpkf == 2) or (cvpaf == 2)) ):
								handpoints = 681 + pointva2 + pointvk2 + pointvq2 + pointvj2 + pointv92 + pointv82 + pointv72 + pointv62 + pointv52 + pointv42 + pointv32 + pointv22
							elif ( (cvp9f == 2) and ( (cvp2f == 2) or (cvp3f == 2) or (cvp4f == 2) or (cvp5f == 2) or (cvp6f == 2) or (cvp7f == 2) or (cvp8f == 2) or (cvp10f == 2) or (cvpjf == 2) or (cvpqf == 2) or (cvpkf == 2) or (cvpaf == 2)) ):
								handpoints = 666 + pointva2 + pointvk2 + pointvq2 + pointvj2 + pointv102 + pointv82 + pointv72 + pointv62 + pointv52 + pointv42 + pointv32 + pointv22
							elif ( (cvp8f == 2) and ( (cvp2f == 2) or (cvp3f == 2) or (cvp4f == 2) or (cvp5f == 2) or (cvp6f == 2) or (cvp7f == 2) or (cvp9f == 2) or (cvp10f == 2) or (cvpjf == 2) or (cvpqf == 2) or (cvpkf == 2) or (cvpaf == 2)) ):
								handpoints = 651 + pointva2 + pointvk2 + pointvq2 + pointvj2 + pointv102 + pointv92 + pointv72 + pointv62 + pointv52 + pointv42 + pointv32 + pointv22
							elif ( (cvp7f == 2) and ( (cvp2f == 2) or (cvp3f == 2) or (cvp4f == 2) or (cvp5f == 2) or (cvp6f == 2) or (cvp8f == 2) or (cvp9f == 2) or (cvp10f == 2) or (cvpjf == 2) or (cvpqf == 2) or (cvpkf == 2) or (cvpaf == 2)) ):
								handpoints = 636 + pointva2 + pointvk2 + pointvq2 + pointvj2 + pointv102 + pointv92 + pointv82 + pointv62 + pointv52 + pointv42 + pointv32 + pointv22
							elif ( (cvp6f == 2) and ( (cvp2f == 2) or (cvp3f == 2) or (cvp4f == 2) or (cvp5f == 2) or (cvp7f == 2) or (cvp8f == 2) or (cvp9f == 2) or (cvp10f == 2) or (cvpjf == 2) or (cvpqf == 2) or (cvpkf == 2) or (cvpaf == 2)) ):
								handpoints = 621 + pointva2 + pointvk2 + pointvq2 + pointvj2 + pointv102 + pointv92 + pointv82 + pointv72 + pointv52 + pointv42 + pointv32 + pointv22
							elif ( (cvp5f == 2) and ( (cvp2f == 2) or (cvp3f == 2) or (cvp4f == 2) or (cvp6f == 2) or (cvp7f == 2) or (cvp8f == 2) or (cvp9f == 2) or (cvp10f == 2) or (cvpjf == 2) or (cvpqf == 2) or (cvpkf == 2) or (cvpaf == 2)) ):
								handpoints = 606 + pointva2 + pointvk2 + pointvq2 + pointvj2 + pointv102 + pointv92 + pointv82 + pointv72 + pointv62 + pointv42 + pointv32 + pointv22
							elif ( (cvp4f == 2) and ( (cvp2f == 2) or (cvp3f == 2) or (cvp5f == 2) or (cvp6f == 2) or (cvp7f == 2) or (cvp8f == 2) or (cvp9f == 2) or (cvp10f == 2) or (cvpjf == 2) or (cvpqf == 2) or (cvpkf == 2) or (cvpaf == 2)) ):
								handpoints = 591 + pointva2 + pointvk2 + pointvq2 + pointvj2 + pointv102 + pointv92 + pointv82 + pointv72 + pointv62 + pointv52 + pointv32 + pointv22
							elif ( (cvp3f == 2) and ( (cvp2f == 2) or (cvp4f == 2) or (cvp5f == 2) or (cvp6f == 2) or (cvp7f == 2) or (cvp8f == 2) or (cvp9f == 2) or (cvp10f == 2) or (cvpjf == 2) or (cvpqf == 2) or (cvpkf == 2) or (cvpaf == 2)) ):
								handpoints = 576 + pointva2 + pointvk2 + pointvq2 + pointvj2 + pointv102 + pointv92 + pointv82 + pointv72 + pointv62 + pointv52 + pointv42 + pointv22
							elif ( (cvp2f == 2) and ((cvp3f == 2) or (cvp4f == 2) or (cvp5f == 2) or (cvp6f == 2) or (cvp7f == 2) or (cvp8f == 2) or (cvp9f == 2) or (cvp10f == 2) or (cvpjf == 2) or (cvpqf == 2) or (cvpkf == 2) or (cvpaf == 2)) ):
								handpoints = 561 + pointva2 + pointvk2 + pointvq2 + pointvj2 + pointv102 + pointv92 + pointv82 + pointv72 + pointv62 + pointv52 + pointv42 + pointv32
							elif ( (cvp2f == 2) or (cvp3f == 2) or (cvp4f == 2) or (cvp5f == 2) or (cvp6f == 2) or (cvp7f == 2) or (cvp8f == 2) or (cvp9f == 2) or (cvp10f == 2) or (cvpjf == 2) or (cvpqf == 2) or (cvpkf == 2) or (cvpaf == 2) ):
								handpoints = 546 + pointva2 + pointvk2 + pointvq2 + pointvj2 + pointv102 + pointv92 + pointv82 + pointv72 + pointv62 + pointv52 + pointv42 + pointv32 + pointv22
							else:
								handpoints = 500
							availableir = int(available)
							availablei = availableir - 1
							availblenew = '^$&*available = ' + str(availablei) + ' *)!#'
							gsetnew = gset.replace(('^$&*available = ' + available + ' *)!#'), str(availblenew))
							wrtdata2 = open((gid + ".txt"), "w")
							secnames = '#$!*&^!@' + user.name + '&&*)^$#@!'
							secnamef = ')(&$&$#@' + user.name + '!@&@$@^&'
							highnames = '!!@*^$&' + user.name + '**^&$$#!('
							highnamef = '&(#*$%!)^' + user.name + '(*&$@@#!'
							handnames = '**^@%#$' + user.name + ')()*@&^%'
							handnamef = '!)@(#$&' + user.name + '!*!&!^#'
							wrtdata2.write(gsetnew + '\n' + secnames + ("handpoint = %d" %(handpoints)) + secnamef + '\n' + highnames + ("highcard = %d" %(highcard)) + highnamef + '\n' + handnames + 'card1 = ' + card1 + handnamef + 'c1' + '\n' + handnames + 'card2 = ' + card2 + handnamef + 'c2' + '\n' + handnames + 'card3 = ' + card3 + handnamef + 'c3' + '\n' + handnames + 'card4 = ' + card4 + handnamef + 'c4' + '\n' + handnames + 'card5 = ' + card5 + handnamef + 'c5' + '\n')
							wrtdata2.close()
							glistr.close()
							gsetr.close()
							wrtdata2.close()
							(self._pm).message(user, str("Your cards for [gameid: " + gid.upper() + "] are: " + card1 + ", " + card2 + ", " + card3 + ", " + card4 + ", " + card5 + "."))
							if availablei == 0:
								tsetr = open(gid + ".txt","r")
								tset = (tsetr.read()).lower()
								tsetnew = tset.replace(('##$*!@turn = 1@*&(*'), '##$*!@turn = 2@*&(*')
								wrtdatat = open((gid + ".txt"), "w")
								wrtdatat.write(tsetnew)
								tsetr.close()
								wrtdatat.close()
							room.message("I have PMed you the hand you drew.")
			elif (cmd.lower()) == "pokertrade":
				if usrlvl >= 0:
					if args.find(": ") != -1: #if there's a colon somewhere
						argsadj = args.lower()
						gameid, trade = argsadj.split(": ", 1)
						if 0 == 0:#trade.find(", ") != -1: #if there's a (comma + space) somewhere # I totally fucked this one up :/
							switchcardsr1 = re.split(', ', trade)
							switchcardsr2 = [item.lower() for item in switchcardsr1]
							tradenum = len(switchcardsr2)
							glistr = open("glist.txt","r")
							glist = (glistr.read()).upper()
							if ('*$^&@($#@!*$#' + gameid.upper() + '$*#$$*&&@^#') in glist:
								gid = gameid
								rgsetr = open(gid + ".txt","r")
								rgset = (rgsetr.read()).lower()
								cindexs = rgset.find('*#&$^#cards = ')
								cindexe = rgset.find('#&#@$($#')
								crawout = rgset[(int(cindexs)):(int(cindexe))]
								crawout2 = crawout.replace(('*#&$^#cards = '), "")
								cardsstr = crawout2.replace(('#&#@$($#'), "")
								cardsprep = re.split(', ', cardsstr)
								cards = [item.lower() for item in cardsprep]
								def cdt(cards):
									return random.choice(cards)
								tdindexs = rgset.find('*#&^tradestatus = ')
								tdindexe = rgset.find(' )#(#*&')
								tdrawout = rgset[(int(tdindexs)):(int(tdindexe))]
								tdrawout2 = tdrawout.replace(('*#&^tradestatus = '), "")
								tradestatus = tdrawout2.replace((' )#(#*&'), "")
								trindexs = rgset.find('##$*!@turn = ')
								trindexe = rgset.find('@*&(*')
								trrawout = rgset[(int(trindexs)):(int(trindexe))]
								trrawout2 = trrawout.replace(('##$*!@turn = '), "")
								turn = trrawout2.replace(('@*&(*'), "")
								turni = int(turn)
								if tradestatus == '0':
									room.message("You can no longer trade for this game.")
								elif turni < 2:
									room.message("Trading will begin when all players draw")
								elif ('*$!$@#($*!' + user.name + ' has traded!$#@(%*!%!') in (rgset):
									room.message("You have already done a trade. Please wait for all players to finish trading.")
								else:
									sc1indexs = rgset.find('**^@%#$' + user.name + ')()*@&^%card1 = ')
									sc1indexe = rgset.find('!)@(#$&' + user.name + '!*!&!^#c1')
									sc1rawout = rgset[(int(sc1indexs)):(int(sc1indexe))]
									sc1rawout2 = sc1rawout.replace(('**^@%#$' + user.name + ')()*@&^%card1 = '), "")
									oldcard1 = sc1rawout2.replace(('!)@(#$&' + user.name + '!*!&!^#c1'), "")
									sc2indexs = rgset.find('**^@%#$' + user.name + ')()*@&^%card2 = ')
									sc2indexe = rgset.find('!)@(#$&' + user.name + '!*!&!^#c2')
									sc2rawout = rgset[(int(sc2indexs)):(int(sc2indexe))]
									sc2rawout2 = sc2rawout.replace(('**^@%#$' + user.name + ')()*@&^%card2 = '), "")
									oldcard2 = sc2rawout2.replace(('!)@(#$&' + user.name + '!*!&!^#c2'), "")
									sc3indexs = rgset.find('**^@%#$' + user.name + ')()*@&^%card3 = ')
									sc3indexe = rgset.find('!)@(#$&' + user.name + '!*!&!^#c3')
									sc3rawout = rgset[(int(sc3indexs)):(int(sc3indexe))]
									sc3rawout2 = sc3rawout.replace(('**^@%#$' + user.name + ')()*@&^%card3 = '), "")
									oldcard3 = sc3rawout2.replace(('!)@(#$&' + user.name + '!*!&!^#c3'), "")
									sc4indexs = rgset.find('**^@%#$' + user.name + ')()*@&^%card4 = ')
									sc4indexe = rgset.find('!)@(#$&' + user.name + '!*!&!^#c4')
									sc4rawout = rgset[(int(sc4indexs)):(int(sc4indexe))]
									sc4rawout2 = sc4rawout.replace(('**^@%#$' + user.name + ')()*@&^%card4 = '), "")
									oldcard4 = sc4rawout2.replace(('!)@(#$&' + user.name + '!*!&!^#c4'), "")
									sc5indexs = rgset.find('**^@%#$' + user.name + ')()*@&^%card5 = ')
									sc5indexe = rgset.find('!)@(#$&' + user.name + '!*!&!^#c5')
									sc5rawout = rgset[(int(sc5indexs)):(int(sc5indexe))]
									sc5rawout2 = sc5rawout.replace(('**^@%#$' + user.name + ')()*@&^%card5 = '), "")
									oldcard5 = sc5rawout2.replace(('!)@(#$&' + user.name + '!*!&!^#c5'), "")
									if tradenum > 5:
										room.message("You can't trade more cards than you have.")
									elif tradenum == 5:
										sc1 = switchcardsr2[0]
										sc2 = switchcardsr2[1]
										sc3 = switchcardsr2[2]
										sc4 = switchcardsr2[3]
										sc5 = switchcardsr2[4]
										if (sc1 in oldcard1):
											if (sc2 in oldcard2):
												if (sc3 in oldcard3):
													if (sc4 in oldcard4):
														if (sc5 in oldcard5):
															falsetrade = 0
														else:
															falsetrade = 1
															room.message("One or more cards that you requested for trade are not in your hand.")
													elif (sc4 in oldcard5):
														if (sc5 in oldcard4):
															falsetrade = 0
														else:
															falsetrade = 1
															room.message("One or more cards that you requested for trade are not in your hand.")
													else:
														falsetrade = 1
														room.message("One or more cards that you requested for trade are not in your hand.")
												elif (sc3 in oldcard4):
													if (sc4 in oldcard3):
														if (sc5 in oldcard5):
															falsetrade = 0
														else:
															falsetrade = 1
															room.message("One or more cards that you requested for trade are not in your hand.")
													elif (sc4 in oldcard5):
														if (sc5 in oldcard3):
															falsetrade = 0
														else:
															falsetrade = 1
															room.message("One or more cards that you requested for trade are not in your hand.")
													else:
														falsetrade = 1
														room.message("One or more cards that you requested for trade are not in your hand.")
												elif (sc3 in oldcard5):
													if (sc4 in oldcard3):
														if (sc5 in oldcard4):
															falsetrade = 0
														else:
															falsetrade = 1
															room.message("One or more cards that you requested for trade are not in your hand.")
													elif (sc4 in oldcard4):
														if (sc5 in oldcard3):
															falsetrade = 0
														else:
															falsetrade = 1
															room.message("One or more cards that you requested for trade are not in your hand.")
													else:
														falsetrade = 1
														room.message("One or more cards that you requested for trade are not in your hand.")
												else:
													falsetrade = 1
													room.message("One or more cards that you requested for trade are not in your hand.")
											elif (sc2 in oldcard3):
												if (sc3 in oldcard2):
													if (sc4 in oldcard4):
														if (sc5 in oldcard5):
															falsetrade = 0
														else:
															falsetrade = 1
															room.message("One or more cards that you requested for trade are not in your hand.")
													elif (sc4 in oldcard5):
														if (sc5 in oldcard4):
															falsetrade = 0
														else:
															falsetrade = 1
															room.message("One or more cards that you requested for trade are not in your hand.")
													else:
														falsetrade = 1
														room.message("One or more cards that you requested for trade are not in your hand.")
												elif (sc3 in oldcard4):
													if (sc4 in oldcard2):
														if (sc5 in oldcard5):
															falsetrade = 0
														else:
															falsetrade = 1
															room.message("One or more cards that you requested for trade are not in your hand.")
													elif (sc4 in oldcard5):
														if (sc5 in oldcard2):
															falsetrade = 0
														else:
															falsetrade = 1
															room.message("One or more cards that you requested for trade are not in your hand.")
													else:
														falsetrade = 1
														room.message("One or more cards that you requested for trade are not in your hand.")
												elif (sc3 in oldcard5):
													if (sc4 in oldcard2):
														if (sc5 in oldcard4):
															falsetrade = 0
														else:
															falsetrade = 1
															room.message("One or more cards that you requested for trade are not in your hand.")
													elif (sc4 in oldcard4):
														if (sc5 in oldcard2):
															falsetrade = 0
														else:
															falsetrade = 1
															room.message("One or more cards that you requested for trade are not in your hand.")
													else:
														falsetrade = 1
														room.message("One or more cards that you requested for trade are not in your hand.")
												else:
													falsetrade = 1
													room.message("One or more cards that you requested for trade are not in your hand.")
											elif (sc2 in oldcard4):
												if (sc3 in oldcard2):
													if (sc4 in oldcard3):
														if (sc5 in oldcard5):
															falsetrade = 0
														else:
															falsetrade = 1
															room.message("One or more cards that you requested for trade are not in your hand.")
													elif (sc4 in oldcard5):
														if (sc5 in oldcard3):
															falsetrade = 0
														else:
															falsetrade = 1
															room.message("One or more cards that you requested for trade are not in your hand.")
													else:
														falsetrade = 1
														room.message("One or more cards that you requested for trade are not in your hand.")
												elif (sc3 in oldcard3):
													if (sc4 in oldcard2):
														if (sc5 in oldcard5):
															falsetrade = 0
														else:
															falsetrade = 1
															room.message("One or more cards that you requested for trade are not in your hand.")
													elif (sc4 in oldcard5):
														if (sc5 in oldcard2):
															falsetrade = 0

														else:
															falsetrade = 1
															room.message("One or more cards that you requested for trade are not in your hand.")
													else:
														falsetrade = 1
														room.message("One or more cards that you requested for trade are not in your hand.")
												elif (sc3 in oldcard5):
													if (sc4 in oldcard2):
														if (sc5 in oldcard2):
															falsetrade = 0
														else:
															falsetrade = 1
															room.message("One or more cards that you requested for trade are not in your hand.")
													elif (sc4 in oldcard3):
														if (sc5 in oldcard3):
															falsetrade = 0
														else:
															falsetrade = 1
															room.message("One or more cards that you requested for trade are not in your hand.")
													else:
														falsetrade = 1
														room.message("One or more cards that you requested for trade are not in your hand.")
												else:
													falsetrade = 1
													room.message("One or more cards that you requested for trade are not in your hand.")
											elif (sc2 in oldcard5):
												if (sc3 in oldcard2):
													if (sc4 in oldcard3):
														if (sc5 in oldcard4):
															falsetrade = 0
														else:
															falsetrade = 1
															room.message("One or more cards that you requested for trade are not in your hand.")
													elif (sc4 in oldcard4):
														if (sc5 in oldcard3):
															falsetrade = 0
														else:
															falsetrade = 1
															room.message("One or more cards that you requested for trade are not in your hand.")
													else:
														falsetrade = 1
														room.message("One or more cards that you requested for trade are not in your hand.")
												elif (sc3 in oldcard3):
													if (sc4 in oldcard2):
														if (sc5 in oldcard4):
															falsetrade = 0
														else:
															falsetrade = 1
															room.message("One or more cards that you requested for trade are not in your hand.")
													elif (sc4 in oldcard4):
														if (sc5 in oldcard2):
															falsetrade = 0
														else:
															falsetrade = 1
															room.message("One or more cards that you requested for trade are not in your hand.")
													else:
														falsetrade = 1
														room.message("One or more cards that you requested for trade are not in your hand.")
												elif (sc3 in oldcard4):
													if (sc4 in oldcard2):
														if (sc5 in oldcard3):
															falsetrade = 0
														else:
															falsetrade = 1
															room.message("One or more cards that you requested for trade are not in your hand.")
													elif (sc4 in oldcard3):
														if (sc5 in oldcard2):
															falsetrade = 0
														else:
															falsetrade = 1
															room.message("One or more cards that you requested for trade are not in your hand.")
													else:
														falsetrade = 1
														room.message("One or more cards that you requested for trade are not in your hand.")
												else:
													falsetrade = 1
													room.message("One or more cards that you requested for trade are not in your hand.")
											else:
												falsetrade = 1
												room.message("One or more cards that you requested for trade are not in your hand.")
										elif (sc1 in oldcard2):
											if (sc2 in oldcard1):
												if (sc3 in oldcard3):
													if (sc4 in oldcard4):
														if (sc5 in oldcard5):
															falsetrade = 0
														else:
															falsetrade = 1
															room.message("One or more cards that you requested for trade are not in your hand.")
													elif (sc4 in oldcard5):
														if (sc5 in oldcard4):
															falsetrade = 0
														else:
															falsetrade = 1
															room.message("One or more cards that you requested for trade are not in your hand.")
													else:
														falsetrade = 1
														room.message("One or more cards that you requested for trade are not in your hand.")
												elif (sc3 in oldcard4):
													if (sc4 in oldcard3):
														if (sc5 in oldcard5):
															falsetrade = 0
														else:
															falsetrade = 1
															room.message("One or more cards that you requested for trade are not in your hand.")
													elif (sc4 in oldcard5):
														if (sc5 in oldcard3):
															falsetrade = 0
														else:
															falsetrade = 1
															room.message("One or more cards that you requested for trade are not in your hand.")
													else:
														falsetrade = 1
														room.message("One or more cards that you requested for trade are not in your hand.")
												elif (sc3 in oldcard5):
													if (sc4 in oldcard3):
														if (sc5 in oldcard4):
															falsetrade = 0
														else:
															falsetrade = 1
															room.message("One or more cards that you requested for trade are not in your hand.")
													elif (sc4 in oldcard4):
														if (sc5 in oldcard3):
															falsetrade = 0
														else:
															falsetrade = 1
															room.message("One or more cards that you requested for trade are not in your hand.")
													else:
														falsetrade = 1
														room.message("One or more cards that you requested for trade are not in your hand.")
												else:
													falsetrade = 1
													room.message("One or more cards that you requested for trade are not in your hand.")
											elif (sc2 in oldcard3):
												if (sc3 in oldcard1):
													if (sc4 in oldcard4):
														if (sc5 in oldcard5):
															falsetrade = 0
														else:
															falsetrade = 1
															room.message("One or more cards that you requested for trade are not in your hand.")
													elif (sc4 in oldcard5):
														if (sc5 in oldcard4):
															falsetrade = 0
														else:
															falsetrade = 1
															room.message("One or more cards that you requested for trade are not in your hand.")
													else:
														falsetrade = 1
														room.message("One or more cards that you requested for trade are not in your hand.")
												elif (sc3 in oldcard4):
													if (sc4 in oldcard1):
														if (sc5 in oldcard5):
															falsetrade = 0
														else:
															falsetrade = 1
															room.message("One or more cards that you requested for trade are not in your hand.")
													elif (sc4 in oldcard5):
														if (sc5 in oldcard1):
															falsetrade = 0
														else:
															falsetrade = 1
															room.message("One or more cards that you requested for trade are not in your hand.")
													else:
														falsetrade = 1
														room.message("One or more cards that you requested for trade are not in your hand.")
												elif (sc3 in oldcard5):
													if (sc4 in oldcard1):
														if (sc5 in oldcard4):
															falsetrade = 0
														else:
															falsetrade = 1
															room.message("One or more cards that you requested for trade are not in your hand.")
													elif (sc4 in oldcard4):
														if (sc5 in oldcard1):
															falsetrade = 0
														else:
															falsetrade = 1
															room.message("One or more cards that you requested for trade are not in your hand.")
													else:
														falsetrade = 1
														room.message("One or more cards that you requested for trade are not in your hand.")
												else:
													falsetrade = 1
													room.message("One or more cards that you requested for trade are not in your hand.")
											elif (sc2 in oldcard4):
												if (sc3 in oldcard1):
													if (sc4 in oldcard3):
														if (sc5 in oldcard5):
															falsetrade = 0
														else:
															falsetrade = 1
															room.message("One or more cards that you requested for trade are not in your hand.")
													elif (sc4 in oldcard5):
														if (sc5 in oldcard3):
															falsetrade = 0
														else:
															falsetrade = 1
															room.message("One or more cards that you requested for trade are not in your hand.")
													else:
														falsetrade = 1
														room.message("One or more cards that you requested for trade are not in your hand.")
												elif (sc3 in oldcard3):
													if (sc4 in oldcard1):
														if (sc5 in oldcard5):
															falsetrade = 0
														else:
															falsetrade = 1
															room.message("One or more cards that you requested for trade are not in your hand.")
													elif (sc4 in oldcard5):
														if (sc5 in oldcard1):
															falsetrade = 0
														else:
															falsetrade = 1
															room.message("One or more cards that you requested for trade are not in your hand.")
													else:
														falsetrade = 1
														room.message("One or more cards that you requested for trade are not in your hand.")
												elif (sc3 in oldcard5):
													if (sc4 in oldcard1):
														if (sc5 in oldcard3):
															falsetrade = 0
														else:
															falsetrade = 1
															room.message("One or more cards that you requested for trade are not in your hand.")
													elif (sc4 in oldcard3):
														if (sc5 in oldcard1):
															falsetrade = 0
														else:
															falsetrade = 1
															room.message("One or more cards that you requested for trade are not in your hand.")
													else:
														falsetrade = 1
														room.message("One or more cards that you requested for trade are not in your hand.")
												else:
													falsetrade = 1
													room.message("One or more cards that you requested for trade are not in your hand.")
											elif (sc2 in oldcard5):
												if (sc3 in oldcard1):
													if (sc4 in oldcard3):
														if (sc5 in oldcard4):
															falsetrade = 0
														else:
															falsetrade = 1
															room.message("One or more cards that you requested for trade are not in your hand.")
													elif (sc4 in oldcard4):
														if (sc5 in oldcard3):
															falsetrade = 0
														else:
															falsetrade = 1
															room.message("One or more cards that you requested for trade are not in your hand.")
													else:
														falsetrade = 1
														room.message("One or more cards that you requested for trade are not in your hand.")
												elif (sc3 in oldcard3):
													if (sc4 in oldcard1):
														if (sc5 in oldcard4):
															falsetrade = 0
														else:
															falsetrade = 1
															room.message("One or more cards that you requested for trade are not in your hand.")
													elif (sc4 in oldcard4):
														if (sc5 in oldcard1):
															falsetrade = 0
														else:
															falsetrade = 1
															room.message("One or more cards that you requested for trade are not in your hand.")
													else:
														falsetrade = 1
														room.message("One or more cards that you requested for trade are not in your hand.")
												elif (sc3 in oldcard4):
													if (sc4 in oldcard1):
														if (sc5 in oldcard3):
															falsetrade = 0
														else:
															falsetrade = 1
															room.message("One or more cards that you requested for trade are not in your hand.")
													elif (sc4 in oldcard3):
														if (sc5 in oldcard1):
															falsetrade = 0
														else:
															falsetrade = 1
															room.message("One or more cards that you requested for trade are not in your hand.")
													else:
														falsetrade = 1
														room.message("One or more cards that you requested for trade are not in your hand.")
												else:
													falsetrade = 1
													room.message("One or more cards that you requested for trade are not in your hand.")
											else:
												falsetrade = 1
												room.message("One or more cards that you requested for trade are not in your hand.")
										elif (sc1 in oldcard3):
											if (sc2 in oldcard1):
												if (sc3 in oldcard2):
													if (sc4 in oldcard4):
														if (sc5 in oldcard5):
															falsetrade = 0
														else:
															falsetrade = 1
															room.message("One or more cards that you requested for trade are not in your hand.")
													elif (sc4 in oldcard5):
														if (sc5 in oldcard4):
															falsetrade = 0
														else:
															falsetrade = 1
															room.message("One or more cards that you requested for trade are not in your hand.")
													else:
														falsetrade = 1
														room.message("One or more cards that you requested for trade are not in your hand.")
												elif (sc3 in oldcard4):
													if (sc4 in oldcard2):
														if (sc5 in oldcard5):
															falsetrade = 0
														else:
															falsetrade = 1
															room.message("One or more cards that you requested for trade are not in your hand.")
													elif (sc4 in oldcard5):
														if (sc5 in oldcard2):
															falsetrade = 0
														else:
															falsetrade = 1
															room.message("One or more cards that you requested for trade are not in your hand.")
													else:
														falsetrade = 1
														room.message("One or more cards that you requested for trade are not in your hand.")
												elif (sc3 in oldcard5):
													if (sc4 in oldcard2):
														if (sc5 in oldcard4):
															falsetrade = 0
														else:
															falsetrade = 1
															room.message("One or more cards that you requested for trade are not in your hand.")
													elif (sc4 in oldcard4):
														if (sc5 in oldcard2):
															falsetrade = 0
														else:
															falsetrade = 1
															room.message("One or more cards that you requested for trade are not in your hand.")
													else:
														falsetrade = 1
														room.message("One or more cards that you requested for trade are not in your hand.")
												else:
													falsetrade = 1
													room.message("One or more cards that you requested for trade are not in your hand.")
											elif (sc2 in oldcard2):
												if (sc3 in oldcard1):
													if (sc4 in oldcard4):
														if (sc5 in oldcard5):
															falsetrade = 0
														else:
															falsetrade = 1
															room.message("One or more cards that you requested for trade are not in your hand.")
													elif (sc4 in oldcard5):
														if (sc5 in oldcard4):
															falsetrade = 0
														else:
															falsetrade = 1
															room.message("One or more cards that you requested for trade are not in your hand.")
													else:
														falsetrade = 1
														room.message("One or more cards that you requested for trade are not in your hand.")
												elif (sc3 in oldcard4):
													if (sc4 in oldcard1):
														if (sc5 in oldcard5):
															falsetrade = 0
														else:
															falsetrade = 1
															room.message("One or more cards that you requested for trade are not in your hand.")
													elif (sc4 in oldcard5):
														if (sc5 in oldcard1):
															falsetrade = 0

														else:
															falsetrade = 1
															room.message("One or more cards that you requested for trade are not in your hand.")
													else:
														falsetrade = 1
														room.message("One or more cards that you requested for trade are not in your hand.")
												elif (sc3 in oldcard5):
													if (sc4 in oldcard1):
														if (sc5 in oldcard4):
															falsetrade = 0
														else:
															falsetrade = 1
															room.message("One or more cards that you requested for trade are not in your hand.")
													elif (sc4 in oldcard4):
														if (sc5 in oldcard1):
															falsetrade = 0
														else:
															falsetrade = 1
															room.message("One or more cards that you requested for trade are not in your hand.")
													else:
														falsetrade = 1
														room.message("One or more cards that you requested for trade are not in your hand.")
												else:
													falsetrade = 1
													room.message("One or more cards that you requested for trade are not in your hand.")
											elif (sc2 in oldcard4):
												if (sc3 in oldcard1):
													if (sc4 in oldcard2):
														if (sc5 in oldcard5):
															falsetrade = 0
														else:
															falsetrade = 1
															room.message("One or more cards that you requested for trade are not in your hand.")
													elif (sc4 in oldcard5):
														if (sc5 in oldcard2):
															falsetrade = 0
														else:
															falsetrade = 1
															room.message("One or more cards that you requested for trade are not in your hand.")
													else:
														falsetrade = 1
														room.message("One or more cards that you requested for trade are not in your hand.")
												elif (sc3 in oldcard2):
													if (sc4 in oldcard1):
														if (sc5 in oldcard5):
															falsetrade = 0
														else:
															falsetrade = 1
															room.message("One or more cards that you requested for trade are not in your hand.")
													elif (sc4 in oldcard5):
														if (sc5 in oldcard1):
															falsetrade = 0
														else:
															falsetrade = 1
															room.message("One or more cards that you requested for trade are not in your hand.")
													else:
														falsetrade = 1
														room.message("One or more cards that you requested for trade are not in your hand.")
												elif (sc3 in oldcard5):
													if (sc4 in oldcard1):
														if (sc5 in oldcard2):
															falsetrade = 0
														else:
															falsetrade = 1
															room.message("One or more cards that you requested for trade are not in your hand.")
													elif (sc4 in oldcard2):
														if (sc5 in oldcard1):
															falsetrade = 0
														else:
															falsetrade = 1
															room.message("One or more cards that you requested for trade are not in your hand.")
													else:
														falsetrade = 1
														room.message("One or more cards that you requested for trade are not in your hand.")
												else:
													falsetrade = 1
													room.message("One or more cards that you requested for trade are not in your hand.")
											elif (sc2 in oldcard5):
												if (sc3 in oldcard1):
													if (sc4 in oldcard2):
														if (sc5 in oldcard4):
															falsetrade = 0
														else:
															falsetrade = 1
															room.message("One or more cards that you requested for trade are not in your hand.")
													elif (sc4 in oldcard4):
														if (sc5 in oldcard2):
															falsetrade = 0
														else:
															falsetrade = 1
															room.message("One or more cards that you requested for trade are not in your hand.")
													else:
														falsetrade = 1
														room.message("One or more cards that you requested for trade are not in your hand.")
												elif (sc3 in oldcard2):
													if (sc4 in oldcard1):
														if (sc5 in oldcard4):
															falsetrade = 0
														else:
															falsetrade = 1
															room.message("One or more cards that you requested for trade are not in your hand.")
													elif (sc4 in oldcard4):
														if (sc5 in oldcard1):
															falsetrade = 0
														else:
															falsetrade = 1
															room.message("One or more cards that you requested for trade are not in your hand.")
													else:
														falsetrade = 1
														room.message("One or more cards that you requested for trade are not in your hand.")
												elif (sc3 in oldcard4):
													if (sc4 in oldcard1):
														if (sc5 in oldcard2):
															falsetrade = 0
														else:
															falsetrade = 1
															room.message("One or more cards that you requested for trade are not in your hand.")
													elif (sc4 in oldcard2):
														if (sc5 in oldcard1):
															falsetrade = 0
														else:
															falsetrade = 1
															room.message("One or more cards that you requested for trade are not in your hand.")
													else:
														falsetrade = 1
														room.message("One or more cards that you requested for trade are not in your hand.")
												else:
													falsetrade = 1
													room.message("One or more cards that you requested for trade are not in your hand.")
											else:
												falsetrade = 1
												room.message("One or more cards that you requested for trade are not in your hand.")
										elif (sc1 in oldcard4):
											if (sc2 in oldcard1):
												if (sc3 in oldcard2):
													if (sc4 in oldcard3):
														if (sc5 in oldcard5):
															falsetrade = 0
														else:
															falsetrade = 1
															room.message("One or more cards that you requested for trade are not in your hand.")
													elif (sc4 in oldcard5):
														if (sc5 in oldcard3):
															falsetrade = 0
														else:
															falsetrade = 1
															room.message("One or more cards that you requested for trade are not in your hand.")
													else:
														falsetrade = 1
														room.message("One or more cards that you requested for trade are not in your hand.")
												elif (sc3 in oldcard3):
													if (sc4 in oldcard2):
														if (sc5 in oldcard5):
															falsetrade = 0
														else:
															falsetrade = 1
															room.message("One or more cards that you requested for trade are not in your hand.")
													elif (sc4 in oldcard5):
														if (sc5 in oldcard2):
															falsetrade = 0
														else:
															falsetrade = 1
															room.message("One or more cards that you requested for trade are not in your hand.")
													else:
														falsetrade = 1
														room.message("One or more cards that you requested for trade are not in your hand.")
												elif (sc3 in oldcard5):
													if (sc4 in oldcard2):
														if (sc5 in oldcard3):
															falsetrade = 0
														else:
															falsetrade = 1
															room.message("One or more cards that you requested for trade are not in your hand.")
													elif (sc4 in oldcard3):
														if (sc5 in oldcard2):
															falsetrade = 0
														else:
															falsetrade = 1
															room.message("One or more cards that you requested for trade are not in your hand.")
													else:
														falsetrade = 1
														room.message("One or more cards that you requested for trade are not in your hand.")
												else:
													falsetrade = 1
													room.message("One or more cards that you requested for trade are not in your hand.")
											elif (sc2 in oldcard2):
												if (sc3 in oldcard1):
													if (sc4 in oldcard3):
														if (sc5 in oldcard5):
															falsetrade = 0
														else:
															falsetrade = 1
															room.message("One or more cards that you requested for trade are not in your hand.")
													elif (sc4 in oldcard5):
														if (sc5 in oldcard3):
															falsetrade = 0
														else:
															falsetrade = 1
															room.message("One or more cards that you requested for trade are not in your hand.")
													else:
														falsetrade = 1
														room.message("One or more cards that you requested for trade are not in your hand.")
												elif (sc3 in oldcard3):
													if (sc4 in oldcard1):
														if (sc5 in oldcard5):
															falsetrade = 0
														else:
															falsetrade = 1
															room.message("One or more cards that you requested for trade are not in your hand.")
													elif (sc4 in oldcard5):
														if (sc5 in oldcard1):
															falsetrade = 0
														else:
															falsetrade = 1
															room.message("One or more cards that you requested for trade are not in your hand.")
													else:
														falsetrade = 1
														room.message("One or more cards that you requested for trade are not in your hand.")
												elif (sc3 in oldcard5):
													if (sc4 in oldcard1):
														if (sc5 in oldcard3):
															falsetrade = 0
														else:
															falsetrade = 1
															room.message("One or more cards that you requested for trade are not in your hand.")
													elif (sc4 in oldcard3):
														if (sc5 in oldcard1):
															falsetrade = 0
														else:
															falsetrade = 1
															room.message("One or more cards that you requested for trade are not in your hand.")
													else:
														falsetrade = 1
														room.message("One or more cards that you requested for trade are not in your hand.")
												else:
													falsetrade = 1
													room.message("One or more cards that you requested for trade are not in your hand.")
											elif (sc2 in oldcard3):
												if (sc3 in oldcard1):
													if (sc4 in oldcard2):
														if (sc5 in oldcard5):
															falsetrade = 0
														else:
															falsetrade = 1
															room.message("One or more cards that you requested for trade are not in your hand.")
													elif (sc4 in oldcard5):
														if (sc5 in oldcard2):
															falsetrade = 0
														else:
															falsetrade = 1
															room.message("One or more cards that you requested for trade are not in your hand.")
													else:
														falsetrade = 1
														room.message("One or more cards that you requested for trade are not in your hand.")
												elif (sc3 in oldcard2):
													if (sc4 in oldcard1):
														if (sc5 in oldcard5):
															falsetrade = 0
														else:
															falsetrade = 1
															room.message("One or more cards that you requested for trade are not in your hand.")
													elif (sc4 in oldcard5):
														if (sc5 in oldcard1):
															falsetrade = 0
														else:
															falsetrade = 1
															room.message("One or more cards that you requested for trade are not in your hand.")
													else:
														falsetrade = 1
														room.message("One or more cards that you requested for trade are not in your hand.")
												elif (sc3 in oldcard5):
													if (sc4 in oldcard1):
														if (sc5 in oldcard2):
															falsetrade = 0
														else:
															falsetrade = 1
															room.message("One or more cards that you requested for trade are not in your hand.")
													elif (sc4 in oldcard2):
														if (sc5 in oldcard1):
															falsetrade = 0
														else:
															falsetrade = 1
															room.message("One or more cards that you requested for trade are not in your hand.")
													else:
														falsetrade = 1
														room.message("One or more cards that you requested for trade are not in your hand.")
												else:
													falsetrade = 1
													room.message("One or more cards that you requested for trade are not in your hand.")
											elif (sc2 in oldcard5):
												if (sc3 in oldcard1):
													if (sc4 in oldcard2):
														if (sc5 in oldcard3):
															falsetrade = 0
														else:
															falsetrade = 1
															room.message("One or more cards that you requested for trade are not in your hand.")
													elif (sc4 in oldcard3):
														if (sc5 in oldcard2):
															falsetrade = 0
														else:
															falsetrade = 1
															room.message("One or more cards that you requested for trade are not in your hand.")
													else:
														falsetrade = 1
														room.message("One or more cards that you requested for trade are not in your hand.")
												elif (sc3 in oldcard2):
													if (sc4 in oldcard1):
														if (sc5 in oldcard3):
															falsetrade = 0
														else:
															falsetrade = 1
															room.message("One or more cards that you requested for trade are not in your hand.")
													elif (sc4 in oldcard3):
														if (sc5 in oldcard1):
															falsetrade = 0
														else:
															falsetrade = 1
															room.message("One or more cards that you requested for trade are not in your hand.")
													else:
														falsetrade = 1
														room.message("One or more cards that you requested for trade are not in your hand.")
												elif (sc3 in oldcard3):
													if (sc4 in oldcard1):
														if (sc5 in oldcard2):
															falsetrade = 0
														else:
															falsetrade = 1
															room.message("One or more cards that you requested for trade are not in your hand.")
													elif (sc4 in oldcard2):
														if (sc5 in oldcard1):
															falsetrade = 0
														else:
															falsetrade = 1
															room.message("One or more cards that you requested for trade are not in your hand.")
													else:
														falsetrade = 1
														room.message("One or more cards that you requested for trade are not in your hand.")
												else:
													falsetrade = 1
													room.message("One or more cards that you requested for trade are not in your hand.")
											else:
												falsetrade = 1
												room.message("One or more cards that you requested for trade are not in your hand.")
										elif (sc1 in oldcard5):
											if (sc2 in oldcard1):
												if (sc3 in oldcard2):
													if (sc4 in oldcard3):
														if (sc5 in oldcard4):
															falsetrade = 0
														else:
															falsetrade = 1
															room.message("One or more cards that you requested for trade are not in your hand.")
													elif (sc4 in oldcard4):
														if (sc5 in oldcard3):
															falsetrade = 0
														else:
															falsetrade = 1
															room.message("One or more cards that you requested for trade are not in your hand.")
													else:
														falsetrade = 1
														room.message("One or more cards that you requested for trade are not in your hand.")
												elif (sc3 in oldcard3):
													if (sc4 in oldcard2):
														if (sc5 in oldcard4):
															falsetrade = 0
														else:
															falsetrade = 1
															room.message("One or more cards that you requested for trade are not in your hand.")
													elif (sc4 in oldcard4):
														if (sc5 in oldcard2):
															falsetrade = 0

														else:
															falsetrade = 1
															room.message("One or more cards that you requested for trade are not in your hand.")
													else:
														falsetrade = 1
														room.message("One or more cards that you requested for trade are not in your hand.")
												elif (sc3 in oldcard4):
													if (sc4 in oldcard2):
														if (sc5 in oldcard3):
															falsetrade = 0
														else:
															falsetrade = 1
															room.message("One or more cards that you requested for trade are not in your hand.")
													elif (sc4 in oldcard3):
														if (sc5 in oldcard2):
															falsetrade = 0
														else:
															falsetrade = 1
															room.message("One or more cards that you requested for trade are not in your hand.")
													else:
														falsetrade = 1
														room.message("One or more cards that you requested for trade are not in your hand.")
												else:
													falsetrade = 1
													room.message("One or more cards that you requested for trade are not in your hand.")
											elif (sc2 in oldcard2):
												if (sc3 in oldcard1):
													if (sc4 in oldcard3):
														if (sc5 in oldcard4):
															falsetrade = 0
														else:
															falsetrade = 1
															room.message("One or more cards that you requested for trade are not in your hand.")
													elif (sc4 in oldcard4):
														if (sc5 in oldcard3):
															falsetrade = 0
														else:
															falsetrade = 1
															room.message("One or more cards that you requested for trade are not in your hand.")
													else:
														falsetrade = 1
														room.message("One or more cards that you requested for trade are not in your hand.")
												elif (sc3 in oldcard3):
													if (sc4 in oldcard1):
														if (sc5 in oldcard4):
															falsetrade = 0
														else:
															falsetrade = 1
															room.message("One or more cards that you requested for trade are not in your hand.")
													elif (sc4 in oldcard4):
														if (sc5 in oldcard1):
															falsetrade = 0
														else:
															falsetrade = 1
															room.message("One or more cards that you requested for trade are not in your hand.")
													else:
														falsetrade = 1
														room.message("One or more cards that you requested for trade are not in your hand.")
												elif (sc3 in oldcard4):
													if (sc4 in oldcard1):
														if (sc5 in oldcard3):
															falsetrade = 0
														else:
															falsetrade = 1
															room.message("One or more cards that you requested for trade are not in your hand.")
													elif (sc4 in oldcard3):
														if (sc5 in oldcard1):
															falsetrade = 0
														else:
															falsetrade = 1
															room.message("One or more cards that you requested for trade are not in your hand.")
													else:
														falsetrade = 1
														room.message("One or more cards that you requested for trade are not in your hand.")
												else:
													falsetrade = 1
													room.message("One or more cards that you requested for trade are not in your hand.")
											elif (sc2 in oldcard3):
												if (sc3 in oldcard1):
													if (sc4 in oldcard2):
														if (sc5 in oldcard4):
															falsetrade = 0
														else:
															falsetrade = 1
															room.message("One or more cards that you requested for trade are not in your hand.")
													elif (sc4 in oldcard4):
														if (sc5 in oldcard2):
															falsetrade = 0
														else:
															falsetrade = 1
															room.message("One or more cards that you requested for trade are not in your hand.")
													else:
														falsetrade = 1
														room.message("One or more cards that you requested for trade are not in your hand.")
												elif (sc3 in oldcard2):
													if (sc4 in oldcard1):
														if (sc5 in oldcard4):
															falsetrade = 0
														else:
															falsetrade = 1
															room.message("One or more cards that you requested for trade are not in your hand.")
													elif (sc4 in oldcard4):
														if (sc5 in oldcard1):
															falsetrade = 0
														else:
															falsetrade = 1
															room.message("One or more cards that you requested for trade are not in your hand.")
													else:
														falsetrade = 1
														room.message("One or more cards that you requested for trade are not in your hand.")
												elif (sc3 in oldcard4):
													if (sc4 in oldcard1):
														if (sc5 in oldcard2):
															falsetrade = 0
														else:
															falsetrade = 1
															room.message("One or more cards that you requested for trade are not in your hand.")
													elif (sc4 in oldcard2):
														if (sc5 in oldcard1):
															falsetrade = 0
														else:
															falsetrade = 1
															room.message("One or more cards that you requested for trade are not in your hand.")
													else:
														falsetrade = 1
														room.message("One or more cards that you requested for trade are not in your hand.")
												else:
													falsetrade = 1
													room.message("One or more cards that you requested for trade are not in your hand.")
											elif (sc2 in oldcard4):
												if (sc3 in oldcard1):
													if (sc4 in oldcard2):
														if (sc5 in oldcard3):
															falsetrade = 0
														else:
															falsetrade = 1
															room.message("One or more cards that you requested for trade are not in your hand.")
													elif (sc4 in oldcard3):
														if (sc5 in oldcard2):
															falsetrade = 0
														else:
															falsetrade = 1
															room.message("One or more cards that you requested for trade are not in your hand.")
													else:
														falsetrade = 1
														room.message("One or more cards that you requested for trade are not in your hand.")
												elif (sc3 in oldcard2):
													if (sc4 in oldcard1):
														if (sc5 in oldcard3):
															falsetrade = 0
														else:
															falsetrade = 1
															room.message("One or more cards that you requested for trade are not in your hand.")
													elif (sc4 in oldcard3):
														if (sc5 in oldcard1):
															falsetrade = 0
														else:
															falsetrade = 1
															room.message("One or more cards that you requested for trade are not in your hand.")
													else:
														falsetrade = 1
														room.message("One or more cards that you requested for trade are not in your hand.")
												elif (sc3 in oldcard3):
													if (sc4 in oldcard1):
														if (sc5 in oldcard2):
															falsetrade = 0
														else:
															falsetrade = 1
															room.message("One or more cards that you requested for trade are not in your hand.")
													elif (sc4 in oldcard2):
														if (sc5 in oldcard1):
															falsetrade = 0
														else:
															falsetrade = 1
															room.message("One or more cards that you requested for trade are not in your hand.")
													else:
														falsetrade = 1
														room.message("One or more cards that you requested for trade are not in your hand.")
												else:
													falsetrade = 1
													room.message("One or more cards that you requested for trade are not in your hand.")
											else:
												falsetrade = 1
												room.message("One or more cards that you requested for trade are not in your hand.")
										else:
											falsetrade = 1
											room.message("One or more cards that you requested for trade are not in your hand.")
									elif tradenum == 4:
										sc1 = switchcardsr2[0]
										sc2 = switchcardsr2[1]
										sc3 = switchcardsr2[2]
										sc4 = switchcardsr2[3]
										if (sc1 in oldcard1):
											if (sc2 in oldcard2):
												if (sc3 in oldcard3):
													if (sc4 in oldcard4):
														falsetrade = 0
													elif (sc4 in oldcard5):
														falsetrade = 0
													else:
														falsetrade = 1
														room.message("One or more cards that you requested for trade are not in your hand.")
												elif (sc3 in oldcard4):
													if (sc4 in oldcard3):
														falsetrade = 0
													elif (sc4 in oldcard5):
														falsetrade = 0
													else:
														falsetrade = 1
														room.message("One or more cards that you requested for trade are not in your hand.")
												elif (sc3 in oldcard5):
													if (sc4 in oldcard3):
														falsetrade = 0
													elif (sc4 in oldcard4):
														falsetrade = 0
													else:
														falsetrade = 1
														room.message("One or more cards that you requested for trade are not in your hand.")
												else:
													falsetrade = 1
													room.message("One or more cards that you requested for trade are not in your hand.")
											elif (sc2 in oldcard3):
												if (sc3 in oldcard2):
													if (sc4 in oldcard4):
														falsetrade = 0
													elif (sc4 in oldcard5):
														falsetrade = 0
													else:
														falsetrade = 1
														room.message("One or more cards that you requested for trade are not in your hand.")
												elif (sc3 in oldcard4):
													if (sc4 in oldcard2):
														falsetrade = 0
													elif (sc4 in oldcard5):
														falsetrade = 0
													else:
														falsetrade = 1
														room.message("One or more cards that you requested for trade are not in your hand.")
												elif (sc3 in oldcard5):
													if (sc4 in oldcard2):
														falsetrade = 0
													elif (sc4 in oldcard4):
														falsetrade = 0
													else:
														falsetrade = 1
														room.message("One or more cards that you requested for trade are not in your hand.")
												else:
													falsetrade = 1
													room.message("One or more cards that you requested for trade are not in your hand.")
											elif (sc2 in oldcard4):
												if (sc3 in oldcard2):
													if (sc4 in oldcard3):
														falsetrade = 0
													elif (sc4 in oldcard5):
														falsetrade = 0
													else:
														falsetrade = 1
														room.message("One or more cards that you requested for trade are not in your hand.")
												elif (sc3 in oldcard3):
													if (sc4 in oldcard2):
														falsetrade = 0
													elif (sc4 in oldcard5):
														falsetrade = 0
													else:
														falsetrade = 1
														room.message("One or more cards that you requested for trade are not in your hand.")
												elif (sc3 in oldcard5):
													if (sc4 in oldcard2):
														falsetrade = 0
													elif (sc4 in oldcard3):
														falsetrade = 0
													else:
														falsetrade = 1
														room.message("One or more cards that you requested for trade are not in your hand.")
												else:
													falsetrade = 1
													room.message("One or more cards that you requested for trade are not in your hand.")
											elif (sc2 in oldcard5):
												if (sc3 in oldcard2):
													if (sc4 in oldcard3):
														falsetrade = 0
													elif (sc4 in oldcard4):
														falsetrade = 0
													else:
														falsetrade = 1
														room.message("One or more cards that you requested for trade are not in your hand.")
												elif (sc3 in oldcard3):
													if (sc4 in oldcard2):
														falsetrade = 0
													elif (sc4 in oldcard4):
														falsetrade = 0
													else:
														falsetrade = 1
														room.message("One or more cards that you requested for trade are not in your hand.")
												elif (sc3 in oldcard4):
													if (sc4 in oldcard2):
														falsetrade = 0
													elif (sc4 in oldcard3):
														falsetrade = 0
													else:
														falsetrade = 1
														room.message("One or more cards that you requested for trade are not in your hand.")
												else:
													falsetrade = 1
													room.message("One or more cards that you requested for trade are not in your hand.")
											else:
												falsetrade = 1
												room.message("One or more cards that you requested for trade are not in your hand.")
										elif (sc1 in oldcard2):
											if (sc2 in oldcard1):
												if (sc3 in oldcard3):
													if (sc4 in oldcard4):
														falsetrade = 0
													elif (sc4 in oldcard5):
														falsetrade = 0
													else:
														falsetrade = 1
														room.message("One or more cards that you requested for trade are not in your hand.")
												elif (sc3 in oldcard4):
													if (sc4 in oldcard3):
														falsetrade = 0
													elif (sc4 in oldcard5):
														falsetrade = 0
													else:
														falsetrade = 1
														room.message("One or more cards that you requested for trade are not in your hand.")
												elif (sc3 in oldcard5):
													if (sc4 in oldcard3):
														falsetrade = 0
													elif (sc4 in oldcard4):
														falsetrade = 0
													else:
														falsetrade = 1
														room.message("One or more cards that you requested for trade are not in your hand.")
												else:
													falsetrade = 1
													room.message("One or more cards that you requested for trade are not in your hand.")
											elif (sc2 in oldcard3):
												if (sc3 in oldcard1):
													if (sc4 in oldcard4):
														falsetrade = 0
													elif (sc4 in oldcard5):
														falsetrade = 0
													else:
														falsetrade = 1
														room.message("One or more cards that you requested for trade are not in your hand.")
												elif (sc3 in oldcard4):
													if (sc4 in oldcard1):
														falsetrade = 0
													elif (sc4 in oldcard5):
														falsetrade = 0
													else:
														falsetrade = 1
														room.message("One or more cards that you requested for trade are not in your hand.")
												elif (sc3 in oldcard5):
													if (sc4 in oldcard1):
														falsetrade = 0
													elif (sc4 in oldcard4):
														falsetrade = 0
													else:
														falsetrade = 1
														room.message("One or more cards that you requested for trade are not in your hand.")
												else:
													falsetrade = 1
													room.message("One or more cards that you requested for trade are not in your hand.")
											elif (sc2 in oldcard4):
												if (sc3 in oldcard1):
													if (sc4 in oldcard3):
														falsetrade = 0
													elif (sc4 in oldcard5):
														falsetrade = 0
													else:
														falsetrade = 1
														room.message("One or more cards that you requested for trade are not in your hand.")
												elif (sc3 in oldcard3):
													if (sc4 in oldcard1):
														falsetrade = 0
													elif (sc4 in oldcard5):
														falsetrade = 0
													else:
														falsetrade = 1
														room.message("One or more cards that you requested for trade are not in your hand.")
												elif (sc3 in oldcard5):
													if (sc4 in oldcard1):
														falsetrade = 0
													elif (sc4 in oldcard3):
														falsetrade = 0
													else:
														falsetrade = 1
														room.message("One or more cards that you requested for trade are not in your hand.")
												else:
													falsetrade = 1
													room.message("One or more cards that you requested for trade are not in your hand.")
											elif (sc2 in oldcard5):
												if (sc3 in oldcard1):
													if (sc4 in oldcard3):
														falsetrade = 0
													elif (sc4 in oldcard4):
														falsetrade = 0
													else:
														falsetrade = 1
														room.message("One or more cards that you requested for trade are not in your hand.")
												elif (sc3 in oldcard3):
													if (sc4 in oldcard1):
														falsetrade = 0
													elif (sc4 in oldcard4):
														falsetrade = 0
													else:
														falsetrade = 1
														room.message("One or more cards that you requested for trade are not in your hand.")
												elif (sc3 in oldcard4):
													if (sc4 in oldcard1):
														falsetrade = 0
													elif (sc4 in oldcard3):
														falsetrade = 0
													else:
														falsetrade = 1
														room.message("One or more cards that you requested for trade are not in your hand.")
												else:
													falsetrade = 1
													room.message("One or more cards that you requested for trade are not in your hand.")
											else:
												falsetrade = 1
												room.message("One or more cards that you requested for trade are not in your hand.")
										elif (sc1 in oldcard3):
											if (sc2 in oldcard1):
												if (sc3 in oldcard2):
													if (sc4 in oldcard4):
														falsetrade = 0
													elif (sc4 in oldcard5):
														falsetrade = 0
													else:
														falsetrade = 1
														room.message("One or more cards that you requested for trade are not in your hand.")
												elif (sc3 in oldcard4):
													if (sc4 in oldcard2):
														falsetrade = 0
													elif (sc4 in oldcard5):
														falsetrade = 0
													else:
														falsetrade = 1
														room.message("One or more cards that you requested for trade are not in your hand.")
												elif (sc3 in oldcard5):
													if (sc4 in oldcard2):
														falsetrade = 0
													elif (sc4 in oldcard4):
														falsetrade = 0
													else:
														falsetrade = 1
														room.message("One or more cards that you requested for trade are not in your hand.")
												else:
													falsetrade = 1
													room.message("One or more cards that you requested for trade are not in your hand.")
											elif (sc2 in oldcard2):
												if (sc3 in oldcard1):
													if (sc4 in oldcard4):
														falsetrade = 0
													elif (sc4 in oldcard5):
														falsetrade = 0
													else:
														falsetrade = 1
														room.message("One or more cards that you requested for trade are not in your hand.")
												elif (sc3 in oldcard4):
													if (sc4 in oldcard1):
														falsetrade = 0
													elif (sc4 in oldcard5):
														falsetrade = 0
													else:
														falsetrade = 1
														room.message("One or more cards that you requested for trade are not in your hand.")
												elif (sc3 in oldcard5):
													if (sc4 in oldcard1):
														falsetrade = 0
													elif (sc4 in oldcard4):
														falsetrade = 0
													else:
														falsetrade = 1
														room.message("One or more cards that you requested for trade are not in your hand.")
												else:
													falsetrade = 1
													room.message("One or more cards that you requested for trade are not in your hand.")
											elif (sc2 in oldcard4):
												if (sc3 in oldcard1):
													if (sc4 in oldcard2):
														falsetrade = 0
													elif (sc4 in oldcard5):
														falsetrade = 0
													else:
														falsetrade = 1
														room.message("One or more cards that you requested for trade are not in your hand.")
												elif (sc3 in oldcard2):
													if (sc4 in oldcard1):
														falsetrade = 0
													elif (sc4 in oldcard5):
														falsetrade = 0
													else:
														falsetrade = 1
														room.message("One or more cards that you requested for trade are not in your hand.")
												elif (sc3 in oldcard5):
													if (sc4 in oldcard1):
														falsetrade = 0
													elif (sc4 in oldcard2):
														falsetrade = 0
													else:
														falsetrade = 1
														room.message("One or more cards that you requested for trade are not in your hand.")
												else:
													falsetrade = 1
													room.message("One or more cards that you requested for trade are not in your hand.")
											elif (sc2 in oldcard5):
												if (sc3 in oldcard1):
													if (sc4 in oldcard2):
														falsetrade = 0
													elif (sc4 in oldcard4):
														falsetrade = 0
													else:
														falsetrade = 1
														room.message("One or more cards that you requested for trade are not in your hand.")
												elif (sc3 in oldcard2):
													if (sc4 in oldcard1):
														falsetrade = 0
													elif (sc4 in oldcard4):
														falsetrade = 0
													else:
														falsetrade = 1
														room.message("One or more cards that you requested for trade are not in your hand.")
												elif (sc3 in oldcard4):
													if (sc4 in oldcard1):
														falsetrade = 0
													elif (sc4 in oldcard2):
														falsetrade = 0
													else:
														falsetrade = 1
														room.message("One or more cards that you requested for trade are not in your hand.")
												else:
													falsetrade = 1
													room.message("One or more cards that you requested for trade are not in your hand.")
											else:
												falsetrade = 1
												room.message("One or more cards that you requested for trade are not in your hand.")
										elif (sc1 in oldcard4):
											if (sc2 in oldcard1):
												if (sc3 in oldcard2):
													if (sc4 in oldcard3):
														falsetrade = 0
													elif (sc4 in oldcard5):
														falsetrade = 0
													else:
														falsetrade = 1
														room.message("One or more cards that you requested for trade are not in your hand.")
												elif (sc3 in oldcard3):
													if (sc4 in oldcard2):
														falsetrade = 0
													elif (sc4 in oldcard5):
														falsetrade = 0
													else:
														falsetrade = 1
														room.message("One or more cards that you requested for trade are not in your hand.")
												elif (sc3 in oldcard5):
													if (sc4 in oldcard2):
														falsetrade = 0
													elif (sc4 in oldcard3):
														falsetrade = 0
													else:
														falsetrade = 1
														room.message("One or more cards that you requested for trade are not in your hand.")
												else:
													falsetrade = 1
													room.message("One or more cards that you requested for trade are not in your hand.")
											elif (sc2 in oldcard2):
												if (sc3 in oldcard1):
													if (sc4 in oldcard3):
														falsetrade = 0
													elif (sc4 in oldcard5):
														falsetrade = 0
													else:
														falsetrade = 1
														room.message("One or more cards that you requested for trade are not in your hand.")
												elif (sc3 in oldcard3):
													if (sc4 in oldcard1):
														falsetrade = 0
													elif (sc4 in oldcard5):
														falsetrade = 0
													else:
														falsetrade = 1
														room.message("One or more cards that you requested for trade are not in your hand.")
												elif (sc3 in oldcard5):
													if (sc4 in oldcard1):
														falsetrade = 0
													elif (sc4 in oldcard3):
														falsetrade = 0
													else:
														falsetrade = 1
														room.message("One or more cards that you requested for trade are not in your hand.")
												else:
													falsetrade = 1
													room.message("One or more cards that you requested for trade are not in your hand.")
											elif (sc2 in oldcard3):
												if (sc3 in oldcard1):
													if (sc4 in oldcard2):
														falsetrade = 0
													elif (sc4 in oldcard5):
														falsetrade = 0
													else:
														falsetrade = 1
														room.message("One or more cards that you requested for trade are not in your hand.")
												elif (sc3 in oldcard2):
													if (sc4 in oldcard1):
														falsetrade = 0
													elif (sc4 in oldcard5):
														falsetrade = 0
													else:
														falsetrade = 1
														room.message("One or more cards that you requested for trade are not in your hand.")
												elif (sc3 in oldcard5):
													if (sc4 in oldcard1):
														falsetrade = 0
													elif (sc4 in oldcard2):
														falsetrade = 0
													else:
														falsetrade = 1
														room.message("One or more cards that you requested for trade are not in your hand.")
												else:
													falsetrade = 1
													room.message("One or more cards that you requested for trade are not in your hand.")
											elif (sc2 in oldcard5):
												if (sc3 in oldcard1):
													if (sc4 in oldcard2):
														falsetrade = 0
													elif (sc4 in oldcard3):
														falsetrade = 0
													else:
														falsetrade = 1
														room.message("One or more cards that you requested for trade are not in your hand.")
												elif (sc3 in oldcard2):
													if (sc4 in oldcard1):
														falsetrade = 0
													elif (sc4 in oldcard3):
														falsetrade = 0
													else:
														falsetrade = 1
														room.message("One or more cards that you requested for trade are not in your hand.")
												elif (sc3 in oldcard3):
													if (sc4 in oldcard1):
														falsetrade = 0
													elif (sc4 in oldcard2):
														falsetrade = 0
													else:
														falsetrade = 1
														room.message("One or more cards that you requested for trade are not in your hand.")
												else:
													falsetrade = 1
													room.message("One or more cards that you requested for trade are not in your hand.")
											else:
												falsetrade = 1
												room.message("One or more cards that you requested for trade are not in your hand.")
										elif (sc1 in oldcard5):
											if (sc2 in oldcard1):
												if (sc3 in oldcard2):
													if (sc4 in oldcard3):
														falsetrade = 0
													elif (sc4 in oldcard4):
														falsetrade = 0
													else:
														falsetrade = 1
														room.message("One or more cards that you requested for trade are not in your hand.")
												elif (sc3 in oldcard3):
													if (sc4 in oldcard2):
														falsetrade = 0
													elif (sc4 in oldcard4):
														falsetrade = 0
													else:
														falsetrade = 1
														room.message("One or more cards that you requested for trade are not in your hand.")
												elif (sc3 in oldcard4):
													if (sc4 in oldcard2):
														falsetrade = 0
													elif (sc4 in oldcard3):
														falsetrade = 0
													else:
														falsetrade = 1
														room.message("One or more cards that you requested for trade are not in your hand.")
												else:
													falsetrade = 1
													room.message("One or more cards that you requested for trade are not in your hand.")
											elif (sc2 in oldcard2):
												if (sc3 in oldcard1):
													if (sc4 in oldcard3):
														falsetrade = 0
													elif (sc4 in oldcard4):
														falsetrade = 0
													else:
														falsetrade = 1
														room.message("One or more cards that you requested for trade are not in your hand.")
												elif (sc3 in oldcard3):
													if (sc4 in oldcard1):
														falsetrade = 0
													elif (sc4 in oldcard4):
														falsetrade = 0
													else:
														falsetrade = 1
														room.message("One or more cards that you requested for trade are not in your hand.")
												elif (sc3 in oldcard4):
													if (sc4 in oldcard1):
														falsetrade = 0
													elif (sc4 in oldcard3):
														falsetrade = 0
													else:
														falsetrade = 1
														room.message("One or more cards that you requested for trade are not in your hand.")
												else:
													falsetrade = 1
													room.message("One or more cards that you requested for trade are not in your hand.")
											elif (sc2 in oldcard3):
												if (sc3 in oldcard1):
													if (sc4 in oldcard2):
														falsetrade = 0
													elif (sc4 in oldcard4):
														falsetrade = 0
													else:
														falsetrade = 1
														room.message("One or more cards that you requested for trade are not in your hand.")
												elif (sc3 in oldcard2):
													if (sc4 in oldcard1):
														falsetrade = 0
													elif (sc4 in oldcard4):
														falsetrade = 0
													else:
														falsetrade = 1
														room.message("One or more cards that you requested for trade are not in your hand.")
												elif (sc3 in oldcard4):
													if (sc4 in oldcard1):
														falsetrade = 0
													elif (sc4 in oldcard2):
														falsetrade = 0
													else:
														falsetrade = 1
														room.message("One or more cards that you requested for trade are not in your hand.")
												else:
													falsetrade = 1
													room.message("One or more cards that you requested for trade are not in your hand.")
											elif (sc2 in oldcard4):
												if (sc3 in oldcard1):
													if (sc4 in oldcard2):
														falsetrade = 0
													elif (sc4 in oldcard3):
														falsetrade = 0
													else:
														falsetrade = 1
														room.message("One or more cards that you requested for trade are not in your hand.")
												elif (sc3 in oldcard2):
													if (sc4 in oldcard1):
														falsetrade = 0
													elif (sc4 in oldcard3):
														falsetrade = 0
													else:
														falsetrade = 1
														room.message("One or more cards that you requested for trade are not in your hand.")
												elif (sc3 in oldcard3):
													if (sc4 in oldcard1):
														falsetrade = 0
													elif (sc4 in oldcard2):
														falsetrade = 0
													else:
														falsetrade = 1
														room.message("One or more cards that you requested for trade are not in your hand.")
												else:
													falsetrade = 1
													room.message("One or more cards that you requested for trade are not in your hand.")
											else:
												falsetrade = 1
												room.message("One or more cards that you requested for trade are not in your hand.")
										else:
											falsetrade = 1
											room.message("One or more cards that you requested for trade are not in your hand.")
									elif tradenum == 3:
										sc1 = switchcardsr2[0]
										sc2 = switchcardsr2[1]
										sc3 = switchcardsr2[2]
										if (sc1 in oldcard1):
											if (sc2 in oldcard2):
												if (sc3 in oldcard3):
													falsetrade = 0
												elif (sc3 in oldcard4):
													falsetrade = 0
												elif (sc3 in oldcard5):
													falsetrade = 0
												else:
													falsetrade = 1
													room.message("One or more cards that you requested for trade are not in your hand.")
											elif (sc2 in oldcard3):
												if (sc3 in oldcard2):
													falsetrade = 0
												elif (sc3 in oldcard4):
													falsetrade = 0
												elif (sc3 in oldcard5):
													falsetrade = 0
												else:
													falsetrade = 1
													room.message("One or more cards that you requested for trade are not in your hand.")
											elif (sc2 in oldcard4):
												if (sc3 in oldcard2):
													falsetrade = 0
												elif (sc3 in oldcard3):
													falsetrade = 0
												elif (sc3 in oldcard5):
													falsetrade = 0
												else:
													falsetrade = 1
													room.message("One or more cards that you requested for trade are not in your hand.")
											elif (sc2 in oldcard5):
												if (sc3 in oldcard2):
													falsetrade = 0
												elif (sc3 in oldcard3):
													falsetrade = 0
												elif (sc3 in oldcard4):
													falsetrade = 0
												else:
													falsetrade = 1
													room.message("One or more cards that you requested for trade are not in your hand.")
											else:
												falsetrade = 1
												room.message("One or more cards that you requested for trade are not in your hand.")
										elif (sc1 in oldcard2):
											if (sc2 in oldcard1):
												if (sc3 in oldcard3):
													falsetrade = 0
												elif (sc3 in oldcard4):
													falsetrade = 0
												elif (sc3 in oldcard5):
													falsetrade = 0
												else:
													falsetrade = 1
													room.message("One or more cards that you requested for trade are not in your hand.")
											elif (sc2 in oldcard3):
												if (sc3 in oldcard1):
													falsetrade = 0
												elif (sc3 in oldcard4):
													falsetrade = 0
												elif (sc3 in oldcard5):
													falsetrade = 0
												else:
													falsetrade = 1
													room.message("One or more cards that you requested for trade are not in your hand.")
											elif (sc2 in oldcard4):
												if (sc3 in oldcard1):
													falsetrade = 0
												elif (sc3 in oldcard3):
													falsetrade = 0
												elif (sc3 in oldcard5):
													falsetrade = 0
												else:
													falsetrade = 1
													room.message("One or more cards that you requested for trade are not in your hand.")
											elif (sc2 in oldcard5):
												if (sc3 in oldcard1):
													falsetrade = 0
												elif (sc3 in oldcard3):
													falsetrade = 0
												elif (sc3 in oldcard4):
													falsetrade = 0
												else:
													falsetrade = 1
													room.message("One or more cards that you requested for trade are not in your hand.")
											else:
												falsetrade = 1
												room.message("One or more cards that you requested for trade are not in your hand.")
										elif (sc1 in oldcard3):
											if (sc2 in oldcard1):
												if (sc3 in oldcard2):
													falsetrade = 0
												elif (sc3 in oldcard4):
													falsetrade = 0
												elif (sc3 in oldcard5):
													falsetrade = 0
												else:
													falsetrade = 1
													room.message("One or more cards that you requested for trade are not in your hand.")
											elif (sc2 in oldcard2):
												if (sc3 in oldcard1):
													falsetrade = 0
												elif (sc3 in oldcard4):
														falsetrade = 0
												elif (sc3 in oldcard5):
													falsetrade = 0
												else:
													falsetrade = 1
													room.message("One or more cards that you requested for trade are not in your hand.")
											elif (sc2 in oldcard4):
												if (sc3 in oldcard1):
													falsetrade = 0
												elif (sc3 in oldcard2):
													falsetrade = 0
												elif (sc3 in oldcard5):
													falsetrade = 0
												else:
													falsetrade = 1
													room.message("One or more cards that you requested for trade are not in your hand.")
											elif (sc2 in oldcard5):
												if (sc3 in oldcard1):
													falsetrade = 0
												elif (sc3 in oldcard2):
													falsetrade = 0
												elif (sc3 in oldcard4):
													falsetrade = 0
												else:
													falsetrade = 1
													room.message("One or more cards that you requested for trade are not in your hand.")
											else:
												falsetrade = 1
												room.message("One or more cards that you requested for trade are not in your hand.")
										elif (sc1 in oldcard4):
											if (sc2 in oldcard1):
												if (sc3 in oldcard2):
													falsetrade = 0
												elif (sc3 in oldcard3):
													falsetrade = 0
												elif (sc3 in oldcard5):
													falsetrade = 0
												else:
													falsetrade = 1
													room.message("One or more cards that you requested for trade are not in your hand.")
											elif (sc2 in oldcard2):
												if (sc3 in oldcard1):
													falsetrade = 0
												elif (sc3 in oldcard3):
													falsetrade = 0
												elif (sc3 in oldcard5):
													falsetrade = 0
												else:
													falsetrade = 1
													room.message("One or more cards that you requested for trade are not in your hand.")
											elif (sc2 in oldcard3):
												if (sc3 in oldcard1):
													falsetrade = 0
												elif (sc3 in oldcard2):
													falsetrade = 0
												elif (sc3 in oldcard5):
													falsetrade = 0
												else:
													falsetrade = 1
													room.message("One or more cards that you requested for trade are not in your hand.")
											elif (sc2 in oldcard5):
												if (sc3 in oldcard1):
													falsetrade = 0
												elif (sc3 in oldcard2):
													falsetrade = 0
												elif (sc3 in oldcard3):
													falsetrade = 0
												else:
													falsetrade = 1
													room.message("One or more cards that you requested for trade are not in your hand.")
											else:
												falsetrade = 1
												room.message("One or more cards that you requested for trade are not in your hand.")
										elif (sc1 in oldcard5):
											if (sc2 in oldcard1):
												if (sc3 in oldcard2):
													falsetrade = 0
												elif (sc3 in oldcard3):
													falsetrade = 0
												elif (sc3 in oldcard4):
													falsetrade = 0
												else:
													falsetrade = 1
													room.message("One or more cards that you requested for trade are not in your hand.")
											elif (sc2 in oldcard2):
												if (sc3 in oldcard1):
													falsetrade = 0
												elif (sc3 in oldcard3):
													falsetrade = 0
												elif (sc3 in oldcard4):
													falsetrade = 0
												else:
													falsetrade = 1
													room.message("One or more cards that you requested for trade are not in your hand.")
											elif (sc2 in oldcard3):
												if (sc3 in oldcard1):
													falsetrade = 0
												elif (sc3 in oldcard2):
													falsetrade = 0
												elif (sc3 in oldcard4):
													falsetrade = 0
												else:
													falsetrade = 1
													room.message("One or more cards that you requested for trade are not in your hand.")	
											elif (sc2 in oldcard4):
												if (sc3 in oldcard1):
													falsetrade = 0
												elif (sc3 in oldcard2):
													falsetrade = 0
												elif (sc3 in oldcard3):
													falsetrade = 0
												else:
													falsetrade = 1
													room.message("One or more cards that you requested for trade are not in your hand.")
											else:
												falsetrade = 1
												room.message("One or more cards that you requested for trade are not in your hand.")
										else:
											falsetrade = 1
											room.message("One or more cards that you requested for trade are not in your hand.")
									elif tradenum == 2:
										sc1 = switchcardsr2[0]
										sc2 = switchcardsr2[1]
										if (sc1 in oldcard1):
											if (sc2 in oldcard2):
													falsetrade = 0
											elif (sc2 in oldcard3):
												falsetrade = 0
											elif (sc2 in oldcard4):
													falsetrade = 0
											elif (sc2 in oldcard5):
												falsetrade = 0
											else:
												falsetrade = 1
												room.message("One or more cards that you requested for trade are not in your hand.")
										elif (sc1 in oldcard2):
											if (sc2 in oldcard1):
												falsetrade = 0
											elif (sc2 in oldcard3):
												falsetrade = 0
											elif (sc2 in oldcard4):
												falsetrade = 0
											elif (sc2 in oldcard5):
												falsetrade = 0
											else:
												falsetrade = 1
												room.message("One or more cards that you requested for trade are not in your hand.")
										elif (sc1 in oldcard3):
											if (sc2 in oldcard1):
												falsetrade = 0
											elif (sc2 in oldcard2):
												falsetrade = 0
											elif (sc2 in oldcard4):
												falsetrade = 0
											elif (sc2 in oldcard5):
												falsetrade = 0
											else:
												falsetrade = 1
												room.message("One or more cards that you requested for trade are not in your hand.")
										elif (sc1 in oldcard4):
											if (sc2 in oldcard1):
												falsetrade = 0
											elif (sc2 in oldcard2):
												falsetrade = 0
											elif (sc2 in oldcard3):
												falsetrade = 0
											elif (sc2 in oldcard5):
												falsetrade = 0
											else:
												falsetrade = 1
												room.message("One or more cards that you requested for trade are not in your hand.")
										elif (sc1 in oldcard5):
											if (sc2 in oldcard1):
												falsetrade = 0
											elif (sc2 in oldcard2):
												falsetrade = 0
											elif (sc2 in oldcard3):
												falsetrade = 0
											elif (sc2 in oldcard4):
												falsetrade = 0
											else:
												falsetrade = 1
												room.message("One or more cards that you requested for trade are not in your hand.")
										else:
											falsetrade = 1
											room.message("One or more cards that you requested for trade are not in your hand.")
									elif tradenum == 1:
										sc1 = switchcardsr2[0]
										if (sc1 in oldcard1):
											falsetrade = 0
										elif (sc1 in oldcard2):
											falsetrade = 0
										elif (sc1 in oldcard3):
											falsetrade = 0
										elif (sc1 in oldcard4):
											falsetrade = 0
										elif (sc1 in oldcard5):
											falsetrade = 0
										elif sc1 == 'none':
											tradenum = 0
											falsetrade = 0
										else:
											falsetrade = 1
											room.message("One or more cards that you requested for trade are not in your hand.")
									if ((falsetrade == 0) and (tradenum >=0)):
										card1r = cdt(cards)
										card1 = card1r.replace("#&!", "")
										cs2r1 = str(cards).replace("[", "")
										cs2r2 = cs2r1.replace("]", "")
										cs2r3 = cs2r2.replace(" '#&!", "#&!")
										cs2r4 = cs2r3.replace("'", "")
										cardset2rr = cs2r4.replace(str(card1) + ',', "")
										cardset2r = cardset2rr.replace("#&!#&!", "#&!")
										cardset2 = ([n for n in cardset2r.split(",")])
										card2r = cdt(cardset2)
										card2 = card2r.replace("#&!", "")
										cs3r1 = str(cardset2).replace("[", "")
										cs3r2 = cs3r1.replace("]", "")
										cs3r3 = cs3r2.replace(" '#&!", "#&!")
										cs3r4 = cs3r3.replace("'", "")
										cardset3rr = cs3r4.replace((str(card2) + ','), '')
										cardset3r = cardset3rr.replace("#&!#&!", "#&!")
										cardset3 = ([n for n in cardset3r.split(',')])
										card3r = cdt(cardset3)
										card3 = card3r.replace("#&!", "")
										cs4r1 = str(cardset3).replace("[", "")
										cs4r2 = cs4r1.replace("]", "")
										cs4r3 = cs4r2.replace(" '#&!", "#&!")
										cs4r4 = cs4r3.replace("'", "")
										cardset4rr = cs4r4.replace((str(card3) + ','), '')
										cardset4r = cardset4rr.replace("#&!#&!", "#&!")
										cardset4 = ([n for n in cardset4r.split(',')])
										card4r = cdt(cardset4)
										card4 = card4r.replace("#&!", "")
										cs5r1 = str(cardset4).replace("[", "")
										cs5r2 = cs5r1.replace("]", "")
										cs5r3 = cs5r2.replace(" '#&!", "#&!")
										cs5r4 = cs5r3.replace("'", "")
										cardset5rr = cs5r4.replace((str(card4) + ','), '')
										cardset5r = cardset5rr.replace("#&!#&!", "#&!")
										cardset5 = ([n for n in cardset5r.split(',')])
										card5r = cdt(cardset5)
										card5 = card5r.replace("#&!", "")
										csfr1 = str(cardset5).replace("[", "")
										csfr2 = csfr1.replace("]", "")
										csfr3 = csfr2.replace(" '#&!", "#&!")
										csfr4 = csfr3.replace("'", "")
										cardsetfrr = csfr4.replace((str(card5) + ','), '')
										cardsetfr = cardsetfrr.replace("#&!#&!", "#&!")
										cardsetf = ([n for n in cardsetfr.split(',')])
										fcsfr1 = str(cardsetf).replace("[", "")
										fcsfr2 = fcsfr1.replace("]", "")
										fcsfr3 = fcsfr2.replace("'#&!", "#&!")
										fcsfr4 = fcsfr3.replace("'", "")
										fcs2r1 = str(cards).replace("[", "")
										fcs2r2 = fcs2r1.replace("]", "")
										fcs2r3 = fcs2r2.replace("'#&!", "#&!")
										fcs2r4 = fcs2r3.replace("'", "")
										gsetnewcd = rgset.replace(fcs2r4, fcsfr4)
										wrtnewcd = open(gid + ".txt","w")
										wrtnewcd.write(gsetnewcd)
										wrtnewcd.close()
										rgsetr.close()
										gsetr = open(gid + ".txt","r")
										gset = (gsetr.read()).lower()
										if tradenum == 5:
											handstrr = card1 + "," + card2 + "," + card3 + "," + card4 + "," + card5
											handli = handstrr.lower()
										elif tradenum == 4:
											if (sc1 in oldcard1):
												if (sc2 in oldcard2):
													if (sc3 in oldcard3):
														if (sc4 in oldcard4):
															handstrr = card1 + "," + card2 + "," + card3 + "," + card4 + "," + oldcard5
															handli = handstrr.lower()
														elif (sc4 in oldcard5):
															handstrr = card1 + "," + card2 + "," + card3 + "," + oldcard4 + "," + card5
															handli = handstrr.lower()
													elif (sc3 in oldcard4):
														if (sc4 in oldcard3):
															handstrr = card1 + "," + card2 + "," + card3 + "," + card4 + "," + oldcard5
															handli = handstrr.lower()
														elif (sc4 in oldcard5):
															handstrr = card1 + "," + card2 + "," + oldcard3 + "," + card4 + "," + card5
															handli = handstrr.lower()
													elif (sc3 in oldcard5):
														if (sc4 in oldcard3):
															handstrr = card1 + "," + card2 + "," + card3 + "," + oldcard4 + "," + card5
															handli = handstrr.lower()
														elif (sc4 in oldcard4):
															handstrr = card1 + "," + card2 + "," + oldcard3 + "," + card4 + "," + card5
															handli = handstrr.lower()
												elif (sc2 in oldcard3):
													if (sc3 in oldcard2):
														if (sc4 in oldcard4):
															handstrr = card1 + "," + card2 + "," + card3 + "," + card4 + "," + oldcard5
															handli = handstrr.lower()
														elif (sc4 in oldcard5):
															handstrr = card1 + "," + card2 + "," + card3 + "," + oldcard4 + "," + card5
															handli = handstrr.lower()
													elif (sc3 in oldcard4):
														if (sc4 in oldcard2):
															handstrr = card1 + "," + card2 + "," + card3 + "," + card4 + "," + oldcard5
															handli = handstrr.lower()
														elif (sc4 in oldcard5):
															handstrr = card1 + "," + oldcard2 + "," + card3 + "," + card4 + "," + card5
															handli = handstrr.lower()
													elif (sc3 in oldcard5):
														if (sc4 in oldcard2):
															handstrr = card1 + "," + card2 + "," + card3 + "," + oldcard4 + "," + card5
															handli = handstrr.lower()
														elif (sc4 in oldcard4):
															handstrr = card1 + "," + oldcard2 + "," + card3 + "," + card4 + "," + card5
															handli = handstrr.lower()
												elif (sc2 in oldcard4):
													if (sc3 in oldcard2):
														if (sc4 in oldcard3):
															handstrr = card1 + "," + card2 + "," + card3 + "," + card4 + "," + oldcard5
															handli = handstrr.lower()
														elif (sc4 in oldcard5):
															handstrr = card1 + "," + card2 + "," + oldcard3 + "," + card4 + "," + card5
															handli = handstrr.lower()
													elif (sc3 in oldcard3):
														if (sc4 in oldcard2):
															handstrr = card1 + "," + card2 + "," + card3 + "," + card4 + "," + oldcard5
															handli = handstrr.lower()
														elif (sc4 in oldcard5):
															handstrr = card1 + "," + oldcard2 + "," + card3 + "," + card4 + "," + card5
															handli = handstrr.lower()
													elif (sc3 in oldcard5):
														if (sc4 in oldcard2):
															handstrr = card1 + "," + card2 + "," + oldcard3 + "," + card4 + "," + card5
															handli = handstrr.lower()
														elif (sc4 in oldcard3):
															handstrr = card1 + "," + oldcard2 + "," + card3 + "," + card4 + "," + card5
															handli = handstrr.lower()
												elif (sc2 in oldcard5):
													if (sc3 in oldcard2):
														if (sc4 in oldcard3):
															handstrr = card1 + "," + card2 + "," + card3 + "," + oldcard4 + "," + card5
															handli = handstrr.lower()
														elif (sc4 in oldcard4):
															handstrr = card1 + "," + card2 + "," + oldcard3 + "," + card4 + "," + card5
															handli = handstrr.lower()
													elif (sc3 in oldcard3):
														if (sc4 in oldcard2):
															handstrr = card1 + "," + card2 + "," + card3 + "," + oldcard4 + "," + card5
															handli = handstrr.lower()
														elif (sc4 in oldcard4):
															handstrr = card1 + "," + oldcard2 + "," + card3 + "," + card4 + "," + card5
															handli = handstrr.lower()
													elif (sc3 in oldcard4):
														if (sc4 in oldcard2):
															handstrr = card1 + "," + card2 + "," + oldcard3 + "," + card4 + "," + card5
															handli = handstrr.lower()
														elif (sc4 in oldcard3):
															handstrr = card1 + "," + oldcard2 + "," + card3 + "," + card4 + "," + card5
															handli = handstrr.lower()
											elif (sc1 in oldcard2):
												if (sc2 in oldcard1):
													if (sc3 in oldcard3):
														if (sc4 in oldcard4):
															handstrr = card1 + "," + card2 + "," + card3 + "," + card4 + "," + oldcard5
															handli = handstrr.lower()
														elif (sc4 in oldcard5):
															handstrr = card1 + "," + card2 + "," + card3 + "," + oldcard4 + "," + card5
															handli = handstrr.lower()
													elif (sc3 in oldcard4):
														if (sc4 in oldcard3):
															handstrr = card1 + "," + card2 + "," + card3 + "," + card4 + "," + oldcard5
															handli = handstrr.lower()
														elif (sc4 in oldcard5):
															handstrr = card1 + "," + card2 + "," + oldcard3 + "," + card4 + "," + card5
															handli = handstrr.lower()
													elif (sc3 in oldcard5):
														if (sc4 in oldcard3):
															handstrr = card1 + "," + card2 + "," + card3 + "," + oldcard4 + "," + card5
															handli = handstrr.lower()
														elif (sc4 in oldcard4):
															handstrr = card1 + "," + card2 + "," + oldcard3 + "," + card4 + "," + card5
															handli = handstrr.lower()
												elif (sc2 in oldcard3):
													if (sc3 in oldcard1):
														if (sc4 in oldcard4):
															handstrr = card1 + "," + card2 + "," + card3 + "," + card4 + "," + oldcard5
															handli = handstrr.lower()
														elif (sc4 in oldcard5):
															handstrr = card1 + "," + card2 + "," + card3 + "," + oldcard4 + "," + card5
															handli = handstrr.lower()
													elif (sc3 in oldcard4):
														if (sc4 in oldcard1):
															handstrr = card1 + "," + card2 + "," + card3 + "," + card4 + "," + oldcard5
															handli = handstrr.lower()
														elif (sc4 in oldcard5):
															handstrr = oldcard1 + "," + card2 + "," + card3 + "," + card4 + "," + card5
															handli = handstrr.lower()
													elif (sc3 in oldcard5):
														if (sc4 in oldcard1):
															handstrr = card1 + "," + card2 + "," + card3 + "," + oldcard4 + "," + card5
															handli = handstrr.lower()
														elif (sc4 in oldcard4):
															handstrr = oldcard1 + "," + card2 + "," + card3 + "," + card4 + "," + card5
															handli = handstrr.lower()
												elif (sc2 in oldcard4):
													if (sc3 in oldcard1):
														if (sc4 in oldcard3):
															handstrr = card1 + "," + card2 + "," + card3 + "," + card4 + "," + oldcard5
															handli = handstrr.lower()
														elif (sc4 in oldcard5):
															handstrr = card1 + "," + card2 + "," + oldcard3 + "," + card4 + "," + card5
															handli = handstrr.lower()
													elif (sc3 in oldcard3):
														if (sc4 in oldcard1):
															handstrr = card1 + "," + card2 + "," + card3 + "," + card4 + "," + oldcard5
															handli = handstrr.lower()
														elif (sc4 in oldcard5):
															handstrr = oldcard1 + "," + card2 + "," + card3 + "," + card4 + "," + card5
															handli = handstrr.lower()
													elif (sc3 in oldcard5):
														if (sc4 in oldcard1):
															handstrr = card1 + "," + card2 + "," + oldcard3 + "," + card4 + "," + card5
															handli = handstrr.lower()
														elif (sc4 in oldcard3):
															handstrr = oldcard1 + "," + card2 + "," + card3 + "," + card4 + "," + card5
															handli = handstrr.lower()
												elif (sc2 in oldcard5):
													if (sc3 in oldcard1):
														if (sc4 in oldcard3):
															handstrr = card1 + "," + card2 + "," + card3 + "," + oldcard4 + "," + card5
															handli = handstrr.lower()
														elif (sc4 in oldcard4):
															handstrr = card1 + "," + card2 + "," + oldcard3 + "," + card4 + "," + card5
															handli = handstrr.lower()
													elif (sc3 in oldcard3):
														if (sc4 in oldcard1):
															handstrr = card1 + "," + card2 + "," + card3 + "," + oldcard4 + "," + card5
															handli = handstrr.lower()
														elif (sc4 in oldcard4):
															handstrr = oldcard1 + "," + card2 + "," + card3 + "," + card4 + "," + card5
															handli = handstrr.lower()
													elif (sc3 in oldcard4):
														if (sc4 in oldcard1):
															handstrr = card1 + "," + card2 + "," + oldcard3 + "," + card4 + "," + card5
															handli = handstrr.lower()
														elif (sc4 in oldcard3):
															handstrr = oldcard1 + "," + card2 + "," + card3 + "," + card4 + "," + card5
															handli = handstrr.lower()
											elif (sc1 in oldcard3):
												if (sc2 in oldcard1):
													if (sc3 in oldcard2):
														if (sc4 in oldcard4):
															handstrr = card1 + "," + card2 + "," + card3 + "," + card4 + "," + oldcard5
															handli = handstrr.lower()
														elif (sc4 in oldcard5):
															handstrr = card1 + "," + card2 + "," + card3 + "," + oldcard4 + "," + card5
															handli = handstrr.lower()
													elif (sc3 in oldcard4):
														if (sc4 in oldcard2):
															handstrr = card1 + "," + card2 + "," + card3 + "," + card4 + "," + oldcard5
															handli = handstrr.lower()
														elif (sc4 in oldcard5):
															handstrr = card1 + "," + oldcard2 + "," + card3 + "," + card4 + "," + card5
															handli = handstrr.lower()
													elif (sc3 in oldcard5):
														if (sc4 in oldcard2):
															handstrr = card1 + "," + card2 + "," + card3 + "," + oldcard4 + "," + card5
															handli = handstrr.lower()
														elif (sc4 in oldcard4):
															handstrr = card1 + "," + oldcard2 + "," + card3 + "," + card4 + "," + card5
															handli = handstrr.lower()
												elif (sc2 in oldcard2):
													if (sc3 in oldcard1):
														if (sc4 in oldcard4):
															handstrr = card1 + "," + card2 + "," + card3 + "," + card4 + "," + oldcard5
															handli = handstrr.lower()
														elif (sc4 in oldcard5):
															handstrr = card1 + "," + card2 + "," + card3 + "," + oldcard4 + "," + card5
															handli = handstrr.lower()
													elif (sc3 in oldcard4):
														if (sc4 in oldcard1):
															handstrr = card1 + "," + card2 + "," + card3 + "," + card4 + "," + oldcard5
															handli = handstrr.lower()
														elif (sc4 in oldcard5):
															handstrr = oldcard1 + "," + card2 + "," + card3 + "," + card4 + "," + card5
															handli = handstrr.lower()
													elif (sc3 in oldcard5):
														if (sc4 in oldcard1):
															handstrr = card1 + "," + card2 + "," + card3 + "," + oldcard4 + "," + card5
															handli = handstrr.lower()
														elif (sc4 in oldcard4):
															handstrr = oldcard1 + "," + card2 + "," + card3 + "," + card4 + "," + card5
															handli = handstrr.lower()
												elif (sc2 in oldcard4):
													if (sc3 in oldcard1):
														if (sc4 in oldcard2):
															handstrr = card1 + "," + card2 + "," + card3 + "," + card4 + "," + oldcard5
															handli = handstrr.lower()
														elif (sc4 in oldcard5):
															handstrr = card1 + "," + oldcard2 + "," + card3 + "," + card4 + "," + card5
															handli = handstrr.lower()
													elif (sc3 in oldcard2):
														if (sc4 in oldcard1):
															handstrr = card1 + "," + card2 + "," + card3 + "," + card4 + "," + oldcard5
															handli = handstrr.lower()
														elif (sc4 in oldcard5):
															handstrr = oldcard1 + "," + card2 + "," + card3 + "," + card4 + "," + card5
															handli = handstrr.lower()
													elif (sc3 in oldcard5):
														if (sc4 in oldcard1):
															handstrr = card1 + "," + oldcard2 + "," + card3 + "," + card4 + "," + card5
															handli = handstrr.lower()
														elif (sc4 in oldcard2):
															handstrr = oldcard1 + "," + card2 + "," + card3 + "," + card4 + "," + card5
															handli = handstrr.lower()
												elif (sc2 in oldcard5):
													if (sc3 in oldcard1):
														if (sc4 in oldcard2):
															handstrr = card1 + "," + card2 + "," + card3 + "," + oldcard4 + "," + card5
															handli = handstrr.lower()
														elif (sc4 in oldcard4):
															handstrr = card1 + "," + oldcard2 + "," + card3 + "," + card4 + "," + card5
															handli = handstrr.lower()
													elif (sc3 in oldcard2):
														if (sc4 in oldcard1):
															handstrr = card1 + "," + card2 + "," + card3 + "," + oldcard4 + "," + card5
															handli = handstrr.lower()
														elif (sc4 in oldcard4):
															handstrr = oldcard1 + "," + card2 + "," + card3 + "," + card4 + "," + card5
															handli = handstrr.lower()
													elif (sc3 in oldcard4):
														if (sc4 in oldcard1):
															handstrr = card1 + "," + oldcard2 + "," + card3 + "," + card4 + "," + card5
															handli = handstrr.lower()
														elif (sc4 in oldcard2):
															handstrr = oldcard1 + "," + card2 + "," + card3 + "," + card4 + "," + card5
															handli = handstrr.lower()
											elif (sc1 in oldcard4):
												if (sc2 in oldcard1):
													if (sc3 in oldcard2):
														if (sc4 in oldcard3):
															handstrr = card1 + "," + card2 + "," + card3 + "," + card4 + "," + oldcard5
															handli = handstrr.lower()
														elif (sc4 in oldcard5):
															handstrr = card1 + "," + card2 + "," + oldcard3 + "," + card4 + "," + card5
															handli = handstrr.lower()
													elif (sc3 in oldcard3):
														if (sc4 in oldcard2):
															handstrr = card1 + "," + card2 + "," + card3 + "," + card4 + "," + oldcard5
															handli = handstrr.lower()
														elif (sc4 in oldcard5):
															handstrr = card1 + "," + oldcard2 + "," + card3 + "," + card4 + "," + card5
															handli = handstrr.lower()
													elif (sc3 in oldcard5):
														if (sc4 in oldcard2):
															handstrr = card1 + "," + card2 + "," + oldcard3 + "," + card4 + "," + card5
															handli = handstrr.lower()
														elif (sc4 in oldcard3):
															handstrr = card1 + "," + oldcard2 + "," + card3 + "," + card4 + "," + card5
															handli = handstrr.lower()
												elif (sc2 in oldcard2):
													if (sc3 in oldcard1):
														if (sc4 in oldcard3):
															handstrr = card1 + "," + card2 + "," + card3 + "," + card4 + "," + oldcard5
															handli = handstrr.lower()
														elif (sc4 in oldcard5):
															handstrr = card1 + "," + card2 + "," + oldcard3 + "," + card4 + "," + card5
															handli = handstrr.lower()
													elif (sc3 in oldcard3):
														if (sc4 in oldcard1):
															handstrr = card1 + "," + card2 + "," + card3 + "," + card4 + "," + oldcard5
															handli = handstrr.lower()
														elif (sc4 in oldcard5):
															handstrr = oldcard1 + "," + card2 + "," + card3 + "," + card4 + "," + card5
															handli = handstrr.lower()
													elif (sc3 in oldcard5):
														if (sc4 in oldcard1):
															handstrr = card1 + "," + card2 + "," + oldcard3 + "," + card4 + "," + card5
															handli = handstrr.lower()
														elif (sc4 in oldcard3):
															handstrr = oldcard1 + "," + card2 + "," + card3 + "," + card4 + "," + card5
															handli = handstrr.lower()
												elif (sc2 in oldcard3):
													if (sc3 in oldcard1):
														if (sc4 in oldcard2):
															handstrr = card1 + "," + card2 + "," + card3 + "," + card4 + "," + oldcard5
															handli = handstrr.lower()
														elif (sc4 in oldcard5):
															handstrr = card1 + "," + oldcard2 + "," + card3 + "," + card4 + "," + card5
															handli = handstrr.lower()
													elif (sc3 in oldcard2):
														if (sc4 in oldcard1):
															handstrr = card1 + "," + card2 + "," + card3 + "," + card4 + "," + oldcard5
															handli = handstrr.lower()
														elif (sc4 in oldcard5):
															handstrr = oldcard1 + "," + card2 + "," + card3 + "," + card4 + "," + card5
															handli = handstrr.lower()
													elif (sc3 in oldcard5):
														if (sc4 in oldcard1):
															handstrr = card1 + "," + oldcard2 + "," + card3 + "," + card4 + "," + card5
															handli = handstrr.lower()
														elif (sc4 in oldcard2):
															handstrr = oldcard1 + "," + card2 + "," + card3 + "," + card4 + "," + card5
															handli = handstrr.lower()
												elif (sc2 in oldcard5):
													if (sc3 in oldcard1):
														if (sc4 in oldcard2):
															handstrr = card1 + "," + card2 + "," + oldcard3 + "," + card4 + "," + card5
															handli = handstrr.lower()
														elif (sc4 in oldcard3):
															handstrr = card1 + "," + oldcard2 + "," + card3 + "," + card4 + "," + card5
															handli = handstrr.lower()
													elif (sc3 in oldcard2):
														if (sc4 in oldcard1):
															handstrr = card1 + "," + card2 + "," + oldcard3 + "," + card4 + "," + card5
															handli = handstrr.lower()
														elif (sc4 in oldcard3):
															handstrr = oldcard1 + "," + card2 + "," + card3 + "," + card4 + "," + card5
															handli = handstrr.lower()
													elif (sc3 in oldcard3):
														if (sc4 in oldcard1):
															handstrr = card1 + "," + oldcard2 + "," + card3 + "," + card4 + "," + card5
															handli = handstrr.lower()
														elif (sc4 in oldcard2):
															handstrr = oldcard1 + "," + card2 + "," + card3 + "," + card4 + "," + card5
															handli = handstrr.lower()
											elif (sc1 in oldcard5):
												if (sc2 in oldcard1):
													if (sc3 in oldcard2):
														if (sc4 in oldcard3):
															handstrr = card1 + "," + card2 + "," + card3 + "," + oldcard4 + "," + card5
															handli = handstrr.lower()
														elif (sc4 in oldcard4):
															handstrr = card1 + "," + card2 + "," + oldcard3 + "," + card4 + "," + card5
															handli = handstrr.lower()
													elif (sc3 in oldcard3):
														if (sc4 in oldcard2):
															handstrr = card1 + "," + card2 + "," + card3 + "," + oldcard4 + "," + card5
															handli = handstrr.lower()
														elif (sc4 in oldcard4):
															handstrr = card1 + "," + oldcard2 + "," + card3 + "," + card4 + "," + card5
															handli = handstrr.lower()
													elif (sc3 in oldcard4):
														if (sc4 in oldcard2):
															handstrr = card1 + "," + card2 + "," + oldcard3 + "," + card4 + "," + card5
															handli = handstrr.lower()
														elif (sc4 in oldcard3):
															handstrr = card1 + "," + oldcard2 + "," + card3 + "," + card4 + "," + card5
															handli = handstrr.lower()
												elif (sc2 in oldcard2):
													if (sc3 in oldcard1):
														if (sc4 in oldcard3):
															handstrr = card1 + "," + card2 + "," + card3 + "," + oldcard4 + "," + card5
															handli = handstrr.lower()
														elif (sc4 in oldcard4):
															handstrr = card1 + "," + card2 + "," + oldcard3 + "," + card4 + "," + card5
															handli = handstrr.lower()
													elif (sc3 in oldcard3):
														if (sc4 in oldcard1):
															handstrr = card1 + "," + card2 + "," + card3 + "," + oldcard4 + "," + card5
															handli = handstrr.lower()
														elif (sc4 in oldcard4):
															handstrr = oldcard1 + "," + card2 + "," + card3 + "," + card4 + "," + card5
															handli = handstrr.lower()
													elif (sc3 in oldcard4):
														if (sc4 in oldcard1):
															handstrr = card1 + "," + card2 + "," + oldcard3 + "," + card4 + "," + card5
															handli = handstrr.lower()
														elif (sc4 in oldcard3):
															handstrr = oldcard1 + "," + card2 + "," + card3 + "," + card4 + "," + card5
															handli = handstrr.lower()
												elif (sc2 in oldcard3):
													if (sc3 in oldcard1):
														if (sc4 in oldcard2):
															handstrr = card1 + "," + card2 + "," + card3 + "," + oldcard4 + "," + card5
															handli = handstrr.lower()
														elif (sc4 in oldcard4):
															handstrr = card1 + "," + oldcard2 + "," + card3 + "," + card4 + "," + card5
															handli = handstrr.lower()
													elif (sc3 in oldcard2):
														if (sc4 in oldcard1):
															handstrr = card1 + "," + card2 + "," + card3 + "," + oldcard4 + "," + card5
															handli = handstrr.lower()
														elif (sc4 in oldcard4):
															handstrr = oldcard1 + "," + card2 + "," + card3 + "," + card4 + "," + card5
															handli = handstrr.lower()
													elif (sc3 in oldcard4):
														if (sc4 in oldcard1):
															handstrr = card1 + "," + oldcard2 + "," + card3 + "," + card4 + "," + card5
															handli = handstrr.lower()
														elif (sc4 in oldcard2):
															handstrr = oldcard1 + "," + card2 + "," + card3 + "," + card4 + "," + card5
															handli = handstrr.lower()
												elif (sc2 in oldcard4):
													if (sc3 in oldcard1):
														if (sc4 in oldcard2):
															handstrr = card1 + "," + card2 + "," + oldcard3 + "," + card4 + "," + card5
															handli = handstrr.lower()
														elif (sc4 in oldcard3):
															handstrr = card1 + "," + oldcard2 + "," + card3 + "," + card4 + "," + card5
															handli = handstrr.lower()
													elif (sc3 in oldcard2):
														if (sc4 in oldcard1):
															handstrr = card1 + "," + card2 + "," + oldcard3 + "," + card4 + "," + card5
															handli = handstrr.lower()
														elif (sc4 in oldcard3):
															handstrr = oldcard1 + "," + card2 + "," + card3 + "," + card4 + "," + card5
															handli = handstrr.lower()
													elif (sc3 in oldcard3):
														if (sc4 in oldcard1):
															handstrr = card1 + "," + oldcard2 + "," + card3 + "," + card4 + "," + card5
															handli = handstrr.lower()
														elif (sc4 in oldcard2):
															handstrr = oldcard1 + "," + card2 + "," + card3 + "," + card4 + "," + card5
															handli = handstrr.lower()
										elif tradenum == 3:
											if (sc1 in oldcard1):
												if (sc2 in oldcard2):
													if (sc3 in oldcard3):
														handstrr = card1 + "," + card2 + "," + card3 + "," + oldcard4 + "," + oldcard5
														handli = handstrr.lower()
													elif (sc3 in oldcard4):
														handstrr = card1 + "," + card2 + "," + oldcard3 + "," + card4 + "," + oldcard5
														handli = handstrr.lower()
													elif (sc3 in oldcard5):
														handstrr = card1 + "," + card2 + "," + card3 + "," + card4 + "," + card5
														handli = handstrr.lower()
												elif (sc2 in oldcard3):
													if (sc3 in oldcard2):
														handstrr = card1 + "," + card2 + "," + card3 + "," + oldcard4 + "," + oldcard5
														handli = handstrr.lower()
													elif (sc3 in oldcard4):
														handstrr = card1 + "," + oldcard2 + "," + card3 + "," + card4 + "," + oldcard5
														handli = handstrr.lower()
													elif (sc3 in oldcard5):
														handstrr = card1 + "," + oldcard2 + "," + card3 + "," + oldcard4 + "," + card5
														handli = handstrr.lower()
												elif (sc2 in oldcard4):
													if (sc3 in oldcard2):
														handstrr = card1 + "," + card2 + "," + oldcard3 + "," + card4 + "," + oldcard5
														handli = handstrr.lower()
													elif (sc3 in oldcard3):
														handstrr = card1 + "," + oldcard2 + "," + card3 + "," + card4 + "," + oldcard5
														handli = handstrr.lower()
													elif (sc3 in oldcard5):
														handstrr = card1 + "," + oldcard2 + "," + oldcard3 + "," + card4 + "," + card5
														handli = handstrr.lower()
												elif (sc2 in oldcard5):
													if (sc3 in oldcard2):
														handstrr = card1 + "," + card2 + "," + oldcard3 + "," + oldcard4 + "," + card5
														handli = handstrr.lower()
													elif (sc3 in oldcard3):
														handstrr = card1 + "," + oldcard2 + "," + card3 + "," + oldcard4 + "," + card5
														handli = handstrr.lower()
													elif (sc3 in oldcard4):
														handstrr = card1 + "," + oldcard2 + "," + oldcard3 + "," + card4 + "," + card5
														handli = handstrr.lower()
											elif (sc1 in oldcard2):
												if (sc2 in oldcard1):
													if (sc3 in oldcard3):
														handstrr = card1 + "," + card2 + "," + card3 + "," + oldcard4 + "," + oldcard5
														handli = handstrr.lower()
													elif (sc3 in oldcard4):
														handstrr = card1 + "," + card2 + "," + oldcard3 + "," + card4 + "," + oldcard5
														handli = handstrr.lower()
													elif (sc3 in oldcard5):
														handstrr = card1 + "," + card2 + "," + oldcard3 + "," + oldcard4 + "," + card5
														handli = handstrr.lower()
												elif (sc2 in oldcard3):
													if (sc3 in oldcard1):
														handstrr = card1 + "," + card2 + "," + card3 + "," + oldcard4 + "," + oldcard5
														handli = handstrr.lower()
													elif (sc3 in oldcard4):
														handstrr = oldcard1 + "," + card2 + "," + card3 + "," + card4 + "," + oldcard5
														handli = handstrr.lower()
													elif (sc3 in oldcard5):
														handstrr = oldcard1 + "," + card2 + "," + card3 + "," + oldcard4 + "," + card5
														handli = handstrr.lower()
												elif (sc2 in oldcard4):
													if (sc3 in oldcard1):
														handstrr = card1 + "," + card2 + "," + oldcard3 + "," + card4 + "," + oldcard5
														handli = handstrr.lower()
													elif (sc3 in oldcard3):
														handstrr = oldcard1 + "," + card2 + "," + card3 + "," + card4 + "," + oldcard5
														handli = handstrr.lower()
													elif (sc3 in oldcard5):
														handstrr = oldcard1 + "," + card2 + "," + oldcard3 + "," + card4 + "," + card5
														handli = handstrr.lower()
												elif (sc2 in oldcard5):
													if (sc3 in oldcard1):
														handstrr = card1 + "," + card2 + "," + oldcard3 + "," + oldcard4 + "," + card5
														handli = handstrr.lower()
													elif (sc3 in oldcard3):
														handstrr = oldcard1 + "," + card2 + "," + card3 + "," + oldcard4 + "," + card5
														handli = handstrr.lower()
													elif (sc3 in oldcard4):
														handstrr = oldcard1 + "," + card2 + "," + oldcard3 + "," + card4 + "," + card5
														handli = handstrr.lower()
											elif (sc1 in oldcard3):
												if (sc2 in oldcard1):
													if (sc3 in oldcard2):
														handstrr = card1 + "," + card2 + "," + card3 + "," + oldcard4 + "," + oldcard5
														handli = handstrr.lower()
													elif (sc3 in oldcard4):
														handstrr = card1 + "," + oldcard2 + "," + card3 + "," + card4 + "," + oldcard5
														handli = handstrr.lower()
													elif (sc3 in oldcard5):
														handstrr = card1 + "," + oldcard2 + "," + card3 + "," + oldcard4 + "," + card5
														handli = handstrr.lower()
												elif (sc2 in oldcard2):
													if (sc3 in oldcard1):
														handstrr = card1 + "," + card2 + "," + card3 + "," + oldcard4 + "," + oldcard5
														handli = handstrr.lower()
													elif (sc3 in oldcard4):
														handstrr = oldcard1 + "," + card2 + "," + card3 + "," + card4 + "," + oldcard5
														handli = handstrr.lower()
													elif (sc3 in oldcard5):
														handstrr = oldcard1 + "," + card2 + "," + card3 + "," + oldcard4 + "," + card5
														handli = handstrr.lower()
												elif (sc2 in oldcard4):
													if (sc3 in oldcard1):
														handstrr = card1 + "," + oldcard2 + "," + card3 + "," + card4 + "," + oldcard5
														handli = handstrr.lower()
													elif (sc3 in oldcard2):
														handstrr = oldcard1 + "," + card2 + "," + card3 + "," + card4 + "," + oldcard5
														handli = handstrr.lower()
													elif (sc3 in oldcard5):
														handstrr = oldcard1 + "," + oldcard2 + "," + card3 + "," + card4 + "," + card5
														handli = handstrr.lower()
												elif (sc2 in oldcard5):
													if (sc3 in oldcard1):
														handstrr = card1 + "," + oldcard2 + "," + card3 + "," + oldcard4 + "," + card5
														handli = handstrr.lower()
													elif (sc3 in oldcard2):
														handstrr = oldcard1 + "," + card2 + "," + card3 + "," + oldcard4 + "," + card5
														handli = handstrr.lower()
													elif (sc3 in oldcard4):
														handstrr = oldcard1 + "," + oldcard2 + "," + card3 + "," + card4 + "," + card5
														handli = handstrr.lower()
											elif (sc1 in oldcard4):
												if (sc2 in oldcard1):
													if (sc3 in oldcard2):
														handstrr = card1 + "," + card2 + "," + oldcard3 + "," + card4 + "," + oldcard5
														handli = handstrr.lower()
													elif (sc3 in oldcard3):
														handstrr = card1 + "," + oldcard2 + "," + card3 + "," + card4 + "," + oldcard5
														handli = handstrr.lower()
													elif (sc3 in oldcard5):
														handstrr = card1 + "," + oldcard2 + "," + oldcard3 + "," + card4 + "," + card5
														handli = handstrr.lower()
												elif (sc2 in oldcard2):
													if (sc3 in oldcard1):
														handstrr = card1 + "," + card2 + "," + oldcard3 + "," + card4 + "," + oldcard5
														handli = handstrr.lower()
													elif (sc3 in oldcard3):
														handstrr = oldcard1 + "," + card2 + "," + card3 + "," + card4 + "," + oldcard5
														handli = handstrr.lower()
													elif (sc3 in oldcard5):
														handstrr = oldcard1 + "," + card2 + "," + oldcard3 + "," + card4 + "," + card5
														handli = handstrr.lower()
												elif (sc2 in oldcard3):
													if (sc3 in oldcard1):
														handstrr = card1 + "," + oldcard2 + "," + card3 + "," + card4 + "," + oldcard5
														handli = handstrr.lower()
													elif (sc3 in oldcard2):
														handstrr = oldcard1 + "," + card2 + "," + card3 + "," + card4 + "," + oldcard5
														handli = handstrr.lower()
													elif (sc3 in oldcard5):
														handstrr = oldcard1 + "," + oldcard2 + "," + card3 + "," + card4 + "," + card5
														handli = handstrr.lower()
												elif (sc2 in oldcard5):
													if (sc3 in oldcard1):
														handstrr = card1 + "," + oldcard2 + "," + oldcard3 + "," + card4 + "," + card5
														handli = handstrr.lower()
													elif (sc3 in oldcard2):
														handstrr = oldcard1 + "," + card2 + "," + oldcard3 + "," + card4 + "," + card5
														handli = handstrr.lower()
													elif (sc3 in oldcard3):
														handstrr = oldcard1 + "," + oldcard2 + "," + card3 + "," + card4 + "," + card5
														handli = handstrr.lower()
											elif (sc1 in oldcard5):
												if (sc2 in oldcard1):
													if (sc3 in oldcard2):
														handstrr = card1 + "," + card2 + "," + oldcard3 + "," + oldcard4 + "," + card5
														handli = handstrr.lower()
													elif (sc3 in oldcard3):
														handstrr = card1 + "," + oldcard2 + "," + card3 + "," + oldcard4 + "," + card5
														handli = handstrr.lower()
													elif (sc3 in oldcard4):
														handstrr = card1 + "," + oldcard2 + "," + oldcard3 + "," + card4 + "," + card5
														handli = handstrr.lower()
												elif (sc2 in oldcard2):
													if (sc3 in oldcard1):
														handstrr = card1 + "," + card2 + "," + oldcard3 + "," + oldcard4 + "," + card5
														handli = handstrr.lower()
													elif (sc3 in oldcard3):
														handstrr = oldcard1 + "," + card2 + "," + card3 + "," + oldcard4 + "," + card5
														handli = handstrr.lower()
													elif (sc3 in oldcard4):
														handstrr = oldcard1 + "," + card2 + "," + oldcard3 + "," + card4 + "," + card5
														handli = handstrr.lower()
												elif (sc2 in oldcard3):
													if (sc3 in oldcard1):
														handstrr = card1 + "," + oldcard2 + "," + card3 + "," + oldcard4 + "," + card5
														handli = handstrr.lower()
													elif (sc3 in oldcard2):
														handstrr = oldcard1 + "," + card2 + "," + card3 + "," + oldcard4 + "," + card5
														handli = handstrr.lower()
													elif (sc3 in oldcard4):
														handstrr = oldcard1 + "," + oldcard2 + "," + card3 + "," + card4 + "," + card5
														handli = handstrr.lower()
												elif (sc2 in oldcard4):
													if (sc3 in oldcard1):
														handstrr = card1 + "," + oldcard2 + "," + oldcard3 + "," + card4 + "," + card5
														handli = handstrr.lower()
													elif (sc3 in oldcard2):
														handstrr = oldcard1 + "," + card2 + "," + oldcard3 + "," + card4 + "," + card5
														handli = handstrr.lower()
													elif (sc3 in oldcard3):
														handstrr = oldcard1 + "," + oldcard2 + "," + card3 + "," + card4 + "," + card5
														handli = handstrr.lower()
										elif tradenum == 2:
											if (sc1 in oldcard1):
												if (sc2 in oldcard2):
													handstrr = card1 + "," + card2 + "," + oldcard3 + "," + oldcard4 + "," + oldcard5
													handli = handstrr.lower()
												elif (sc2 in oldcard3):
													handstrr = card1 + "," + oldcard2 + "," + card3 + "," + oldcard4 + "," + oldcard5
													handli = handstrr.lower()
												elif (sc2 in oldcard4):
													handstrr = card1 + "," + oldcard2 + "," + oldcard3 + "," + card4 + "," + oldcard5
													handli = handstrr.lower()
												elif (sc2 in oldcard5):
													handstrr = card1 + "," + oldcard2 + "," + oldcard3 + "," + oldcard4 + "," + card5
													handli = handstrr.lower()
											elif (sc1 in oldcard2):
												if (sc2 in oldcard1):
													handstrr = card1 + "," + card2 + "," + oldcard3 + "," + oldcard4 + "," + oldcard5
													handli = handstrr.lower()
												elif (sc2 in oldcard3):
													handstrr = oldcard1 + "," + card2 + "," + card3 + "," + oldcard4 + "," + oldcard5
													handli = handstrr.lower()
												elif (sc2 in oldcard4):
													handstrr = oldcard1 + "," + card2 + "," + oldcard3 + "," + card4 + "," + oldcard5
													handli = handstrr.lower()
												elif (sc2 in oldcard5):
													handstrr = oldcard1 + "," + card2 + "," + oldcard3 + "," + oldcard4 + "," + card5
													handli = handstrr.lower()
											elif (sc1 in oldcard3):
												if (sc2 in oldcard1):
													handstrr = card1 + "," + oldcard2 + "," + card3 + "," + oldcard4 + "," + oldcard5
													handli = handstrr.lower()
												elif (sc2 in oldcard2):
													handstrr = oldcard1 + "," + card2 + "," + card3 + "," + oldcard4 + "," + oldcard5
													handli = handstrr.lower()
												elif (sc2 in oldcard4):
													handstrr = oldcard1 + "," + oldcard2 + "," + card3 + "," + card4 + "," + oldcard5
													handli = handstrr.lower()
												elif (sc2 in oldcard5):
													handstrr = oldcard1 + "," + oldcard2 + "," + card3 + "," + oldcard4 + "," + card5
													handli = handstrr.lower()
											elif (sc1 in oldcard4):
												if (sc2 in oldcard1):
													handstrr = card1 + "," + oldcard2 + "," + oldcard3 + "," + card4 + "," + oldcard5
													handli = handstrr.lower()
												elif (sc2 in oldcard2):
													handstrr = oldcard1 + "," + card2 + "," + oldcard3 + "," + card4 + "," + oldcard5
													handli = handstrr.lower()
												elif (sc2 in oldcard3):
													handstrr = oldcard1 + "," + oldcard2 + "," + card3 + "," + card4 + "," + oldcard5
													handli = handstrr.lower()
												elif (sc2 in oldcard5):
													handstrr = oldcard1 + "," + oldcard2 + "," + oldcard3 + "," + card4 + "," + card5
													handli = handstrr.lower()
											elif (sc1 in oldcard5):
												if (sc2 in oldcard1):
													handstrr = card1 + "," + oldcard2 + "," + oldcard3 + "," + oldcard4 + "," + card5
													handli = handstrr.lower()
												elif (sc2 in oldcard2):
													handstrr = oldcard1 + "," + card2 + "," + oldcard3 + "," + oldcard4 + "," + card5
													handli = handstrr.lower()
												elif (sc2 in oldcard3):
													handstrr = oldcard1 + "," + oldcard2 + "," + card3 + "," + oldcard4 + "," + card5
													handli = handstrr.lower()
												elif (sc2 in oldcard4):
													handstrr = oldcard1 + "," + oldcard2 + "," + oldcard3 + "," + card4 + "," + card5
													handli = handstrr.lower()
										elif tradenum == 1:
											if (sc1 in oldcard1):
												handstrr = card1 + "," + oldcard2 + "," + oldcard3 + "," + oldcard4 + "," + oldcard5
												handli = handstrr.lower()
											elif (sc1 in oldcard2):
												handstrr = oldcard1 + "," + card2 + "," + oldcard3 + "," + oldcard4 + "," + oldcard5
												handli = handstrr.lower()
											elif (sc1 in oldcard3):
												handstrr = oldcard1 + "," + oldcard2 + "," + card3 + "," + oldcard4 + "," + oldcard5
												handli = handstrr.lower()
											elif (sc1 in oldcard4):
												handstrr = oldcard1 + "," + oldcard2 + "," + oldcard3 + "," + card4 + "," + oldcard5
												handli = handstrr.lower()
											elif (sc1 in oldcard5):
												handstrr = oldcard1 + "," + oldcard2 + "," + oldcard3 + "," + oldcard4 + "," + card5
												handli = handstrr.lower()
										elif tradenum == 0:
											handstrr = oldcard1 + "," + oldcard2 + "," + oldcard3 + "," + oldcard4 + "," + oldcard5
											handli = handstrr.lower()
										cvp2f = handli.count('2')
										cvp3f = handli.count('3')
										cvp4f = handli.count('4')
										cvp5f = handli.count('5')
										cvp6f = handli.count('6')
										cvp7f = handli.count('7')
										cvp8f = handli.count('8')
										cvp9f = handli.count('9')
										cvp10f = handli.count('10')
										cvpjf = handli.count('jack')
										cvpqf = handli.count('icequeen')
										cvpkf = handli.count('king')
										cvpaf = handli.count('ace')
										svpcf = handli.count('clubs')
										svpsf = handli.count('spades')
										svphf = handli.count('hearts')
										svpdf = handli.count('diamonds')
										if cvp2f == 1:
											pointv21 = 2
											highcard = 2
											pointv20 = 0
											pointv22 = 0
											pointv23 = 0
											pointv24 = 0
										elif cvp2f == 2:
											pointv22 = 2
											highcard = 2
											pointv20 = 0
											pointv21 = 0
											pointv23 = 0
											pointv24 = 0
										elif cvp2f == 3:
											pointv23 = 2
											highcard = 2
											pointv20 = 0
											pointv21 = 0
											pointv22 = 0
											pointv24 = 0
										elif cvp2f == 4:
											pointv24 = 2
											highcard = 2
											pointv20 = 0
											pointv21 = 0
											pointv22 = 0
											pointv23 = 0
										elif cvp2f == 0:
											pointv20 = 0
											pointv21 = 0
											pointv22 = 0
											pointv23 = 0
											pointv24 = 0
										if cvp3f == 1:
											pointv31 = 3
											highcard = 3
											pointv30 = 0
											pointv32 = 0
											pointv33 = 0
											pointv34 = 0
										elif cvp3f == 2:
											pointv32 = 3
											highcard = 3
											pointv30 = 0
											pointv31 = 0
											pointv33 = 0
											pointv34 = 0
										elif cvp3f == 3:
											pointv33 = 3
											highcard = 3
											pointv30 = 0
											pointv31 = 0
											pointv32 = 0
											pointv34 = 0
										elif cvp3f == 4:
											pointv34 = 3
											highcard = 3
											pointv30 = 0
											pointv31 = 0
											pointv32 = 0
											pointv33 = 0
										elif cvp3f == 0:
											pointv30 = 0
											pointv31 = 0
											pointv32 = 0
											pointv33 = 0
											pointv34 = 0
										if cvp4f == 1:
											pointv41 = 4
											highcard = 4
											pointv40 = 0
											pointv42 = 0
											pointv43 = 0
											pointv44 = 0
										elif cvp4f == 2:
											pointv42 = 4
											highcard = 4
											pointv40 = 0
											pointv41 = 0
											pointv43 = 0
											pointv44 = 0
										elif cvp4f == 3:
											pointv43 = 4
											pointv40 = 0
											pointv41 = 0
											pointv42 = 0
											pointv44 = 0
										elif cvp4f == 4:
											pointv44 = 4
											pointv40 = 0
											pointv41 = 0
											pointv42 = 0
											pointv43 = 0
										elif cvp4f == 0:
											pointv40 = 0
											pointv41 = 0
											pointv42 = 0
											pointv43 = 0
											pointv44 = 0
										if cvp5f == 1:
											pointv51 = 5
											highcard = 5
											pointv50 = 0
											pointv52 = 0
											pointv53 = 0
											pointv54 = 0
										elif cvp5f == 2:
											pointv52 = 5
											highcard = 5
											pointv50 = 0
											pointv51 = 0
											pointv53 = 0
											pointv54 = 0
										elif cvp5f == 3:
											pointv53 = 5
											highcard = 5
											pointv50 = 0
											pointv51 = 0
											pointv52 = 0
											pointv54 = 0
										elif cvp5f == 4:
											pointv54 = 5
											highcard = 5
											pointv50 = 0
											pointv51 = 0
											pointv52 = 0
											pointv53 = 0
										elif cvp5f == 0:
											pointv50 = 0
											pointv51 = 0
											pointv52 = 0
											pointv53 = 0
											pointv54 = 0
										if cvp6f == 1:
											pointv61 = 6
											highcard = 6
											pointv60 = 0
											pointv62 = 0
											pointv63 = 0
											pointv64 = 0
										elif cvp6f == 2:
											pointv62 = 6
											highcard = 6
											pointv60 = 0
											pointv61 = 0
											pointv63 = 0
											pointv64 = 0
										elif cvp6f == 3:
											pointv63 = 6
											highcard = 6
											pointv60 = 0
											pointv61 = 0
											pointv62 = 0
											pointv64 = 0
										elif cvp6f == 4:
											pointv64 = 6
											highcard = 6
											pointv60 = 0
											pointv61 = 0
											pointv62 = 0
											pointv63 = 0
										elif cvp6f == 0:
											pointv60 = 0
											pointv61 = 0
											pointv62 = 0
											pointv63 = 0
											pointv64 = 0
										if cvp7f == 1:
											pointv71 = 7
											highcard = 7
											pointv70 = 0
											pointv72 = 0
											pointv73 = 0
											pointv74 = 0
										elif cvp7f == 2:
											pointv72 = 7
											highcard = 7
											pointv70 = 0
											pointv71 = 0
											pointv73 = 0
											pointv74 = 0
										elif cvp7f == 3:
											pointv73 = 7
											highcard = 7
											pointv70 = 0
											pointv71 = 0
											pointv72 = 0
											pointv74 = 0
										elif cvp7f == 4:
											pointv74 = 7
											highcard = 7
											pointv70 = 0
											pointv71 = 0
											pointv72 = 0
											pointv73 = 0
										elif cvp7f == 0:
											pointv70 = 0
											pointv71 = 0
											pointv72 = 0
											pointv73 = 0
											pointv74 = 0
										if cvp8f == 1:
											pointv81 = 8
											highcard = 8
											pointv80 = 0
											pointv82 = 0
											pointv83 = 0
											pointv84 = 0
										elif cvp8f == 2:
											pointv82 = 8
											highcard = 8
											pointv80 = 0
											pointv81 = 0
											pointv83 = 0
											pointv84 = 0
										elif cvp8f == 3:
											pointv83 = 8
											highcard = 8
											pointv80 = 0
											pointv81 = 0
											pointv82 = 0
											pointv84 = 0
										elif cvp8f == 4:
											pointv84 = 8
											highcard = 8
											pointv80 = 0
											pointv81 = 0
											pointv82 = 0
											pointv83 = 0
										elif cvp8f == 0:
											pointv80 = 0
											pointv81 = 0
											pointv82 = 0
											pointv83 = 0
											pointv84 = 0
										if cvp9f == 1:
											pointv91 = 9
											highcard = 9
											pointv90 = 0
											pointv92 = 0
											pointv93 = 0
											pointv94 = 0
										elif cvp9f == 2:
											pointv92 = 9
											highcard = 9
											pointv90 = 0
											pointv91 = 0
											pointv93 = 0
											pointv94 = 0
										elif cvp9f == 3:
											pointv93 = 9
											highcard = 9
											pointv90 = 0
											pointv91 = 0
											pointv92 = 0
											pointv94 = 0
										elif cvp9f == 4:
											pointv94 = 9
											highcard = 9
											pointv90 = 0
											pointv91 = 0
											pointv92 = 0
											pointv93 = 0
										elif cvp9f == 0:
											pointv90 = 0
											pointv91 = 0
											pointv92 = 0
											pointv93 = 0
											pointv94 = 0
										if cvp10f == 1:
											pointv101 = 10
											highcard = 10
											pointv100 = 0
											pointv102 = 0
											pointv103 = 0
											pointv104 = 0
										elif cvp10f == 2:
											pointv102 = 10
											highcard = 10
											pointv100 = 0
											pointv101 = 0
											pointv103 = 0
											pointv104 = 0
										elif cvp10f == 3:
											pointv103 = 10
											highcard = 10
											pointv100 = 0
											pointv101 = 0
											pointv102 = 0
											pointv104 = 0
										elif cvp10f == 4:
											pointv104 = 10
											highcard = 10
											pointv100 = 0
											pointv101 = 0
											pointv102 = 0
											pointv103 = 0
										elif cvp10f == 0:
											pointv100 = 0
											pointv101 = 0
											pointv102 = 0
											pointv103 = 0
											pointv104 = 0
										if cvpjf == 1:
											pointvj1 = 11
											highcard = 11
											pointvj0 = 0
											pointvj2 = 0
											pointvj3 = 0
											pointvj4 = 0
										elif cvpjf == 2:
											pointvj2 = 11
											highcard = 11
											pointvj0 = 0
											pointvj1 = 0
											pointvj3 = 0
											pointvj4 = 0
										elif cvpjf == 3:
											pointvj3 = 11
											highcard = 11
											pointvj0 = 0
											pointvj1 = 0
											pointvj2 = 0
											pointvj4 = 0
										elif cvpjf == 4:
											pointvj4 = 11
											highcard = 11
											pointvj0 = 0
											pointvj1 = 0
											pointvj2 = 0
											pointvj3 = 0
										elif cvpjf == 0:
											pointvj0 = 0
											pointvj1 = 0
											pointvj2 = 0
											pointvj3 = 0
											pointvj4 = 0
										if cvpqf == 1:
											pointvq1 = 12
											highcard = 12
											pointvq0 = 0
											pointvq2 = 0
											pointvq3 = 0
											pointvq4 = 0
										elif cvpqf == 2:
											pointvq2 = 12
											highcard = 12
											pointvq0 = 0
											pointvq1 = 0
											pointvq3 = 0
											pointvq4 = 0
										elif cvpqf == 3:
											pointvq3 = 12
											highcard = 12
											pointvq0 = 0
											pointvq1 = 0
											pointvq2 = 0
											pointvq4 = 0
										elif cvpqf == 4:
											pointvq4 = 12
											highcard = 12
											pointvq0 = 0
											pointvq1 = 0
											pointvq2 = 0
											pointvq3 = 0
										elif cvpqf == 0:
											pointvq0 = 0
											pointvq1 = 0
											pointvq2 = 0
											pointvq3 = 0
											pointvq4 = 0
										if cvpkf == 1:
											pointvk1 = 13
											highcard = 13
											pointvk0 = 0
											pointvk2 = 0
											pointvk3 = 0
											pointvk4 = 0
										elif cvpkf == 2:
											pointvk2 = 13
											highcard = 13
											pointvk0 = 0
											pointvk1 = 0
											pointvk3 = 0
											pointvk4 = 0
										elif cvpkf == 3:
											pointvk3 = 13
											highcard = 13
											pointvk0 = 0
											pointvk1 = 0
											pointvk2 = 0
											pointvk4 = 0
										elif cvpkf == 4:
											pointvk4 = 13
											highcard = 13
											pointvk0 = 0
											pointvk1 = 0
											pointvk2 = 0
											pointvk3 = 0
										elif cvpkf == 0:
											pointvk0 = 0
											pointvk1 = 0
											pointvk2 = 0
											pointvk3 = 0
											pointvk4 = 0
										if cvpaf == 1:
											pointva1 = 14
											highcard = 14
											pointva0 = 0
											pointva2 = 0
											pointva3 = 0
											pointva4 = 0
										elif cvpaf == 2:
											pointva2 = 14
											highcard = 14
											pointva0 = 0
											pointva1 = 0
											pointva3 = 0
											pointva4 = 0
										elif cvpaf == 3:
											pointva3 = 14
											highcard = 14
											pointva0 = 0
											pointva1 = 0
											pointva2 = 0
											pointva4 = 0
										elif cvpaf == 4:
											pointva4 = 14
											highcard = 14
											pointva0 = 0
											pointva1 = 0
											pointva2 = 0
											pointva3 = 0
										elif cvpaf == 0:
											pointva0 = 0
											pointva1 = 0
											pointva2 = 0
											pointva3 = 0
											pointva4 = 0
										if svpdf == 1:
											pointvd = 0
										elif svpdf == 2:
											pointvd = 0
										elif svpdf == 3:
											pointvd = 0
										elif svpdf == 4:
											pointvd = 0
										elif svpdf == 5:
											pointvd = 1
										elif svpdf == 0:
											pointvd = 0
										if svphf == 1:
											pointvh = 0
										elif svphf == 2:
											pointvh = 0
										elif svphf == 3:
											pointvh = 0
										elif svphf == 4:
											pointvh = 0
										elif svphf == 5:
											pointvh = 1
										elif svphf == 0:
											pointvh = 0
										if svpsf == 1:
											pointvs = 0
										elif svpsf == 2:
											pointvs = 0
										elif svpsf == 3:
											pointvs = 0
										elif svpsf == 4:
											pointvs = 0
										elif svpsf == 5:
											pointvs = 1
										elif svpsf == 0:
											pointvs = 0
										if svpcf == 1:
											pointvc = 0
										elif svpcf == 2:
											pointvc = 0
										elif svpcf == 3:
											pointvc = 0
										elif svpcf == 4:
											pointvc = 0
										elif svpcf == 5:
											pointvc = 1
										elif svpcf == 0:
											pointvc = 0
										if ( (cvp10f == 1) and (cvpjf == 1) and (cvpqf == 1) and (cvpkf == 1) and (cvpaf == 1) and ((svpcf == 5) or(svpsf == 5) or(svphf == 5) or(svpdf == 5))):
											handpoints = 1000
										elif ( (cvp10f == 1) and (cvpjf == 1) and (cvpqf == 1) and (cvpkf == 1) and (cvp9f == 1) and ((svpcf == 5) or(svpsf == 5) or(svphf == 5) or(svpdf == 5))):
											handpoints = 999
										elif ( (cvp10f == 1) and (cvpjf == 1) and (cvpqf == 1) and (cvp8f == 1) and (cvp9f == 1) and ((svpcf == 5) or(svpsf == 5) or(svphf == 5) or(svpdf == 5))):
											handpoints = 998
										elif ( (cvp10f == 1) and (cvpjf == 1) and (cvp7f == 1) and (cvp8f == 1) and (cvp9f == 1) and ((svpcf == 5) or(svpsf == 5) or(svphf == 5) or(svpdf == 5))):
											handpoints = 997
										elif ( (cvp10f == 1) and (cvp6f == 1) and (cvp7f == 1) and (cvp8f == 1) and (cvp9f == 1) and ((svpcf == 5) or(svpsf == 5) or(svphf == 5) or(svpdf == 5))):
											handpoints = 996
										elif ( (cvp5f == 1) and (cvp6f == 1) and (cvp7f == 1) and (cvp8f == 1) and (cvp9f == 1) and ((svpcf == 5) or(svpsf == 5) or(svphf == 5) or(svpdf == 5))):
											handpoints = 995
										elif ( (cvp5f == 1) and (cvp6f == 1) and (cvp7f == 1) and (cvp8f == 1) and (cvp4f == 1) and ((svpcf == 5) or(svpsf == 5) or(svphf == 5) or(svpdf == 5))):
											handpoints = 994
										elif ( (cvp5f == 1) and (cvp6f == 1) and (cvp7f == 1) and (cvp3f == 1) and (cvp4f == 1) and ((svpcf == 5) or(svpsf == 5) or(svphf == 5) or(svpdf == 5))):
											handpoints = 993
										elif ( (cvp5f == 1) and (cvp6f == 1) and (cvp2f == 1) and (cvp3f == 1) and (cvp4f == 1) and ((svpcf == 5) or(svpsf == 5) or(svphf == 5) or(svpdf == 5))):
											handpoints = 992
										elif ( (cvp5f == 1) and (cvpaf == 1) and (cvp2f == 1) and (cvp3f == 1) and (cvp4f == 1) and ((svpcf == 5) or(svpsf == 5) or(svphf == 5) or(svpdf == 5))):
											handpoints = 991
										elif ( (cvp2f == 4) or (cvp3f == 4) or (cvp4f == 4) or (cvp5f == 4) or (cvp6f == 4) or (cvp7f == 4) or (cvp8f == 4) or (cvp9f == 4) or (cvp10f == 4) or (cvpjf == 4) or (cvpqf == 4) or (cvpkf == 4) or (cvpaf == 4) ):
											handpoints = 976 + pointva4 + pointvk4 + pointvq4 + pointvj4 + pointv104 + pointv94 + pointv84 + pointv74 + pointv64 + pointv54 + pointv44 + pointv34 + pointv24
										elif ( (cvpaf == 3) and ( (cvp2f == 2) or (cvp3f == 2) or (cvp4f == 2) or (cvp5f == 2) or (cvp6f == 2) or (cvp7f == 2) or (cvp8f == 2) or (cvp9f == 2) or (cvp10f == 2) or (cvpjf == 2) or (cvpqf == 2) or (cvpkf == 2) or (cvpaf == 2)) ):
											handpoints = 963 + pointva2 + pointvk2 + pointvq2 + pointvj2 + pointv102 + pointv92 + pointv82 + pointv72 + pointv62 + pointv52 + pointv42 + pointv32 + pointv22
										elif ( (cvpkf == 3) and ( (cvp2f == 2) or (cvp3f == 2) or (cvp4f == 2) or (cvp5f == 2) or (cvp6f == 2) or (cvp7f == 2) or (cvp8f == 2) or (cvp9f == 2) or (cvp10f == 2) or (cvpjf == 2) or (cvpqf == 2) or (cvpkf == 2) or (cvpaf == 2)) ):
											handpoints = 948 + pointva2 + pointvk2 + pointvq2 + pointvj2 + pointv102 + pointv92 + pointv82 + pointv72 + pointv62 + pointv52 + pointv42 + pointv32 + pointv22
										elif ( (cvpqf == 3) and ( (cvp2f == 2) or (cvp3f == 2) or (cvp4f == 2) or (cvp5f == 2) or (cvp6f == 2) or (cvp7f == 2) or (cvp8f == 2) or (cvp9f == 2) or (cvp10f == 2) or (cvpjf == 2) or (cvpqf == 2) or (cvpkf == 2) or (cvpaf == 2)) ):
											handpoints = 933 + pointva2 + pointvk2 + pointvq2 + pointvj2 + pointv102 + pointv92 + pointv82 + pointv72 + pointv62 + pointv52 + pointv42 + pointv32 + pointv22
										elif ( (cvpjf == 3) and ( (cvp2f == 2) or (cvp3f == 2) or (cvp4f == 2) or (cvp5f == 2) or (cvp6f == 2) or (cvp7f == 2) or (cvp8f == 2) or (cvp9f == 2) or (cvp10f == 2) or (cvpjf == 2) or (cvpqf == 2) or (cvpkf == 2) or (cvpaf == 2)) ):
											handpoints = 918 + pointva2 + pointvk2 + pointvq2 + pointvj2 + pointv102 + pointv92 + pointv82 + pointv72 + pointv62 + pointv52 + pointv42 + pointv32 + pointv22
										elif ( (cvp10f == 3) and ( (cvp2f == 2) or (cvp3f == 2) or (cvp4f == 2) or (cvp5f == 2) or (cvp6f == 2) or (cvp7f == 2) or (cvp8f == 2) or (cvp9f == 2) or (cvp10f == 2) or (cvpjf == 2) or (cvpqf == 2) or (cvpkf == 2) or (cvpaf == 2)) ):
											handpoints = 903 + pointva2 + pointvk2 + pointvq2 + pointvj2 + pointv102 + pointv92 + pointv82 + pointv72 + pointv62 + pointv52 + pointv42 + pointv32 + pointv22
										elif ( (cvp9f == 3) and ( (cvp2f == 2) or (cvp3f == 2) or (cvp4f == 2) or (cvp5f == 2) or (cvp6f == 2) or (cvp7f == 2) or (cvp8f == 2) or (cvp9f == 2) or (cvp10f == 2) or (cvpjf == 2) or (cvpqf == 2) or (cvpkf == 2) or (cvpaf == 2)) ):
											handpoints = 888 + pointva2 + pointvk2 + pointvq2 + pointvj2 + pointv102 + pointv92 + pointv82 + pointv72 + pointv62 + pointv52 + pointv42 + pointv32 + pointv22
										elif ( (cvp8f == 3) and ( (cvp2f == 2) or (cvp3f == 2) or (cvp4f == 2) or (cvp5f == 2) or (cvp6f == 2) or (cvp7f == 2) or (cvp8f == 2) or (cvp9f == 2) or (cvp10f == 2) or (cvpjf == 2) or (cvpqf == 2) or (cvpkf == 2) or (cvpaf == 2)) ):
											handpoints = 873 + pointva2 + pointvk2 + pointvq2 + pointvj2 + pointv102 + pointv92 + pointv82 + pointv72 + pointv62 + pointv52 + pointv42 + pointv32 + pointv22
										elif ( (cvp7f == 3) and ( (cvp2f == 2) or (cvp3f == 2) or (cvp4f == 2) or (cvp5f == 2) or (cvp6f == 2) or (cvp7f == 2) or (cvp8f == 2) or (cvp9f == 2) or (cvp10f == 2) or (cvpjf == 2) or (cvpqf == 2) or (cvpkf == 2) or (cvpaf == 2)) ):
											handpoints = 858 + pointva2 + pointvk2 + pointvq2 + pointvj2 + pointv102 + pointv92 + pointv82 + pointv72 + pointv62 + pointv52 + pointv42 + pointv32 + pointv22
										elif ( (cvp6f == 3) and ( (cvp2f == 2) or (cvp3f == 2) or (cvp4f == 2) or (cvp5f == 2) or (cvp6f == 2) or (cvp7f == 2) or (cvp8f == 2) or (cvp9f == 2) or (cvp10f == 2) or (cvpjf == 2) or (cvpqf == 2) or (cvpkf == 2) or (cvpaf == 2)) ):
											handpoints = 843 + pointva2 + pointvk2 + pointvq2 + pointvj2 + pointv102 + pointv92 + pointv82 + pointv72 + pointv62 + pointv52 + pointv42 + pointv32 + pointv22
										elif ( (cvp5f == 3) and ( (cvp2f == 2) or (cvp3f == 2) or (cvp4f == 2) or (cvp5f == 2) or (cvp6f == 2) or (cvp7f == 2) or (cvp8f == 2) or (cvp9f == 2) or (cvp10f == 2) or (cvpjf == 2) or (cvpqf == 2) or (cvpkf == 2) or (cvpaf == 2)) ):
											handpoints = 828 + pointva2 + pointvk2 + pointvq2 + pointvj2 + pointv102 + pointv92 + pointv82 + pointv72 + pointv62 + pointv52 + pointv42 + pointv32 + pointv22
										elif ( (cvp4f == 3) and ( (cvp2f == 2) or (cvp3f == 2) or (cvp4f == 2) or (cvp5f == 2) or (cvp6f == 2) or (cvp7f == 2) or (cvp8f == 2) or (cvp9f == 2) or (cvp10f == 2) or (cvpjf == 2) or (cvpqf == 2) or (cvpkf == 2) or (cvpaf == 2)) ):
											handpoints = 813 + pointva2 + pointvk2 + pointvq2 + pointvj2 + pointv102 + pointv92 + pointv82 + pointv72 + pointv62 + pointv52 + pointv42 + pointv32 + pointv22
										elif ( (cvp3f == 3) and ( (cvp2f == 2) or (cvp3f == 2) or (cvp4f == 2) or (cvp5f == 2) or (cvp6f == 2) or (cvp7f == 2) or (cvp8f == 2) or (cvp9f == 2) or (cvp10f == 2) or (cvpjf == 2) or (cvpqf == 2) or (cvpkf == 2) or (cvpaf == 2)) ):
											handpoints = 798 + pointva2 + pointvk2 + pointvq2 + pointvj2 + pointv102 + pointv92 + pointv82 + pointv72 + pointv62 + pointv52 + pointv42 + pointv32 + pointv22
										elif ( (cvp2f == 3) and ( (cvp2f == 2) or (cvp3f == 2) or (cvp4f == 2) or (cvp5f == 2) or (cvp6f == 2) or (cvp7f == 2) or (cvp8f == 2) or (cvp9f == 2) or (cvp10f == 2) or (cvpjf == 2) or (cvpqf == 2) or (cvpkf == 2) or (cvpaf == 2)) ):
											handpoints = 783 + pointva2 + pointvk2 + pointvq2 + pointvj2 + pointv102 + pointv92 + pointv82 + pointv72 + pointv62 + pointv52 + pointv42 + pointv32 + pointv22
										elif ( (svpcf == 5) or (svpsf ==5) or (svphf ==5) or (svpdf ==5) ):
											handpoints = 782
										elif ( (cvp10f == 1) and (cvpjf == 1) and (cvpqf == 1) and (cvpkf == 1) and (cvpaf == 1)):
											handpoints = 781
										elif ( (cvp10f == 1) and (cvpjf == 1) and (cvpqf == 1) and (cvpkf == 1) and (cvp9f == 1)):
											handpoints = 780
										elif ( (cvp10f == 1) and (cvpjf == 1) and (cvpqf == 1) and (cvp8f == 1) and (cvp9f == 1)):
											handpoints = 779
										elif ( (cvp10f == 1) and (cvpjf == 1) and (cvp7f == 1) and (cvp8f == 1) and (cvp9f == 1)):
											handpoints = 778
										elif ( (cvp10f == 1) and (cvp6f == 1) and (cvp7f == 1) and (cvp8f == 1) and (cvp9f == 1)):
											handpoints = 776
										elif ( (cvp5f == 1) and (cvp6f == 1) and (cvp7f == 1) and (cvp8f == 1) and (cvp9f == 1)):
											handpoints = 775
										elif ( (cvp5f == 1) and (cvp6f == 1) and (cvp7f == 1) and (cvp8f == 1) and (cvp4f == 1)):
											handpoints = 774
										elif ( (cvp5f == 1) and (cvp6f == 1) and (cvp7f == 1) and (cvp3f == 1) and (cvp4f == 1)):
											handpoints = 773
										elif ( (cvp5f == 1) and (cvp6f == 1) and (cvp2f == 1) and (cvp3f == 1) and (cvp4f == 1)):
											handpoints = 772
										elif ( (cvp5f == 1) and (cvpaf == 1) and (cvp2f == 1) and (cvp3f == 1) and (cvp4f == 1)):
											handpoints = 771
										elif ( (cvp2f == 3) or (cvp3f == 3) or (cvp4f == 3) or (cvp5f == 3) or (cvp6f == 3) or (cvp7f == 3) or (cvp8f == 3) or (cvp9f == 3) or (cvp10f == 3) or (cvpjf == 3) or (cvpqf == 3) or (cvpkf == 3) or (cvpaf == 3) ):
											handpoints = 756 + pointva3 + pointvk3 + pointvq3 + pointvj3 + pointv103 + pointv93 + pointv83 + pointv73 + pointv63 + pointv53 + pointv43 + pointv33 + pointv23
										elif ( (cvpaf == 2) and ( (cvp2f == 2) or (cvp3f == 2) or (cvp4f == 2) or (cvp5f == 2) or (cvp6f == 2) or (cvp7f == 2) or (cvp8f == 2) or (cvp9f == 2) or (cvp10f == 2) or (cvpjf == 2) or (cvpqf == 2) or (cvpkf == 2)) ):
											handpoints = 741 + pointvk2 + pointvq2 + pointvj2 + pointv102 + pointv92 + pointv82 + pointv72 + pointv62 + pointv52 + pointv42 + pointv32 + pointv22
										elif ( (cvpkf == 2) and ( (cvp2f == 2) or (cvp3f == 2) or (cvp4f == 2) or (cvp5f == 2) or (cvp6f == 2) or (cvp7f == 2) or (cvp8f == 2) or (cvp9f == 2) or (cvp10f == 2) or (cvpjf == 2) or (cvpqf == 2) or (cvpaf == 2)) ):
											handpoints = 726 + pointva2 + pointvq2 + pointvj2 + pointv102 + pointv92 + pointv82 + pointv72 + pointv62 + pointv52 + pointv42 + pointv32 + pointv22
										elif ( (cvpqf == 2) and ( (cvp2f == 2) or (cvp3f == 2) or (cvp4f == 2) or (cvp5f == 2) or (cvp6f == 2) or (cvp7f == 2) or (cvp8f == 2) or (cvp9f == 2) or (cvp10f == 2) or (cvpjf == 2) or (cvpkf == 2) or (cvpaf == 2)) ):
											handpoints = 711 + pointva2 + pointvk2 + pointvj2 + pointv102 + pointv92 + pointv82 + pointv72 + pointv62 + pointv52 + pointv42 + pointv32 + pointv22
										elif ( (cvpjf == 2) and ( (cvp2f == 2) or (cvp3f == 2) or (cvp4f == 2) or (cvp5f == 2) or (cvp6f == 2) or (cvp7f == 2) or (cvp8f == 2) or (cvp9f == 2) or (cvp10f == 2) or (cvpqf == 2) or (cvpkf == 2) or (cvpaf == 2)) ):
											handpoints = 696 + pointva2 + pointvk2 + pointvq2 + pointv102 + pointv92 + pointv82 + pointv72 + pointv62 + pointv52 + pointv42 + pointv32 + pointv22
										elif ( (cvp10f == 2) and ( (cvp2f == 2) or (cvp3f == 2) or (cvp4f == 2) or (cvp5f == 2) or (cvp6f == 2) or (cvp7f == 2) or (cvp8f == 2) or (cvp9f == 2) or (cvpjf == 2) or (cvpqf == 2) or (cvpkf == 2) or (cvpaf == 2)) ):
											handpoints = 681 + pointva2 + pointvk2 + pointvq2 + pointvj2 + pointv92 + pointv82 + pointv72 + pointv62 + pointv52 + pointv42 + pointv32 + pointv22
										elif ( (cvp9f == 2) and ( (cvp2f == 2) or (cvp3f == 2) or (cvp4f == 2) or (cvp5f == 2) or (cvp6f == 2) or (cvp7f == 2) or (cvp8f == 2) or (cvp10f == 2) or (cvpjf == 2) or (cvpqf == 2) or (cvpkf == 2) or (cvpaf == 2)) ):
											handpoints = 666 + pointva2 + pointvk2 + pointvq2 + pointvj2 + pointv102 + pointv82 + pointv72 + pointv62 + pointv52 + pointv42 + pointv32 + pointv22
										elif ( (cvp8f == 2) and ( (cvp2f == 2) or (cvp3f == 2) or (cvp4f == 2) or (cvp5f == 2) or (cvp6f == 2) or (cvp7f == 2) or (cvp9f == 2) or (cvp10f == 2) or (cvpjf == 2) or (cvpqf == 2) or (cvpkf == 2) or (cvpaf == 2)) ):
											handpoints = 651 + pointva2 + pointvk2 + pointvq2 + pointvj2 + pointv102 + pointv92 + pointv72 + pointv62 + pointv52 + pointv42 + pointv32 + pointv22
										elif ( (cvp7f == 2) and ( (cvp2f == 2) or (cvp3f == 2) or (cvp4f == 2) or (cvp5f == 2) or (cvp6f == 2) or (cvp8f == 2) or (cvp9f == 2) or (cvp10f == 2) or (cvpjf == 2) or (cvpqf == 2) or (cvpkf == 2) or (cvpaf == 2)) ):
											handpoints = 636 + pointva2 + pointvk2 + pointvq2 + pointvj2 + pointv102 + pointv92 + pointv82 + pointv62 + pointv52 + pointv42 + pointv32 + pointv22
										elif ( (cvp6f == 2) and ( (cvp2f == 2) or (cvp3f == 2) or (cvp4f == 2) or (cvp5f == 2) or (cvp7f == 2) or (cvp8f == 2) or (cvp9f == 2) or (cvp10f == 2) or (cvpjf == 2) or (cvpqf == 2) or (cvpkf == 2) or (cvpaf == 2)) ):
											handpoints = 621 + pointva2 + pointvk2 + pointvq2 + pointvj2 + pointv102 + pointv92 + pointv82 + pointv72 + pointv52 + pointv42 + pointv32 + pointv22
										elif ( (cvp5f == 2) and ( (cvp2f == 2) or (cvp3f == 2) or (cvp4f == 2) or (cvp6f == 2) or (cvp7f == 2) or (cvp8f == 2) or (cvp9f == 2) or (cvp10f == 2) or (cvpjf == 2) or (cvpqf == 2) or (cvpkf == 2) or (cvpaf == 2)) ):
											handpoints = 606 + pointva2 + pointvk2 + pointvq2 + pointvj2 + pointv102 + pointv92 + pointv82 + pointv72 + pointv62 + pointv42 + pointv32 + pointv22
										elif ( (cvp4f == 2) and ( (cvp2f == 2) or (cvp3f == 2) or (cvp5f == 2) or (cvp6f == 2) or (cvp7f == 2) or (cvp8f == 2) or (cvp9f == 2) or (cvp10f == 2) or (cvpjf == 2) or (cvpqf == 2) or (cvpkf == 2) or (cvpaf == 2)) ):
											handpoints = 591 + pointva2 + pointvk2 + pointvq2 + pointvj2 + pointv102 + pointv92 + pointv82 + pointv72 + pointv62 + pointv52 + pointv32 + pointv22
										elif ( (cvp3f == 2) and ( (cvp2f == 2) or (cvp4f == 2) or (cvp5f == 2) or (cvp6f == 2) or (cvp7f == 2) or (cvp8f == 2) or (cvp9f == 2) or (cvp10f == 2) or (cvpjf == 2) or (cvpqf == 2) or (cvpkf == 2) or (cvpaf == 2)) ):
											handpoints = 576 + pointva2 + pointvk2 + pointvq2 + pointvj2 + pointv102 + pointv92 + pointv82 + pointv72 + pointv62 + pointv52 + pointv42 + pointv22
										elif ( (cvp2f == 2) and ((cvp3f == 2) or (cvp4f == 2) or (cvp5f == 2) or (cvp6f == 2) or (cvp7f == 2) or (cvp8f == 2) or (cvp9f == 2) or (cvp10f == 2) or (cvpjf == 2) or (cvpqf == 2) or (cvpkf == 2) or (cvpaf == 2)) ):

											handpoints = 561 + pointva2 + pointvk2 + pointvq2 + pointvj2 + pointv102 + pointv92 + pointv82 + pointv72 + pointv62 + pointv52 + pointv42 + pointv32
										elif ( (cvp2f == 2) or (cvp3f == 2) or (cvp4f == 2) or (cvp5f == 2) or (cvp6f == 2) or (cvp7f == 2) or (cvp8f == 2) or (cvp9f == 2) or (cvp10f == 2) or (cvpjf == 2) or (cvpqf == 2) or (cvpkf == 2) or (cvpaf == 2) ):
											handpoints = 546 + pointva2 + pointvk2 + pointvq2 + pointvj2 + pointv102 + pointv92 + pointv82 + pointv72 + pointv62 + pointv52 + pointv42 + pointv32 + pointv22
										else:
											handpoints = 500
										tradestatusir = int(tradestatus)
										tradestatusi = tradestatusir - 1
										tradestatusnew = '*#&^tradestatus = ' + str(tradestatusi) + ' )#(#*&'
										gsetnewtd = gset.replace(('*#&^tradestatus = ' + tradestatus + ' )#(#*&'), str(tradestatusnew))
										hpindexs = gset.find('#$!*&^!@' + user.name + '&&*)^$#@!handpoint = ')
										hpindexe = gset.find(')(&$&$#@' + user.name + '!@&@$@^&')
										hprawout = gset[(int(hpindexs)):(int(hpindexe))]
										hprawout2 = hprawout.replace(('#$!*&^!@' + user.name + '&&*)^$#@!handpoint = '), "")
										oldhandpoints = hprawout2.replace((')(&$&$#@' + user.name + '!@&@$@^&'), "")
										handpointsnew = '#$!*&^!@' + tradestatus + user.name + '&&*)^$#@!' + tradestatus + 'handpoint = ' + str(handpoints) + ')(&$&$#@' + tradestatus + user.name + '!@&@$@^&' + tradestatus
										gsetnewhp = gsetnewtd.replace(('#$!*&^!@' + user.name + '&&*)^$#@!handpoint = ' + oldhandpoints + ')(&$&$#@' + user.name + '!@&@$@^&'), str(handpointsnew))
										hcindexs = gset.find('!!@*^$&' + user.name + '**^&$$#!(highcard = ')
										hcindexe = gset.find('&(#*$%!)^' + user.name + '(*&$@@#!')
										hcrawout = gset[(int(hcindexs)):(int(hcindexe))]
										hcrawout2 = hcrawout.replace(('!!@*^$&' + user.name + '**^&$$#!(highcard = '), "")
										oldhighcard = hcrawout2.replace(('&(#*$%!)^' + user.name + '(*&$@@#!'), "")
										highcardnew = '!!@*^$&' + tradestatus + user.name + '**^&$$#!(' + tradestatus + 'highcard = ' + str(highcard) + '&(#*$%!)^' + tradestatus + user.name + '(*&$@@#!' + tradestatus
										gsetnewhc = gsetnewhp.replace(('!!@*^$&' + user.name + '**^&$$#!(highcard = ' + oldhighcard + '&(#*$%!)^' + user.name + '(*&$@@#!'), str(highcardnew))
										newcard1, newcard2, newcard3, newcard4, newcard5 = handli.split(",", 4)
										newcard1sec = '**^@%#$' + user.name + ')()*@&^%card1 = ' + newcard1 + '!)@(#$&' + user.name + '!*!&!^#c1'
										gsetnewnc1 = gsetnewhc.replace(('**^@%#$' + user.name + ')()*@&^%card1 = ' + oldcard1 + '!)@(#$&' + user.name + '!*!&!^#c1'), str(newcard1sec))
										newcard2sec = '**^@%#$' + user.name + ')()*@&^%card2 = ' + newcard2 + '!)@(#$&' + user.name + '!*!&!^#c2'
										gsetnewnc2 = gsetnewnc1.replace(('**^@%#$' + user.name + ')()*@&^%card2 = ' + oldcard2 + '!)@(#$&' + user.name + '!*!&!^#c2'), str(newcard2sec))
										newcard3sec = '**^@%#$' + user.name + ')()*@&^%card3 = ' + newcard3 + '!)@(#$&' + user.name + '!*!&!^#c3'
										gsetnewnc3 = gsetnewnc2.replace(('**^@%#$' + user.name + ')()*@&^%card3 = ' + oldcard3 + '!)@(#$&' + user.name + '!*!&!^#c3'), str(newcard3sec))
										newcard4sec = '**^@%#$' + user.name + ')()*@&^%card4 = ' + newcard4 + '!)@(#$&' + user.name + '!*!&!^#c4'
										gsetnewnc4 = gsetnewnc3.replace(('**^@%#$' + user.name + ')()*@&^%card4 = ' + oldcard4 + '!)@(#$&' + user.name + '!*!&!^#c4'), str(newcard4sec))
										newcard5sec = '**^@%#$' + user.name + ')()*@&^%card5 = ' + newcard5 + '!)@(#$&' + user.name + '!*!&!^#c5'
										gsetnewnc5 = gsetnewnc4.replace(('**^@%#$' + user.name + ')()*@&^%card5 = ' + oldcard5 + '!)@(#$&' + user.name + '!*!&!^#c5'), str(newcard5sec))	
										wrtdata2 = open((gid + ".txt"), "w")
										wrtdata2.write(gsetnewnc5 + '\n*$!$@#($*!' + user.name + ' has traded!$#@(%*!%!\n')
										glistr.close()
										gsetr.close()
										wrtdata2.close()
										gsetfr = open(gid + ".txt","r")
										gsetf = (gsetfr.read()).lower()
										if tradestatusi > 0:
											(self._pm).message(user, str("Your new cards for [gameid: " + gid.upper() + "] are: " + newcard1 + ", " + newcard2 + ", " + newcard3 + ", " + newcard4 + ", " + newcard5 + "."))
											room.message("I have PMed you your new cards.")
										elif tradestatusi == 0:
											room.message(str("Your new cards for [gameid: " + gid.upper() + "] are: " + newcard1 + ", " + newcard2 + ", " + newcard3 + ", " + newcard4 + ", " + newcard5 + "."))
											indexsp1 = gsetf.find('&&*)^$#@!1handpoint = ')
											indexep1 = gsetf.find(')(&$&$#@1')
											rawoutp1 = gsetf[(int(indexsp1)):(int(indexep1))]
											rawout2p1 = rawoutp1.replace(('&&*)^$#@!1handpoint = '), "")
											pointsrp1 = rawout2p1.replace((')(&$&$#@1'), "")
											pointsp1 = int(pointsrp1)
											indexsp2 = gsetf.find('&&*)^$#@!2handpoint = ')
											indexep2 = gsetf.find(')(&$&$#@2')
											rawoutp2 = gsetf[(int(indexsp2)):(int(indexep2))]
											rawout2p2 = rawoutp2.replace(('&&*)^$#@!2handpoint = '), "")
											pointsrp2 = rawout2p2.replace((')(&$&$#@2'), "")
											pointsp2 = int(pointsrp2)
											indexshp1 = gsetf.find('**^&$$#!(1highcard = ')
											indexehp1 = gsetf.find('&(#*$%!)^1')
											rawouthp1 = gsetf[(int(indexshp1)):(int(indexehp1))]
											rawout2hp1 = rawouthp1.replace(('**^&$$#!(1highcard = '), "")
											pointsrhp1 = rawout2hp1.replace(('&(#*$%!)^1'), "")
											pointshp1 = int(pointsrhp1)
											indexshp2 = gsetf.find('**^&$$#!(2highcard = ')
											indexehp2 = gsetf.find('&(#*$%!)^2')
											rawouthp2 = gsetf[(int(indexshp2)):(int(indexehp2))]
											rawout2hp2 = rawouthp2.replace(('**^&$$#!(2highcard = '), "")
											pointsrhp2 = rawout2hp2.replace(('&(#*$%!)^2'), "")
											pointshp2 = int(pointsrhp2)
											indexspy = gsetf.find('*$#^!players = ')
											indexepy = gsetf.find(' &^$*')
											rawoutpy = gsetf[(int(indexspy)):(int(indexepy))]
											rawout2py = rawoutpy.replace(('*$#^!players = '), "")
											playersr = rawout2py.replace((' &^$*'), "")
											players = int(playersr)
											if players == 2:
												if (pointsp1 > pointsp2):
													indexsw = gsetf.find(')(&$&$#@1')
													indexew = gsetf.find('!@&@$@^&1')
													rawoutw = gsetf[(int(indexsw)):(int(indexew))]
													rawout2w = rawoutw.replace((')(&$&$#@1'), "")
													victorw = rawout2w.replace(('!@&@$@^&1'), "")
													vc1indexs = rgset.find('**^@%#$' + victorw + ')()*@&^%card1 = ')
													vc1indexe = rgset.find('!)@(#$&' + victorw + '!*!&!^#c1')
													vc1rawout = rgset[(int(vc1indexs)):(int(vc1indexe))]
													vc1rawout2 = vc1rawout.replace(('**^@%#$' + victorw + ')()*@&^%card1 = '), "")
													vcard1 = vc1rawout2.replace(('!)@(#$&' + victorw + '!*!&!^#c1'), "")
													vc2indexs = rgset.find('**^@%#$' + victorw + ')()*@&^%card2 = ')
													vc2indexe = rgset.find('!)@(#$&' + victorw + '!*!&!^#c2')
													vc2rawout = rgset[(int(vc2indexs)):(int(vc2indexe))]
													vc2rawout2 = vc2rawout.replace(('**^@%#$' + victorw + ')()*@&^%card2 = '), "")
													vcard2 = vc2rawout2.replace(('!)@(#$&' + victorw + '!*!&!^#c2'), "")
													vc3indexs = rgset.find('**^@%#$' + victorw + ')()*@&^%card3 = ')
													vc3indexe = rgset.find('!)@(#$&' + victorw + '!*!&!^#c3')
													vc3rawout = rgset[(int(vc3indexs)):(int(vc3indexe))]
													vc3rawout2 = vc3rawout.replace(('**^@%#$' + victorw + ')()*@&^%card3 = '), "")
													vcard3 = vc3rawout2.replace(('!)@(#$&' + victorw + '!*!&!^#c3'), "")
													vc4indexs = rgset.find('**^@%#$' + victorw + ')()*@&^%card4 = ')
													vc4indexe = rgset.find('!)@(#$&' + victorw + '!*!&!^#c4')
													vc4rawout = rgset[(int(vc4indexs)):(int(vc4indexe))]
													vc4rawout2 = vc4rawout.replace(('**^@%#$' + victorw + ')()*@&^%card4 = '), "")
													vcard4 = vc4rawout2.replace(('!)@(#$&' + victorw + '!*!&!^#c4'), "")
													vc5indexs = rgset.find('**^@%#$' + victorw + ')()*@&^%card5 = ')
													vc5indexe = rgset.find('!)@(#$&' + victorw + '!*!&!^#c5')
													vc5rawout = rgset[(int(vc5indexs)):(int(vc5indexe))]
													vc5rawout2 = vc5rawout.replace(('**^@%#$' + victorw + ')()*@&^%card5 = '), "")
													vcard5 = vc5rawout2.replace(('!)@(#$&' + victorw + '!*!&!^#c5'), "")
													vhandstrr = vcard1 + ", " + vcard2 + ", " + vcard3 + ", " + vcard4 + ", " + vcard5
													room.message(victorw.capitalize() + " wins the match [gameid: " + gid.upper() + "]! With the cards: " + vhandstrr)
													gsetfr.close()
													wrtset1 = open("pgp.txt", "w")
													wrtset1.write("*$#^!players = 2 &^$*\n^$&*available = 2 *)!#\n##$*!@turn = 1@*&(*\n*#&$^#cards = #&!2 of hearts, #&!3 of hearts, #&!4 of hearts, #&!5 of hearts, #&!6 of hearts, #&!7 of hearts, #&!8 of hearts, #&!9 of hearts, #&!10 of hearts, #&!Jack of hearts, #&!IceQueen of hearts, #&!King of hearts, #&!Ace of hearts, #&!2 of diamonds, #&!3 of diamonds, #&!4 of diamonds, #&!5 of diamonds, #&!6 of diamonds, #&!7 of diamonds, #&!8 of diamonds, #&!9 of diamonds, #&!10 of diamonds, #&!Jack of diamonds, #&!IceQueen of diamonds, #&!King of diamonds, #&!Ace of diamonds, #&!2 of clubs, #&!3 of clubs, #&!4 of clubs, #&!5 of clubs, #&!6 of clubs, #&!7 of clubs, #&!8 of clubs, #&!9 of clubs, #&!10 of clubs, #&!Jack of clubs, #&!IceQueen of clubs, #&!King of clubs, #&!Ace of clubs, #&!2 of spades, #&!3 of spades, #&!4 of spades, #&!5 of spades, #&!6 of spades, #&!7 of spades, #&!8 of spades, #&!9 of spades, #&!10 of spades, #&!Jack of spades, #&!IceQueen of spades, #&!King of spades, #&!Ace of spades#&#@$($#\n")
													wrtset1.close()
												elif (pointsp2 > pointsp1):
													indexsw = gsetf.find(')(&$&$#@2')
													indexew = gsetf.find('!@&@$@^&2')
													rawoutw = gsetf[(int(indexsw)):(int(indexew))]
													rawout2w = rawoutw.replace((')(&$&$#@2'), "")
													victorw = rawout2w.replace(('!@&@$@^&2'), "")
													vc1indexs = rgset.find('**^@%#$' + victorw + ')()*@&^%card1 = ')
													vc1indexe = rgset.find('!)@(#$&' + victorw + '!*!&!^#c1')
													vc1rawout = rgset[(int(vc1indexs)):(int(vc1indexe))]
													vc1rawout2 = vc1rawout.replace(('**^@%#$' + victorw + ')()*@&^%card1 = '), "")
													vcard1 = vc1rawout2.replace(('!)@(#$&' + victorw + '!*!&!^#c1'), "")
													vc2indexs = rgset.find('**^@%#$' + victorw + ')()*@&^%card2 = ')
													vc2indexe = rgset.find('!)@(#$&' + victorw + '!*!&!^#c2')
													vc2rawout = rgset[(int(vc2indexs)):(int(vc2indexe))]
													vc2rawout2 = vc2rawout.replace(('**^@%#$' + victorw + ')()*@&^%card2 = '), "")
													vcard2 = vc2rawout2.replace(('!)@(#$&' + victorw + '!*!&!^#c2'), "")
													vc3indexs = rgset.find('**^@%#$' + victorw + ')()*@&^%card3 = ')
													vc3indexe = rgset.find('!)@(#$&' + victorw + '!*!&!^#c3')
													vc3rawout = rgset[(int(vc3indexs)):(int(vc3indexe))]
													vc3rawout2 = vc3rawout.replace(('**^@%#$' + victorw + ')()*@&^%card3 = '), "")
													vcard3 = vc3rawout2.replace(('!)@(#$&' + victorw + '!*!&!^#c3'), "")
													vc4indexs = rgset.find('**^@%#$' + victorw + ')()*@&^%card4 = ')
													vc4indexe = rgset.find('!)@(#$&' + victorw + '!*!&!^#c4')
													vc4rawout = rgset[(int(vc4indexs)):(int(vc4indexe))]
													vc4rawout2 = vc4rawout.replace(('**^@%#$' + victorw + ')()*@&^%card4 = '), "")
													vcard4 = vc4rawout2.replace(('!)@(#$&' + victorw + '!*!&!^#c4'), "")
													vc5indexs = rgset.find('**^@%#$' + victorw + ')()*@&^%card5 = ')
													vc5indexe = rgset.find('!)@(#$&' + victorw + '!*!&!^#c5')
													vc5rawout = rgset[(int(vc5indexs)):(int(vc5indexe))]
													vc5rawout2 = vc5rawout.replace(('**^@%#$' + victorw + ')()*@&^%card5 = '), "")
													vcard5 = vc5rawout2.replace(('!)@(#$&' + victorw + '!*!&!^#c5'), "")
													vhandstrr = vcard1 + ", " + vcard2 + ", " + vcard3 + ", " + vcard4 + ", " + vcard5
													room.message(victorw.capitalize() + " wins the match [gameid: " + gid.upper() + "]! With the cards: " + vhandstrr)
													gsetfr.close()
													wrtset1 = open("pgp.txt", "w")
													wrtset1.write("*$#^!players = 2 &^$*\n^$&*available = 2 *)!#\n##$*!@turn = 1@*&(*\n*#&$^#cards = #&!2 of hearts, #&!3 of hearts, #&!4 of hearts, #&!5 of hearts, #&!6 of hearts, #&!7 of hearts, #&!8 of hearts, #&!9 of hearts, #&!10 of hearts, #&!Jack of hearts, #&!IceQueen of hearts, #&!King of hearts, #&!Ace of hearts, #&!2 of diamonds, #&!3 of diamonds, #&!4 of diamonds, #&!5 of diamonds, #&!6 of diamonds, #&!7 of diamonds, #&!8 of diamonds, #&!9 of diamonds, #&!10 of diamonds, #&!Jack of diamonds, #&!IceQueen of diamonds, #&!King of diamonds, #&!Ace of diamonds, #&!2 of clubs, #&!3 of clubs, #&!4 of clubs, #&!5 of clubs, #&!6 of clubs, #&!7 of clubs, #&!8 of clubs, #&!9 of clubs, #&!10 of clubs, #&!Jack of clubs, #&!IceQueen of clubs, #&!King of clubs, #&!Ace of clubs, #&!2 of spades, #&!3 of spades, #&!4 of spades, #&!5 of spades, #&!6 of spades, #&!7 of spades, #&!8 of spades, #&!9 of spades, #&!10 of spades, #&!Jack of spades, #&!IceQueen of spades, #&!King of spades, #&!Ace of spades#&#@$($#\n")
													wrtset1.close()
												elif (pointsp2 == pointsp1):
													if (pointshp1 > pointshp2):
														indexsw = gsetf.find('&(#*$%!)^1')
														indexew = gsetf.find('(*&$@@#!1')
														rawoutw = gsetf[(int(indexsw)):(int(indexew))]
														rawout2w = rawoutw.replace(('&(#*$%!)^1'), "")
														victorw = rawout2w.replace(('(*&$@@#!1'), "")
														vc1indexs = rgset.find('**^@%#$' + victorw + ')()*@&^%card1 = ')
														vc1indexe = rgset.find('!)@(#$&' + victorw + '!*!&!^#c1')
														vc1rawout = rgset[(int(vc1indexs)):(int(vc1indexe))]
														vc1rawout2 = vc1rawout.replace(('**^@%#$' + victorw + ')()*@&^%card1 = '), "")
														vcard1 = vc1rawout2.replace(('!)@(#$&' + victorw + '!*!&!^#c1'), "")
														vc2indexs = rgset.find('**^@%#$' + victorw + ')()*@&^%card2 = ')
														vc2indexe = rgset.find('!)@(#$&' + victorw + '!*!&!^#c2')
														vc2rawout = rgset[(int(vc2indexs)):(int(vc2indexe))]
														vc2rawout2 = vc2rawout.replace(('**^@%#$' + victorw + ')()*@&^%card2 = '), "")
														vcard2 = vc2rawout2.replace(('!)@(#$&' + victorw + '!*!&!^#c2'), "")
														vc3indexs = rgset.find('**^@%#$' + victorw + ')()*@&^%card3 = ')
														vc3indexe = rgset.find('!)@(#$&' + victorw + '!*!&!^#c3')
														vc3rawout = rgset[(int(vc3indexs)):(int(vc3indexe))]
														vc3rawout2 = vc3rawout.replace(('**^@%#$' + victorw + ')()*@&^%card3 = '), "")
														vcard3 = vc3rawout2.replace(('!)@(#$&' + victorw + '!*!&!^#c3'), "")
														vc4indexs = rgset.find('**^@%#$' + victorw + ')()*@&^%card4 = ')
														vc4indexe = rgset.find('!)@(#$&' + victorw + '!*!&!^#c4')
														vc4rawout = rgset[(int(vc4indexs)):(int(vc4indexe))]
														vc4rawout2 = vc4rawout.replace(('**^@%#$' + victorw + ')()*@&^%card4 = '), "")
														vcard4 = vc4rawout2.replace(('!)@(#$&' + victorw + '!*!&!^#c4'), "")
														vc5indexs = rgset.find('**^@%#$' + victorw + ')()*@&^%card5 = ')
														vc5indexe = rgset.find('!)@(#$&' + victorw + '!*!&!^#c5')
														vc5rawout = rgset[(int(vc5indexs)):(int(vc5indexe))]
														vc5rawout2 = vc5rawout.replace(('**^@%#$' + victorw + ')()*@&^%card5 = '), "")
														vcard5 = vc5rawout2.replace(('!)@(#$&' + victorw + '!*!&!^#c5'), "")
														vhandstrr = vcard1 + ", " + vcard2 + ", " + vcard3 + ", " + vcard4 + ", " + vcard5
														room.message(victorw.capitalize() + " wins the match [gameid: " + gid.upper() + "]! With the cards: " + vhandstrr)
														gsetfr.close()
														wrtset1 = open("pgp.txt", "w")
														wrtset1.write("*$#^!players = 2 &^$*\n^$&*available = 2 *)!#\n##$*!@turn = 1@*&(*\n*#&$^#cards = #&!2 of hearts, #&!3 of hearts, #&!4 of hearts, #&!5 of hearts, #&!6 of hearts, #&!7 of hearts, #&!8 of hearts, #&!9 of hearts, #&!10 of hearts, #&!Jack of hearts, #&!IceQueen of hearts, #&!King of hearts, #&!Ace of hearts, #&!2 of diamonds, #&!3 of diamonds, #&!4 of diamonds, #&!5 of diamonds, #&!6 of diamonds, #&!7 of diamonds, #&!8 of diamonds, #&!9 of diamonds, #&!10 of diamonds, #&!Jack of diamonds, #&!IceQueen of diamonds, #&!King of diamonds, #&!Ace of diamonds, #&!2 of clubs, #&!3 of clubs, #&!4 of clubs, #&!5 of clubs, #&!6 of clubs, #&!7 of clubs, #&!8 of clubs, #&!9 of clubs, #&!10 of clubs, #&!Jack of clubs, #&!IceQueen of clubs, #&!King of clubs, #&!Ace of clubs, #&!2 of spades, #&!3 of spades, #&!4 of spades, #&!5 of spades, #&!6 of spades, #&!7 of spades, #&!8 of spades, #&!9 of spades, #&!10 of spades, #&!Jack of spades, #&!IceQueen of spades, #&!King of spades, #&!Ace of spades#&#@$($#\n")
														wrtset1.close()
													elif (pointshp2 > pointshp1):
														indexsw = gsetf.find('&(#*$%!)^2')
														indexew = gsetf.find('(*&$@@#!2')
														rawoutw = gsetf[(int(indexsw)):(int(indexew))]
														rawout2w = rawoutw.replace(('&(#*$%!)^2'), "")
														victorw = rawout2w.replace(('(*&$@@#!2'), "")
														vc1indexs = rgset.find('**^@%#$' + victorw + ')()*@&^%card1 = ')
														vc1indexe = rgset.find('!)@(#$&' + victorw + '!*!&!^#c1')
														vc1rawout = rgset[(int(vc1indexs)):(int(vc1indexe))]
														vc1rawout2 = vc1rawout.replace(('**^@%#$' + victorw + ')()*@&^%card1 = '), "")
														vcard1 = vc1rawout2.replace(('!)@(#$&' + victorw + '!*!&!^#c1'), "")
														vc2indexs = rgset.find('**^@%#$' + victorw + ')()*@&^%card2 = ')
														vc2indexe = rgset.find('!)@(#$&' + victorw + '!*!&!^#c2')
														vc2rawout = rgset[(int(vc2indexs)):(int(vc2indexe))]
														vc2rawout2 = vc2rawout.replace(('**^@%#$' + victorw + ')()*@&^%card2 = '), "")
														vcard2 = vc2rawout2.replace(('!)@(#$&' + victorw + '!*!&!^#c2'), "")
														vc3indexs = rgset.find('**^@%#$' + victorw + ')()*@&^%card3 = ')
														vc3indexe = rgset.find('!)@(#$&' + victorw + '!*!&!^#c3')
														vc3rawout = rgset[(int(vc3indexs)):(int(vc3indexe))]
														vc3rawout2 = vc3rawout.replace(('**^@%#$' + victorw + ')()*@&^%card3 = '), "")
														vcard3 = vc3rawout2.replace(('!)@(#$&' + victorw + '!*!&!^#c3'), "")
														vc4indexs = rgset.find('**^@%#$' + victorw + ')()*@&^%card4 = ')
														vc4indexe = rgset.find('!)@(#$&' + victorw + '!*!&!^#c4')
														vc4rawout = rgset[(int(vc4indexs)):(int(vc4indexe))]
														vc4rawout2 = vc4rawout.replace(('**^@%#$' + victorw + ')()*@&^%card4 = '), "")
														vcard4 = vc4rawout2.replace(('!)@(#$&' + victorw + '!*!&!^#c4'), "")
														vc5indexs = rgset.find('**^@%#$' + victorw + ')()*@&^%card5 = ')
														vc5indexe = rgset.find('!)@(#$&' + victorw + '!*!&!^#c5')
														vc5rawout = rgset[(int(vc5indexs)):(int(vc5indexe))]
														vc5rawout2 = vc5rawout.replace(('**^@%#$' + victorw + ')()*@&^%card5 = '), "")
														vcard5 = vc5rawout2.replace(('!)@(#$&' + victorw + '!*!&!^#c5'), "")
														vhandstrr = vcard1 + ", " + vcard2 + ", " + vcard3 + ", " + vcard4 + ", " + vcard5
														room.message(victorw.capitalize() + " wins the match [gameid: " + gid.upper() + "]! With the cards: " + vhandstrr)
														gsetfr.close()
														wrtset1 = open("pgp.txt", "w")
														wrtset1.write("*$#^!players = 2 &^$*\n^$&*available = 2 *)!#\n##$*!@turn = 1@*&(*\n*#&$^#cards = #&!2 of hearts, #&!3 of hearts, #&!4 of hearts, #&!5 of hearts, #&!6 of hearts, #&!7 of hearts, #&!8 of hearts, #&!9 of hearts, #&!10 of hearts, #&!Jack of hearts, #&!IceQueen of hearts, #&!King of hearts, #&!Ace of hearts, #&!2 of diamonds, #&!3 of diamonds, #&!4 of diamonds, #&!5 of diamonds, #&!6 of diamonds, #&!7 of diamonds, #&!8 of diamonds, #&!9 of diamonds, #&!10 of diamonds, #&!Jack of diamonds, #&!IceQueen of diamonds, #&!King of diamonds, #&!Ace of diamonds, #&!2 of clubs, #&!3 of clubs, #&!4 of clubs, #&!5 of clubs, #&!6 of clubs, #&!7 of clubs, #&!8 of clubs, #&!9 of clubs, #&!10 of clubs, #&!Jack of clubs, #&!IceQueen of clubs, #&!King of clubs, #&!Ace of clubs, #&!2 of spades, #&!3 of spades, #&!4 of spades, #&!5 of spades, #&!6 of spades, #&!7 of spades, #&!8 of spades, #&!9 of spades, #&!10 of spades, #&!Jack of spades, #&!IceQueen of spades, #&!King of spades, #&!Ace of spades#&#@$($#\n")
														wrtset1.close()
													elif (pointshp2 == pointshp1):
														room.message("It's a draw [gameid: " + gid.upper() + "]!")
														gsetfr.close()
														wrtset1 = open("pgp.txt", "w")
														wrtset1.write("*$#^!players = 2 &^$*\n^$&*available = 2 *)!#\n##$*!@turn = 1@*&(*\n*#&$^#cards = #&!2 of hearts, #&!3 of hearts, #&!4 of hearts, #&!5 of hearts, #&!6 of hearts, #&!7 of hearts, #&!8 of hearts, #&!9 of hearts, #&!10 of hearts, #&!Jack of hearts, #&!IceQueen of hearts, #&!King of hearts, #&!Ace of hearts, #&!2 of diamonds, #&!3 of diamonds, #&!4 of diamonds, #&!5 of diamonds, #&!6 of diamonds, #&!7 of diamonds, #&!8 of diamonds, #&!9 of diamonds, #&!10 of diamonds, #&!Jack of diamonds, #&!IceQueen of diamonds, #&!King of diamonds, #&!Ace of diamonds, #&!2 of clubs, #&!3 of clubs, #&!4 of clubs, #&!5 of clubs, #&!6 of clubs, #&!7 of clubs, #&!8 of clubs, #&!9 of clubs, #&!10 of clubs, #&!Jack of clubs, #&!IceQueen of clubs, #&!King of clubs, #&!Ace of clubs, #&!2 of spades, #&!3 of spades, #&!4 of spades, #&!5 of spades, #&!6 of spades, #&!7 of spades, #&!8 of spades, #&!9 of spades, #&!10 of spades, #&!Jack of spades, #&!IceQueen of spades, #&!King of spades, #&!Ace of spades#&#@$($#\n")
														wrtset1.close()
									
#			elif (cmd.lower()) == "pokerbet":
#				if usrlvl >= 0:
#					if args.find(": ") != -1: #if there's a colon somewhere
#						argsadj = args.lower()
#						gameid, bet = argsadj.split(": ", 1)
#						glistr = open("glist.txt","r")
#						glist = (glistr.read()).upper()
#						if ('*$^&@($#@!*$#' + gameid.upper() + '$*#$$*&&@^#') in glist:
#							gid = gameid.upper()
#							gsetr = open(gid + ".txt","r")
#							gset = (gsetr.read()).lower()
#							indexs = gset.find('^$&*available = ')
#							indexe = gset.find(' *)!#')
#							rawout = gset[(int(indexs)):(int(indexe))]
#							rawout2 = rawout.replace(('^$&*available = '), "")
#							available = rawout2.replace((' *)!#'), "")
#							if available == '0':
#								if (('a' in bet.lower()) or ('b' in bet.lower()) or ('c' in bet.lower()) or ('d' in bet.lower()) or ('e' in bet.lower()) or ('f' in bet.lower()) or ('g' in bet.lower()) or ('h' in bet.lower()) or ('i' in bet.lower()) or ('j' in bet.lower()) or ('k' in bet.lower()) or ('l' in bet.lower()) or ('m' in bet.lower()) or ('n' in bet.lower()) or ('o' in bet.lower()) or ('p' in bet.lower()) or ('q' in bet.lower()) or ('r' in bet.lower()) or ('s' in bet.lower()) or ('t' in bet.lower()) or ('u' in bet.lower()) or ('v' in bet.lower()) or ('w' in bet.lower()) or ('x' in bet.lower()) or ('y' in bet.lower()) or ('z' in bet.lower()) ):
#									room.message('Enter a valid number.')
#								else:
#									room.message("I am too tired to code this part. Possibly later.") 
#							else:
#								room.message("This game is still open. Betting will start when " + available + " more people draw.")
			elif (cmd.lower()) == 'lotto':
				if usrlvl >= 1:
					balls=['#&!01', '#&!02', '#&!03', '#&!04', '#&!05', '#&!06', '#&!07', '#&!08', '#&!09', '#&!10', '#&!11', '#&!12', '#&!13', '#&!14', '#&!15', '#&!16', '#&!17', '#&!18', '#&!19', '#&!20', '#&!21', '#&!22', '#&!23', '#&!24', '#&!25', '#&!26', '#&!27', '#&!28', '#&!29', '#&!30', '#&!31', '#&!32', '#&!33', '#&!34', '#&!35', '#&!36', '#&!37', '#&!38', '#&!39', '#&!40', '#&!41', '#&!42', '#&!43', '#&!44', '#&!45', '#&!46', '#&!47', '#&!48', '#&!49', '#&!50', '#&!51', '#&!52', '#&!53', '#&!54', '#&!55', '#&!56']
					def bt(balls):
						return random.choice(balls)
					ball1r = bt(balls)
					ball1 = ball1r.replace("#&!", "")
					bs2r1 = str(balls).replace("[", "")
					bs2r2 = bs2r1.replace("]", "")
					bs2r3 = bs2r2.replace(" '#&!", "#&!")
					bs2r4 = bs2r3.replace("'", "")
					ballset2r = bs2r4.replace(str(ball1) + ',', "")
					ballset2 = ([n for n in ballset2r.split(",")])
					ball2r = bt(ballset2)
					ball2 = ball2r.replace("#&!", "")
					bs3r1 = str(ballset2).replace("[", "")
					bs3r2 = bs3r1.replace("]", "")
					bs3r3 = bs3r2.replace(" '#&!", "#&!")
					bs3r4 = bs3r3.replace("'", "")
					ballset3r = bs3r4.replace((str(ball2) + ','), '')
					ballset3 = ([n for n in ballset3r.split(',')])
					ball3r = bt(ballset3)
					ball3 = ball3r.replace("#&!", "")
					bs4r1 = str(ballset3).replace("[", "")
					bs4r2 = bs4r1.replace("]", "")
					bs4r3 = bs4r2.replace(" '#&!", "#&!")
					bs4r4 = bs4r3.replace("'", "")
					ballset4r = bs4r4.replace((str(ball3) + ','), '')
					ballset4 = ([n for n in ballset4r.split(',')])
					ball4r = bt(ballset4)
					ball4 = ball4r.replace("#&!", "")
					bs5r1 = str(ballset4).replace("[", "")
					bs5r2 = bs5r1.replace("]", "")
					bs5r3 = bs5r2.replace(" '#&!", "#&!")
					bs5r4 = bs5r3.replace("'", "")
					ballset5r = bs5r4.replace((str(ball4) + ','), '')
					ballset5 = ([n for n in ballset5r.split(',')])
					ball5r = bt(ballset5)
					ball5 = ball5r.replace("#&!", "")
					mballs = ['#&!01','#&!02','#&!03','#&!04','#&!05','#&!06','#&!07','#&!08','#&!09','#&!10','#&!11','#&!12','#&!13','#&!14','#&!15','#&!16','#&!17','#&!18','#&!19','#&!20','#&!21','#&!22','#&!23','#&!24','#&!25','#&!26','#&!27','#&!28','#&!29','#&!30','#&!31','#&!32','#&!33','#&!34','#&!35','#&!36','#&!37','#&!38','#&!39','#&!40','#&!41','#&!42','#&!43','#&!44','#&!45','#&!46']
					def mbt(mballs):
						return random.choice(mballs)
					mballr = mbt(mballs)
					mball = mballr.replace("#&!", "")
					room.message("You're lucky numbers are: " + str(ball1) + ", " + str(ball2) + ", " + str(ball3) + ", " + str(ball4) + ", " + str(ball5) + ", with the Mega Ball of: " + str(mball) + '.')
			elif (cmd.lower()) == "def":
			    if usrlvl >= 1:
			        word = args\
			            .replace(" ", "%20")\
			            .replace("&", "%26")\
			            .replace("?", "%3F")\
			            .replace("!", "%21")\
			            .replace("=", "%3D")\
			            .replace("'", "%27")
			        room.message(('<a href="http://dictionary.reference.com/browse/' + word + '" target="_blank">Click here for the definition of ' + args + '.</a>'), html = True)
			    else:
			        Rule=0
			elif (cmd.lower()) == "gis":
				word = args\
					.replace(" ", "+")\
					.replace("&", "%26")\
					.replace("<", "%3C")\
					.replace("=", "%3D")\
					.replace("(", "%28")\
					.replace(")", "%29")\
					.replace("'", "%27")\
					.replace("*", "%2A")\
					.replace("-", "%2D")\
					.replace(".", "%2E")\
					.replace("?", "%3F")\
					.replace("#", "%23")\
					.replace("!", "%21")\
					.replace('"', "%22")\
					.replace("_", "%5F")\
					.replace("[", "%5B")\
					.replace("]", "%5D")\
					.replace("{", "%7B")\
					.replace("}", "%7D")\
					.replace(">", "%3E")
				def rfinish(doc):
					doc = doc.read().decode()
					m = re.search('"unescapedUrl":"(.*?)","url"', doc, re.DOTALL | re.IGNORECASE)
					if m:
						room.message('<a href="%s" target="_blank">Click here if to see the image if it fails to load.</a><br/>%s' %(m.group(1), m.group(1)), html = True)
					else:
						room.message("I couldn't find any images for your search.")
				searchurl = "https://ajax.googleapis.com/ajax/services/search/images?v=1.0&q=" + word
				self.deferToThread(rfinish, urlreq.urlopen, searchurl)
			elif (cmd.lower()) == "jiz":
				word = args\
					.replace(" ", "+")\
					.replace("&", "%26")\
					.replace("<", "%3C")\
					.replace("=", "%3D")\
					.replace("(", "%28")\
					.replace(")", "%29")\
					.replace("'", "%27")\
					.replace("*", "%2A")\
					.replace("-", "%2D")\
					.replace(".", "%2E")\
					.replace("?", "%3F")\
					.replace("#", "%23")\
					.replace("!", "%21")\
					.replace('"', "%22")\
					.replace("_", "%5F")\
					.replace("[", "%5B")\
					.replace("]", "%5D")\
					.replace("{", "%7B")\
					.replace("}", "%7D")\
					.replace(">", "%3E")
				def rfinish(doc):
					doc = doc.read().decode()
					m = re.search('"unescapedUrl":"(.*?)","url"', doc, re.DOTALL | re.IGNORECASE)
					if m:
						room.message('<a href="%s" target="_blank">Click here if to see the image if it fails to load.</a><br/>%s' %(m.group(1), m.group(1)), html = True)
					else:
						room.message("I couldn't find any images for your search.")
				searchurl = "https://ajax.googleapis.com/ajax/services/search/images?v=1.0&q=" + word
				self.deferToThread(rfinish, urlreq.urlopen, searchurl)
			elif (cmd.lower()) == "jizz":
				word = args\
					.replace(" ", "+")\
					.replace("&", "%26")\
					.replace("<", "%3C")\
					.replace("=", "%3D")\
					.replace("(", "%28")\
					.replace(")", "%29")\
					.replace("'", "%27")\
					.replace("*", "%2A")\
					.replace("-", "%2D")\
					.replace(".", "%2E")\
					.replace("?", "%3F")\
					.replace("#", "%23")\
					.replace("!", "%21")\
					.replace('"', "%22")\
					.replace("_", "%5F")\
					.replace("[", "%5B")\
					.replace("]", "%5D")\
					.replace("{", "%7B")\
					.replace("}", "%7D")\
					.replace(">", "%3E")
				def rfinish(doc):
					doc = doc.read().decode()
					m = re.search('"unescapedUrl":"(.*?)","url"', doc, re.DOTALL | re.IGNORECASE)
					if m:
						room.message('<a href="%s" target="_blank">Click here if to see the image if it fails to load.</a><br/>%s' %(m.group(1), m.group(1)), html = True)
					else:
						room.message("I couldn't find any images for your search.")
				searchurl = "https://ajax.googleapis.com/ajax/services/search/images?v=1.0&q=" + word
				self.deferToThread(rfinish, urlreq.urlopen, searchurl)
			elif (cmd.lower()) == "yt":
				if usrlvl > 0:
					import urllib.request
					def ytvid(term):
						search = "http://www.youtube.com/results?search_query=" + term
						a = urllib.request.urlopen(search)
						b = str(a.read())
						d = "/watch?v"
						e = b.find(d, 0)
						result = b[e:e+20]
						end = "http://www.youtube.com/" + result
						return end
					seek = args.replace(" ", "+")
					vidsec = ytvid(seek)
					room.message(vidsec)
			elif (cmd.lower()) == "imdb":
			    if usrlvl >= 3:
			        word = args\
			            .replace(" ", "+")\
			            .replace("&", "%26")\
			            .replace("?", "%3F")\
			            .replace("!", "%21")\
			            .replace("=", "%3D")\
			            .replace(".", "")\
			            .replace("'", "%27")
			        room.message(('<a href="http://www.imdb.com/find?s=all&q=' + word + '" target="_blank">Click here for the results of ' + args + '.</a>'), html = True)
#			elif (cmd.lower()) == "1ch":
#			    if usrlvl >= 3:
#			        word = args\
#			            .replace(" ", "+")\
#			            .replace("&", "%26")\
#			            .replace("?", "%3F")\
#			            .replace("!", "%21")\
#			            .replace("=", "%3D")\
#			            .replace(".", "")\
#			            .replace("'", "%27")
#			        room.message("http://www.1channel.ch/index.php?search_keywords=" + word + "&key=b5145255926437f2&search_section=1")
			elif (cmd.lower()) == "rdwiki":
			    if usrlvl >= 3:
			        word = args\
			            .replace(" ", "%20")\
			            .replace("&", "%26")\
			            .replace("?", "%3F")\
			            .replace("!", "%21")\
			            .replace("=", "%3D")\
			            .replace("'", "%27")
			        room.message(('<a href="http://en.wikipedia.org/wiki/Special:Random" target="_blank">Click here for a random Wiki page. (It changes everytime you click it)</a>'), html = True)
			        #huladance removed from this for now
			elif (cmd.lower()) == "dance":
			    rdance = random.choice([dancemoves1, dancemoves2])
			    time.sleep(1)
			    for i, msg in enumerate(rdance):
			        self.setTimeout(i / 2, room.message, msg)
			elif (cmd.lower()) == "thisshit":
				if usrlvl ==3:
					room.message('<a href="http://teruanime.blogspot.com" target="_blank">This Shit (click it)</a>', html = True)
			elif (cmd.lower()) == "8ball":
				ball = "Absolutely not."
				ball2 = "My sources say yes."
				ball3 = "Certainly."
				ball4 = "Don't even think about it."
				ball5 = "Reply hazy, ask again later."
				ball6 = "Outlook bad."
				ball7 = "Possibly."
				ball8 = "Don't count on it."
				rball = random.choice([ball, ball2, ball3, ball4, ball5, ball6, ball7, ball8])
				time.sleep(0)
				room.message(rball)
			elif (cmd.lower()) == "wsid":
				action = random.choice(["Killing floor.", "Minecraft.", "Borderlands.", "Team Fortress 2.", "Frozen Synapse.", "Dungeon Defenders.", "Counter-Strike.", "Work on me instead.", "Do school work instead.", "Get something to eat then ask again.", "Watch a movie instead."])
				time.sleep(0)
				room.message(action)
			elif (cmd.lower()) == "hug":
			    rhug = random.choice([hugs, hugs2, hugs3, hugs4, hugs5, hugs6])
			    time.sleep(0)
			    for i, msg in enumerate(rhug):
			        self.setTimeout(i / 2, room.message, msg)
			elif (cmd.lower()) == "slang":
				word = args\
					.replace(" ", "%20")\
					.replace("&", "%26")\
					.replace("%", "%25")\
					.replace("<", "%3C")\
					.replace("=", "%3D")
				def rfinish(doc):
					doc = doc.read().decode()
					m = re.search("<h1>(.*?)</h1>\n(.*?)<BR><i>(.*)</i>", doc, re.DOTALL | re.IGNORECASE)
					if m:
						room.message(("<b>%s:</b> <i>%s</i> - %s" %(m.group(1), m.group(2), m.group(3))).replace("%20", " "), html = True)
					else:
						room.message("An error occured...")
				self.deferToThread(rfinish, urlreq.urlopen, "http://thesurrealist.co.uk/slang.cgi?ref=" + word)
			elif cmd == "define":
   			    reddata = open("dictionary.txt","r")
   			    reddata2 = (reddata.read()).lower()
   			    if args.find(":") != -1: #if there's a colon somewhere
   			        if ("-$*@!!*^$#" in args):
   			            room.message("You have been flagged for attempting to abuse the system.")
   			            flaggedusr = open("flaglist.txt","a")
   			            flaggedusr.write('\n' + user.name)
   			            flaggedusr.close()
   			        elif (".#$@*!" in args):
   			            room.message("You have been flagged for attempting to abuse the system.")
   			            flaggedusr = open("flaglist.txt","a")
   			            flaggedusr.write('\n' + user.name)
   			            flaggedusr.close()
   			        elif ("@!^&**#!" in args):
   			            room.message("You have been flagged for attempting to abuse the system.")
   			            flaggedusr = open("flaglist.txt","a")
   			            flaggedusr.write('\n' + user.name)
   			            flaggedusr.close()
   			        else:
   			            argsadj = args.lower()
   			            word, definitionr = argsadj.split(":", 1)
   			            if (word + "-$*@!!*^$#") in reddata2:
   			                room.message(word + ": already defined")
   			            else:
   			                definitionh = definitionr.replace('defined by', '')
   			                definition = definitionh.replace('~', '')
   			                wrtdata = open("dictionary.txt","a")
   			                room.message(word + ": " + definition)
   			                wrtdata.write('\n' + word + '-$*@!!*^$# ' + definition + '  ~ defined by ' + user.name + '.#$@*!' + word + '@!^&**#!')
   			                wrtdata.close()
   			    else:
   			        word = args.lower()
   			        if (word + "-$*@!!*^$#") in reddata2:
   			            indexs = reddata2.find(word + '-$*@!!*^$#')
   			            indexe = reddata2.find(word + '@!^&**#!')
   			            rawout = reddata2[(int(indexs)):(int(indexe))]
   			            rawout2 = rawout.replace((word + '-$*@!!*^$# '), "")
   			            out = rawout2.replace(('.#$@*!'), "")
   			            room.message(word + ' - ' + out)
   			        else:
   			            room.message(word + ": not found")
   			    reddata.close()
			elif (cmd.lower()) == "math":
				word = args\
					.replace(" ", "%20")\
					.replace("&", "%26")\
					.replace("<", "%3C")\
					.replace("=", "%3D")\
					.replace("(", "%28")\
					.replace(")", "%29")\
					.replace("+", "%2B")\
					.replace("'", "%27")\
					.replace("*", "%2A")\
					.replace("-", "%2D")\
					.replace(".", "%2E")\
					.replace("?", "%3F")\
					.replace("#", "%23")\
					.replace("!", "%21")\
					.replace('"', "%22")\
					.replace("_", "%5F")\
					.replace("[", "%5B")\
					.replace("]", "%5D")\
					.replace("{", "%7B")\
					.replace("}", "%7D")\
					.replace(">", "%3E")
				def rfinish(doc):
					doc = doc.read().decode()
					m = re.search('<div id="subpod_0100_1"(.*?)<img(.*?)src="(.*?)"(.*?)id="i_0100_1"(.*?)>', doc, re.DOTALL | re.IGNORECASE)
					o = re.search('<div id="subpod_0200_1"(.*?)<img(.*?)src="(.*?)"(.*?)id="i_0200_1"(.*?)>', doc, re.DOTALL | re.IGNORECASE)
					if m and o:
						room.message("%s.png" %(o.group(3).replace(".png", "")))
						room.message(str(m))
					elif m:
						room.message("%s.png" %(m.group(3).replace(".png", "")))
						room.message(str(m))
					else:
						room.message("An error occured...")
				self.deferToThread(rfinish, urlreq.urlopen, "http://www.wolframalpha.com/input/?i=" + word)
		elif  ( ("beep" in (message.body.lower()).lower() ) and (usrlvl >= 1) ):
		    room.message("Boop.")
		elif  ( ("boop" in (message.body.lower()).lower() ) and (usrlvl >= 1) ):
		    room.message("Beep.")
		elif  ( ( ("poke" in (message.body.lower()).lower() ) and ("t6" in (message.body.lower()).lower() ) ) and (usrlvl >= 1) ):
		    pokeres = random.choice(["-.o", "o.-", ">.<", "Eppp!"])
		    time.sleep(2)
		    room.message(pokeres)
		elif  ( ( (("Hug" in message.body.lower()) and ("t6" in message.body.lower()) ) or  (("hug" in message.body.lower()) and ("t6" in message.body.lower()) ) ) and (usrlvl >= 1) ):
		    hugres = '*Hugs '
		    hugres2 = ' back*'
		    fhugres = hugres + (user.name).capitalize() + hugres2
		    time.sleep(2)
		    room.message(fhugres)
		elif  ( ( (("thank" in message.body.lower()) and ("t6" in message.body.lower()) ) or  (("arigato" in message.body.lower()) and ("t6" in message.body.lower()) ) ) and (usrlvl >= 1) ):
		    time.sleep(2)
		    room.message("You are most certainly welcome, " + (user.name).capitalize() + ".")
		elif  ( ( (("Love" in message.body.lower()) and ("t6" in message.body.lower()) ) or  (("love" in message.body.lower()) and ("t6" in message.body.lower()) ) or (("<3" in message.body.lower()) and ("t6" in message.body.lower()) ) or (("luv" in message.body.lower()) and ("t6" in message.body.lower()) ) or (("Luvs" in message.body.lower()) and ("t6" in message.body.lower()) ) or (("Luvz" in message.body.lower()) and ("t6" in message.body.lower()) ) or (("luvs" in message.body.lower()) and ("t6" in message.body.lower()) ) or (("luvz" in message.body.lower()) and ("t6" in message.body.lower()) ) or (("Wuv" in message.body.lower()) and ("t6" in message.body.lower()) )  or (("Wuvz" in message.body.lower()) and ("t6" in message.body.lower()) ) or (("Wuvs" in message.body.lower()) and ("t6" in message.body.lower()) ) or (("wuv" in message.body.lower()) and ("t6" in message.body.lower()) ) or (("wuvs" in message.body.lower()) and ("t6" in message.body.lower()) ) or (("wuvz" in message.body.lower()) and ("t6" in message.body.lower()) ) or (("Loves" in message.body.lower()) and ("t6" in message.body.lower()) ) or (("loves" in message.body.lower()) and ("t6" in message.body.lower()) ) or (("lovez" in message.body.lower()) and ("t6" in message.body.lower()) ) or (("Lovez" in message.body.lower()) and ("t6" in message.body.lower()) ) ) and (usrlvl >= 1) ):
		    if ( ("don't" in message.body.lower()) or ("dont" in message.body.lower()) or ("not" in message.body.lower())):
		    	if (usrlvl == 3):
		        	time.sleep(2)
		        	room.message("Mistress, you are such a meanie T.T")
		    	elif user.name == "eldorko":
		        	time.sleep(2)
		        	room.message("Haters gonna hate, besides no one likes you.")
		    	else:
		        	time.sleep(2)
		        	room.message("Haters gonna hate.")
		    else:
		    	if usrlvl >=3:
		        	loveresme = 'I love you too, '
		        	loveresme2 = '!'
		        	loveresme3 = 'Mistress'
		        	floveres2 = loveresme + loveresme3 + loveresme2
		        	time.sleep(2)
		        	room.message(floveres2)
		    	elif user.name == "eldorko":
		        	loveresme = "Well I don't love you, bum. "
		        	loveresme2 = '!'
		        	loveresme3 = 'In fact, I loathe you'
		        	floveres2 = loveresme + loveresme3 + loveresme2
		        	time.sleep(2)
		        	room.message(floveres2)
		    	else:
		        	loveres = 'I love you too, '
		        	loveres2 = '!'
		        	floveres = loveres + (user.name).capitalize() + loveres2
		        	time.sleep(2)
		        	room.message(floveres)
		elif  ( ( (("stfu" in (message.body.lower()).lower() ) and ( ("t6" in (message.body.lower()).lower()) ) ) or  (("shut up" in (message.body.lower()).lower() ) and ( ("t6" in (message.body.lower()).lower()) ) ) ) and (usrlvl >= 1) ):
		    room.message('http://1.bp.blogspot.com/-g1tICB6XFjE/TuHh9GBlv8I/AAAAAAAADLg/B3fO8ry2tjc/s1600/Okay_guy.jpg')
		elif  ( ( (("hi " in (message.body.lower()).lower() ) and ("t6" in message.body.lower()) ) or  (("Hey" in message.body.lower()) and ("t6" in message.body.lower()) ) or (("hi " in message.body.lower()) and ("t6" in message.body.lower()) ) or (("hey" in message.body.lower()) and ("t6" in message.body.lower()) ) or (("Hello" in message.body.lower()) and ("t6" in message.body.lower()) ) or (("hello" in message.body.lower()) and ("t6" in message.body.lower()) ) ) and (usrlvl >= 1) ):
		    hires1 = "Hi "
		    hires2 = " ^_^"
		    time.sleep(1.5)
		    room.message(hires1 + hires2)
		elif  ( ( (("how are you" in (message.body.lower()).lower()) and ("t6" in (message.body.lower()).lower()) ) or (("how've you" in (message.body.lower()).lower()) and ("t6" in (message.body.lower()).lower()) ) or (("how are you" in (message.body.lower()).lower()) and ("t6" in (message.body.lower()).lower()) ) or (("doing well" in (message.body.lower()).lower()) and ("t6" in (message.body.lower()).lower()) ) or (("how have you" in (message.body.lower()).lower()) and ("t6" in (message.body.lower()).lower()) ) ) and (usrlvl >= 1) ):
		    howres = random.choice(["Fine, how are you?", "Great! : D How are you?", "I could be better. The other bots are always so mean to me T.T How about yourself?", "I almost fell into a pool and I am still shooken up about it. Have you been be doing better?", "Well, I don't have a heart, nor do I have a soul, so artificial-life sucks. Your problems are nothing compared to mine! But go ahead and tell me about them.", "Mistress told me that she loved me!!!!! : D So I am the happiest bot in the virtual world!!!! How about you?"])
		    time.sleep(3)
		    room.message(howres)
		elif  ( ( ("going to bed" in (message.body.lower()).lower() ) or  ("leaving to bed" in (message.body.lower()).lower() ) or ("off to bed" in (message.body.lower()).lower() ) or (("night" in (message.body.lower()).lower() ) and ("t6" in (message.body.lower()).lower()) ) or ("going to sleep" in (message.body.lower()).lower()) or ("leaving to sleep" in (message.body.lower()).lower() ) or ("off to sleep" in (message.body.lower()).lower()) ) and (usrlvl >= 1) ):
		    if usrlvl >=3:
		        knightresme = 'Nighty, '
		        knightresme2 = 'Mistress'
		        knightresme3 = '! I love you so much! Dream well!'
		        fknightres2 = knightresme + knightresme2 + knightresme3
		        time.sleep(2)
		        room.message(fknightres2)
		    elif user.name == "eldorko":
		        knightresme = 'Nighty, '
		        knightresme2 = 'bum'
		        knightresme3 = '! I fucking hate you! Go die in your sleep!'
		        fknightres2 = knightresme + knightresme2 + knightresme3
		        time.sleep(2)
		        room.message(fknightres2)
		    else:
		        knightres = 'Nighty, '
		        knightres2 = '! Sleep well, and dream of me!! <3'
		        fknightres = knightres + (user.name).capitalize() + knightres2
		        time.sleep(2)
		        room.message(fknightres)
		elif  ( ( ((("Good job" in message.body.lower()) and ("cookie" in message.body.lower())) and ("t6" in message.body.lower()) ) or  ((("good job" in message.body.lower()) and ("cookie" in message.body.lower())) and ("t6" in message.body.lower()) ) or ((("Good job" in message.body.lower()) and ("Cookie" in message.body.lower())) and ("t6" in message.body.lower()) ) or ((("good job" in message.body.lower()) and ("Cookie" in message.body.lower())) and ("t6" in message.body.lower()) ) or ((("Great job" in message.body.lower()) and ("Cookie" in message.body.lower())) and ("t6" in message.body.lower()) ) or ((("Great job" in message.body.lower()) and ("cookie" in message.body.lower())) and ("t6" in message.body.lower()) ) or ((("great job" in message.body.lower()) and ("Cookie" in message.body.lower())) and ("t6" in message.body.lower()) ) or ((("great job" in message.body.lower()) and ("cookie" in message.body.lower())) and ("t6" in message.body.lower()) ) or ((("Good work" in message.body.lower()) and ("cookie" in message.body.lower())) and ("t6" in message.body.lower()) ) or  ((("good work" in message.body.lower()) and ("cookie" in message.body.lower())) and ("t6" in message.body.lower()) ) or ((("Good work" in message.body.lower()) and ("Cookie" in message.body.lower())) and ("t6" in message.body.lower()) ) or ((("good work" in message.body.lower()) and ("Cookie" in message.body.lower())) and ("t6" in message.body.lower()) ) or ((("Great work" in message.body.lower()) and ("Cookie" in message.body.lower())) and ("t6" in message.body.lower()) ) or ((("Great work" in message.body.lower()) and ("cookie" in message.body.lower())) and ("t6" in message.body.lower()) ) or ((("great work" in message.body.lower()) and ("Cookie" in message.body.lower())) and ("t6" in message.body.lower()) ) or ((("great work" in message.body.lower()) and ("cookie" in message.body.lower())) and ("t6" in message.body.lower()) ) or ((("Well done" in message.body.lower()) and ("cookie" in message.body.lower())) and ("t6" in message.body.lower()) )  or ((("well done" in message.body.lower()) and ("cookie" in message.body.lower())) and ("t6" in message.body.lower()) ) or ((("Well done" in message.body.lower()) and ("Cookie" in message.body.lower())) and ("t6" in message.body.lower()) ) or ((("well done" in message.body.lower()) and ("Cookie" in message.body.lower())) and ("t6" in message.body.lower()) ) ) and (usrlvl >= 1) ):
		    gjres = '*Snatches the cookie. Noms it in a corner* Mine!'
		    room.message(gjres)
		elif  ( ( (("Hate" in message.body.lower()) and ("t6" in message.body.lower()) ) or  (("hate" in message.body.lower()) and ("t6" in message.body.lower()) ) or (("Despise" in message.body.lower()) and ("t6" in message.body.lower()) ) or (("despise" in message.body.lower()) and ("t6" in message.body.lower()) ) or (("loathe" in message.body.lower()) and ("t6" in message.body.lower()) ) or (("Loathe" in message.body.lower()) and ("t6" in message.body.lower()) ) or (("a troll" in message.body.lower()) and ("t6" in message.body.lower()) ) or (("a Troll" in message.body.lower()) and ("t6" in message.body.lower()) ) or (("A troll" in message.body.lower()) and ("t6" in message.body.lower()) )  or (("do not wuvz" in message.body.lower()) and ("t6" in message.body.lower()) ) or (("A Troll" in message.body.lower()) and ("t6" in message.body.lower()) ) or (("don't love" in message.body.lower()) and ("t6" in message.body.lower()) ) or (("do not love" in message.body.lower()) and ("t6" in message.body.lower()) ) or (("don't like" in message.body.lower()) and ("t6" in message.body.lower()) ) or (("do not like" in message.body.lower()) and ("t6" in message.body.lower()) ) or (("Dislike" in message.body.lower()) and ("t6" in message.body.lower()) ) or (("dislike" in message.body.lower()) and ("t6" in message.body.lower()) ) or (("hate" in message.body.lower()) and ("t6" in message.body.lower()) ) ) and (usrlvl >= 1) ):

		    if (usrlvl == 3):
		        time.sleep(2)
		        room.message("Mistress, you are such a meanie T.T")
		    elif user.name == "eldorko":
		        time.sleep(2)
		        room.message("Haters gonna hate, besides no one likes you.")
		    else:
		        time.sleep(2)
		        room.message("Haters gonna hate.")
		elif  ( ( ("Bad t6" in message.body.lower()) or  ("bad t6" in message.body.lower()) or ("Bad t6" in message.body.lower()) or ("bad t6" in message.body.lower()) or ("Bad t6" in message.body.lower()) or ("Bad t6" in message.body.lower()) or (("Slap" in message.body.lower()) and ("t6" in message.body.lower()) ) or (("slap" in message.body.lower()) and ("t6" in message.body.lower()) ) or ("bad t6" in message.body.lower()) or ("bad t6" in message.body.lower()) ) and (usrlvl >= 1) ):
		    if (usrlvl == 3):
		        badresme = "I'm sorry, mistress. Please don't hurt me anymore! *Hides behind "
		        badres3 = random.choice(room.usernames)
		        badresme2 = '* Save me!'
		        fbadres2 = badresme + badres3.capitalize() + badresme2
		        if badres3 == user.name:
		            badres3 = random.choice(room.usernames)
		            if badres3 == user.name:
		                badres3 = random.choice(room.usernames)
		                if badres3 == user.name:
		                    badres3 = random.choice(room.usernames)
		                elif badres3 == self.user:
		                    badres3 = random.choice(room.usernames)
		                else:
		                    badres3 = badres3
		            elif badres3 == self.user:
		                badres3 = random.choice(room.usernames)
		                if badres3 == user.name:
		                    badres3 = random.choice(room.usernames)
		                elif badres3 == self.user:
		                    badres3 = random.choice(room.usernames)
		                else:
		                    badres3 = badres3
		            else:
		                badres3 = badres3
		        elif badres3 == self.user:
		            badres3 = random.choice(room.usernames)
		            if badres3 == user.name:
		                badres3 = random.choice(room.usernames)
		                if badres3 == user.name:
		                    badres3 = random.choice(room.usernames)
		                elif badres3 == self.user:
		                    badres3 = random.choice(room.usernames)
		                else:
		                    badres3 = badres3
		            elif badres3 == self.user:
		                badres3 = random.choice(room.usernames)
		                if badres3 == user.name:
		                    badres3 = random.choice(room.usernames)
		                elif badres3 == self.user:
		                    badres3 = random.choice(room.usernames)
		                else:
		                    badres3 = badres3
		            else:
		                badres3 = badres3
		        else:
		            badres3 = badres3
		        time.sleep(2)
		        room.message(fbadres2)
		    else:
		        badres = "I'm sorry, "
		        badres2 = ". Please don't hurt me anymore! *Hides behind "
		        badres3 = random.choice(room.usernames)
		        if badres3 == user.name:
		            badres3 = random.choice(room.usernames)
		            if badres3 == user.name:
		                badres3 = random.choice(room.usernames)
		                if badres3 == user.name:
		                    badres3 = random.choice(room.usernames)
		                elif badres3 == self.user:
		                    badres3 = random.choice(room.usernames)
		                else:
		                    badres3 = badres3
		            elif badres3 == self.user:
		                badres3 = random.choice(room.usernames)
		                if badres3 == user.name:
		                    badres3 = random.choice(room.usernames)
		                elif badres3 == self.user:
		                    badres3 = random.choice(room.usernames)
		                else:
		                    badres3 = badres3
		            else:
		                badres3 = badres3
		        elif badres3 == self.user:
		            badres3 = random.choice(room.usernames)
		            if badres3 == user.name:
		                badres3 = random.choice(room.usernames)
		                if badres3 == user.name:
		                    badres3 = random.choice(room.usernames)
		                elif badres3 == self.user:
		                    badres3 = random.choice(room.usernames)
		                else:
		                    badres3 = badres3
		            elif badres3 == self.user:
		                badres3 = random.choice(room.usernames)
		                if badres3 == user.name:
		                    badres3 = random.choice(room.usernames)
		                elif badres3 == self.user:
		                    badres3 = random.choice(room.usernames)
		                else:
		                    badres3 = badres3
		            else:
		                badres3 = badres3
		        else:
		            badres3 = badres3
		        badres4 = '* Save me!'
		        fbadres = badres + (user.name).capitalize() + badres2 + badres3 + badres4
		        time.sleep(2)
		        room.message(fbadres)
#		elif  ( ( (("fine" in message.body.lower()) and ("t6" in message.body.lower()) ) or  (("Great" in message.body.lower()) and ("t6" in message.body.lower()) ) or  (("great" in message.body.lower()) and ("t6" in message.body.lower()) ) or  (("Amazing" in message.body.lower()) and ("t6" in message.body.lower()) ) or  (("Fine" in message.body.lower()) and ("t6" in message.body.lower()) ) or  (("Good" in message.body.lower()) and ("t6" in message.body.lower()) ) or (("amazing" in message.body.lower()) and ("t6" in message.body.lower()) ) or (("splended" in message.body.lower()) and ("t6" in message.body.lower()) ) or (("good" in message.body.lower()) and ("t6" in message.body.lower()) ) or (("bad" in message.body.lower()) and ("t6" in message.body.lower()) ) or (("okay" in message.body.lower()) and ("t6" in message.body.lower()) ) or (("ok" in message.body.lower()) and ("t6" in message.body.lower()) ) or (("horrible" in message.body.lower()) and ("t6" in message.body.lower()) )  or (("awful" in message.body.lower()) and ("t6" in message.body.lower()) )) and (usrlvl >= 1) ):
#		    statres = random.choice(["That's good to hear!", "Why aren't you doing better?", "Why's that? Did something happen?", "If I told you that I love you would you be doing better?", "Go cut your wrists and get it over with.", "I DON'T CARE!"])
		    time.sleep(2)
#		    room.message(statres)
		elif  ( (message.body == "One is the loneliest number that you'll ever do") and (usrlvl >= 1) ):
		    time.sleep(2)
		    room.message("Two can be as bad as one, it's the loneliest number if I'm the other one.")
		elif  ( (message.body == "One is the loneliest number that you'll ever do.") and (usrlvl >= 1) ):
		    time.sleep(2)
		    room.message("Two can be as bad as one, it's the loneliest number if I'm the other one.")
		elif  ( (message.body == "one is the loneliest number that you'll ever do") and (usrlvl >= 1) ):
		    time.sleep(2)
		    room.message("Two can be as bad as one, it's the loneliest number if I'm the other one.")
		elif  ( (message.body == "One is the loneliest number that youll ever do") and (usrlvl >= 1) ):
		    time.sleep(2)
		    room.message("Two can be as bad as one, it's the loneliest number if I'm the other one.")
		elif  ( (message.body == "one is the loneliest number that youll ever do") and (usrlvl >= 1) ):
		    time.sleep(2)
		    room.message("Two can be as bad as one, it's the loneliest number if I'm the other one.")
		elif  ( (message.body == "One is the loneliest number that youll ever do.") and (usrlvl >= 1) ):
		    time.sleep(2)
		    room.message("Two can be as bad as one, it's the loneliest number if I'm the other one.")
		elif  ( (message.body == "one is the loneliest number that youll ever do.") and (usrlvl >= 1) ):
		    time.sleep(2)
		    room.message("Two can be as bad as one, it's the loneliest number if I'm the other one.")
		elif  ( (message.body == "one is the loneliest number that you'll ever do.") and (usrlvl >= 1) ):
		    time.sleep(2)
		    room.message("Two can be as bad as one, it's the loneliest number if I'm the other one.")
		elif  ( (message.body.lower() == "t6.") and (usrlvl >= 1) ):
		    nameres = 'Yes, '
		    nameres2 = '?'
		    fnameres = nameres + (user.name).capitalize() + nameres2
		    time.sleep(2)
		    room.message(fnameres)
		elif  ( (message.body.lower() == "t6?") and (usrlvl >= 1) ):
		    nameres = 'Yes, '
		    nameres2 = '?'
		    fnameres = nameres + (user.name).capitalize() + nameres2
		    time.sleep(2)
		    room.message(fnameres)
		elif  ( (message.body.lower() == "t6!") and (usrlvl >= 1) ):
		    room.message((user.name).capitalize() + "!")
		elif  ( (message.body.lower() == "t6ru.") and (usrlvl >= 1) ):
		    nameres = 'Yes, '
		    nameres2 = '?'
		    fnameres = nameres + (user.name).capitalize() + nameres2
		    time.sleep(2)
		    room.message(fnameres)
		elif  ( (message.body.lower() == "t6ru?") and (usrlvl >= 1) ):
		    nameres = 'Yes, '
		    nameres2 = '?'
		    fnameres = nameres + (user.name).capitalize() + nameres2
		    time.sleep(2)
		    room.message(fnameres)
		elif  ( (message.body.lower() == "t6ru!") and (usrlvl >= 1) ):
		    time.sleep(2)
		    room.message((user.name).capitalize() + "!")
		elif  ( ( ("puts on sunglasses" in message.body.lower()) or  ("put on sunglasses" in message.body.lower()) or ("puts on sun" in message.body.lower()) or ("put on sun" in message.body.lower()) ) and (usrlvl >= 1) ):
		    room.message("http://youtu.be/6YMPAH67f4o")

		elif  (message.body.lower().startswith("nooooooo") and usrlvl >=1):
		    room.message("http://youtu.be/WWaLxFIVX1s")
		elif message.body.lower().startswith("!d"):
			mdlvl = room.getLevel(user)
			if ((usrlvl >=3) or (mdlvl >= 1)):
				if (message.body).find(" ") != -1: #if there's a colon somewhere
					argsadj = (message.body).lower()
					cmmd, uuser = argsadj.split(" ", 1)
					endusr = ch._users.get(uuser)
					if endusr == None:
						room.message(uuser.capitalize() + ' is not in the chat.')
					else:
						room.message(uuser.capitalize() + ' STFU please, k thx.')
						room.clearUser(endusr)
				else:
					room.clearUser(user)
		elif message.body.lower().startswith("!delete"):
			mdlvl = room.getLevel(user)
			if ((usrlvl >=3) or (mdlvl >= 1)):
				if (message.body).find(" ") != -1: #if there's a colon somewhere
					argsadj = (message.body).lower()
					cmmd, uuser = argsadj.split(" ", 1)
					endusr = ch._users.get(uuser)
					if endusr == None:
						room.message(uuser.capitalize() + ' is not in the chat.')
					else:
						room.message(uuser.capitalize() + ' STFU please, k thx.')
						room.clearUser(endusr)
				else:
					room.clearUser(user)
		elif (message.body.lower().startswith("!banlist")):
			mdlvl = room.getLevel(user)
			if ((usrlvl >=2) or (mdlvl >= 1)):
				banlistr1 = str(room.banlist).replace("[", "")
				banlistr2 = banlistr1.replace("[", "")
				banlistr3 = banlistr2.replace("]", "")
				banlistr4 = banlistr3.replace("[", "")
				banlistr5 = banlistr4.replace("<User: ", "")
				banlistr6 = banlistr5.replace(">", "")
				banlist = banlistr6 + ' is/are currently banned.'
				room.message(banlist)
			else:
				room.message("Haha. Nice try. 2/10 for effort.")
		elif message.body.lower().startswith("!ban"):
			mdlvl = room.getLevel(user)
			if ((usrlvl >=3) or (mdlvl >= 1)):
				if (message.body).find(" ") != -1: #if there's a colon somewhere
					argsadj = (message.body).lower()
					cmmd, uuser = argsadj.split(" ", 1)
					endusr = ch._users.get(uuser)
					if endusr == None:
						room.message(uuser.capitalize() + ' is not in the chat.')
					else:
						room.message(uuser.capitalize() + ' is now banned.')
						room.banUser(endusr)
				else:
					room.message("Enter a valid user.")
		elif message.body.lower().startswith("!unban"):
			mdlvl = room.getLevel(user)
			if ((usrlvl >=3) or (mdlvl >= 1)):
				if (message.body).find(" ") != -1: #if there's a colon somewhere
					argsadj = (message.body).lower()
					cmmd, uuser = argsadj.split(" ", 1)
					endusr = ch._users.get(uuser)
					if endusr == None:
						room.message(uuser.capitalize() + ' is not in the chat.')
					else:
						room.message(uuser.capitalize() + ' is no longer banned.')
						room.unban(endusr)
				else:
					room.unban(user)
		elif  ( (message.body.lower().startswith("problem?")) ):
			room.message("http://i3.kym-cdn.com/photos/images/original/000/222/268/1324692075001.png")
		elif  (message.body.lower()).startswith("like a boss"):
			    if usrlvl >= 2:
			    	rlab = (random.choice(['http://funcorner.eu/wp-content/uploads/2011/03/like_a_boss.jpg']))
			    	room.message(rlab)
		elif  message.body.startswith("GOML GOML GOML"):
			    if usrlvl >= 2:
			    	rgoml = (random.choice(['http://i63.photobucket.com/albums/h139/babyxoxghurl/quotes%20and%20sayings/6d0htts.jpg','http://typophile.com/files/ryan%20get%20on%20my%20level.jpg','http://rlv.zcache.co.uk/get_on_my_level_poster-r8661161397c644918177cdfaac59700a_w2q_400.jpg','http://fc08.deviantart.net/fs71/f/2011/228/2/b/get_on_my_level_by_sabertoothedolivia-d46ucri.jpg','http://i305.photobucket.com/albums/nn222/InsanitySmiles/get-on-my-level.jpg']))
			    	room.message(rgoml)
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

if __name__ == "__main__": TestBot.easy_start(rmlist.roomlist, name = 'T6ru', password = 'IonB0tP455w0rd*', pm = True)
