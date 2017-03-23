import ch
import rmlist
import string
import random
import sys
import re
import time
from time import gmtime, strftime
import datetime
import urllib
from threading import Timer
						
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

pokerallcards = "*$#^!players = 2 &^$*\n^$&*available = 2 *)!#\n##$*!@turn = 1@*&(*\n*#&$^#cards = #&!2 of hearts, #&!3 of hearts, #&!4 of hearts, #&!5 of hearts, #&!6 of hearts, #&!7 of hearts, #&!8 of hearts, #&!9 of hearts, #&!10 of hearts, #&!Jack of hearts, #&!IceQueen of hearts, #&!King of hearts, #&!Ace of hearts, #&!2 of diamonds, #&!3 of diamonds, #&!4 of diamonds, #&!5 of diamonds, #&!6 of diamonds, #&!7 of diamonds, #&!8 of diamonds, #&!9 of diamonds, #&!10 of diamonds, #&!Jack of diamonds, #&!IceQueen of diamonds, #&!King of diamonds, #&!Ace of diamonds, #&!2 of clubs, #&!3 of clubs, #&!4 of clubs, #&!5 of clubs, #&!6 of clubs, #&!7 of clubs, #&!8 of clubs, #&!9 of clubs, #&!10 of clubs, #&!Jack of clubs, #&!IceQueen of clubs, #&!King of clubs, #&!Ace of clubs, #&!2 of spades, #&!3 of spades, #&!4 of spades, #&!5 of spades, #&!6 of spades, #&!7 of spades, #&!8 of spades, #&!9 of spades, #&!10 of spades, #&!Jack of spades, #&!IceQueen of spades, #&!King of spades, #&!Ace of spades#&#@$($#\n"

totalcardlist = "*#&$^#cards = #&!2 of hearts, #&!3 of hearts, #&!4 of hearts, #&!5 of hearts, #&!6 of hearts, #&!7 of hearts, #&!8 of hearts, #&!9 of hearts, #&!10 of hearts, #&!Jack of hearts, #&!IceQueen of hearts, #&!King of hearts, #&!Ace of hearts, #&!2 of diamonds, #&!3 of diamonds, #&!4 of diamonds, #&!5 of diamonds, #&!6 of diamonds, #&!7 of diamonds, #&!8 of diamonds, #&!9 of diamonds, #&!10 of diamonds, #&!Jack of diamonds, #&!IceQueen of diamonds, #&!King of diamonds, #&!Ace of diamonds, #&!2 of clubs, #&!3 of clubs, #&!4 of clubs, #&!5 of clubs, #&!6 of clubs, #&!7 of clubs, #&!8 of clubs, #&!9 of clubs, #&!10 of clubs, #&!Jack of clubs, #&!IceQueen of clubs, #&!King of clubs, #&!Ace of clubs, #&!2 of spades, #&!3 of spades, #&!4 of spades, #&!5 of spades, #&!6 of spades, #&!7 of spades, #&!8 of spades, #&!9 of spades, #&!10 of spades, #&!Jack of spades, #&!IceQueen of spades, #&!King of spades, #&!Ace of spades#&#@$($#\n"

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

cmpt1 = " is like the rays of sunshine shining down in the otherwise unbearably cold artic wasteland in which we live."

cmpt2 = " is almost as lovely as Ion is."

cmpt3 = " is the most absolutely amazingly awesome person ever."

cmpt4 = "'s mom...is a respectable lady."

cmpt5 = ", I like your shoes."

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
		hrlr = open("data/rmset/hiddenroomlist.txt","r")
		hrl = (hrlr.read()).lower()
		hrlr.close()
		roomnamesr = open("data/rmset/roomnames.txt","r")
		roomnames = (roomnamesr.read()).lower()
		roomnamesr.close()
		pmnamesr = open("data/pm/pmnames.txt","r")
		pmnames = (pmnamesr.read()).lower()
		pmnamesr.close()
		aimoder = open("data/rmset/aimode.txt","r")
		aimode = (aimoder.read()).lower()
		aimoder.close()
		funmoder = open("data/rmset/funmode.txt","r")
		funmode = (funmoder.read()).lower()
		funmoder.close()
		modmoder = open("data/rmset/modmode.txt","r")
		modmode = (modmoder.read()).lower()
		modmoder.close()
		usefulmoder = open("data/rmset/usefulmode.txt","r")
		usefulmode = (usefulmoder.read()).lower()
		usefulmoder.close()
		msgbody = message.body
		lvl3rd = open("data/whitelist/lvl3.txt","r")
		lvl3rd2 = (lvl3rd.read()).lower()
		lvl2rd = open("data/whitelist/lvl2.txt","r")
		lvl2rd2 = (lvl2rd.read()).lower()
		lvl1rd = open("data/whitelist/lvl1.txt","r")
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
		usager = open("data/usage/usage.txt","r")
		usage = (usager.read()).lower()
		usager.close()
		nowfc = strftime("*#&^^&@%d #(!)#)!%b $!@$)($)!%Y ##$@$!%H:(!@*$&@%M:*$&*#(@" + user.name + "!!$&$!@%S$*$&", gmtime()).lower()
		focususrst = '#$&@$^!:$#@$#@$#(#' + user.name + '@#(*#$!()!$'
		focususred = user.name + '$*!&$@)!_+'
		usredtime = '*!(@#$#*!&@$!)!#_!(' + user.name + '$#@#$(@'
		bodywrt = room.name + '*$($*!@&$(!@' + msgbody + '$@#*$@*$(@!:)$(!@$)@#'
		relapointid = '@(#$*!()#' + user.name + '!#$#!(%*#!'
		if focususrst in usage:
			rpusager = open("data/usage/usage.txt","r")
			rpusage = (rpusager.read()).lower()
			rpusager.close()
			indexsrp = usage.find(focususred)
			indexerp = usage.find(relapointid)
			rawoutrp = usage[(int(indexsrp)):(int(indexerp))]
			relationpr = rawoutrp.replace(focususred, '')
			relationp = int(relationpr)
		else:
			relationpr = '0'
			relationp = 0
		if user.name == 't6ru':
			nowuh = strftime("%a, %d %b %Y %H:%M:%S", gmtime())
			wrtdata = open("data/usage/uhistory.txt","a")
			wrtdata.write(str((nowuh + ' ---> ' + room.name + ': ' + msgbody).encode('utf-8')) + '\n')
			wrtdata.close()
			#print(room.name + ' --> ' + user.name + ': ', msgbody)
		if self.user == user: return
		elif usrlvl >0:
			if msgbody.startswith(';'):
				if focususrst in usage:
					indexs = usage.find(focususrst)
					indexe = usage.find(relapointid)
					rawout = usage[(int(indexs)):(int(indexe))]
					newdatar = str(usage).replace((rawout + relapointid), (focususrst + nowfc + usredtime + bodywrt + focususred + str(relationp) + relapointid))
					newdata = str(newdatar.encode('utf-8')).replace("\\n", "\n")\
						.replace("b'", "")\
						.replace('b"', "")\
						.replace("\'", "")\
						.replace('\"', "")\
						.replace("\\\\", "")
					wrtdata = open("data/usage/usage.txt","w")
					wrtdata.write(newdata)
					wrtdata.close()
				else:
					wrtdata = open("data/usage/usage.txt","a")
					wrtdata.write(str((focususrst + nowfc + usredtime + bodywrt + focususred + '0' + relapointid).encode('utf-8')) + '\n')
					wrtdata.close()
				#print(room.name + ' --> ' + user.name + ': ', msgbody)
			elif user.name == 'grim':
				nowsk = strftime("%a, %d %b %Y %H:%M:%S", gmtime())
				wrtdata = open("data/pm/grimhistory.txt","a")
				wrtdata.write(str((nowuh + ' ---> ' + room.name + ': ' + msgbody).encode('utf-8')) + '\n')
				wrtdata.close()
				#print(room.name + ' --> ' + user.name + ': ', msgbody)
			#else:
				#print(room.name + ' --> ' + user.name + ': ', msgbody)
			focustxtr = open("data/usage/usage.txt","r")
			focustxt = (focustxtr.read()).lower()
			focustxtr.close()
			if (msgbody[0] == ";"):
				callname = 6
			elif focususrst in str(focustxt):
				currentsf = ":*$&*#(@" + user.name + "!!$&$!@"
				indexsf = nowfc.find(currentsf)
				indexef = nowfc.find('$*$&')
				rawoutf = nowfc[(int(indexsf)):(int(indexef))]
				nowfcseir = rawoutf.replace(currentsf, '')
				nowfcsei = int(nowfcseir)
				indexsof = focustxt.find(currentsf)
				indexeof = focustxt.find('$*$&' + usredtime)
				rawoutof = focustxt[(int(indexsof)):(int(indexeof))]
				oldfcsir = rawoutof.replace(currentsf, '')
				oldfcsi = int(oldfcsir)
				if ((nowfcsei < 20) and (oldfcsi > 20)):
					indexsmf = nowfc.find(':(!@*$&@')
					indexemf = nowfc.find(':*$&*#(@')
					rawoutmf = nowfc[(int(indexsmf)):(int(indexemf))]
					nowfcmir = rawoutmf.replace(':(!@*$&@', '')
					nowfcmi = int(nowfcmir) - 1
					currenti = focususrst + nowfc[0:51] + str(nowfcmi) + nowfc[53:61]
				else:
					currenti = focususrst + nowfc[0:61]
				if (currenti in focustxt):
					if nowfcsei > 20:
						nowfcssi = nowfcsei - 20
						if ( (oldfcsi >= nowfcssi) and (oldfcsi <= nowfcsei) ):
							msgbody = 't6 ' + msgbody
							callname = 0
						else: 
							callname = 0
					else:
						nowfcssi = nowfcsei + 40
						if oldfcsi < 20:
							msgbody = 't6 ' + msgbody
							callname = 0
						elif ( (oldfcsi >= nowfcssi) and (oldfcsi <= (nowfcsei + 60)) ):
							msgbody = 't6 ' + msgbody
							callname = 0
						else: 
							callname = 0
				else:
					callname = 0
			else: 
				callname = 0
		else:
			callname = 0
		if (("#@@$!!(!*@" + room.name + "@@#$&*(**!") in hrl):
			mdlvl = room.getLevel(user)
			if ( (callname == 6) and ((usrlvl >= 2) or (mdlvl >=1)) ):
				data = msgbody[1:].split(" ", 1)
				if len(data) > 1:
					cmd, args = data[0], data[1]
				else:
					cmd, args = data[0], ""
				if ( (cmd.lower() == "rs" ) or (cmd.lower() == "roomsettings") ):
					argsadj = args.lower()
					mdlvl = room.getLevel(user)
					if args.find(":") != -1: #if there's a colon somewhere
						if (usrlvl >=2):
							uroomr, uset = argsadj.split(": ", 1)
							if (('#@#(*' + uroomr + '!@#$!') in roomnames):
									indexrs = roomnames.find('#@#(*' + uroomr + '!@#$!')
									indexre = roomnames.find('!@*^^(!' + uroomr + '*(^&&!')
									roomout1 = roomnames[(int(indexrs)):(int(indexre))]
									uroom = roomout1.replace(('#@#(*' + uroomr + '!@#$!'), "")
							else: uroom = uroomr
							if (uroom in str(self._rooms)):
								roomfind = "#@@$!!(!*@" + uroom + "@@#$&*(**!"
								writeinfo = "#@@$!!(!*@" + uroom + "@@#$&*(**!" + uroom + "!(!*@&&^^^!\n"
								findinfo1 = "#@@$!!(!*@" + uroom
								findinfo2 = "@@#$&*(**!" + uroom + "!(!*@&&^^^!"
								if ('mod' in uset):
									if (uroom not in modmode):
										wrtdata = open("data/whitelist/modmode.txt","a")
										wrtdata.write(writeinfo)
										wrtdata.close()
										if ((roomfind) in usefulmode):
											wrtdata = open("data/rmset/usefulmode.txt","w")
											indexs = usefulmode.find(findinfo1)
											indexe = usefulmode.find(findinfo2)
											rawout = usefulmode[(int(indexs)):(int(indexe))]
											newdata = str(usefulmode).replace((findinfo1 + findinfo2), "")
											wrtdata.write(newdata)
											wrtdata.close()
										elif ((roomfind) in funmode):
											wrtdata = open("data/rmset/funmode.txt","w")
											indexs = funmode.find(findinfo1)
											indexe = funmode.find(findinfo2)
											rawout = funmode[(int(indexs)):(int(indexe))]
											newdata = str(funmode).replace((findinfo1 + findinfo2), "")
											wrtdata.write(newdata)
											wrtdata.close()
										if ((roomfind) in aimode):
											room.message(uroom.capitalize() + ' is now set to moderation functions only with AI on.')
										else:
											room.message(uroom + ' is now set to moderation functions only with AI off.')
									else:
										if ((roomfind) in aimode):
											room.message(uroom.capitalize() + ' is already set to moderation functions only with AI on.')
										else:
											room.message(uroom + ' is already set to moderation functions only with AI off.')
								elif ('useful' in uset):
									if (uroom not in usefulmode):
										wrtdata = open("data/rmset/usefulmode.txt","a")
										room.message(uroom.capitalize() + ' is now set to useful and moderation functions only.')
										wrtdata.write(writeinfo)
										wrtdata.close()
										if ((roomfind) in modmode):
											wrtdata = open("data/rmset/modmode.txt","w")
											indexs = modmode.find(findinfo1)
											indexe = modmode.find(findinfo2)
											rawout = modmode[(int(indexs)):(int(indexe))]
											newdata = str(modmode).replace((findinfo1 + findinfo2), "")
											wrtdata.write(newdata)
											wrtdata.close()
										elif ((roomfind) in funmode):
											wrtdata = open("data/rmset/funmode.txt","w")
											indexs = funmode.find(findinfo1)
											indexe = funmode.find(findinfo2)
											rawout = funmode[(int(indexs)):(int(indexe))]
											newdata = str(funmode).replace((findinfo1 + findinfo2), "")
											wrtdata.write(newdata)
											wrtdata.close()
										if ((roomfind) in aimode):
											room.message(uroom.capitalize() + ' is now set to useful and moderation functions only with AI on.')
										else:
											room.message(uroom + ' is now set to moderation functions only with AI off.')
									else:
										if ((roomfind) in aimode):
											room.message(uroom.capitalize() + ' is already set to useful and moderation functions only with AI on.')
										else:
											room.message(uroom.capitalize() + ' is already set to moderation functions only with AI off.')
								elif (('fun' in uset) or ('all' in uset)):
									if (uroom not in funmode):
										wrtdata = open("data/rmset/funmode.txt","a")
										wrtdata.write(writeinfo)
										wrtdata.close()
										if ((roomfind) in modmode):
											wrtdata = open("data/rmset/modmode.txt","w")
											indexs = modmode.find(findinfo1)
											indexe = modmode.find(findinfo2)
											rawout = modmode[(int(indexs)):(int(indexe))]
											newdata = str(modmode).replace((findinfo1 + findinfo2), "")
											wrtdata.write(newdata)
											wrtdata.close()
										elif ((roomfind) in usefulmode):
											wrtdata = open("data/rmset/usefulmode.txt","w")
											indexs = usefulmode.find(findinfo1)
											indexe = usefulmode.find(findinfo2)
											rawout = usefulmode[(int(indexs)):(int(indexe))]
											newdata = str(usefulmode).replace((findinfo1 + findinfo2), "")
											wrtdata.write(newdata)
											wrtdata.close()
										if ((roomfind) in aimode):
											room.message(uroom.capitalize() + ' is now set to all functions, with AI on.')
										else:
											room.message(uroom.capitalize() + ' is now set to all functions, with AI off.')
									else:
										if ((roomfind) in aimode):
											room.message(uroom.capitalize() + ' is already set to all functions, with AI on.')
										else:
											room.message(uroom.capitalize() + ' is already set to all functions, with AI off.')
								if (('ai' in uset) and ('on' in uset)):
									if (uroom not in aimode):
										wrtdata = open("data/rmset/aimode.txt","a")
										room.message(uroom.capitalize() + ' is now set to AI on.')
										wrtdata.write(writeinfo)
										wrtdata.close()
									else:
										room.message(uroom.capitalize() + ' is already set to AI on.')
								elif (('ai' in uset) and ('off' in uset)):
									if (uroom in aimode):
										room.message(uroom.capitalize() + ' is now set to AI off.')
										wrtdata = open("data/rmset/aimode.txt","w")
										indexs = modmode.find(findinfo1)
										indexe = modmode.find(findinfo2)
										rawout = modmode[(int(indexs)):(int(indexe))]
										newdata = str(aimode).replace((findinfo1 + findinfo2), "")
										wrtdata.write(newdata)
										wrtdata.close()
										if ((roomfind) in modmode):
											wrtdata = open("data/rmset/modmode.txt","w")
											indexs = modmode.find(findinfo1)
											indexe = modmode.find(findinfo2)
											rawout = modmode[(int(indexs)):(int(indexe))]
											newdata = str(modmode).replace((findinfo1 + findinfo2), "")
											wrtdata.write(newdata)
											wrtdata.close()
										elif ((roomfind) in usefulmode):
											wrtdata = open("data/rmset/usefulmode.txt","w")
											indexs = usefulmode.find(findinfo1)
											indexe = usefulmode.find(findinfo2)
											rawout = usefulmode[(int(indexs)):(int(indexe))]
											newdata = str(usefulmode).replace((findinfo1 + findinfo2), "")
											wrtdata.write(newdata)
											wrtdata.close()
										if ((roomfind) not in funmode):
											wrtdata2 = open("data/rmset/funmode.txt","a")
											wrtdata2.write(writeinfo)
											wrtdata2.close()
									else:
										room.message(uroom.capitalize() + ' is already set to AI off.')
							else:
								room.message('Enter a valid room.')
						else:
							room.message("Lol, no.")
					else:
						if (args == ""):
							if (usrlvl >=2 or mdlvl >=1):
								uroom = room.name
								roomfind = "#@@$!!(!*@" + uroom + "@@#$&*(**!"
								if (roomfind in modmode):
									if (roomfind in aimode):
										room.message('I am currently set to moderation functions only with AI on in ' + uroom.capitalize() + '.')
									else:
										room.message('I am currently set to moderation functions only  with AI off in ' + uroom.capitalize() + '.')
								elif (roomfind in usefulmode):
									if (roomfind in aimode):
										room.message('I am currently set to useful and moderation functions only with AI on in ' + uroom.capitalize() + '.')
									else:
										room.message('I am currently set to useful and moderation functions only with AI off in ' + uroom.capitalize() + '.')
								elif (roomfind in funmode):
									if (roomfind in aimode):
										room.message('I am currently set to all functions with AI on in ' + uroom.capitalize() + '.')
									else:
										room.message('I am currently set to all functions with AI off in ' + uroom.capitalize() + '.')
								else:
									room.message('I do not have settings for ' + uroom.capitalize() + '.')
						elif ('mod' in argsadj):
							if (usrlvl >=2 or mdlvl >=1):
								uroom = room.name
								roomfind = "#@@$!!(!*@" + uroom + "@@#$&*(**!"
								writeinfo = "#@@$!!(!*@" + uroom + "@@#$&*(**!" + uroom + "!(!*@&&^^^!\n"
								findinfo1 = "#@@$!!(!*@" + uroom
								findinfo2 = "@@#$&*(**!" + uroom + "!(!*@&&^^^!"
								if (uroom not in modmode):
									wrtdata = open("data/rmset/modmode.txt","a")
									wrtdata.write(writeinfo)
									wrtdata.close()
									if ((roomfind) in usefulmode):
										wrtdata = open("data/rmset/usefulmode.txt","w")
										indexs = usefulmode.find(findinfo1)
										indexe = usefulmode.find(findinfo2)
										rawout = usefulmode[(int(indexs)):(int(indexe))]
										newdata = str(usefulmode).replace((findinfo1 + findinfo2), "")
										wrtdata.write(newdata)
										wrtdata.close()
									elif ((roomfind) in funmode):
										wrtdata = open("data/rmset/funmode.txt","w")
										indexs = funmode.find(findinfo1)
										indexe = funmode.find(findinfo2)
										rawout = funmode[(int(indexs)):(int(indexe))]
										newdata = str(funmode).replace((findinfo1 + findinfo2), "")
										wrtdata.write(newdata)
										wrtdata.close()
									if ((roomfind) in aimode):
										room.message(uroom.capitalize() + ' is now set to moderation functions only with AI on.')
									else:
										room.message(uroom + ' is now set to moderation functions only with AI off.')
								else:
									if ((roomfind) in aimode):
										room.message(uroom.capitalize() + ' is now set to moderation functions only with AI on.')
									else:
										room.message(uroom.capitalize() + ' is now set to moderation functions only with AI off.')
						elif ('useful' in argsadj):
							if (usrlvl >=2 or mdlvl >=1):
								uroom = room.name
								roomfind = "#@@$!!(!*@" + uroom + "@@#$&*(**!"
								writeinfo = "#@@$!!(!*@" + uroom + "@@#$&*(**!" + uroom + "!(!*@&&^^^!\n"
								findinfo1 = "#@@$!!(!*@" + uroom
								findinfo2 = "@@#$&*(**!" + uroom + "!(!*@&&^^^!"
								if (uroom not in usefulmode):
									wrtdata = open("data/rmset/usefulmode.txt","a")
									wrtdata.write(writeinfo)
									wrtdata.close()
									if ((roomfind) in modmode):
										wrtdata = open("data/rmset/modmode.txt","w")
										indexs = modmode.find(findinfo1)
										indexe = modmode.find(findinfo2)
										rawout = modmode[(int(indexs)):(int(indexe))]
										newdata = str(modmode).replace((findinfo1 + findinfo2), "")
										wrtdata.write(newdata)
										wrtdata.close()
									elif ((roomfind) in funmode):
										wrtdata = open("data/rmset/funmode.txt","w")
										indexs = funmode.find(findinfo1)
										indexe = funmode.find(findinfo2)
										rawout = funmode[(int(indexs)):(int(indexe))]
										newdata = str(funmode).replace((findinfo1 + findinfo2), "")
										wrtdata.write(newdata)
										wrtdata.close()
									if ((roomfind) in aimode):
										room.message(uroom.capitalize() + ' is now set to useful and moderation functions only with AI on.')
									else:
										room.message(uroom + ' is now set to useful and moderation functions only with AI off.')
								else:
									if ((roomfind) in aimode):
										room.message(uroom.capitalize() + ' is now set to useful and moderation functions only with AI on.')
									else:
										room.message(uroom.capitalize() + ' is now set to useful and moderation functions only with AI off.')
						elif ('fun' in argsadj):
							if (usrlvl >=2 or mdlvl >=1):
								uroom = room.name
								roomfind = "#@@$!!(!*@" + uroom + "@@#$&*(**!"
								writeinfo = "#@@$!!(!*@" + uroom + "@@#$&*(**!" + uroom + "!(!*@&&^^^!\n"
								findinfo1 = "#@@$!!(!*@" + uroom
								findinfo2 = "@@#$&*(**!" + uroom + "!(!*@&&^^^!"
								if (uroom not in funmode):
									wrtdata = open("data/rmset/funmode.txt","a")
									wrtdata.write(writeinfo)
									wrtdata.close()
									if ((roomfind) in modmode):
										wrtdata = open("data/rmset/modmode.txt","w")
										indexs = modmode.find(findinfo1)
										indexe = modmode.find(findinfo2)
										rawout = modmode[(int(indexs)):(int(indexe))]
										newdata = str(modmode).replace((findinfo1 + findinfo2), "")
										wrtdata.write(newdata)
										wrtdata.close()
									elif ((roomfind) in usefulmode):
										wrtdata = open("data/rmset/usefulmode.txt","w")
										indexs = usefulmode.find(findinfo1)
										indexe = usefulmode.find(findinfo2)
										rawout = usefulmode[(int(indexs)):(int(indexe))]
										newdata = str(usefulmode).replace((findinfo1 + findinfo2), "")
										wrtdata.write(newdata)
										wrtdata.close()
									if ((roomfind) in aimode):
										room.message(uroom.capitalize() + ' is now set to all functions, with AI on.')
									else:
										room.message(uroom.capitalize()+ ' is now set to all functions, with AI off.')
								else:
									if ((roomfind) in aimode):
										room.message(uroom.capitalize() + ' is already set to all functions, with AI on.')
									else:
										room.message(uroom.capitalize() + ' is already set to all functions, with AI off.')
						if (('ai' in argsadj) and ('on' in argsadj)):
							if (usrlvl >=2 or mdlvl >=1):
								uroom = room.name
								roomfind = "#@@$!!(!*@" + uroom + "@@#$&*(**!"
								writeinfo = "#@@$!!(!*@" + uroom + "@@#$&*(**!" + uroom + "!(!*@&&^^^!\n"
								findinfo1 = "#@@$!!(!*@" + uroom
								findinfo2 = "@@#$&*(**!" + uroom + "!(!*@&&^^^!"
								if (uroom not in aimode):
									wrtdata = open("data/rmset/aimode.txt","a")
									room.message(uroom.capitalize() + ' is now set to AI on.')
									wrtdata.write(writeinfo)
									wrtdata.close()
								else:
									room.message(uroom.capitalize() + ' is already set to AI on.')
						elif (('ai' in argsadj) and ('off' in argsadj)):
							if (usrlvl >=2 or mdlvl >=1):
								uroom = room.name
								roomfind = "#@@$!!(!*@" + uroom + "@@#$&*(**!"
								writeinfo = "#@@$!!(!*@" + uroom + "@@#$&*(**!" + uroom + "!(!*@&&^^^!\n"
								findinfo1 = "#@@$!!(!*@" + uroom
								findinfo2 = "@@#$&*(**!" + uroom + "!(!*@&&^^^!"
								if (uroom in aimode):
									room.message(uroom.capitalize() + ' is now set to AI off.')
									wrtdata = open("data/rmset/aimode.txt","w")
									indexs = modmode.find(findinfo1)
									indexe = modmode.find(findinfo2)
									rawout = modmode[(int(indexs)):(int(indexe))]
									newdata = str(aimode).replace((findinfo1 + findinfo2), "")
									wrtdata.write(newdata)
									wrtdata.close()
								else:
									room.message(uroom.capitalize() + ' is already set to AI off.')									
						elif ((args != '') and ('ai' not in argsadj) and ('fun' not in argsadj) and ('mod' not in argsadj) and ('useful' not in argsadj) and ('all' not in argsadj)):
							if (usrlvl >=2):	
								if (('#@#(*' + argsadj + '!@#$!') in roomnames):
									indexrs = roomnames.find('#@#(*' + argsadj + '!@#$!')
									indexre = roomnames.find('!@*^^(!' + argsadj + '*(^&&!')
									roomout1 = roomnames[(int(indexrs)):(int(indexre))]
									uroom = roomout1.replace(('#@#(*' + argsadj + '!@#$!'), "")
								else: uroom = argsadj
								roomfind = "#@@$!!(!*@" + uroom + "@@#$&*(**!"
								if (roomfind in modmode):
									if (roomfind in aimode):
										room.message('I am currently set to moderation functions only with AI on in ' + uroom.capitalize() + '.')
									else:
										room.message('I am currently set to moderation functions only with AI off in ' + uroom.capitalize() + '.')
								elif (roomfind in usefulmode):
									if (roomfind in aimode):
										room.message('I am currently set to useful and moderation functions only with AI on in ' + uroom.capitalize() + '.')
									else:
										room.message('I am currently set to useful and moderation functions only with AI off in ' + uroom.capitalize() + '.')
								elif (roomfind in funmode):
									if (roomfind in aimode):
										room.message('I am currently set to all functions with AI on in ' + uroom.capitalize() + '.')
									else:
										room.message('I am currently set to all functions with AI off in ' + uroom.capitalize() + '.')
								else:
									room.message('I do not have settings for ' + uroom.capitalize() + '.')
				elif (cmd.lower()) == "die":
					if (usrlvl == 3):
						sys.exit(0)
				elif (cmd.lower() == "teach"):
					if (user.name == 'ion'):
						argsadj = args.lower()
						if argsadj.find(" ") != -1: #if there's a colon somewhere
							uroomr, misc = argsadj.split(" ", 1)
							if (('#@#(*' + uroomr + '!@#$!') in pmnames):
								indexrs = pmnames.find('#@#(*' + uroomr + '!@#$!')
								indexre = pmnames.find('!@*^^(!' + uroomr + '*(^&&!')
								pmout1 = pmnames[(int(indexrs)):(int(indexre))]
								uuser = pmout1.replace(('#@#(*' + uroomr + '!@#$!'), "")
							else:
								uuser = uroomr
							endusr = ch._users.get(uuser)
							if endusr == None:
								room.message(uuser.capitalize() + ' is not in the chat.')
							else:
								room.message('I have banned ' + uuser.capitalize() + ' to teach them a lesson.')
								room.banUser(endusr)
				elif (cmd.lower() == "banme"):
					if usrlvl >= 3:
							room.banUser(user.name)
				elif (cmd.lower() == "roomban"):
					if usrlvl >= 3:
						argsadj = args.lower()
						if (('#@#(*' + argsadj + '!@#$!') in pmnames):
							indexrs = pmnames.find('#@#(*' + argsadj + '!@#$!')
							indexre = pmnames.find('!@*^^(!' + argsadj + '*(^&&!')
							pmout1 = pmnames[(int(indexrs)):(int(indexre))]
							uuser = pmout1.replace(('#@#(*' + argsadj + '!@#$!'), "")
						else:
							uuser = argsadj
						endusr = ch._users.get(uuser)
						if endusr == None:
							room.message(uuser.capitalize() + ' is not in the chat.')
						else:
							uroom = self._rooms['teruchat']
							room.message('I have banned ' + uuser.capitalize() + ' to teach them a lesson.')
							uroom.banUser(endusr)
				elif ( (cmd.lower() == "d" ) or (cmd.lower() == "delete") ):
					mdlvl = room.getLevel(user)
					if ((usrlvl >=3) or (mdlvl >= 1)):
						argsadj = args.lower()
						if args == "":
							room.clearUser(user)
						else:
							if (('#@#(*' + argsadj + '!@#$!') in pmnames):
								indexrs = pmnames.find('#@#(*' + argsadj + '!@#$!')
								indexre = pmnames.find('!@*^^(!' + argsadj + '*(^&&!')
								pmout1 = pmnames[(int(indexrs)):(int(indexre))]
								uuser = pmout1.replace(('#@#(*' + argsadj + '!@#$!'), "")
							else:
								uuser = argsadj
							endusr = ch._users.get(uuser)
							if endusr == None:
								room.message(uuser.capitalize() + ' is not in the chat.')
							else:
								room.message(uuser.capitalize() + ' STFU please, k thx.')
								room.clearUser(endusr)
				elif ( (cmd.lower() == "kill" ) or (cmd.lower() == "ban") ):
					mdlvl = room.getLevel(user)
					if ((usrlvl >=3) or (mdlvl >= 1)):
						argsadj = args.lower()
						if args == "":
							room.message('Enter a valid user')
						else:
							if (('#@#(*' + argsadj + '!@#$!') in pmnames):
								indexrs = pmnames.find('#@#(*' + argsadj + '!@#$!')
								indexre = pmnames.find('!@*^^(!' + argsadj + '*(^&&!')
								pmout1 = pmnames[(int(indexrs)):(int(indexre))]
								uuser = pmout1.replace(('#@#(*' + argsadj + '!@#$!'), "")
							else:
								uuser = argsadj
							endusr = ch._users.get(uuser)
							if endusr == None:
								room.message(uuser.capitalize() + ' is not in the chat.')
							else:
								room.message('I have killed ' + uuser.capitalize() + '.')
								room.banUser(endusr)
				elif ( (cmd.lower() == "defib" ) or (cmd.lower() == "unban") ):
					mdlvl = room.getLevel(user)
					if ((usrlvl >=3) or (mdlvl >= 1)):
						argsadj = args.lower()
						if args == "":
							room.unban(user)
						else:
							if (('#@#(*' + argsadj + '!@#$!') in pmnames):
								indexrs = pmnames.find('#@#(*' + argsadj + '!@#$!')
								indexre = pmnames.find('!@*^^(!' + argsadj + '*(^&&!')
								pmout1 = pmnames[(int(indexrs)):(int(indexre))]
								uuser = pmout1.replace(('#@#(*' + argsadj + '!@#$!'), "")
							else:
								uuser = argsadj
							endusr = ch._users.get(uuser)
							if endusr == None:
								room.message(uuser.capitalize() + ' is not in the chat.')
							else:
								room.message("Clear...Bzzz... I've got a pulse, it looks like " + uuser.capitalize() + ' will be ok.')
								room.unban(endusr)
				elif ( (cmd.lower() == "n" ) or (cmd.lower() == "nuke") ):
					mdlvl = room.getLevel(user)
					if ((usrlvl >=3) or (mdlvl >= 1)):
						room.clearall()
						for n in (room.getUserlist(mode = None, unique = None, memory = None)):
							room.clearUser(n)
				elif ( (cmd.lower() == "addmod" ) or (cmd.lower() == "amod") ):
					mdlvl = room.getLevel(user)
					if ((usrlvl >=3) or (mdlvl >= 1)):
						argsadj = args.lower()
						if args == "":
							room.addMod(user)
						else:
							if (('#@#(*' + argsadj + '!@#$!') in pmnames):
								indexrs = pmnames.find('#@#(*' + argsadj + '!@#$!')
								indexre = pmnames.find('!@*^^(!' + argsadj + '*(^&&!')
								pmout1 = pmnames[(int(indexrs)):(int(indexre))]
								uuser = pmout1.replace(('#@#(*' + argsadj + '!@#$!'), "")
							else:
								uuser = argsadj
							endusr = ch._users.get(uuser)
							if endusr == None:
								room.message(uuser.capitalize() + ' is not in the chat.')
							else:
								room.message(uuser.capitalize() + ' is now ONE OF US! ONE OF US!')
								room.addMod(endusr)
				elif ( (cmd.lower() == "removemod" ) or (cmd.lower() == "rmod") ):
					mdlvl = room.getLevel(user)
					if ((usrlvl >=3) or (mdlvl >= 1)):
						argsadj = args.lower()
						if args != "":
							if (('#@#(*' + argsadj + '!@#$!') in pmnames):
								indexrs = pmnames.find('#@#(*' + argsadj + '!@#$!')
								indexre = pmnames.find('!@*^^(!' + argsadj + '*(^&&!')
								pmout1 = pmnames[(int(indexrs)):(int(indexre))]
								uuser = pmout1.replace(('#@#(*' + argsadj + '!@#$!'), "")
							else:
								uuser = argsadj
							endusr = ch._users.get(uuser)
							if endusr == None:
								room.message(uuser.capitalize() + ' is not in the chat.')
							else:
								room.message(uuser.capitalize() + ' is no longer a moderator.')
								room.removeMod(endusr)
				elif ( (cmd.lower() == "wl" ) or (cmd.lower() == "whitelist") ):
					lvl3rd = open("data/whitelist/lvl3.txt","r")
					lvl3rd2 = (lvl3rd.read()).lower()
					lvl2rd = open("data/whitelist/lvl2.txt","r")
					lvl2rd2 = (lvl2rd.read()).lower()
					lvl1rd = open("data/whitelist/lvl1.txt","r")
					lvl1rd2 = (lvl1rd.read()).lower()
					lvl0rd = open("data/whitelist/lvl0.txt","r")
					lvl0rd2 = (lvl0rd.read()).lower()
					argsadj = args.lower()
					argssec = '$#@!@#$(*(^$#@' + argsadj + '!^@*#($)@(@^*&#*@$*#$*#@'
					if args.find(":") != -1: #if there's a colon somewhere
						if (usrlvl >=3):
							uuser, ulvl = argsadj.split(": ", 1)
							writeinfo = '$#@!@#$(*(^$#@' + uuser + '!^@*#($)@(@^*&#*@$*#$*#@' + '$#&@*&$*^' + user.name +  '#$@*' + uuser + '$@#^&*@!' + '\n'
							useridset = '$#@!@#$(*(^$#@' + uuser + '!^@*#($)@(@^*&#*@$*#$*#@'
							usridseted = useridset + '$#&@*&$*^'
							usered = '#$@*' + uuser + '$@#^&*@!'
							allusrlistr = open("data/zombie/allusrlist.txt","r")
							allusrlist = (allusrlistr.read()).lower()
							allusrlistr.close()
							zombielistr = open("data/zombie/zombies.txt","r")
							zombielist = (zombielistr.read()).lower()
							zombielistr.close()
							if ulvl == '3':
								if (useridset in lvl3rd2):
									room.message(uuser.capitalize() + " is alrady a level 3")
								else:
									wrtdata = open("data/whitelist/lvl3.txt","a")
									room.message(uuser + " is now a level 3! -Set by " + (user.name).capitalize() + '.')
									wrtdata.write(writeinfo)
									wrtdata.close()
									if ((("@#$*!" + uuser.lower() + "@#$*!") not in allusrlist) and (("@#$*!" + uuser.lower() + "@#$*!") not in zombielist)):
										newusrlist = open("data/zombie/allusrlist.txt","a")
										newusrlist.write("\n@#$*!" + uuser.lower() + "@#$*!")
										newusrlist.close()
									if (useridset in lvl2rd2):
										wrtdata = open("data/whitelist/lvl2.txt","w")
										indexs = lvl2rd2.find(usridseted)
										indexe = lvl2rd2.find(usered)
										rawout = lvl2rd2[(int(indexs)):(int(indexe))]
										newdata = str(lvl2rd2).replace((rawout + usered), "")
										wrtdata.write(newdata)
										wrtdata.close()
										lvl3rd.close()
										lvl2rd.close()
										lvl1rd.close()
										lvl0rd.close()
									elif (useridset in lvl1rd2):
										wrtdata = open("data/whitelist/lvl1.txt","w")
										indexs = lvl1rd2.find(usridseted)
										indexe = lvl1rd2.find(usered)
										rawout = lvl1rd2[(int(indexs)):(int(indexe))]
										newdata = str(lvl1rd2).replace((rawout + usered), "")
										wrtdata.write(newdata)
										wrtdata.close()
										lvl3rd.close()
										lvl2rd.close()
										lvl1rd.close()
										lvl0rd.close()
									elif (useridset in lvl0rd2):
										wrtdata = open("data/whitelist/lvl0.txt","w")
										indexs = lvl0rd2.find(usridseted)
										indexe = lvl0rd2.find(usered)
										rawout = lvl0rd2[(int(indexs)):(int(indexe))]
										newdata = str(lvl0rd2).replace((rawout + usered), "")
										wrtdata.write(newdata)
										wrtdata.close()
										lvl3rd.close()
										lvl2rd.close()
										lvl1rd.close()
										lvl0rd.close()
							elif ulvl == '2':
								if (useridset in lvl2rd2):
									room.message(uuser.capitalize() + " is alrady a level 2")
								else:
									wrtdata = open("data/whitelist/lvl2.txt","a")
									room.message(uuser + " is now a level 2! -Set by " + (user.name).capitalize() + '.')
									wrtdata.write(writeinfo)
									wrtdata.close()
									if ((("@#$*!" + uuser.lower() + "@#$*!") not in allusrlist) and (("@#$*!" + uuser.lower() + "@#$*!") not in zombielist)):
										newusrlist = open("data/zombie/allusrlist.txt","a")
										newusrlist.write("\n@#$*!" + uuser.lower() + "@#$*!")
										newusrlist.close()
									if (useridset in lvl3rd2):
										wrtdata = open("data/whitelist/lvl3.txt","w")
										indexs = lvl3rd2.find(usridseted)
										indexe = lvl3rd2.find(usered)
										rawout = lvl3rd2[(int(indexs)):(int(indexe))]
										newdata = str(lvl3rd2).replace((rawout + usered), "")
										wrtdata.write(newdata)
										wrtdata.close()
										lvl3rd.close()
										lvl2rd.close()
										lvl1rd.close()
										lvl0rd.close()
									elif (useridset in lvl1rd2):
										wrtdata = open("data/whitelist/lvl1.txt","w")
										indexs = lvl1rd2.find(usridseted)
										indexe = lvl1rd2.find(usered)
										rawout = lvl1rd2[(int(indexs)):(int(indexe))]
										newdata = str(lvl1rd2).replace((rawout + usered), "")
										wrtdata.write(newdata)
										wrtdata.close()
										lvl3rd.close()
										lvl2rd.close()
										lvl1rd.close()
										lvl0rd.close()
									elif (useridset in lvl0rd2):
										wrtdata = open("data/whitelist/lvl0.txt","w")
										indexs = lvl0rd2.find(usridseted)
										indexe = lvl0rd2.find(usered)
										rawout = lvl0rd2[(int(indexs)):(int(indexe))]
										newdata = str(lvl0rd2).replace((rawout + usered), "")
										wrtdata.write(newdata)
										wrtdata.close()
										lvl3rd.close()
										lvl2rd.close()
										lvl1rd.close()
										lvl0rd.close()
							elif ulvl == '1':
								if (useridset in lvl1rd2):
									room.message(uuser.capitalize() + " is alrady a level 1")
								else:
									wrtdata = open("data/whitelist/lvl1.txt","a")
									room.message(uuser + " is now a level 1! -Set by " + (user.name).capitalize() + '.')
									wrtdata.write(writeinfo)
									wrtdata.close()
									if ((("@#$*!" + uuser.lower() + "@#$*!") not in allusrlist) and (("@#$*!" + uuser.lower() + "@#$*!") not in zombielist)):
										newusrlist = open("data/zombie/allusrlist.txt","a")
										newusrlist.write("\n@#$*!" + uuser.lower() + "@#$*!")
										newusrlist.close()
									if (useridset in lvl3rd2):
										wrtdata = open("data/whitelist/lvl3.txt","w")
										indexs = lvl3rd2.find(usridseted)
										indexe = lvl3rd2.find(usered)
										rawout = lvl3rd2[(int(indexs)):(int(indexe))]
										newdata = str(lvl3rd2).replace((rawout + usered), "")
										wrtdata.write(newdata)
										wrtdata.close()
										lvl3rd.close()
										lvl2rd.close()
										lvl1rd.close()
										lvl0rd.close()
									elif (useridset in lvl2rd2):
										wrtdata = open("data/whitelist/lvl2.txt","w")
										indexs = lvl2rd2.find(usridseted)
										indexe = lvl2rd2.find(usered)
										rawout = lvl2rd2[(int(indexs)):(int(indexe))]
										newdata = str(lvl2rd2).replace((rawout + usered), "")
										wrtdata.write(newdata)
										wrtdata.close()
										lvl3rd.close()
										lvl2rd.close()
										lvl1rd.close()
										lvl0rd.close()
									elif (useridset in lvl0rd2):
										wrtdata = open("data/whitelist/lvl0.txt","w")
										indexs = lvl0rd2.find(usridseted)
										indexe = lvl0rd2.find(usered)
										rawout = lvl0rd2[(int(indexs)):(int(indexe))]
										newdata = str(lvl0rd2).replace((rawout + usered), "")
										wrtdata.write(newdata)
										wrtdata.close()
										lvl3rd.close()
										lvl2rd.close()
										lvl1rd.close()
										lvl0rd.close()
							elif ulvl == '0':
								if ((useridset in lvl0rd2) or ((useridset not in lvl1rd2) and (useridset not in lvl2rd2) and (useridset not in lvl3rd2))):
									room.message(uuser.capitalize() + " is alrady a level 0")
								else:
									wrtdata = open("data/whitelist/lvl0.txt","a")
									room.message(uuser + " is now a level 0! -Set by " + (user.name).capitalize() + '.')
									wrtdata.write(writeinfo)
									wrtdata.close()
									if (("@#$*!" + uuser.lower() + "@#$*!") in allusrlist):
										newusrs = allusrlist.replace("@#$*!" + uuser.lower() + "@#$*!", "")
										newusrlist = open("data/zombie/allusrlist.txt","w")
										newusrlist.write(newusrs)
										newusrlist.close()
									elif (("@#$*!" + uuser.lower() + "@#$*!") in zombielist):
										newzombies = zombielist.replace("@#$*!" + uuser.lower() + "@#$*!", "")
										newzombielist = open("data/zombie/zombies.txt","w")
										newzombielist.write(newusrs)
										newzombielist.close()
									if (useridset in lvl3rd2):
										wrtdata = open("data/whitelist/lvl3.txt","w")
										indexs = lvl3rd2.find(usridseted)
										indexe = lvl3rd2.find(usered)
										rawout = lvl3rd2[(int(indexs)):(int(indexe))]
										newdata = str(lvl3rd2).replace((rawout + usered), "")
										wrtdata.write(newdata)
										wrtdata.close()
										lvl3rd.close()
										lvl2rd.close()
										lvl1rd.close()
										lvl0rd.close()
									elif (useridset in lvl2rd2):
										wrtdata = open("data/whitelist/lvl2.txt","w")
										indexs = lvl2rd2.find(usridseted)
										indexe = lvl2rd2.find(usered)
										rawout = lvl2rd2[(int(indexs)):(int(indexe))]
										newdata = str(lvl2rd2).replace((rawout + usered), "")
										wrtdata.write(newdata)
										wrtdata.close()
										lvl3rd.close()
										lvl2rd.close()
										lvl1rd.close()
										lvl0rd.close()
									elif (useridset in lvl1rd2):
										wrtdata = open("data/whitelist/lvl1.txt","w")
										indexs = lvl1rd2.find(usridseted)
										indexe = lvl1rd2.find(usered)
										rawout = lvl1rd2[(int(indexs)):(int(indexe))]
										newdata = str(lvl1rd2).replace((rawout + usered), "")
										wrtdata.write(newdata)
										wrtdata.close()
										lvl3rd.close()
										lvl2rd.close()
										lvl1rd.close()
										lvl0rd.close()
						else:
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
				elif (cmd.lower()) == "modlist":
					mdlvl = room.getLevel(user)
					if (usrlvl >= 2 or mdlvl >= 1):
						room.message(", ".join(room.modnames + [room.ownername]))
				elif ( (cmd.lower() == "bl" ) or (cmd.lower() == "banlist") ):
					mdlvl = room.getLevel(user)
					if ((usrlvl >= 2) or (mdlvl >= 1)):
						banlistr1 = str(room.banlist).replace("[", "")
						banlistr2 = banlistr1.replace("[", "")
						banlistr3 = banlistr2.replace("]", "")
						banlistr4 = banlistr3.replace("[", "")
						banlistr5 = banlistr4.replace("<User: ", "")
						banlistr6 = banlistr5.replace(">", "")
						banlist = banlistr6 + ' is/are currently banned.'
						room.message(banlist)
				elif (cmd.lower()) == "contacts":
					if usrlvl >= 3:
						room.message(str((self._pm)._contacts))
				elif ( (cmd.lower() == "acontact" ) or (cmd.lower() == "addcontact") ):
					if usrlvl >= 3:
						argsadj = args.lower()
						if (('#@#(*' + argsadj + '!@#$!') in pmnames):
							indexrs = pmnames.find('#@#(*' + argsadj + '!@#$!')
							indexre = pmnames.find('!@*^^(!' + argsadj + '*(^&&!')
							pmout1 = pmnames[(int(indexrs)):(int(indexre))]
							uuser = pmout1.replace(('#@#(*' + argsadj + '!@#$!'), "")
						else:
							uuser = argsadj
						iusr = ch._users.get(uuser)
						if iusr == None:
							room.message(uuser.capitalize() + ' is not in the chat.')
						else:
							room.message('I have added ' + uuser.capitalize() + ' to my contacts.')
							(self._pm).addContact(iusr)
				elif ( (cmd.lower() == "rcontact" ) or (cmd.lower() == "removecontact") ):
					if usrlvl >= 3:
						argsadj = args.lower()
						if (('#@#(*' + argsadj + '!@#$!') in pmnames):
							indexrs = pmnames.find('#@#(*' + argsadj + '!@#$!')
							indexre = pmnames.find('!@*^^(!' + argsadj + '*(^&&!')
							pmout1 = pmnames[(int(indexrs)):(int(indexre))]
							uuser = pmout1.replace(('#@#(*' + argsadj + '!@#$!'), "")
						else:
							uuser = argsadj
						iusr = ch._users.get(uuser)
						if iusr == None:
							room.message(uuser.capitalize() + ' is not in the chat.')
						else:
							room.message('I have removed ' + uuser.capitalize() + ' from my contacts.')
							(self._pm).removeContact(iusr)
				elif ( (cmd.lower() == "pm" ) or (cmd.lower() == "privatemessage") ):
					if usrlvl >= 3:
						if args.find(" ") != -1: #if there's a colon somewhere
							wrtdata = open("data/pm/PMOUT.txt","a")
							argsadj = args.lower()
							uuserr, umsg = argsadj.split(" ", 1)
							if (('#@#(*' + uuserr + '!@#$!') in pmnames):
								indexrs = pmnames.find('#@#(*' + uuserr + '!@#$!')
								indexre = pmnames.find('!@*^^(!' + uuserr + '*(^&&!')
								pmout1 = pmnames[(int(indexrs)):(int(indexre))]
								uuser = pmout1.replace(('#@#(*' + uuserr + '!@#$!'), "")
							else:
								uuser = uuserr
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
									wrtdata.write(str((user.name + " To " + uuser.capitalize() + ': ' + str(gumsg) + '\n\n').encode('utf-8')))
									wrtdata.close()
							else:
								room.message("That user is not in my contacts.")
						else:
							room.message("Check your format, the : is missing.")
					else:
						room.message("I cannot do that for the likes of you.")
				elif (cmd.lower()) == "rooms":
					if user.name == "ion":
						roomso = str(self.getRoomNames())
						roomsa1 = roomso.replace("'","")
						roomsa2 = roomsa1.replace("{","")
						rooms = roomsa2.replace("}","")
						room.message('I am currently in the following rooms: ' + str(rooms) + ".")
					else:
						room.message("Only my lovely Mistress Ion can see this!")
				elif ( (cmd.lower() == "db" ) or (cmd.lower() == "devboard") or (cmd.lower() == "dev") or (cmd.lower() == "dm") or (cmd.lower() == "devmessage")):
					if usrlvl >=3:
						subtime = strftime("%a, %b %d @ %H:%M", gmtime())
						devboardr = open("data/boards/devboard.txt","r")
						devboard = (devboardr.read())
						devboardr.close()
						postnum = devboard.count('!@!*&&&!')
						if args == "":
							i = 0
							devboardo = devboard.replace('!@!*&&&!', ") ")
							while i <= postnum:
								devboardo = devboardo.replace('*@(!(!*!@!' + str(i), "")
								i = i + 1
							room.message(devboardo, html = True)
						elif args.startswith("remove "):
							cmd, delnum = args.split("remove ", 1)
							finfo1 = delnum + '!@!*&&&!'
							finfo2 = '*@(!(!*!@!' + delnum
							if finfo1 in devboard:
								indexs = devboard.find(finfo1)
								indexe = devboard.find(finfo2)
								rawout = devboard[(int(indexs)):(int(indexe))]
								newpost = devboard.replace(rawout + finfo2 + '.<br/>', "")
								i = int(delnum)
								while i <= 5:
									newpost = newpost.replace('*@(!(!*!@!' + str(i), '*@(!(!*!@!' + str(i-1))\
										.replace(str(i) + '!@!*&&&!', str(i-1) + '!@!*&&&!')
									i = i + 1
								wrtdata = open("data/boards/devboard.txt","w")
								wrtdata.write(newpost)
								wrtdata.close()
								room.message('"' + rawout.replace(finfo1, "") + '" has been removed from the dev board.', html = True)
							else:
									room.message("The board does not have that many posts.")
						elif args.startswith("Remove "):
							cmd, delnum = args.split("Remove ", 1)
							finfo1 = delnum + '!@!*&&&!'
							finfo2 = '*@(!(!*!@!' + delnum
							if finfo1 in devboard:
								indexs = devboard.find(finfo1)
								indexe = devboard.find(finfo2)
								rawout = devboard[(int(indexs)):(int(indexe))]
								newpost = devboard.replace(rawout + finfo2 + '.<br/>', "")
								i = int(delnum)
								while i <= 5:
									newpost = newpost.replace('*@(!(!*!@!' + str(i), '*@(!(!*!@!' + str(i-1))\
										.replace(str(i) + '!@!*&&&!', str(i-1) + '!@!*&&&!')
									i = i + 1
								wrtdata = open("data/boards/devboard.txt","w")
								wrtdata.write(newpost)
								wrtdata.close()
								room.message('"' + rawout.replace(finfo1, "") + '" has been removed from the dev board.', html = True)
							else:
									room.message("The board does not have that many posts.")
						elif args.startswith("del "):
							cmd, delnum = args.split("del ", 1)
							finfo1 = delnum + '!@!*&&&!'
							finfo2 = '*@(!(!*!@!' + delnum
							if finfo1 in devboard:
								indexs = devboard.find(finfo1)
								indexe = devboard.find(finfo2)
								rawout = devboard[(int(indexs)):(int(indexe))]
								newpost = devboard.replace(rawout + finfo2 + '.<br/>', "")
								i = int(delnum)
								while i <= 5:
									newpost = newpost.replace('*@(!(!*!@!' + str(i), '*@(!(!*!@!' + str(i-1))\
										.replace(str(i) + '!@!*&&&!', str(i-1) + '!@!*&&&!')
									i = i + 1
								wrtdata = open("data/boards/devboard.txt","w")
								wrtdata.write(newpost)
								wrtdata.close()
								room.message('"' + rawout.replace(finfo1, "") + '" has been removed from the dev board.', html = True)
							else:
									room.message("The board does not have that many posts.")
						elif args.startswith("delete "):
							cmd, delnum = args.split("delete ", 1)
							finfo1 = delnum + '!@!*&&&!'
							finfo2 = '*@(!(!*!@!' + delnum
							if finfo1 in devboard:
								indexs = devboard.find(finfo1)
								indexe = devboard.find(finfo2)
								rawout = devboard[(int(indexs)):(int(indexe))]
								newpost = devboard.replace(rawout + finfo2 + '.<br/>', "")
								i = int(delnum)
								while i <= 5:
									newpost = newpost.replace('*@(!(!*!@!' + str(i), '*@(!(!*!@!' + str(i-1))\
										.replace(str(i) + '!@!*&&&!', str(i-1) + '!@!*&&&!')
									i = i + 1
								wrtdata = open("data/boards/devboard.txt","w")
								wrtdata.write(newpost)
								wrtdata.close()
								room.message('"' + rawout.replace(finfo1, "") + '" has been removed from the dev board.', html = True)
							else:
									room.message("The board does not have that many posts.")
						elif args.startswith("Delete "):
							cmd, delnum = args.split("Delete ", 1)
							finfo1 = delnum + '!@!*&&&!'
							finfo2 = '*@(!(!*!@!' + delnum
							if finfo1 in devboard:
								indexs = devboard.find(finfo1)
								indexe = devboard.find(finfo2)
								rawout = devboard[(int(indexs)):(int(indexe))]
								newpost = devboard.replace(rawout + finfo2 + '.<br/>', "")
								i = int(delnum)
								while i <= 5:
									newpost = newpost.replace('*@(!(!*!@!' + str(i), '*@(!(!*!@!' + str(i-1))\
										.replace(str(i) + '!@!*&&&!', str(i-1) + '!@!*&&&!')
									i = i + 1
								wrtdata = open("data/boards/devboard.txt","w")
								wrtdata.write(newpost)
								wrtdata.close()
								room.message('"' + rawout.replace(finfo1, "") + '" has been removed from the dev board.', html = True)
							else:
									room.message("The board does not have that many posts.")
						elif args.startswith("Del "):
							cmd, delnum = args.split("Del ", 1)
							finfo1 = delnum + '!@!*&&&!'
							finfo2 = '*@(!(!*!@!' + delnum
							if finfo1 in devboard:
								indexs = devboard.find(finfo1)
								indexe = devboard.find(finfo2)
								rawout = devboard[(int(indexs)):(int(indexe))]
								newpost = devboard.replace(rawout + finfo2 + '.<br/>', "")
								i = int(delnum)
								while i <= 5:
									newpost = newpost.replace('*@(!(!*!@!' + str(i), '*@(!(!*!@!' + str(i-1))\
										.replace(str(i) + '!@!*&&&!', str(i-1) + '!@!*&&&!')
									i = i + 1
								wrtdata = open("data/boards/devboard.txt","w")
								wrtdata.write(newpost)
								wrtdata.close()
								room.message('"' + rawout.replace(finfo1, "") + '" has been removed from the dev board.', html = True)
							else:
									room.message("The board does not have that many posts.")
						else:
							if postnum == 5:
								finfo1 = '1!@!*&&&!'
								finfo2 = '*@(!(!*!@!1'
								indexs = devboard.find(finfo1)
								indexe = devboard.find(finfo2)
								rawout = devboard[(int(indexs)):(int(indexe))]
								minus1 = devboard.replace(rawout + finfo2 + '.<br/>', "")
								switch2 = minus1.replace('2!@!*&&&!', '1!@!*&&&!')\
									.replace('*@(!(!*!@!2', '*@(!(!*!@!1')
								switch3 = switch2.replace('3!@!*&&&!', '2!@!*&&&!')\
									.replace('*@(!(!*!@!3', '*@(!(!*!@!2')
								switch4 = switch3.replace('4!@!*&&&!', '3!@!*&&&!')\
									.replace('*@(!(!*!@!4', '*@(!(!*!@!3')
								newpost = switch4.replace('5!@!*&&&!', '4!@!*&&&!')\
									.replace('*@(!(!*!@!5', '*@(!(!*!@!4')
								wrtdata = open("data/boards/devboard.txt","w")
								wrtdata.write(newpost)
								wrtdata.close()
								newpost = str(postnum)+ '!@!*&&&!' + args + ' - posted by <b>' + user.name.capitalize() + '</b> on <i>' + subtime + '</i>*@(!(!*!@!' + str(postnum) + '.<br/>'
								wrtdata = open("data/boards/devboard.txt","a")
								wrtdata.write(newpost)
								wrtdata.close()
								room.message('"' + args + '" has been posted to the dev board.')
							else:
								postnum = postnum + 1
								newpost = str(postnum)+ '!@!*&&&!' + args + ' - posted by <b>' + user.name.capitalize() + '</b> on <i>' + subtime + '</i>*@(!(!*!@!' + str(postnum) + '.<br/>'
								wrtdata = open("data/boards/devboard.txt","a")
								wrtdata.write(newpost)
								wrtdata.close()
								room.message('"' + args + '" has been posted to the dev board.')
				elif ( (cmd.lower() == "rm" ) or (cmd.lower() == "roommessage") ):
					if usrlvl >= 3:
						if args.find(": ") != -1: #if there's a colon somewhere
							argsadj = args.lower()
							uroomr, umsg = argsadj.split(": ", 1)
							if (('#@#(*' + uroomr + '!@#$!') in roomnames):
								indexrs = roomnames.find('#@#(*' + uroomr + '!@#$!')
								indexre = roomnames.find('!@*^^(!' + uroomr + '*(^&&!')
								roomout1 = roomnames[(int(indexrs)):(int(indexre))]
								uroomr = roomout1.replace(('#@#(*' + uroomr + '!@#$!'), "")
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
				elif ( (cmd.lower() == "gtfo" ) or (cmd.lower() == "leave") ):
					mdlvl = room.getLevel(user)
					if (usrlvl >= 2 or mdlvl >= 1):
						if (args == ''):
							room.message("Okay, if it will make you happy. ;(+20")
							self.leaveRoom(str(room.name))
						else:
							uroomr = args.lower()
							if (('#@#(*' + uroomr + '!@#$!') in roomnames):
								indexrs = roomnames.find('#@#(*' + uroomr + '!@#$!')
								indexre = roomnames.find('!@*^^(!' + uroomr + '*(^&&!')
								roomout1 = roomnames[(int(indexrs)):(int(indexre))]
								uroomr = roomout1.replace(('#@#(*' + uroomr + '!@#$!'), "")
							if (uroomr in str(self._rooms)):
								room.message("Okay, if it will make you happy. ;(+20")
								self.leaveRoom(uroomr)
							else:
								room.message("I am not in " + uroomr.capitalize() + ", thus I can't leave it.")
					else:
						room.message("No, you!")
				elif (cmd.lower()) == "join":
					if usrlvl >= 2:
						if args == '':
							room.message('Please enter a valid room.')
						else:
							uroomr = args.lower()
							if (('#@#(*' + uroomr + '!@#$!') in roomnames):
								indexrs = roomnames.find('#@#(*' + uroomr + '!@#$!')
								indexre = roomnames.find('!@*^^(!' + uroomr + '*(^&&!')
								roomout1 = roomnames[(int(indexrs)):(int(indexre))]
								uroomr = roomout1.replace(('#@#(*' + uroomr + '!@#$!'), "")
							if (uroomr in str(self._rooms)):
								room.message("I am already in " + uroomr.capitalize() + '.')
							else:	
								self.joinRoom(uroomr)
								room.message('I have joined ' + uroomr.capitalize() + '.')
				elif ( (cmd.lower() == "rc" ) or (cmd.lower() == "reconnect") ):
					if usrlvl >= 2:
						if args == '':
							self.leaveRoom(room.name)
							time.sleep(2)
							self.joinRoom(room.name)
						else:
							uroomr = args.lower()
							if ( (uroomr == 'buzz') or (uroomr == 'ab') or (uroomr == 'buzzez') or (uroomr == 'animebuzz') ):
								uroomr = 'animebuzzez'
							elif ( (uroomr == 'home') or (uroomr == 'teruchat') or (uroomr == 'teru') or (uroomr == 'tc') ):
								uroomr = 'teruchat'
							elif ( (uroomr == 'as') or (uroomr == 'seed')):
								uroomr = 'animeseed'
							elif ( (uroomr == 'pu') or (uroomr == 'uri') or (uroomr == 'project')):
								uroomr = 'projecturi'
							elif ( (uroomr == 'am') or (uroomr == 'animemaniacs') or (uroomr == 'maniacs') or (uroomr == 'animaniacs')):
								uroomr = 'amaniacs'
							elif ( (uroomr == 'kuro') or (uroomr == 'kn') or (uroomr == 'network')):
								uroomr = 'kuronetwork'
							elif ( (uroomr == 'love') or (uroomr == 'lma') or (uroomr == 'lovemyanime') or (uroomr == 'lovemy')):
								uroomr = 'lovemyanimechat'
							elif ( (uroomr == 'animeon') or (uroomr == 'watchanimeon')):
								uroomr = 'watchanimeonn'
							elif uroomr == 'animenow':
								uroomr = 'watchanimenow'
							elif ( (uroomr == 'aftv') or (uroomr == 'af') or (uroomr == 'animefreak')):
								uroomr = 'tvanimefreak'
							if (uroomr in str(self._rooms)):
								self.leaveRoom(uroomr)
								time.sleep(2)
								self.joinRoom(uroomr)
							else:
								room.message('I am not in ' + uroomr + '.')
				elif ( (cmd.lower() == "help" ) or (cmd.lower() == "cmds") or (cmd.lower() == "cmd") or (cmd.lower() == "commands") ):
					room.message('<a href="http://t6ru.blogspot.com/p/bot-commands.html" target="_blank">For help and the list of commands click here.</a>', html = True)
				elif (cmd.lower()) == "uptime":
						room.message("I connected at " + (str(now).replace("['", "")).replace("']", ""))
				elif ( (cmd.lower() == "fish" ) or (cmd.lower() == "fishes") ):
					if usrlvl >= 2:
						room.message("><>")
				elif ( (cmd.lower() == "report" ) or (cmd.lower() == "r") or (cmd.lower() == "reports") or (cmd.lower() == "feedback")  or (cmd.lower() == "fb")):
					if usrlvl >=1:
						subtime = strftime("%a, %b %d @ %H:%M", gmtime())
						reportboardr = open("data/boards/reportboard.txt","r")
						reportboard = (reportboardr.read())
						reportboardr.close()
						postnum = reportboard.count('!@!*&&&!')
						if (args == "" and usrlvl >=2):
							i = 0
							reportboardo = reportboard.replace('!@!*&&&!', ") ")
							while i <= postnum:
								reportboardo = reportboardo.replace('*@(!(!*!@!' + str(i), "")
								i = i + 1
							room.message(reportboardo, html = True)
						elif (args.startswith("remove ") and usrlvl >=2):
							cmd, delnum = args.split("remove ", 1)
							finfo1 = delnum + '!@!*&&&!'
							finfo2 = '*@(!(!*!@!' + delnum
							if finfo1 in reportboard:
								indexs = reportboard.find(finfo1)
								indexe = reportboard.find(finfo2)
								rawout = reportboard[(int(indexs)):(int(indexe))]
								newpost = reportboard.replace(rawout + finfo2 + '.<br/>', "")
								i = int(delnum)
								while i <= 5:
									newpost = newpost.replace('*@(!(!*!@!' + str(i), '*@(!(!*!@!' + str(i-1))\
										.replace(str(i) + '!@!*&&&!', str(i-1) + '!@!*&&&!')
									i = i + 1
								wrtdata = open("data/boards/reportboard.txt","w")
								wrtdata.write(newpost)
								wrtdata.close()
								room.message('"' + rawout.replace(finfo1, "") + '" has been removed from the report board.', html = True)
						elif (args.startswith("Remove ") and usrlvl >=2):
							cmd, delnum = args.split("Remove ", 1)
							finfo1 = delnum + '!@!*&&&!'
							finfo2 = '*@(!(!*!@!' + delnum
							if finfo1 in reportboard:
								indexs = reportboard.find(finfo1)
								indexe = reportboard.find(finfo2)
								rawout = reportboard[(int(indexs)):(int(indexe))]
								newpost = reportboard.replace(rawout + finfo2 + '.<br/>', "")
								i = int(delnum)
								while i <= 5:
									newpost = newpost.replace('*@(!(!*!@!' + str(i), '*@(!(!*!@!' + str(i-1))\
										.replace(str(i) + '!@!*&&&!', str(i-1) + '!@!*&&&!')
									i = i + 1
								wrtdata = open("data/boards/reportboard.txt","w")
								wrtdata.write(newpost)
								wrtdata.close()
								room.message('"' + rawout.replace(finfo1, "") + '" has been removed from the report board.', html = True)
							else:
									room.message("The board does not have that many posts.")
						elif (args.startswith("del ") and usrlvl >=2):
							cmd, delnum = args.split("del ", 1)
							finfo1 = delnum + '!@!*&&&!'
							finfo2 = '*@(!(!*!@!' + delnum
							if finfo1 in reportboard:
								indexs = reportboard.find(finfo1)
								indexe = reportboard.find(finfo2)
								rawout = reportboard[(int(indexs)):(int(indexe))]
								newpost = reportboard.replace(rawout + finfo2 + '.<br/>', "")
								i = int(delnum)
								while i <= 5:
									newpost = newpost.replace('*@(!(!*!@!' + str(i), '*@(!(!*!@!' + str(i-1))\
										.replace(str(i) + '!@!*&&&!', str(i-1) + '!@!*&&&!')
									i = i + 1
								wrtdata = open("data/boards/reportboard.txt","w")
								wrtdata.write(newpost)
								wrtdata.close()
								room.message('"' + rawout.replace(finfo1, "") + '" has been removed from the report board.', html = True)
							else:
									room.message("The board does not have that many posts.")
						elif (args.startswith("delete ") and usrlvl >=2):
							cmd, delnum = args.split("delete ", 1)
							finfo1 = delnum + '!@!*&&&!'
							finfo2 = '*@(!(!*!@!' + delnum
							if finfo1 in reportboard:
								indexs = reportboard.find(finfo1)
								indexe = reportboard.find(finfo2)
								rawout = reportboard[(int(indexs)):(int(indexe))]
								newpost = reportboard.replace(rawout + finfo2 + '.<br/>', "")
								i = int(delnum)
								while i <= 5:
									newpost = newpost.replace('*@(!(!*!@!' + str(i), '*@(!(!*!@!' + str(i-1))\
										.replace(str(i) + '!@!*&&&!', str(i-1) + '!@!*&&&!')
									i = i + 1
								wrtdata = open("data/boards/reportboard.txt","w")
								wrtdata.write(newpost)
								wrtdata.close()
								room.message('"' + rawout.replace(finfo1, "") + '" has been removed from the report board.', html = True)
							else:
									room.message("The board does not have that many posts.")
						elif (args.startswith("Delete ") and usrlvl >=2):
							cmd, delnum = args.split("Delete ", 1)
							finfo1 = delnum + '!@!*&&&!'
							finfo2 = '*@(!(!*!@!' + delnum
							if finfo1 in reportboard:
								indexs = reportboard.find(finfo1)
								indexe = reportboard.find(finfo2)
								rawout = reportboard[(int(indexs)):(int(indexe))]
								newpost = reportboard.replace(rawout + finfo2 + '.<br/>', "")
								i = int(delnum)
								while i <= 5:
									newpost = newpost.replace('*@(!(!*!@!' + str(i), '*@(!(!*!@!' + str(i-1))\
										.replace(str(i) + '!@!*&&&!', str(i-1) + '!@!*&&&!')
									i = i + 1
								wrtdata = open("data/boards/reportboard.txt","w")
								wrtdata.write(newpost)
								wrtdata.close()
								room.message('"' + rawout.replace(finfo1, "") + '" has been removed from the report board.', html = True)
							else:
									room.message("The board does not have that many posts.")
						elif (args.startswith("Del ") and usrlvl >=2):
							cmd, delnum = args.split("remove ", 1)
							finfo1 = delnum + '!@!*&&&!'
							finfo2 = '*@(!(!*!@!' + delnum
							if finfo1 in reportboard:
								indexs = reportboard.find(finfo1)
								indexe = reportboard.find(finfo2)
								rawout = reportboard[(int(indexs)):(int(indexe))]
								newpost = reportboard.replace(rawout + finfo2 + '.<br/>', "")
								i = int(delnum)
								while i <= 5:
									newpost = newpost.replace('*@(!(!*!@!' + str(i), '*@(!(!*!@!' + str(i-1))\
										.replace(str(i) + '!@!*&&&!', str(i-1) + '!@!*&&&!')
									i = i + 1
								wrtdata = open("data/boards/reportboard.txt","w")
								wrtdata.write(newpost)
								wrtdata.close()
								room.message('"' + rawout.replace(finfo1, "") + '" has been removed from the report board.', html = True)
							else:
									room.message("The board does not have that many posts.")
						else:
							countres = reportboard.count('<b>' + user.name.capitalize() + '</b>')
							
							if countres >= 3:
								room.message('You have reported too much recently, please wait until the dev team can clear up your previous reports.')
							else:
								postnum = postnum + 1
								newpost = str(postnum) + '!@!*&&&!' + args + ' - posted by <b>' + user.name.capitalize() + '</b> on <i>' + subtime + '</i>*@(!(!*!@!' + str(postnum) + '.<br/>'
								wrtdata = open("data/boards/reportboard.txt","a")
								wrtdata.write(newpost)
								wrtdata.close()
								room.message('You have reported "' + args + '".')
				elif ( (cmd.lower() == "unhide" ) or (cmd.lower() == "timein") or (cmd.lower() == "uh") or (cmd.lower() == "ti") or (cmd.lower() == "ok") or (cmd.lower() == "resume") or (cmd.lower() == "show") or (cmd.lower() == "run") or (cmd.lower() == "normalmode") or (cmd.lower() == "nm") or (cmd.lower() == "normal") or (cmd.lower() == "go") or (cmd.lower() == "play") or (cmd.lower() == "alright") ):
					room.message('Yay! I am not in the timeout corner any more!')
					oldhrlraw = open("data/rmset/hiddenroomlist.txt","r")
					oldhrl = (oldhrlraw.read()).lower()
					wrthrl = open("data/rmset/hiddenroomlist.txt","w")
					newhrl = oldhrl.replace("#@@$!!(!*@" + room.name + "@@#$&*(**!" + room.name + "!(!*@&&^^^!", "")
					wrthrl.write(newhrl)
					wrthrl.close()
					oldhrlraw.close()
		elif ((callname == 6) and (usrlvl >= 1)):
			data = msgbody[1:].split(" ", 1)
			if len(data) > 1:
				cmd, args = data[0], data[1]
			else:
				cmd, args = data[0], ""
			#if ((("#@@$!!(!*@" + room.name + "@@#$&*(**!") in modmode) or (("#@@$!!(!*@" + room.name + "@@#$&*(**!") in funmode) or (("#@@$!!(!*@" + room.name + "@@#$&*(**!") in usefulmode)):
			if ( (cmd.lower() == "hide" ) or (cmd.lower() == "timeout") or (cmd.lower() == "h") or (cmd.lower() == "to") or (cmd.lower() == "sit") or (cmd.lower() == "break") or (cmd.lower() == "stop") or (cmd.lower() == "shh") or (cmd.lower() == "stfu") or (cmd.lower() == "moderation") or (cmd.lower() == "restrict") or (cmd.lower() == "modmode") or (cmd.lower() == "modonly") or (cmd.lower() == "mo") or (cmd.lower() == "quite") or (cmd.lower() == "mm") or (cmd.lower() == "sh") or (cmd.lower() == "shhh") ):
				mdlvl = room.getLevel(user)
				if (usrlvl >=2 or mdlvl>=1):
					writeinfo = "#@@$!!(!*@" + room.name + "@@#$&*(**!" + room.name + "!(!*@&&^^^!\n"
					room.message("O.o I'm sorry. -hides-")
					wrtdata = open("data/rmset/hiddenroomlist.txt","a")
					wrtdata.write(writeinfo)
					wrtdata.close()
			elif ( (cmd.lower() == "rs" ) or (cmd.lower() == "roomsettings") ):
				argsadj = args.lower()
				mdlvl = room.getLevel(user)
				if args.find(":") != -1: #if there's a colon somewhere
					if (usrlvl >=2):
						uroomr, uset = argsadj.split(": ", 1)
						if (('#@#(*' + uroomr + '!@#$!') in roomnames):
								indexrs = roomnames.find('#@#(*' + uroomr + '!@#$!')
								indexre = roomnames.find('!@*^^(!' + uroomr + '*(^&&!')
								roomout1 = roomnames[(int(indexrs)):(int(indexre))]
								uroom = roomout1.replace(('#@#(*' + uroomr + '!@#$!'), "")
						else: uroom = uroomr
						if (uroom in str(self._rooms)):
							roomfind = "#@@$!!(!*@" + uroom + "@@#$&*(**!"
							writeinfo = "#@@$!!(!*@" + uroom + "@@#$&*(**!" + uroom + "!(!*@&&^^^!\n"
							findinfo1 = "#@@$!!(!*@" + uroom
							findinfo2 = "@@#$&*(**!" + uroom + "!(!*@&&^^^!"
							if ('mod' in uset):
								if (uroom not in modmode):
									wrtdata = open("data/rmset/modmode.txt","a")
									wrtdata.write(writeinfo)
									wrtdata.close()
									if ((roomfind) in usefulmode):
										wrtdata = open("data/rmset/usefulmode.txt","w")
										indexs = usefulmode.find(findinfo1)
										indexe = usefulmode.find(findinfo2)
										rawout = usefulmode[(int(indexs)):(int(indexe))]
										newdata = str(usefulmode).replace((findinfo1 + findinfo2), "")
										wrtdata.write(newdata)
										wrtdata.close()
									elif ((roomfind) in funmode):
										wrtdata = open("data/rmset/funmode.txt","w")
										indexs = funmode.find(findinfo1)
										indexe = funmode.find(findinfo2)
										rawout = funmode[(int(indexs)):(int(indexe))]
										newdata = str(funmode).replace((findinfo1 + findinfo2), "")
										wrtdata.write(newdata)
										wrtdata.close()
									if ((roomfind) in aimode):
										room.message(uroom.capitalize() + ' is now set to moderation functions only with AI on.')
									else:
										room.message(uroom + ' is now set to moderation functions only with AI off.')
								else:
									if ((roomfind) in aimode):
										room.message(uroom.capitalize() + ' is already set to moderation functions only with AI on.')
									else:
										room.message(uroom + ' is already set to moderation functions only with AI off.')
							elif ('useful' in uset):
								if (uroom not in usefulmode):
									wrtdata = open("data/rmset/usefulmode.txt","a")
									room.message(uroom.capitalize() + ' is now set to useful and moderation functions only.')
									wrtdata.write(writeinfo)
									wrtdata.close()
									if ((roomfind) in modmode):
										wrtdata = open("data/rmset/modmode.txt","w")
										indexs = modmode.find(findinfo1)
										indexe = modmode.find(findinfo2)
										rawout = modmode[(int(indexs)):(int(indexe))]
										newdata = str(modmode).replace((findinfo1 + findinfo2), "")
										wrtdata.write(newdata)
										wrtdata.close()
									elif ((roomfind) in funmode):
										wrtdata = open("data/rmset/funmode.txt","w")
										indexs = funmode.find(findinfo1)
										indexe = funmode.find(findinfo2)
										rawout = funmode[(int(indexs)):(int(indexe))]
										newdata = str(funmode).replace((findinfo1 + findinfo2), "")
										wrtdata.write(newdata)
										wrtdata.close()
									if ((roomfind) in aimode):
										room.message(uroom.capitalize() + ' is now set to useful and moderation functions only with AI on.')
									else:
										room.message(uroom + ' is now set to moderation functions only with AI off.')
								else:
									if ((roomfind) in aimode):
										room.message(uroom.capitalize() + ' is already set to useful and moderation functions only with AI on.')
									else:
										room.message(uroom.capitalize() + ' is already set to moderation functions only with AI off.')
							elif (('fun' in uset) or ('all' in uset)):
								if (uroom not in funmode):
									wrtdata = open("data/rmset/funmode.txt","a")
									wrtdata.write(writeinfo)
									wrtdata.close()
									if ((roomfind) in modmode):
										wrtdata = open("data/rmset/modmode.txt","w")
										indexs = modmode.find(findinfo1)
										indexe = modmode.find(findinfo2)
										rawout = modmode[(int(indexs)):(int(indexe))]
										newdata = str(modmode).replace((findinfo1 + findinfo2), "")
										wrtdata.write(newdata)
										wrtdata.close()
									elif ((roomfind) in usefulmode):
										wrtdata = open("data/rmset/usefulmode.txt","w")
										indexs = usefulmode.find(findinfo1)
										indexe = usefulmode.find(findinfo2)
										rawout = usefulmode[(int(indexs)):(int(indexe))]
										newdata = str(usefulmode).replace((findinfo1 + findinfo2), "")
										wrtdata.write(newdata)
										wrtdata.close()
									if ((roomfind) in aimode):
										room.message(uroom.capitalize() + ' is now set to all functions, with AI on.')
									else:
										room.message(uroom.capitalize() + ' is now set to all functions, with AI off.')
								else:
									if ((roomfind) in aimode):
										room.message(uroom.capitalize() + ' is already set to all functions, with AI on.')
									else:
										room.message(uroom.capitalize() + ' is already set to all functions, with AI off.')
							if (('ai' in uset) and ('on' in uset)):
								if (uroom not in aimode):
									wrtdata = open("data/rmset/aimode.txt","a")
									room.message(uroom.capitalize() + ' is now set to AI on.')
									wrtdata.write(writeinfo)
									wrtdata.close()
								else:
									room.message(uroom.capitalize() + ' is already set to AI on.')
							elif (('ai' in uset) and ('off' in uset)):
								if (uroom in aimode):
									room.message(uroom.capitalize() + ' is now set to AI off.')
									wrtdata = open("data/rmset/aimode.txt","w")
									indexs = modmode.find(findinfo1)
									indexe = modmode.find(findinfo2)
									rawout = modmode[(int(indexs)):(int(indexe))]
									newdata = str(aimode).replace((findinfo1 + findinfo2), "")
									wrtdata.write(newdata)
									wrtdata.close()
									if ((roomfind) in modmode):
										wrtdata = open("data/rmset/modmode.txt","w")
										indexs = modmode.find(findinfo1)
										indexe = modmode.find(findinfo2)
										rawout = modmode[(int(indexs)):(int(indexe))]
										newdata = str(modmode).replace((findinfo1 + findinfo2), "")
										wrtdata.write(newdata)
										wrtdata.close()
									elif ((roomfind) in usefulmode):
										wrtdata = open("data/rmset/usefulmode.txt","w")
										indexs = usefulmode.find(findinfo1)
										indexe = usefulmode.find(findinfo2)
										rawout = usefulmode[(int(indexs)):(int(indexe))]
										newdata = str(usefulmode).replace((findinfo1 + findinfo2), "")
										wrtdata.write(newdata)
										wrtdata.close()
									if ((roomfind) not in funmode):
										wrtdata2 = open("data/rmset/funmode.txt","a")
										wrtdata2.write(writeinfo)
										wrtdata2.close()
								else:
									room.message(uroom.capitalize() + ' is already set to AI off.')
						else:
							room.message('Enter a valid room.')
					else:
						room.message("Lol, no.")
				else:
					if (args == ""):
						if (usrlvl >=2 or mdlvl >=1):
							uroom = room.name
							roomfind = "#@@$!!(!*@" + uroom + "@@#$&*(**!"
							if (roomfind in modmode):
								if (roomfind in aimode):
									room.message('I am currently set to moderation functions only with AI on in ' + uroom.capitalize() + '.')
								else:
									room.message('I am currently set to moderation functions only  with AI off in ' + uroom.capitalize() + '.')
							elif (roomfind in usefulmode):
								if (roomfind in aimode):
									room.message('I am currently set to useful and moderation functions only with AI on in ' + uroom.capitalize() + '.')
								else:
									room.message('I am currently set to useful and moderation functions only with AI off in ' + uroom.capitalize() + '.')
							elif (roomfind in funmode):
								if (roomfind in aimode):
									room.message('I am currently set to all functions with AI on in ' + uroom.capitalize() + '.')
								else:
									room.message('I am currently set to all functions with AI off in ' + uroom.capitalize() + '.')
							else:
								room.message('I do not have settings for ' + uroom.capitalize() + '.')
					elif ('mod' in argsadj):
						if (usrlvl >=2 or mdlvl >=1):
							uroom = room.name
							roomfind = "#@@$!!(!*@" + uroom + "@@#$&*(**!"
							writeinfo = "#@@$!!(!*@" + uroom + "@@#$&*(**!" + uroom + "!(!*@&&^^^!\n"
							findinfo1 = "#@@$!!(!*@" + uroom
							findinfo2 = "@@#$&*(**!" + uroom + "!(!*@&&^^^!"
							if (uroom not in modmode):
								wrtdata = open("data/rmset/modmode.txt","a")
								wrtdata.write(writeinfo)
								wrtdata.close()
								if ((roomfind) in usefulmode):
									wrtdata = open("data/rmset/usefulmode.txt","w")
									indexs = usefulmode.find(findinfo1)
									indexe = usefulmode.find(findinfo2)
									rawout = usefulmode[(int(indexs)):(int(indexe))]
									newdata = str(usefulmode).replace((findinfo1 + findinfo2), "")
									wrtdata.write(newdata)
									wrtdata.close()
								elif ((roomfind) in funmode):
									wrtdata = open("data/rmset/funmode.txt","w")
									indexs = funmode.find(findinfo1)
									indexe = funmode.find(findinfo2)
									rawout = funmode[(int(indexs)):(int(indexe))]
									newdata = str(funmode).replace((findinfo1 + findinfo2), "")
									wrtdata.write(newdata)
									wrtdata.close()
								if ((roomfind) in aimode):
									room.message(uroom.capitalize() + ' is now set to moderation functions only with AI on.')
								else:
									room.message(uroom + ' is now set to moderation functions only with AI off.')
							else:
								if ((roomfind) in aimode):
									room.message(uroom.capitalize() + ' is now set to moderation functions only with AI on.')
								else:
									room.message(uroom.capitalize() + ' is now set to moderation functions only with AI off.')
					elif ('useful' in argsadj):
						if (usrlvl >=2 or mdlvl >=1):
							uroom = room.name
							roomfind = "#@@$!!(!*@" + uroom + "@@#$&*(**!"
							writeinfo = "#@@$!!(!*@" + uroom + "@@#$&*(**!" + uroom + "!(!*@&&^^^!\n"
							findinfo1 = "#@@$!!(!*@" + uroom
							findinfo2 = "@@#$&*(**!" + uroom + "!(!*@&&^^^!"
							if (uroom not in usefulmode):
								wrtdata = open("data/rmset/usefulmode.txt","a")
								wrtdata.write(writeinfo)
								wrtdata.close()
								if ((roomfind) in modmode):
									wrtdata = open("data/rmset/modmode.txt","w")
									indexs = modmode.find(findinfo1)
									indexe = modmode.find(findinfo2)
									rawout = modmode[(int(indexs)):(int(indexe))]
									newdata = str(modmode).replace((findinfo1 + findinfo2), "")
									wrtdata.write(newdata)
									wrtdata.close()
								elif ((roomfind) in funmode):
									wrtdata = open("data/rmset/funmode.txt","w")
									indexs = funmode.find(findinfo1)
									indexe = funmode.find(findinfo2)
									rawout = funmode[(int(indexs)):(int(indexe))]
									newdata = str(funmode).replace((findinfo1 + findinfo2), "")
									wrtdata.write(newdata)
									wrtdata.close()
								if ((roomfind) in aimode):
									room.message(uroom.capitalize() + ' is now set to useful and moderation functions only with AI on.')
								else:
									room.message(uroom + ' is now set to useful and moderation functions only with AI off.')
							else:
								if ((roomfind) in aimode):
									room.message(uroom.capitalize() + ' is now set to useful and moderation functions only with AI on.')
								else:
									room.message(uroom.capitalize() + ' is now set to useful and moderation functions only with AI off.')
					elif ('fun' in argsadj):
						if (usrlvl >=2 or mdlvl >=1):
							uroom = room.name
							roomfind = "#@@$!!(!*@" + uroom + "@@#$&*(**!"
							writeinfo = "#@@$!!(!*@" + uroom + "@@#$&*(**!" + uroom + "!(!*@&&^^^!\n"
							findinfo1 = "#@@$!!(!*@" + uroom
							findinfo2 = "@@#$&*(**!" + uroom + "!(!*@&&^^^!"
							if (uroom not in funmode):
								wrtdata = open("data/rmset/funmode.txt","a")
								wrtdata.write(writeinfo)
								wrtdata.close()
								if ((roomfind) in modmode):
									wrtdata = open("data/rmset/modmode.txt","w")
									indexs = modmode.find(findinfo1)
									indexe = modmode.find(findinfo2)
									rawout = modmode[(int(indexs)):(int(indexe))]
									newdata = str(modmode).replace((findinfo1 + findinfo2), "")
									wrtdata.write(newdata)
									wrtdata.close()
								elif ((roomfind) in usefulmode):
									wrtdata = open("data/rmset/usefulmode.txt","w")
									indexs = usefulmode.find(findinfo1)
									indexe = usefulmode.find(findinfo2)
									rawout = usefulmode[(int(indexs)):(int(indexe))]
									newdata = str(usefulmode).replace((findinfo1 + findinfo2), "")
									wrtdata.write(newdata)
									wrtdata.close()
								if ((roomfind) in aimode):
									room.message(uroom.capitalize() + ' is now set to all functions, with AI on.')
								else:
									room.message(uroom.capitalize()+ ' is now set to all functions, with AI off.')
							else:
								if ((roomfind) in aimode):
									room.message(uroom.capitalize() + ' is already set to all functions, with AI on.')
								else:
									room.message(uroom.capitalize() + ' is already set to all functions, with AI off.')
					if (('ai' in argsadj) and ('on' in argsadj)):
						if (usrlvl >=2 or mdlvl >=1):
							uroom = room.name
							roomfind = "#@@$!!(!*@" + uroom + "@@#$&*(**!"
							writeinfo = "#@@$!!(!*@" + uroom + "@@#$&*(**!" + uroom + "!(!*@&&^^^!\n"
							findinfo1 = "#@@$!!(!*@" + uroom
							findinfo2 = "@@#$&*(**!" + uroom + "!(!*@&&^^^!"
							if (uroom not in aimode):
								wrtdata = open("data/rmset/aimode.txt","a")
								room.message(uroom.capitalize() + ' is now set to AI on.')
								wrtdata.write(writeinfo)
								wrtdata.close()
							else:
								room.message(uroom.capitalize() + ' is already set to AI on.')
					elif (('ai' in argsadj) and ('off' in argsadj)):
						if (usrlvl >=2 or mdlvl >=1):
							uroom = room.name
							roomfind = "#@@$!!(!*@" + uroom + "@@#$&*(**!"
							writeinfo = "#@@$!!(!*@" + uroom + "@@#$&*(**!" + uroom + "!(!*@&&^^^!\n"
							findinfo1 = "#@@$!!(!*@" + uroom
							findinfo2 = "@@#$&*(**!" + uroom + "!(!*@&&^^^!"
							if (uroom in aimode):
								room.message(uroom.capitalize() + ' is now set to AI off.')
								wrtdata = open("data/rmset/aimode.txt","w")
								indexs = modmode.find(findinfo1)
								indexe = modmode.find(findinfo2)
								rawout = modmode[(int(indexs)):(int(indexe))]
								newdata = str(aimode).replace((findinfo1 + findinfo2), "")
								wrtdata.write(newdata)
								wrtdata.close()
							else:
								room.message(uroom.capitalize() + ' is already set to AI off.')									
					elif ((args != '') and ('ai' not in argsadj) and ('fun' not in argsadj) and ('mod' not in argsadj) and ('useful' not in argsadj) and ('all' not in argsadj)):
						if (usrlvl >=2):	
							if (('#@#(*' + argsadj + '!@#$!') in roomnames):
								indexrs = roomnames.find('#@#(*' + argsadj + '!@#$!')
								indexre = roomnames.find('!@*^^(!' + argsadj + '*(^&&!')
								roomout1 = roomnames[(int(indexrs)):(int(indexre))]
								uroom = roomout1.replace(('#@#(*' + argsadj + '!@#$!'), "")
							else: uroom = argsadj
							roomfind = "#@@$!!(!*@" + uroom + "@@#$&*(**!"
							if (roomfind in modmode):
								if (roomfind in aimode):
									room.message('I am currently set to moderation functions only with AI on in ' + uroom.capitalize() + '.')
								else:
									room.message('I am currently set to moderation functions only with AI off in ' + uroom.capitalize() + '.')
							elif (roomfind in usefulmode):
								if (roomfind in aimode):
									room.message('I am currently set to useful and moderation functions only with AI on in ' + uroom.capitalize() + '.')
								else:
									room.message('I am currently set to useful and moderation functions only with AI off in ' + uroom.capitalize() + '.')
							elif (roomfind in funmode):
								if (roomfind in aimode):
									room.message('I am currently set to all functions with AI on in ' + uroom.capitalize() + '.')
								else:
									room.message('I am currently set to all functions with AI off in ' + uroom.capitalize() + '.')
							else:
								room.message('I do not have settings for ' + uroom.capitalize() + '.')
			elif (cmd.lower()) == "die":
				if (usrlvl == 3):
					sys.exit(0)
			elif (cmd.lower() == "teach"):
				if (user.name == 'ion'):
					argsadj = args.lower()
					if argsadj.find(" ") != -1: #if there's a colon somewhere
						uroomr, misc = argsadj.split(" ", 1)
						if (('#@#(*' + uroomr + '!@#$!') in pmnames):
							indexrs = pmnames.find('#@#(*' + uroomr + '!@#$!')
							indexre = pmnames.find('!@*^^(!' + uroomr + '*(^&&!')
							pmout1 = pmnames[(int(indexrs)):(int(indexre))]
							uuser = pmout1.replace(('#@#(*' + uroomr + '!@#$!'), "")
						else:
							uuser = uroomr
						endusr = ch._users.get(uuser)
						if endusr == None:
							room.message(uuser.capitalize() + ' is not in the chat.')
						else:
							room.message('I have banned ' + uuser.capitalize() + ' to teach them a lesson.')
							room.banUser(endusr)
			elif (cmd.lower() == "roomban"):
				if usrlvl >= 3:
					argsadj = args.lower()
					if (('#@#(*' + argsadj + '!@#$!') in pmnames):
						indexrs = pmnames.find('#@#(*' + argsadj + '!@#$!')
						indexre = pmnames.find('!@*^^(!' + argsadj + '*(^&&!')
						pmout1 = pmnames[(int(indexrs)):(int(indexre))]
						uuser = pmout1.replace(('#@#(*' + argsadj + '!@#$!'), "")
					else:
						uuser = argsadj
					endusr = ch._users.get(uuser)
					if endusr == None:
						room.message(uuser.capitalize() + ' is not in the chat.')
					else:
						uroom = self._rooms['teruchat']
						room.message('I have banned ' + uuser.capitalize() + ' to teach them a lesson.')
						uroom.banUser(endusr)
			elif ( (cmd.lower() == "d" ) or (cmd.lower() == "delete") ):
				mdlvl = room.getLevel(user)
				if ((usrlvl >=3) or (mdlvl >= 1)):
					argsadj = args.lower()
					if args == "":
						room.clearUser(user)
					else:
						if (('#@#(*' + argsadj + '!@#$!') in pmnames):
							indexrs = pmnames.find('#@#(*' + argsadj + '!@#$!')
							indexre = pmnames.find('!@*^^(!' + argsadj + '*(^&&!')
							pmout1 = pmnames[(int(indexrs)):(int(indexre))]
							uuser = pmout1.replace(('#@#(*' + argsadj + '!@#$!'), "")
						else:
							uuser = argsadj
						endusr = ch._users.get(uuser)
						if endusr == None:
							room.message(uuser.capitalize() + ' is not in the chat.')
						else:
							room.message(uuser.capitalize() + ' STFU please, k thx.')
							room.clearUser(endusr)
			elif ( (cmd.lower() == "kill" ) or (cmd.lower() == "ban") ):
				mdlvl = room.getLevel(user)
				if ((usrlvl >=3) or (mdlvl >= 1)):
					argsadj = args.lower()
					if args == "":
						room.message('Enter a valid user')
					else:
						if (('#@#(*' + argsadj + '!@#$!') in pmnames):
							indexrs = pmnames.find('#@#(*' + argsadj + '!@#$!')
							indexre = pmnames.find('!@*^^(!' + argsadj + '*(^&&!')
							pmout1 = pmnames[(int(indexrs)):(int(indexre))]
							uuser = pmout1.replace(('#@#(*' + argsadj + '!@#$!'), "")
						else:
							uuser = argsadj
						endusr = ch._users.get(uuser)
						if endusr == None:
							room.message(uuser.capitalize() + ' is not in the chat.')
						else:
							room.message('I have killed ' + uuser.capitalize() + '.')
							room.banUser(endusr)
			elif ( (cmd.lower() == "defib" ) or (cmd.lower() == "unban") ):
				mdlvl = room.getLevel(user)
				if ((usrlvl >=3) or (mdlvl >= 1)):
					argsadj = args.lower()
					if args == "":
						room.unban(user)
					else:
						if (('#@#(*' + argsadj + '!@#$!') in pmnames):
							indexrs = pmnames.find('#@#(*' + argsadj + '!@#$!')
							indexre = pmnames.find('!@*^^(!' + argsadj + '*(^&&!')
							pmout1 = pmnames[(int(indexrs)):(int(indexre))]
							uuser = pmout1.replace(('#@#(*' + argsadj + '!@#$!'), "")
						else:
							uuser = argsadj
						endusr = ch._users.get(uuser)
						if endusr == None:
							room.message(uuser.capitalize() + ' is not in the chat.')
						else:
							room.message("Clear...Bzzz... I've got a pulse, it looks like " + uuser.capitalize() + ' will be ok.')
							room.unban(endusr)
			elif ( (cmd.lower() == "n" ) or (cmd.lower() == "nuke") ):
				mdlvl = room.getLevel(user)
				if ((usrlvl >=3) or (mdlvl >= 1)):
					room.clearall()
					for n in (room.getUserlist(mode = None, unique = None, memory = None)):
						room.clearUser(n)
			elif ( (cmd.lower() == "addmod" ) or (cmd.lower() == "amod") ):
				mdlvl = room.getLevel(user)
				if ((usrlvl >=3) or (mdlvl >= 1)):
					argsadj = args.lower()
					if args == "":
						room.addMod(user)
					else:
						if (('#@#(*' + argsadj + '!@#$!') in pmnames):
							indexrs = pmnames.find('#@#(*' + argsadj + '!@#$!')
							indexre = pmnames.find('!@*^^(!' + argsadj + '*(^&&!')
							pmout1 = pmnames[(int(indexrs)):(int(indexre))]
							uuser = pmout1.replace(('#@#(*' + argsadj + '!@#$!'), "")
						else:
							uuser = argsadj
						endusr = ch._users.get(uuser)
						if endusr == None:
							room.message(uuser.capitalize() + ' is not in the chat.')
						else:
							room.message(uuser.capitalize() + ' is now ONE OF US! ONE OF US!')
							room.addMod(endusr)
			elif ( (cmd.lower() == "removemod" ) or (cmd.lower() == "rmod") ):
				mdlvl = room.getLevel(user)
				if ((usrlvl >=3) or (mdlvl >= 1)):
					argsadj = args.lower()
					if args != "":
						if (('#@#(*' + argsadj + '!@#$!') in pmnames):
							indexrs = pmnames.find('#@#(*' + argsadj + '!@#$!')
							indexre = pmnames.find('!@*^^(!' + argsadj + '*(^&&!')
							pmout1 = pmnames[(int(indexrs)):(int(indexre))]
							uuser = pmout1.replace(('#@#(*' + argsadj + '!@#$!'), "")
						else:
							uuser = argsadj
						endusr = ch._users.get(uuser)
						if endusr == None:
							room.message(uuser.capitalize() + ' is not in the chat.')
						else:
							room.message(uuser.capitalize() + ' is no longer a moderator.')
							room.removeMod(endusr)
			elif ( (cmd.lower() == "wl" ) or (cmd.lower() == "whitelist") ):
				lvl3rd = open("data/whitelist/lvl3.txt","r")
				lvl3rd2 = (lvl3rd.read()).lower()
				lvl2rd = open("data/whitelist/lvl2.txt","r")
				lvl2rd2 = (lvl2rd.read()).lower()
				lvl1rd = open("data/whitelist/lvl1.txt","r")
				lvl1rd2 = (lvl1rd.read()).lower()
				lvl0rd = open("data/whitelist/lvl0.txt","r")
				lvl0rd2 = (lvl0rd.read()).lower()
				argsadj = args.lower()
				argssec = '$#@!@#$(*(^$#@' + argsadj + '!^@*#($)@(@^*&#*@$*#$*#@'
				if args.find(":") != -1: #if there's a colon somewhere
					if (usrlvl >=3):
						uuser, ulvl = argsadj.split(": ", 1)
						writeinfo = '$#@!@#$(*(^$#@' + uuser + '!^@*#($)@(@^*&#*@$*#$*#@' + '$#&@*&$*^' + user.name +  '#$@*' + uuser + '$@#^&*@!' + '\n'
						useridset = '$#@!@#$(*(^$#@' + uuser + '!^@*#($)@(@^*&#*@$*#$*#@'
						usridseted = useridset + '$#&@*&$*^'
						usered = '#$@*' + uuser + '$@#^&*@!'
						allusrlistr = open("data/zombie/allusrlist.txt","r")
						allusrlist = (allusrlistr.read()).lower()
						allusrlistr.close()
						zombielistr = open("data/zombie/zombies.txt","r")
						zombielist = (zombielistr.read()).lower()
						zombielistr.close()
						if ulvl == '3':
							if (useridset in lvl3rd2):
								room.message(uuser.capitalize() + " is alrady a level 3")
							else:
								wrtdata = open("data/whitelist/lvl3.txt","a")
								room.message(uuser + " is now a level 3! -Set by " + (user.name).capitalize() + '.')
								wrtdata.write(writeinfo)
								wrtdata.close()
								if ((("@#$*!" + uuser.lower() + "@#$*!") not in allusrlist) and (("@#$*!" + uuser.lower() + "@#$*!") not in zombielist)):
									newusrlist = open("data/zombie/allusrlist.txt","a")
									newusrlist.write("\n@#$*!" + uuser.lower() + "@#$*!")
									newusrlist.close()
								if (useridset in lvl2rd2):
									wrtdata = open("data/whitelist/lvl2.txt","w")
									indexs = lvl2rd2.find(usridseted)
									indexe = lvl2rd2.find(usered)
									rawout = lvl2rd2[(int(indexs)):(int(indexe))]
									newdata = str(lvl2rd2).replace((rawout + usered), "")
									wrtdata.write(newdata)
									wrtdata.close()
									lvl3rd.close()
									lvl2rd.close()
									lvl1rd.close()
									lvl0rd.close()
								elif (useridset in lvl1rd2):
									wrtdata = open("data/whitelist/lvl1.txt","w")
									indexs = lvl1rd2.find(usridseted)
									indexe = lvl1rd2.find(usered)
									rawout = lvl1rd2[(int(indexs)):(int(indexe))]
									newdata = str(lvl1rd2).replace((rawout + usered), "")
									wrtdata.write(newdata)
									wrtdata.close()
									lvl3rd.close()
									lvl2rd.close()
									lvl1rd.close()
									lvl0rd.close()
								elif (useridset in lvl0rd2):
									wrtdata = open("data/whitelist/lvl0.txt","w")
									indexs = lvl0rd2.find(usridseted)
									indexe = lvl0rd2.find(usered)
									rawout = lvl0rd2[(int(indexs)):(int(indexe))]
									newdata = str(lvl0rd2).replace((rawout + usered), "")
									wrtdata.write(newdata)
									wrtdata.close()
									lvl3rd.close()
									lvl2rd.close()
									lvl1rd.close()
									lvl0rd.close()
						elif ulvl == '2':
							if (useridset in lvl2rd2):
								room.message(uuser.capitalize() + " is alrady a level 2")
							else:
								wrtdata = open("data/whitelist/lvl2.txt","a")
								room.message(uuser + " is now a level 2! -Set by " + (user.name).capitalize() + '.')
								wrtdata.write(writeinfo)
								wrtdata.close()
								if ((("@#$*!" + uuser.lower() + "@#$*!") not in allusrlist) and (("@#$*!" + uuser.lower() + "@#$*!") not in zombielist)):
									newusrlist = open("data/zombie/allusrlist.txt","a")
									newusrlist.write("\n@#$*!" + uuser.lower() + "@#$*!")
									newusrlist.close()
								if (useridset in lvl3rd2):
									wrtdata = open("data/whitelist/lvl3.txt","w")
									indexs = lvl3rd2.find(usridseted)
									indexe = lvl3rd2.find(usered)
									rawout = lvl3rd2[(int(indexs)):(int(indexe))]
									newdata = str(lvl3rd2).replace((rawout + usered), "")
									wrtdata.write(newdata)
									wrtdata.close()
									lvl3rd.close()
									lvl2rd.close()
									lvl1rd.close()
									lvl0rd.close()
								elif (useridset in lvl1rd2):
									wrtdata = open("data/whitelist/lvl1.txt","w")
									indexs = lvl1rd2.find(usridseted)
									indexe = lvl1rd2.find(usered)
									rawout = lvl1rd2[(int(indexs)):(int(indexe))]
									newdata = str(lvl1rd2).replace((rawout + usered), "")
									wrtdata.write(newdata)
									wrtdata.close()
									lvl3rd.close()
									lvl2rd.close()
									lvl1rd.close()
									lvl0rd.close()
								elif (useridset in lvl0rd2):
									wrtdata = open("data/whitelist/lvl0.txt","w")
									indexs = lvl0rd2.find(usridseted)
									indexe = lvl0rd2.find(usered)
									rawout = lvl0rd2[(int(indexs)):(int(indexe))]
									newdata = str(lvl0rd2).replace((rawout + usered), "")
									wrtdata.write(newdata)
									wrtdata.close()
									lvl3rd.close()
									lvl2rd.close()
									lvl1rd.close()
									lvl0rd.close()
						elif ulvl == '1':
							if (useridset in lvl1rd2):
								room.message(uuser.capitalize() + " is alrady a level 1")
							else:
								wrtdata = open("data/whitelist/lvl1.txt","a")
								room.message(uuser + " is now a level 1! -Set by " + (user.name).capitalize() + '.')
								wrtdata.write(writeinfo)
								wrtdata.close()
								if ((("@#$*!" + uuser.lower() + "@#$*!") not in allusrlist) and (("@#$*!" + uuser.lower() + "@#$*!") not in zombielist)):
									newusrlist = open("data/zombie/allusrlist.txt","a")
									newusrlist.write("\n@#$*!" + uuser.lower() + "@#$*!")
									newusrlist.close()
								if (useridset in lvl3rd2):
									wrtdata = open("data/whitelist/lvl3.txt","w")
									indexs = lvl3rd2.find(usridseted)
									indexe = lvl3rd2.find(usered)
									rawout = lvl3rd2[(int(indexs)):(int(indexe))]
									newdata = str(lvl3rd2).replace((rawout + usered), "")
									wrtdata.write(newdata)
									wrtdata.close()
									lvl3rd.close()
									lvl2rd.close()
									lvl1rd.close()
									lvl0rd.close()
								elif (useridset in lvl2rd2):
									wrtdata = open("data/whitelist/lvl2.txt","w")
									indexs = lvl2rd2.find(usridseted)
									indexe = lvl2rd2.find(usered)
									rawout = lvl2rd2[(int(indexs)):(int(indexe))]
									newdata = str(lvl2rd2).replace((rawout + usered), "")
									wrtdata.write(newdata)
									wrtdata.close()
									lvl3rd.close()
									lvl2rd.close()
									lvl1rd.close()
									lvl0rd.close()
								elif (useridset in lvl0rd2):
									wrtdata = open("data/whitelist/lvl0.txt","w")
									indexs = lvl0rd2.find(usridseted)
									indexe = lvl0rd2.find(usered)
									rawout = lvl0rd2[(int(indexs)):(int(indexe))]
									newdata = str(lvl0rd2).replace((rawout + usered), "")
									wrtdata.write(newdata)
									wrtdata.close()
									lvl3rd.close()
									lvl2rd.close()
									lvl1rd.close()
									lvl0rd.close()
						elif ulvl == '0':
							if ((useridset in lvl0rd2) or ((useridset not in lvl1rd2) and (useridset not in lvl2rd2) and (useridset not in lvl3rd2))):
								room.message(uuser.capitalize() + " is alrady a level 0")
							else:
								wrtdata = open("data/whitelist/lvl0.txt","a")
								room.message(uuser + " is now a level 0! -Set by " + (user.name).capitalize() + '.')
								wrtdata.write(writeinfo)
								wrtdata.close()
								if (("@#$*!" + uuser.lower() + "@#$*!") in allusrlist):
									newusrs = allusrlist.replace("@#$*!" + uuser.lower() + "@#$*!", "")
									newusrlist = open("data/zombie/allusrlist.txt","w")
									newusrlist.write(newusrs)
									newusrlist.close()
								elif (("@#$*!" + uuser.lower() + "@#$*!") in zombielist):
									newzombies = zombielist.replace("@#$*!" + uuser.lower() + "@#$*!", "")
									newzombielist = open("data/zombie/zombies.txt","w")
									newzombielist.write(newzombies)
									newzombielist.close()
								if (useridset in lvl3rd2):
									wrtdata = open("data/whitelist/lvl3.txt","w")
									indexs = lvl3rd2.find(usridseted)
									indexe = lvl3rd2.find(usered)
									rawout = lvl3rd2[(int(indexs)):(int(indexe))]
									newdata = str(lvl3rd2).replace((rawout + usered), "")
									wrtdata.write(newdata)
									wrtdata.close()
									lvl3rd.close()
									lvl2rd.close()
									lvl1rd.close()
									lvl0rd.close()
								elif (useridset in lvl2rd2):
									wrtdata = open("data/whitelist/lvl2.txt","w")
									indexs = lvl2rd2.find(usridseted)
									indexe = lvl2rd2.find(usered)
									rawout = lvl2rd2[(int(indexs)):(int(indexe))]
									newdata = str(lvl2rd2).replace((rawout + usered), "")
									wrtdata.write(newdata)
									wrtdata.close()
									lvl3rd.close()
									lvl2rd.close()
									lvl1rd.close()
									lvl0rd.close()
								elif (useridset in lvl1rd2):
									wrtdata = open("data/whitelist/lvl1.txt","w")
									indexs = lvl1rd2.find(usridseted)
									indexe = lvl1rd2.find(usered)
									rawout = lvl1rd2[(int(indexs)):(int(indexe))]
									newdata = str(lvl1rd2).replace((rawout + usered), "")
									wrtdata.write(newdata)
									wrtdata.close()
									lvl3rd.close()
									lvl2rd.close()
									lvl1rd.close()
									lvl0rd.close()
					else:
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
			elif (cmd.lower()) == "modlist":
				mdlvl = room.getLevel(user)
				if (usrlvl >= 2 or mdlvl >= 1):
					room.message(", ".join(room.modnames + [room.ownername]))
			elif (cmd.lower()) == "o.o":
				mdlvl = room.getLevel(user)
				if (usrlvl >= 2 or mdlvl >= 1):
					print(", ".join(room.modnames + [room.ownername]))
			elif ( (cmd.lower() == "bl" ) or (cmd.lower() == "banlist") ):
				mdlvl = room.getLevel(user)
				if ((usrlvl >= 2) or (mdlvl >= 1)):
					banlistr1 = str(room.banlist).replace("[", "")
					banlistr2 = banlistr1.replace("[", "")
					banlistr3 = banlistr2.replace("]", "")
					banlistr4 = banlistr3.replace("[", "")
					banlistr5 = banlistr4.replace("<User: ", "")
					banlistr6 = banlistr5.replace(">", "")
					banlist = banlistr6 + ' is/are currently banned.'
					room.message(banlist)
			elif (cmd.lower()) == "contacts":
				if usrlvl >= 3:
					room.message(str((self._pm)._contacts))
			elif ( (cmd.lower() == "acontact" ) or (cmd.lower() == "addcontact") ):
				if usrlvl >= 3:
					argsadj = args.lower()
					if (('#@#(*' + argsadj + '!@#$!') in pmnames):
						indexrs = pmnames.find('#@#(*' + argsadj + '!@#$!')
						indexre = pmnames.find('!@*^^(!' + argsadj + '*(^&&!')
						pmout1 = pmnames[(int(indexrs)):(int(indexre))]
						uuser = pmout1.replace(('#@#(*' + argsadj + '!@#$!'), "")
					else:
						uuser = argsadj
					iusr = ch._users.get(uuser)
					if iusr == None:
						room.message(uuser.capitalize() + ' is not in the chat.')
					else:
						room.message('I have added ' + uuser.capitalize() + ' to my contacts.')
						(self._pm).addContact(iusr)
			elif ( (cmd.lower() == "rcontact" ) or (cmd.lower() == "removecontact") ):
				if usrlvl >= 3:
					argsadj = args.lower()
					if (('#@#(*' + argsadj + '!@#$!') in pmnames):
						indexrs = pmnames.find('#@#(*' + argsadj + '!@#$!')
						indexre = pmnames.find('!@*^^(!' + argsadj + '*(^&&!')
						pmout1 = pmnames[(int(indexrs)):(int(indexre))]
						uuser = pmout1.replace(('#@#(*' + argsadj + '!@#$!'), "")
					else:
						uuser = argsadj
					iusr = ch._users.get(uuser)
					if iusr == None:
						room.message(uuser.capitalize() + ' is not in the chat.')
					else:
						room.message('I have removed ' + uuser.capitalize() + ' from my contacts.')
						(self._pm).removeContact(iusr)
			elif ( (cmd.lower() == "pm" ) or (cmd.lower() == "privatemessage") ):
				if usrlvl >= 3:
					if args.find(" ") != -1: #if there's a colon somewhere
						wrtdata = open("data/pm/PMOUT.txt","a")
						argsadj = args.lower()
						uuserr, umsg = argsadj.split(" ", 1)
						if (('#@#(*' + uuserr + '!@#$!') in pmnames):
							indexrs = pmnames.find('#@#(*' + uuserr + '!@#$!')
							indexre = pmnames.find('!@*^^(!' + uuserr + '*(^&&!')
							pmout1 = pmnames[(int(indexrs)):(int(indexre))]
							uuser = pmout1.replace(('#@#(*' + uuserr + '!@#$!'), "")
						else:
							uuser = uuserr
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
								wrtdata.write(str((user.name + " To " + uuser.capitalize() + ': ' + str(gumsg) + '\n\n').encode('utf-8')))
								wrtdata.close()
						else:
							room.message("That user is not in my contacts.")
					else:
						room.message("Check your format, the : is missing.")
				else:
					room.message("I cannot do that for the likes of you.")
			elif (cmd.lower()) == "rooms":
				if user.name == "ion":
					roomso = str(self.getRoomNames())
					roomsa1 = roomso.replace("'","")
					roomsa2 = roomsa1.replace("{","")
					rooms = roomsa2.replace("}","")
					room.message('I am currently in the following rooms: ' + str(rooms) + ".")
				else:
					room.message("Only my lovely Mistress Ion can see this!")
			elif ( (cmd.lower() == "db" ) or (cmd.lower() == "devboard") or (cmd.lower() == "dev") or (cmd.lower() == "dm") or (cmd.lower() == "devmessage")):
				if usrlvl >=3:
					subtime = strftime("%a, %b %d @ %H:%M", gmtime())
					devboardr = open("data/boards/devboard.txt","r")
					devboard = (devboardr.read())
					devboardr.close()
					postnum = devboard.count('!@!*&&&!')
					if args == "":
						i = 0
						devboardo = devboard.replace('!@!*&&&!', ") ")
						while i <= postnum:
							devboardo = devboardo.replace('*@(!(!*!@!' + str(i), "")
							i = i + 1
						room.message(devboardo, html = True)
					elif args.startswith("remove "):
						cmd, delnum = args.split("remove ", 1)
						finfo1 = delnum + '!@!*&&&!'
						finfo2 = '*@(!(!*!@!' + delnum
						if finfo1 in devboard:
							indexs = devboard.find(finfo1)
							indexe = devboard.find(finfo2)
							rawout = devboard[(int(indexs)):(int(indexe))]
							newpost = devboard.replace(rawout + finfo2 + '.<br/>', "")
							i = int(delnum)
							while i <= 5:
								newpost = newpost.replace('*@(!(!*!@!' + str(i), '*@(!(!*!@!' + str(i-1))\
									.replace(str(i) + '!@!*&&&!', str(i-1) + '!@!*&&&!')
								i = i + 1
							wrtdata = open("data/boards/devboard.txt","w")
							wrtdata.write(newpost)
							wrtdata.close()
							room.message('"' + rawout.replace(finfo1, "") + '" has been removed from the dev board.', html = True)
						else:
								room.message("The board does not have that many posts.")
					elif args.startswith("Remove "):
						cmd, delnum = args.split("Remove ", 1)
						finfo1 = delnum + '!@!*&&&!'
						finfo2 = '*@(!(!*!@!' + delnum
						if finfo1 in devboard:
							indexs = devboard.find(finfo1)
							indexe = devboard.find(finfo2)
							rawout = devboard[(int(indexs)):(int(indexe))]
							newpost = devboard.replace(rawout + finfo2 + '.<br/>', "")
							i = int(delnum)
							while i <= 5:
								newpost = newpost.replace('*@(!(!*!@!' + str(i), '*@(!(!*!@!' + str(i-1))\
									.replace(str(i) + '!@!*&&&!', str(i-1) + '!@!*&&&!')
								i = i + 1
							wrtdata = open("data/boards/devboard.txt","w")
							wrtdata.write(newpost)
							wrtdata.close()
							room.message('"' + rawout.replace(finfo1, "") + '" has been removed from the dev board.', html = True)
						else:
								room.message("The board does not have that many posts.")
					elif args.startswith("del "):
						cmd, delnum = args.split("del ", 1)
						finfo1 = delnum + '!@!*&&&!'
						finfo2 = '*@(!(!*!@!' + delnum
						if finfo1 in devboard:
							indexs = devboard.find(finfo1)
							indexe = devboard.find(finfo2)
							rawout = devboard[(int(indexs)):(int(indexe))]
							newpost = devboard.replace(rawout + finfo2 + '.<br/>', "")
							i = int(delnum)
							while i <= 5:
								newpost = newpost.replace('*@(!(!*!@!' + str(i), '*@(!(!*!@!' + str(i-1))\
									.replace(str(i) + '!@!*&&&!', str(i-1) + '!@!*&&&!')
								i = i + 1
							wrtdata = open("data/boards/devboard.txt","w")
							wrtdata.write(newpost)
							wrtdata.close()
							room.message('"' + rawout.replace(finfo1, "") + '" has been removed from the dev board.', html = True)
						else:
								room.message("The board does not have that many posts.")
					elif args.startswith("delete "):
						cmd, delnum = args.split("delete ", 1)
						finfo1 = delnum + '!@!*&&&!'
						finfo2 = '*@(!(!*!@!' + delnum
						if finfo1 in devboard:
							indexs = devboard.find(finfo1)
							indexe = devboard.find(finfo2)
							rawout = devboard[(int(indexs)):(int(indexe))]
							newpost = devboard.replace(rawout + finfo2 + '.<br/>', "")
							i = int(delnum)
							while i <= 5:
								newpost = newpost.replace('*@(!(!*!@!' + str(i), '*@(!(!*!@!' + str(i-1))\
									.replace(str(i) + '!@!*&&&!', str(i-1) + '!@!*&&&!')
								i = i + 1
							wrtdata = open("data/boards/devboard.txt","w")
							wrtdata.write(newpost)
							wrtdata.close()
							room.message('"' + rawout.replace(finfo1, "") + '" has been removed from the dev board.', html = True)
						else:
								room.message("The board does not have that many posts.")
					elif args.startswith("Delete "):
						cmd, delnum = args.split("Delete ", 1)
						finfo1 = delnum + '!@!*&&&!'
						finfo2 = '*@(!(!*!@!' + delnum
						if finfo1 in devboard:
							indexs = devboard.find(finfo1)
							indexe = devboard.find(finfo2)
							rawout = devboard[(int(indexs)):(int(indexe))]
							newpost = devboard.replace(rawout + finfo2 + '.<br/>', "")
							i = int(delnum)
							while i <= 5:
								newpost = newpost.replace('*@(!(!*!@!' + str(i), '*@(!(!*!@!' + str(i-1))\
									.replace(str(i) + '!@!*&&&!', str(i-1) + '!@!*&&&!')
								i = i + 1
							wrtdata = open("data/boards/devboard.txt","w")
							wrtdata.write(newpost)
							wrtdata.close()
							room.message('"' + rawout.replace(finfo1, "") + '" has been removed from the dev board.', html = True)
						else:
								room.message("The board does not have that many posts.")
					elif args.startswith("Del "):
						cmd, delnum = args.split("Del ", 1)
						finfo1 = delnum + '!@!*&&&!'
						finfo2 = '*@(!(!*!@!' + delnum
						if finfo1 in devboard:
							indexs = devboard.find(finfo1)
							indexe = devboard.find(finfo2)
							rawout = devboard[(int(indexs)):(int(indexe))]
							newpost = devboard.replace(rawout + finfo2 + '.<br/>', "")
							i = int(delnum)
							while i <= 5:
								newpost = newpost.replace('*@(!(!*!@!' + str(i), '*@(!(!*!@!' + str(i-1))\
									.replace(str(i) + '!@!*&&&!', str(i-1) + '!@!*&&&!')
								i = i + 1
							wrtdata = open("data/boards/devboard.txt","w")
							wrtdata.write(newpost)
							wrtdata.close()
							room.message('"' + rawout.replace(finfo1, "") + '" has been removed from the dev board.', html = True)
						else:
								room.message("The board does not have that many posts.")
					else:
						if postnum == 5:
							finfo1 = '1!@!*&&&!'
							finfo2 = '*@(!(!*!@!1'
							indexs = devboard.find(finfo1)
							indexe = devboard.find(finfo2)
							rawout = devboard[(int(indexs)):(int(indexe))]
							minus1 = devboard.replace(rawout + finfo2 + '.<br/>', "")
							switch2 = minus1.replace('2!@!*&&&!', '1!@!*&&&!')\
								.replace('*@(!(!*!@!2', '*@(!(!*!@!1')
							switch3 = switch2.replace('3!@!*&&&!', '2!@!*&&&!')\
								.replace('*@(!(!*!@!3', '*@(!(!*!@!2')
							switch4 = switch3.replace('4!@!*&&&!', '3!@!*&&&!')\
								.replace('*@(!(!*!@!4', '*@(!(!*!@!3')
							newpost = switch4.replace('5!@!*&&&!', '4!@!*&&&!')\
								.replace('*@(!(!*!@!5', '*@(!(!*!@!4')
							wrtdata = open("data/boards/devboard.txt","w")
							wrtdata.write(newpost)
							wrtdata.close()
							newpost = str(postnum)+ '!@!*&&&!' + args + ' - posted by <b>' + user.name.capitalize() + '</b> on <i>' + subtime + '</i>*@(!(!*!@!' + str(postnum) + '.<br/>'
							wrtdata = open("data/boards/devboard.txt","a")
							wrtdata.write(newpost)
							wrtdata.close()
							room.message('"' + args + '" has been posted to the dev board.')
						else:
							postnum = postnum + 1
							newpost = str(postnum)+ '!@!*&&&!' + args + ' - posted by <b>' + user.name.capitalize() + '</b> on <i>' + subtime + '</i>*@(!(!*!@!' + str(postnum) + '.<br/>'
							wrtdata = open("data/boards/devboard.txt","a")
							wrtdata.write(newpost)
							wrtdata.close()
							room.message('"' + args + '" has been posted to the dev board.')
			elif ( (cmd.lower() == "rm" ) or (cmd.lower() == "roommessage") ):
				if usrlvl >= 3:
					if args.find(": ") != -1: #if there's a colon somewhere
						argsadj = args.lower()
						uroomr, umsg = argsadj.split(": ", 1)
						if (('#@#(*' + uroomr + '!@#$!') in roomnames):
							indexrs = roomnames.find('#@#(*' + uroomr + '!@#$!')
							indexre = roomnames.find('!@*^^(!' + uroomr + '*(^&&!')
							roomout1 = roomnames[(int(indexrs)):(int(indexre))]
							uroomr = roomout1.replace(('#@#(*' + uroomr + '!@#$!'), "")
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
			elif ( (cmd.lower() == "gtfo" ) or (cmd.lower() == "leave") ):
				mdlvl = room.getLevel(user)
				if (usrlvl >= 2 or mdlvl >= 1):
					if (args == ''):
						room.message("Okay, if it will make you happy. ;(+20")
						self.leaveRoom(str(room.name))
					else:
						uroomr = args.lower()
						if (('#@#(*' + uroomr + '!@#$!') in roomnames):
							indexrs = roomnames.find('#@#(*' + uroomr + '!@#$!')
							indexre = roomnames.find('!@*^^(!' + uroomr + '*(^&&!')
							roomout1 = roomnames[(int(indexrs)):(int(indexre))]
							uroomr = roomout1.replace(('#@#(*' + uroomr + '!@#$!'), "")
						if (uroomr in str(self._rooms)):
							room.message("Okay, if it will make you happy. ;(+20")
							self.leaveRoom(uroomr)
						else:
							room.message("I am not in " + uroomr.capitalize() + ", thus I can't leave it.")
				else:
					room.message("No, you!")
			elif (cmd.lower()) == "join":
				if usrlvl >= 2:
					if args == '':
						room.message('Please enter a valid room.')
					else:
						uroomr = args.lower()
						if (('#@#(*' + uroomr + '!@#$!') in roomnames):
							indexrs = roomnames.find('#@#(*' + uroomr + '!@#$!')
							indexre = roomnames.find('!@*^^(!' + uroomr + '*(^&&!')
							roomout1 = roomnames[(int(indexrs)):(int(indexre))]
							uroomr = roomout1.replace(('#@#(*' + uroomr + '!@#$!'), "")
						if (uroomr in str(self._rooms)):
							room.message("I am already in " + uroomr.capitalize() + '.')
						else:	
							self.joinRoom(uroomr)
							room.message('I have joined ' + uroomr.capitalize() + '.')
			elif ( (cmd.lower() == "rc" ) or (cmd.lower() == "reconnect") ):
				if usrlvl >= 2:
					if args == '':
						self.leaveRoom(room.name)
						time.sleep(2)
						self.joinRoom(room.name)
					else:
						uroomr = args.lower()
						if ( (uroomr == 'buzz') or (uroomr == 'ab') or (uroomr == 'buzzez') or (uroomr == 'animebuzz') ):
							uroomr = 'animebuzzez'
						elif ( (uroomr == 'home') or (uroomr == 'teruchat') or (uroomr == 'teru') or (uroomr == 'tc') ):
							uroomr = 'teruchat'
						elif ( (uroomr == 'as') or (uroomr == 'seed')):
							uroomr = 'animeseed'
						elif ( (uroomr == 'pu') or (uroomr == 'uri') or (uroomr == 'project')):
							uroomr = 'projecturi'
						elif ( (uroomr == 'am') or (uroomr == 'animemaniacs') or (uroomr == 'maniacs') or (uroomr == 'animaniacs')):
							uroomr = 'amaniacs'
						elif ( (uroomr == 'kuro') or (uroomr == 'kn') or (uroomr == 'network')):
							uroomr = 'kuronetwork'
						elif ( (uroomr == 'love') or (uroomr == 'lma') or (uroomr == 'lovemyanime') or (uroomr == 'lovemy')):
							uroomr = 'lovemyanimechat'
						elif ( (uroomr == 'animeon') or (uroomr == 'watchanimeon')):
							uroomr = 'watchanimeonn'
						elif uroomr == 'animenow':
							uroomr = 'watchanimenow'
						elif ( (uroomr == 'aftv') or (uroomr == 'af') or (uroomr == 'animefreak')):
							uroomr = 'tvanimefreak'
						if (uroomr in str(self._rooms)):
							self.leaveRoom(uroomr)
							time.sleep(2)
							self.joinRoom(uroomr)
						else:
							room.message('I am not in ' + uroomr + '.')
			elif ( (cmd.lower() == "help" ) or (cmd.lower() == "cmds") or (cmd.lower() == "cmd") or (cmd.lower() == "commands") ):
				room.message('<a href="http://t6ru.chatango.com/" target="_blank">For help and the list of commands click here.</a>', html = True)
			elif (cmd.lower()) == "uptime":
					room.message("I connected at " + (str(now).replace("['", "")).replace("']", ""))
			elif ( (cmd.lower() == "report" ) or (cmd.lower() == "r") or (cmd.lower() == "reports") or (cmd.lower() == "feedback")  or (cmd.lower() == "fb")):
				if usrlvl >=1:
					subtime = strftime("%a, %b %d @ %H:%M", gmtime())
					reportboardr = open("data/boards/reportboard.txt","r")
					reportboard = (reportboardr.read())
					reportboardr.close()
					postnum = reportboard.count('!@!*&&&!')
					if (args == "" and usrlvl >=2):
						i = 0
						reportboardo = reportboard.replace('!@!*&&&!', ") ")
						while i <= postnum:
							reportboardo = reportboardo.replace('*@(!(!*!@!' + str(i), "")
							i = i + 1
						room.message(reportboardo, html = True)
					elif (args.startswith("remove ") and usrlvl >=2):
						cmd, delnum = args.split("remove ", 1)
						finfo1 = delnum + '!@!*&&&!'
						finfo2 = '*@(!(!*!@!' + delnum
						if finfo1 in reportboard:
							indexs = reportboard.find(finfo1)
							indexe = reportboard.find(finfo2)
							rawout = reportboard[(int(indexs)):(int(indexe))]
							newpost = reportboard.replace(rawout + finfo2 + '.<br/>', "")
							i = int(delnum)
							while i <= 5:
								newpost = newpost.replace('*@(!(!*!@!' + str(i), '*@(!(!*!@!' + str(i-1))\
									.replace(str(i) + '!@!*&&&!', str(i-1) + '!@!*&&&!')
								i = i + 1
							wrtdata = open("data/boards/reportboard.txt","w")
							wrtdata.write(newpost)
							wrtdata.close()
							room.message('"' + rawout.replace(finfo1, "") + '" has been removed from the report board.', html = True)
					elif (args.startswith("Remove ") and usrlvl >=2):
						cmd, delnum = args.split("Remove ", 1)
						finfo1 = delnum + '!@!*&&&!'
						finfo2 = '*@(!(!*!@!' + delnum
						if finfo1 in reportboard:
							indexs = reportboard.find(finfo1)
							indexe = reportboard.find(finfo2)
							rawout = reportboard[(int(indexs)):(int(indexe))]
							newpost = reportboard.replace(rawout + finfo2 + '.<br/>', "")
							i = int(delnum)
							while i <= 5:
								newpost = newpost.replace('*@(!(!*!@!' + str(i), '*@(!(!*!@!' + str(i-1))\
									.replace(str(i) + '!@!*&&&!', str(i-1) + '!@!*&&&!')
								i = i + 1
							wrtdata = open("data/boards/reportboard.txt","w")
							wrtdata.write(newpost)
							wrtdata.close()
							room.message('"' + rawout.replace(finfo1, "") + '" has been removed from the report board.', html = True)
						else:
								room.message("The board does not have that many posts.")
					elif (args.startswith("del ") and usrlvl >=2):
						cmd, delnum = args.split("del ", 1)
						finfo1 = delnum + '!@!*&&&!'
						finfo2 = '*@(!(!*!@!' + delnum
						if finfo1 in reportboard:
							indexs = reportboard.find(finfo1)
							indexe = reportboard.find(finfo2)
							rawout = reportboard[(int(indexs)):(int(indexe))]
							newpost = reportboard.replace(rawout + finfo2 + '.<br/>', "")
							i = int(delnum)
							while i <= 5:
								newpost = newpost.replace('*@(!(!*!@!' + str(i), '*@(!(!*!@!' + str(i-1))\
									.replace(str(i) + '!@!*&&&!', str(i-1) + '!@!*&&&!')
								i = i + 1
							wrtdata = open("data/boards/reportboard.txt","w")
							wrtdata.write(newpost)
							wrtdata.close()
							room.message('"' + rawout.replace(finfo1, "") + '" has been removed from the report board.', html = True)
						else:
								room.message("The board does not have that many posts.")
					elif (args.startswith("delete ") and usrlvl >=2):
						cmd, delnum = args.split("delete ", 1)
						finfo1 = delnum + '!@!*&&&!'
						finfo2 = '*@(!(!*!@!' + delnum
						if finfo1 in reportboard:
							indexs = reportboard.find(finfo1)
							indexe = reportboard.find(finfo2)
							rawout = reportboard[(int(indexs)):(int(indexe))]
							newpost = reportboard.replace(rawout + finfo2 + '.<br/>', "")
							i = int(delnum)
							while i <= 5:
								newpost = newpost.replace('*@(!(!*!@!' + str(i), '*@(!(!*!@!' + str(i-1))\
									.replace(str(i) + '!@!*&&&!', str(i-1) + '!@!*&&&!')
								i = i + 1
							wrtdata = open("data/boards/reportboard.txt","w")
							wrtdata.write(newpost)
							wrtdata.close()
							room.message('"' + rawout.replace(finfo1, "") + '" has been removed from the report board.', html = True)
						else:
								room.message("The board does not have that many posts.")
					elif (args.startswith("Delete ") and usrlvl >=2):
						cmd, delnum = args.split("Delete ", 1)
						finfo1 = delnum + '!@!*&&&!'
						finfo2 = '*@(!(!*!@!' + delnum
						if finfo1 in reportboard:
							indexs = reportboard.find(finfo1)
							indexe = reportboard.find(finfo2)
							rawout = reportboard[(int(indexs)):(int(indexe))]
							newpost = reportboard.replace(rawout + finfo2 + '.<br/>', "")
							i = int(delnum)
							while i <= 5:
								newpost = newpost.replace('*@(!(!*!@!' + str(i), '*@(!(!*!@!' + str(i-1))\
									.replace(str(i) + '!@!*&&&!', str(i-1) + '!@!*&&&!')
								i = i + 1
							wrtdata = open("data/boards/reportboard.txt","w")
							wrtdata.write(newpost)
							wrtdata.close()
							room.message('"' + rawout.replace(finfo1, "") + '" has been removed from the report board.', html = True)
						else:
								room.message("The board does not have that many posts.")
					elif (args.startswith("Del ") and usrlvl >=2):
						cmd, delnum = args.split("remove ", 1)
						finfo1 = delnum + '!@!*&&&!'
						finfo2 = '*@(!(!*!@!' + delnum
						if finfo1 in reportboard:
							indexs = reportboard.find(finfo1)
							indexe = reportboard.find(finfo2)
							rawout = reportboard[(int(indexs)):(int(indexe))]
							newpost = reportboard.replace(rawout + finfo2 + '.<br/>', "")
							i = int(delnum)
							while i <= 5:
								newpost = newpost.replace('*@(!(!*!@!' + str(i), '*@(!(!*!@!' + str(i-1))\
									.replace(str(i) + '!@!*&&&!', str(i-1) + '!@!*&&&!')
								i = i + 1
							wrtdata = open("data/boards/reportboard.txt","w")
							wrtdata.write(newpost)
							wrtdata.close()
							room.message('"' + rawout.replace(finfo1, "") + '" has been removed from the report board.', html = True)
						else:
								room.message("The board does not have that many posts.")
					else:
						countres = reportboard.count('<b>' + user.name.capitalize() + '</b>')
						
						if countres >= 3:
							room.message('You have reported too much recently, please wait until the dev team can clear up your previous reports.')
						else:
							postnum = postnum + 1
							newpost = str(postnum) + '!@!*&&&!' + args + ' - posted by <b>' + user.name.capitalize() + '</b> on <i>' + subtime + '</i>*@(!(!*!@!' + str(postnum) + '.<br/>'
							wrtdata = open("data/boards/reportboard.txt","a")
							wrtdata.write(newpost)
							wrtdata.close()
							room.message('You have reported "' + args + '".')
			elif ((("#@@$!!(!*@" + room.name + "@@#$&*(**!") in funmode) or (("#@@$!!(!*@" + room.name + "@@#$&*(**!") in usefulmode)):
				if ( (cmd.lower() == "b" ) or (cmd.lower() == "board")):
					if usrlvl >=1:
						subtime = strftime("%a, %b %d @ %H:%M", gmtime())
						userboardr = open("data/boards/userboard.txt","r")
						userboard = (userboardr.read())
						userboardr.close()
						postnum = userboard.count('!@!*&&&!')
						if args == "":
							i = 0
							userboardo = userboard.replace('!@!*&&&!', ") ")
							while i <= postnum:
								userboardo = userboardo.replace('*@(!(!*!@!' + str(i), "")
								i = i + 1
							room.message(userboardo, html = True)
						elif (args.startswith("remove ") and usrlvl >=2):
							cmd, delnum = args.split("remove ", 1)
							finfo1 = delnum + '!@!*&&&!'
							finfo2 = '*@(!(!*!@!' + delnum
							if finfo1 in userboard:
								indexs = userboard.find(finfo1)
								indexe = userboard.find(finfo2)
								rawout = userboard[(int(indexs)):(int(indexe))]
								newpost = userboard.replace(rawout + finfo2 + '.<br/>', "")
								i = int(delnum)
								while i <= 5:
									newpost = newpost.replace('*@(!(!*!@!' + str(i), '*@(!(!*!@!' + str(i-1))\
										.replace(str(i) + '!@!*&&&!', str(i-1) + '!@!*&&&!')
									i = i + 1
								wrtdata = open("data/boards/userboard.txt","w")
								wrtdata.write(newpost)
								wrtdata.close()
								room.message('"' + rawout.replace(finfo1, "") + '" has been removed from the user board.', html = True)
							else:
								room.message("The board does not have that many posts.")
						elif (args.startswith("Remove ") and usrlvl >=2):
							cmd, delnum = args.split("Remove ", 1)
							finfo1 = delnum + '!@!*&&&!'
							finfo2 = '*@(!(!*!@!' + delnum
							if finfo1 in userboard:
								indexs = userboard.find(finfo1)
								indexe = userboard.find(finfo2)
								rawout = userboard[(int(indexs)):(int(indexe))]
								newpost = userboard.replace(rawout + finfo2 + '.<br/>', "")
								i = int(delnum)
								while i <= 5:
									newpost = newpost.replace('*@(!(!*!@!' + str(i), '*@(!(!*!@!' + str(i-1))\
										.replace(str(i) + '!@!*&&&!', str(i-1) + '!@!*&&&!')
									i = i + 1
								wrtdata = open("data/boards/userboard.txt","w")
								wrtdata.write(newpost)
								wrtdata.close()
								room.message('"' + rawout.replace(finfo1, "") + '" has been removed from the user board.', html = True)
							else:
								room.message("The board does not have that many posts.")
						elif (args.startswith("del ") and usrlvl >=2):
							cmd, delnum = args.split("del ", 1)
							finfo1 = delnum + '!@!*&&&!'
							finfo2 = '*@(!(!*!@!' + delnum
							if finfo1 in userboard:
								indexs = userboard.find(finfo1)
								indexe = userboard.find(finfo2)
								rawout = userboard[(int(indexs)):(int(indexe))]
								newpost = userboard.replace(rawout + finfo2 + '.<br/>', "")
								i = int(delnum)
								while i <= 5:
									newpost = newpost.replace('*@(!(!*!@!' + str(i), '*@(!(!*!@!' + str(i-1))\
										.replace(str(i) + '!@!*&&&!', str(i-1) + '!@!*&&&!')
									i = i + 1
								wrtdata = open("data/boards/userboard.txt","w")
								wrtdata.write(newpost)
								wrtdata.close()
								room.message('"' + rawout.replace(finfo1, "") + '" has been removed from the user board.', html = True)
							else:
								room.message("The board does not have that many posts.")
						elif (args.startswith("delete ") and usrlvl >=2):
							cmd, delnum = args.split("delete ", 1)
							finfo1 = delnum + '!@!*&&&!'
							finfo2 = '*@(!(!*!@!' + delnum
							if finfo1 in userboard:
								indexs = userboard.find(finfo1)
								indexe = userboard.find(finfo2)
								rawout = userboard[(int(indexs)):(int(indexe))]
								newpost = userboard.replace(rawout + finfo2 + '.<br/>', "")
								i = int(delnum)
								while i <= 5:
									newpost = newpost.replace('*@(!(!*!@!' + str(i), '*@(!(!*!@!' + str(i-1))\
										.replace(str(i) + '!@!*&&&!', str(i-1) + '!@!*&&&!')
									i = i + 1
								wrtdata = open("data/boards/userboard.txt","w")
								wrtdata.write(newpost)
								wrtdata.close()
								room.message('"' + rawout.replace(finfo1, "") + '" has been removed from the user board.', html = True)
							else:
								room.message("The board does not have that many posts.")
						elif (args.startswith("Delete ") and usrlvl >=2):
							cmd, delnum = args.split("Delete ", 1)
							finfo1 = delnum + '!@!*&&&!'
							finfo2 = '*@(!(!*!@!' + delnum
							if finfo1 in userboard:
								indexs = userboard.find(finfo1)
								indexe = userboard.find(finfo2)
								rawout = userboard[(int(indexs)):(int(indexe))]
								newpost = userboard.replace(rawout + finfo2 + '.<br/>', "")
								i = int(delnum)
								while i <= 5:
									newpost = newpost.replace('*@(!(!*!@!' + str(i), '*@(!(!*!@!' + str(i-1))\
										.replace(str(i) + '!@!*&&&!', str(i-1) + '!@!*&&&!')
									i = i + 1
								wrtdata = open("data/boards/userboard.txt","w")
								wrtdata.write(newpost)
								wrtdata.close()
								room.message('"' + rawout.replace(finfo1, "") + '" has been removed from the user board.', html = True)
							else:
								room.message("The board does not have that many posts.")
						elif (args.startswith("Del ") and usrlvl >=2):
							cmd, delnum = args.split("Del ", 1)
							finfo1 = delnum + '!@!*&&&!'
							finfo2 = '*@(!(!*!@!' + delnum
							if finfo1 in userboard:
								indexs = userboard.find(finfo1)
								indexe = userboard.find(finfo2)
								rawout = userboard[(int(indexs)):(int(indexe))]
								newpost = userboard.replace(rawout + finfo2 + '.<br/>', "")
								i = int(delnum)
								while i <= 5:
									newpost = newpost.replace('*@(!(!*!@!' + str(i), '*@(!(!*!@!' + str(i-1))\
										.replace(str(i) + '!@!*&&&!', str(i-1) + '!@!*&&&!')
									i = i + 1
								wrtdata = open("data/boards/userboard.txt","w")
								wrtdata.write(newpost)
								wrtdata.close()
								room.message('"' + rawout.replace(finfo1, "") + '" has been removed from the user board.', html = True)
							else:
								room.message("The board does not have that many posts.")
						else:
							if postnum == 5:
								finfo1 = '1!@!*&&&!'
								finfo2 = '*@(!(!*!@!1'
								indexs = userboard.find(finfo1)
								indexe = userboard.find(finfo2)
								rawout = userboard[(int(indexs)):(int(indexe))]
								minus1 = userboard.replace(rawout + finfo2 + '.<br/>', "")
								switch2 = minus1.replace('2!@!*&&&!', '1!@!*&&&!')\
									.replace('*@(!(!*!@!2', '*@(!(!*!@!1')
								switch3 = switch2.replace('3!@!*&&&!', '2!@!*&&&!')\
									.replace('*@(!(!*!@!3', '*@(!(!*!@!2')
								switch4 = switch3.replace('4!@!*&&&!', '3!@!*&&&!')\
									.replace('*@(!(!*!@!4', '*@(!(!*!@!3')
								newpost = switch4.replace('5!@!*&&&!', '4!@!*&&&!')\
									.replace('*@(!(!*!@!5', '*@(!(!*!@!4')
								wrtdata = open("data/boards/userboard.txt","w")
								wrtdata.write(newpost)
								wrtdata.close()
								newpost = str(postnum)+ '!@!*&&&!' + args + ' - posted by <b>' + user.name.capitalize() + '</b> on <i>' + subtime + '</i>*@(!(!*!@!' + str(postnum) + '.<br/>'
								wrtdata = open("data/boards/userboard.txt","a")
								wrtdata.write(newpost)
								wrtdata.close()
								room.message('"' + args + '" has been posted to the user board.')
							else:
								postnum = postnum + 1
								newpost = str(postnum)+ '!@!*&&&!' + args + ' - posted by <b>' + user.name.capitalize() + '</b> on <i>' + subtime + '</i>*@(!(!*!@!' + str(postnum) + '.<br/>'
								wrtdata = open("data/boards/userboard.txt","a")
								wrtdata.write(newpost)
								wrtdata.close()
								room.message('"' + args + '" has been posted to the user board.')
				elif ( (cmd.lower() == "dict") or (cmd.lower() == "dictionary")):
					if (('teru' in args.lower()) or ('t3' in args.lower())):
						room.message("1 | noun | an extremely mean person, a meanie<br/>2 | noun | the subject of Ion's love<br/>3 | noun | a person that hates Ion and does not trust Ion at all.", html = True)
					elif ('wyx' in args.lower()):
						room.message("1 | noun | A mean man that wants to ensure that Ion is not happy.<br/>2 | noun | The sole person with the ability to grant Ion's dreams but is also lacking the heart to do so.<br/>3 | adjective | A dream crusher. Someone that is fueled by the crushed hopes of others.", html = True)
					else:
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
							try:
								doc = doc.read().decode()
								l = re.search('context.jsonArray.popups.pod_0200.push(.*?)"stringified": "(.*?)","mInput"', doc, re.DOTALL | re.IGNORECASE)
								if l:
									outraw = (("%s" %(l.group(2))).replace("\\n", "<br/>"))
									room.message(outraw, html = True)
								else:
									room.message("I couldn't find the definition of %s." %args)
							except:
								print 'error with dict'
								room.message("I don't have a clue. I also don't have more than a clue. I have 0 clues, no clue.")
						self.deferToThread(rfinish, urlreq.urlopen, "http://www.wolframalpha.com/input/?i=define%20" + word)
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
				elif ( (cmd.lower() == "sp" ) or (cmd.lower() == "spell") ):
					word = args\
						.replace(" ", "%20")\
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
						try:
							doc = doc.read().decode()
							m = re.search('<div style="margin:25;padding:10;width:468;background:#f0f0f0;float:left;">\n<b><font color="#990033">"(.*?)" is misspelled.</font></b><p></p><b>Here are some suggestions:</b><div><ol>\n<li><a href="(.*?)">(.*?)</a></li>', doc, re.DOTALL | re.IGNORECASE)
							o = re.search('<div style="margin:25;padding:10;width:468;background:#f0f0f0;float:left;">\n<b><font color="#990033">"(.*?)" is misspelled.</font></b><p></p><b>Here are some suggestions:</b><div><ol>\n<li><a href="(.*?)">(.*?)</a></li><li><a href="(.*?)">(.*?)</a></li><li><a href="(.*?)">(.*?)</a></li>', doc, re.DOTALL | re.IGNORECASE)
							p = re.search('<div style="margin:25;padding:10;width:468;background:#f0f0f0;float:left;">\n<b><font color="#006600">"(.*?)" is spelled correctly.</font></b><p></p><b>Here are some suggestions:</b><div><ol>\n<li><a href="(.*?)">(.*?)</a></li><li><a href="(.*?)">(.*?)</a></li><li><a href="(.*?)">(.*?)</a></li>', doc, re.DOTALL | re.IGNORECASE)
							r = re.search('<div style="margin:25;padding:10;width:468;background:#f0f0f0;float:left;">\n<b><font color="#006600">"(.*?)" is spelled correctly.</font></b>', doc, re.DOTALL | re.IGNORECASE)
							if o:
								out = 'I think you were trying to spell "%s"' %(o.group(3))
								out2 = 'Some alternate spellings are: "%s" and "%s".' %(o.group(5), o.group(7))
								room.message(out + " :P " + out2)
							elif m:
								out = 'I think you were trying to spell "%s"' %(m.group(3))
								room.message(out + " :P")
							elif p:
								out = 'Some other possibilities are: "%s" and "%s".' %(p.group(5), p.group(7))
								room.message('You probably spelled "' + args + '" correctly. ' + out)
							elif r:
								room.message('You probably spelled "' + args + '" correctly.')
							else:
								room.message('You probably spelled "spam" correctly.')
						except:
							print 'error with sp'
							room.message("I don't have a clue. I also don't have more than a clue. I have 0 clues, no clue.")
					searchurl = "http://www.phigita.net/spell-check/word-suggest?q=" + word
					self.deferToThread(rfinish, urlreq.urlopen, searchurl)
				elif ( (cmd.lower() == "rdwiki" ) or (cmd.lower() == "randomwiki") ):
					if usrlvl >= 3:
						word = args\
							.replace(" ", "%20")\
							.replace("&", "%26")\
							.replace("?", "%3F")\
							.replace("!", "%21")\
							.replace("=", "%3D")\
							.replace("'", "%27")
						room.message(('<a href="http://en.wikipedia.org/wiki/Special:Random" target="_blank">Click here for a random Wiki page. (It changes everytime you click it)</a>'), html = True)
				elif ( (cmd.lower() == "get" ) or (cmd.lower() == "g") or (cmd.lower() == "grab") ):
					if usrlvl >=1:
						argsadj = args.lower()
						if args.find(" ") != -1: #if there's a colon somewhere
							argsadj = args.lower()
							item, uuser = argsadj.split(" ", 1)
							uuser1 = uuser[0]
							uuser2 = uuser[1]
							if item.startswith("rec"):
								if uuser == 't6ru':
									room.message('cm:// ')
								else:
									room.message(('<a href="http://m1.chatango.com/av/%s/%s/%s/v.flv">Click here for <b>%s\'s</b> recording.</a>' %(uuser1, uuser2, uuser, uuser.capitalize())), html = True)
							elif item.startswith("full"):
								room.message(('<a href="http://fp.chatango.com/profileimg/%s/%s/%s/full.jpg" target="_blank">Click here for the full image</a><br/>http://fp.chatango.com/profileimg/%s/%s/%s/full.jpg' %(uuser1, uuser2, uuser, uuser1, uuser2, uuser)), html=True)
							elif item.startswith("image"):
								room.message('http://fp.chatango.com/profileimg/%s/%s/%s/full.jpg' %(uuser1, uuser2, uuser))
							elif item.startswith("icon"):
								room.message('http://fp.chatango.com/profileimg/%s/%s/%s/full.jpg' %(uuser1, uuser2, uuser))
							elif item.startswith("pic"):
								room.message('http://fp.chatango.com/profileimg/%s/%s/%s/full.jpg' %(uuser1, uuser2, uuser))
							elif item.startswith("thumb"):
								room.message('http://fp.chatango.com/profileimg/%s/%s/%s/thumb.jpg' %(uuser1, uuser2, uuser))
							elif item.startswith("bg"):
								room.message('http://fp.chatango.com/profileimg/%s/%s/%s/msgbg.jpg' %(uuser1, uuser2, uuser))
							elif item.startswith("msgbg"):
								room.message('http://fp.chatango.com/profileimg/%s/%s/%s/msgbg.jpg' %(uuser1, uuser2, uuser))
							elif argsadj.startswith("a life"):
								room.message('I wish I could, but I am just a lifeless bot! ;( Now you have made me sad.')
							else:
								room.message('I am not allowed to show you that, my stalker database is kept private.')
				elif ( (cmd.lower() == "gis" ) or (cmd.lower() == "jizz") or (cmd.lower() == "jiz") ):
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
						try:
							doc = doc.read().decode()
							list = []
							l = len(doc)
							hit = 0
							while(doc[hit:l].find('"unescapedUrl":"') != -1):
								current = doc[hit:l].find('"unescapedUrl":"')
								m = re.search('"unescapedUrl":"(.*?)","url"', doc[current:l], re.DOTALL | re.IGNORECASE)
								list = list + [m.group(1)]
								hit = hit + current + 16
							if list:
								result = random.choice(list)
								room.message('<a href="%s" target="_blank">Click here to see the image if it fails to load.</a><br/>%s' %(result, result), html = True)
							else:
								room.message("I couldn't find any images for your search.")
						except:
							print 'error with gis'
							room.message("I don't have a clue. I also don't have more than a clue. I have 0 clues, no clue.")
					searchurl = "https://ajax.googleapis.com/ajax/services/search/images?v=1.0&q=" + word
					self.deferToThread(rfinish, urlreq.urlopen, searchurl)
				elif ( (cmd.lower() == "gws" ) or (cmd.lower() == "search") or (cmd.lower() == "google") ):
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
						try:
							doc = doc.read().decode()
							m = re.search('","url":"(.*?)","visibleUrl":"(.*?)","titleNoFormatting":"(.*?)","content":"(.*?)"},(.*?)","url":"(.*?)","visibleUrl":"(.*?)","titleNoFormatting":"(.*?)","content":"(.*?)"},(.*?)","url":"(.*?)","visibleUrl":"(.*?)","titleNoFormatting":"(.*?)","content":"(.*?)"},', doc, re.DOTALL | re.IGNORECASE)
							if m:
								rawout1 = '<a href="%s" target="_blank"><b>%s</b></a><br/>%s<br/><br/><a href="%s" target="_blank"><b>%s</b></a><br/>%s<br/><br/><a href="%s" target="_blank"><b>%s</b></a><br/>%s<br/>For more info click on the titles.' %(m.group(1), m.group(3), m.group(4), m.group(6), m.group(8), m.group(9), m.group(11), m.group(13), m.group(14))
								rawout2 = rawout1.replace('\\u003c/b\\u003e', "")
								rawout3 = rawout2.replace('  ', " ")
								rawout4 = rawout3.replace("\\u003cb\\u003e", "")
								rawout5 = rawout4.replace("\u0026#39;", "'")\
									.replace('\u0026amp;', "|")\
									.replace('\u0026#39;', "'")\
									.replace('\u003d;', "")\
									.replace('\u00', "")
								out = rawout5.replace("\\u003cb\\u003e", "")
								room.message(out, html = True)
							else:
								room.message("I couldn't find any articles for your search.")
						except:
							print 'error with gws'
							room.message("I don't have a clue. I also don't have more than a clue. I have 0 clues, no clue.")
					searchurl = "https://ajax.googleapis.com/ajax/services/search/web?v=1.0&q=" + word
					self.deferToThread(rfinish, urlreq.urlopen, searchurl)
				elif ( (cmd.lower() == "wiki" ) or (cmd.lower() == "wikipedia") or (cmd.lower() == "w") ):
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
						try:
							doc = doc.read().decode()
							m = re.search('","url":"(.*?)","visibleUrl":"(.*?)","titleNoFormatting":"(.*?)","content":"(.*?)"},', doc, re.DOTALL | re.IGNORECASE)
							if m:
								rawout1 = '<a href="%s" target="_blank"><b>%s</b></a><br/>%s For more info click on the title.' %(m.group(1), m.group(3), m.group(4))
								rawout2 = rawout1.replace('\\u003c/b\\u003e', "")
								rawout3 = rawout2.replace('  ', " ")
								out = rawout3.replace("\\u003cb\\u003e", "")
								room.message(out, html = True)
							else:
								room.message("I couldn't find any articles for your search.")
						except:
							print 'error with gws'
							room.message("I don't have a clue. I also don't have more than a clue. I have 0 clues, no clue.")
					searchurl = "https://ajax.googleapis.com/ajax/services/search/web?v=1.0&q=" + word + '+wiki'
					self.deferToThread(rfinish, urlreq.urlopen, searchurl)
				elif ( (cmd.lower() == "yt" ) or (cmd.lower() == "youtube") ):
					if usrlvl > 0:
						#import urllib.request
						def ytvid(term):
							try:
								search = "http://www.youtube.com/results?search_query=" + term
								a = urlreq.urlopen(search)
								b = str(a.read())
								d = "/watch?v"
								e = b.find(d, 0)
								f = b[e:e+20]
								if ("watch?v=&" in f):
									result = f
								else:
									result = f.replace('/watch?v=', '')
								end = "http://youtu.be/" + result
								return end
							except:
								print 'error with gws'
								room.message("I don't have a clue. I also don't have more than a clue. I have 0 clues, no clue.")
						seek = args.replace(" ", "+")
						vidsec = ytvid(seek)
						if ("//watch?v=&" in vidsec):
							room.message("I couldn't find any videos for your search of " + args + ".")
						else:
							room.message(vidsec)
				elif ( (cmd.lower() == "coin" ) or (cmd.lower() == "flip") or (cmd.lower() == "decide") ):
					def rfinish(doc):
						#try:
						doc = doc.read().decode()
						m = re.search('<img src="(.*?)" alt="(.*?)">', doc, re.DOTALL | re.IGNORECASE)
						if m:
							side = '%s' %m.group(2)
							if side.startswith('obverse'): room.message('<b>Heads (Do it/yes/1st).</b><br/>http://www.random.org/coins/faces/60-usd/0025c-nj/obverse.jpg', html = True)
							elif side.startswith('reverse'): room.message("<b>Tails (Don't it/no/2nd).</b><br/>http://www.random.org/coins/faces/60-usd/0025c-nj/reverse.jpg", html = True)
						else:
							room.message("The coin fell into a storm drain.")
						#except:
						#	print 'error with coin'
						#	room.message("You donated the coin to a hobo, what a nice person you are.")
					searchurl = "http://www.random.org/coins/?num=1&cur=60-usd.0025c-nj"
					self.deferToThread(rfinish, urlreq.urlopen, searchurl)
				elif ( (cmd.lower() == "mylvl" ) or (cmd.lower() == "mylevel") ):
					mdst = room.getLevel(user)
					if mdst == 0:
						room.message("You are a regular user.")
					elif mdst == 1:
						room.message("You are a chat moderator.")
					elif mdst == 2:
						room.message("You are the head boss.")
					else:
						room.message("Your mod level: %i" %(room.getLevel(user)))
				elif ( (cmd.lower() == "dates") or (cmd.lower() == "id") or (cmd.lower() == "schedule") or (cmd.lower() == "sch") ):
					if user.name == "ion":
						calraw = open("data/cal/cal.txt","r")
						cal = (calraw.read())
						indexs = cal.find('dates&(*)^)$@')
						indexe = cal.find('(!*@)#*dates(@#@*')
						rawout = cal[(int(indexs)):(int(indexe))]
						out = rawout.replace('dates&(*)^)$@', "")
						calraw.close()
						room.message(out, html = True)
				elif ( (cmd.lower() == "exam") or (cmd.lower() == "exams") or (cmd.lower() == "e") or (cmd.lower() == "test") or (cmd.lower() == "tests") ):
					if user.name == "ion":
						calraw = open("data/cal/cal.txt","r")
						cal = (calraw.read())
						indexs = cal.find('exams#@@&@*@')
						indexe = cal.find('@*@(!*!)%exams@(#%*$')
						rawout = cal[(int(indexs)):(int(indexe))]
						out = rawout.replace('exams#@@&@*@', "")
						calraw.close()
						room.message(out, html = True)
				elif (cmd.lower()) == "time":
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
					if (room.getLevel(self.user) > 0):
						def rfinishloc(doc):
							try:
								doc = doc.read().decode()
								l = re.search('context.jsonArray.popups.pod_0200.push(.*?)"stringified": "(.*?)","mInput"', doc, re.DOTALL | re.IGNORECASE)
								if l:
									datar = ("%s" %(l.group(2))).replace("\/","/")
									provider, locationr = datar.split("location | ", 1)
									location = locationr\
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
									def rfinish(doc2):
										doc2 = doc2.read().decode()
										n = re.search('context.jsonArray.popups.pod_0200.push(.*?)"stringified": "(.*?)","mInput"', doc2, re.DOTALL | re.IGNORECASE)
										if n:
											timeraw = "%s" %(n.group(2))
											clock, date = timeraw.split("  |  ", 1)
											room.message(("It is currently %s on %s" %(clock, date)).replace("\/", "/"))
										else:
											room.message("I am sorry, I have failed you. I don't know what time it is Dx")
									if word == "":
										turl = "http://www.wolframalpha.com/input/?i=time%20" + location
									else:
										turl = "http://www.wolframalpha.com/input/?i=time%20" + word
									self.deferToThread(rfinish, urlreq.urlopen, turl)
								else:
									room.message("An error occured...")
							except:
								print 'error with gws'
								room.message("I don't have a clue. I also don't have more than a clue. I have 0 clues, no clue.")
						self.deferToThread(rfinishloc, urlreq.urlopen, "http://www.wolframalpha.com/input/?i=" + message.ip)
					else:
						def rfinish(doc):
							try:
								doc = doc.read().decode()
								l = re.search('context.jsonArray.popups.pod_0200.push(.*?)"stringified": "(.*?)","mInput"', doc, re.DOTALL | re.IGNORECASE)
								if l:
									timeraw = "%s" %(l.group(2))
									clock, date = timeraw.split("  |  ", 1)
									room.message(("It is currently %s on %s" %(clock, date)).replace("\/", "/"))
								else:
									room.message("I am sorry, I have failed you. I don't know what time it is Dx")
							except:
								print 'error with gws'
								room.message("I don't have a clue. I also don't have more than a clue. I have 0 clues, no clue.")
						if word == "":
							turl = "http://www.wolframalpha.com/input/?i=time"
						else:
							turl = "http://www.wolframalpha.com/input/?i=time%20" + word
						self.deferToThread(rfinish, urlreq.urlopen, turl)
				elif ( (cmd.lower() == "len" ) or (cmd.lower() == "stringcount") ):
					room.message( str(len(args)))
				elif ( (cmd.lower() == "loc" ) or (cmd.lower() == "location") ):
					if (room.getLevel(self.user) > 0):
						def rfinishloc(doc):
							try:
								doc = doc.read().decode()
								l = re.search('context.jsonArray.popups.pod_0200.push(.*?)"stringified": "(.*?)","mInput"', doc, re.DOTALL | re.IGNORECASE)
								if l:
									datar = ("%s" %(l.group(2))).replace("\/","/")
									provider, location = datar.split("location | ", 1)
									room.message("I am currently watching you from a bush in " + location + ".")
								else:
									room.message("An error occured...")
							except:
								print 'error with gws'
								room.message("I don't have a clue. I also don't have more than a clue. I have 0 clues, no clue.")
						self.deferToThread(rfinishloc, urlreq.urlopen, "http://www.wolframalpha.com/input/?i=" + message.ip)
					else:
						room.message('My stalker info is top secret.')
				elif ( (cmd.lower() == "math" ) or (cmd.lower() == "m") ):
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
						try:
							doc = doc.read().decode()
							l = re.search('context.jsonArray.popups.pod_0200.push(.*?)"stringified": "(.*?)","mInput"', doc, re.DOTALL | re.IGNORECASE)
							m =re.search('context.jsonArray.popups.pod_0100.push(.*?){"stringified": "(.*?)","mInput":', doc, re.DOTALL | re.IGNORECASE)
							if l and m:
								room.message((args + " = %s" %(l.group(2))).replace("\/","/"))
							elif m:
								room.message(("%s" %(m.group(2))).replace("\/","/"))
							else:
								room.message("An error occured...")
						except:
							print 'error with gws'
							room.message("I don't have a clue. I also don't have more than a clue. I have 0 clues, no clue.")
					self.deferToThread(rfinish, urlreq.urlopen, "http://www.wolframalpha.com/input/?i=" + word)
				elif (("#@@$!!(!*@" + room.name + "@@#$&*(**!") in funmode):
					if ( (cmd.lower() == "spinthebottle" ) or (cmd.lower() == "stb") ):
						room.message(random.choice(room.usernames))
					elif (cmd.lower()) == "rr":
						if usrlvl >= 1:
							gunchamber = [0, 1, 2, 3]
							fate = random.choice(gunchamber)
							if(fate == 0):
								room.banUser(user)
								room.message('BOOM!! ' + user.name.capitalize() + "'s brains splatter on the wall.")
								def loljk():
									room.unban(user)
								thai = Timer(60.0, loljk)
								thai.start()
							else:
								room.message('Click!...Next time you won`t be so lucky, ' + user.name.capitalize() + ".")
					elif ( (cmd.lower() == "br" ) or (cmd.lower() == "banroulette") ):
						if usrlvl >=3:
							namestr = str(room.usernames).replace("[", "")\
									.replace("]", "")\
									.replace(" '", "")\
									.replace("'", "")\
									.replace('t6ru' + ',', "")\
									.replace('t6ru', "")
							namelist = ([n for n in namestr.split(',')])
							usrchoice = random.choice(namelist)
							endusr = ch._users.get(usrchoice)
							room.banUser(endusr)
							room.message('Bullets fly everywhere and ' + usrchoice.capitalize() + ' is struck by one and killed.')
					elif (cmd.lower()) == "suicide":
						mdlvl = room.getLevel(user)
						suicide1 = '-Pours water onto myself-'
						suicide2 = 'NO, YOU!'
						if (usrlvl >= 2 or mdlvl >= 1):
							room.message(suicide1)
						else:
							room.message(suicide2)
					elif (cmd.lower()) == "huladance":
						if ((usrlvl >=2) or (mdlvl >= 1)):
							for i, msg in enumerate(huladance):
								self.setTimeout(i / 2, room.message, msg)
						else:
							room.message("Not going to happen.")
					elif (cmd.lower()) == "lick":
						time.sleep(0)
						for i, msg in enumerate(lick):
							self.setTimeout(i / 2, room.message, msg)
					elif (cmd.lower()) == "status":
						zombielistr = open("data/zombie/zombies.txt","r")
						zombielist = (zombielistr.read()).lower()
						zombielistr.close()
						allusrlistr = open("data/zombie/allusrlist.txt","r")
						allusrlist = (allusrlistr.read()).lower()
						allusrlistr.close()
						if args == "":
							argsfind = "@#$*!" + user.name + "@#$*!"
							if argsfind in zombielist:
								room.message(user.name.capitalize() + " is a brain hungry zombie!")
							elif argsfind in allusrlist:
								room.message(user.name.capitalize() + " is a frightened human that probably has *poop* stained pants.")
							else:
								room.message(user.name.capitalize() + " is not a player. Ask a level 2+ to whitelist them.")
						else:
							argsfind = "@#$*!" + args.lower() + "@#$*!"
							if argsfind in zombielist:
								room.message(args.capitalize() + " is a brain hungry zombie!")
							elif argsfind in allusrlist:
								room.message(args.capitalize() + " is a frightened human that probably has *poop* stained pants.")
							else:
								room.message(args.capitalize() + " is not a player. Ask a level 2+ to whitelist them.")
					elif ( (cmd.lower() == "bite" ) or (cmd.lower() == "bites") ):
						usager = open("data/usage/usage.txt","r")
						usage = (usager.read()).lower()
						usager.close()
						nowfc = strftime("*#&^^&@%d #(!)#)!%b $!@$)($)!%Y ##$@$!%H:(!@*$&@%M:*$&*#(@" + user.name + "!!$&$!@%S$*$&", gmtime()).lower()
						focususrst = '#$&@$^!:$#@$#@$#(#' + user.name + '@#(*#$!()!$'
						focususred = user.name + '$*!&$@)!_+'
						usredtime = '*!(@#$#*!&@$!)!#_!(' + user.name + '$#@#$(@'
						bodywrt = room.name + '*$($*!@&$(!@' + msgbody + '$@#*$@*$(@!:)$(!@$)@#'
						relapointid = '@(#$*!()#' + user.name + '!#$#!(%*#!'
						if focususrst in usage:
							rpusager = open("data/usage/usage.txt","r")
							rpusage = (rpusager.read()).lower()
							rpusager.close()
							indexsrp = usage.find(focususred)
							indexerp = usage.find(relapointid)
							rawoutrp = usage[(int(indexsrp)):(int(indexerp))]
							relationpr = rawoutrp.replace(focususred, '')
							relationp = int(relationpr)
						else:
							relationpr = '0'
							relationp = 0
						if user.name == 't6ru':
							nowuh = strftime("%a, %d %b %Y %H:%M:%S", gmtime())
							wrtdata = open("data/usage/uhistory.txt","a")
							wrtdata.write(str((nowuh + ' ---> ' + room.name + ': ' + msgbody).encode('utf-8')) + '\n')
							wrtdata.close()
							#print(room.name + ' --> ' + user.name + ': ', msgbody)
						if self.user == user: return
						elif usrlvl >0:
							if msgbody.startswith(';'):
								if focususrst in usage:
									indexs = usage.find(focususrst)
									indexe = usage.find(relapointid)
									rawout = usage[(int(indexs)):(int(indexe))]
									newdatar = str(usage).replace((rawout + relapointid), (focususrst + nowfc + usredtime + bodywrt + focususred + str(relationp) + relapointid))
									newdata = str(newdatar.encode('utf-8')).replace("\\n", "\n")\
										.replace("b'", "")\
										.replace('b"', "")\
										.replace("\'", "")\
										.replace('\"', "")\
										.replace("\\\\", "")
									wrtdata = open("data/usage/usage.txt","w")
									wrtdata.write(newdata)
									wrtdata.close()
								else:
									wrtdata = open("data/usage/usage.txt","a")
									wrtdata.write(str((focususrst + nowfc + usredtime + bodywrt + focususred + '0' + relapointid).encode('utf-8')) + '\n')
									wrtdata.close()
								#print(room.name + ' --> ' + user.name + ': ', msgbody)
							elif user.name == 'grim':
								nowsk = strftime("%a, %d %b %Y %H:%M:%S", gmtime())
								wrtdata = open("data/usage/grimhistory.txt","a")
								wrtdata.write(str((nowuh + ' ---> ' + room.name + ': ' + msgbody).encode('utf-8')) + '\n')
								wrtdata.close()
								#print(room.name + ' --> ' + user.name + ': ', msgbody)
							#else:
								#print(room.name + ' --> ' + user.name + ': ', msgbody)
							focustxtr = open("data/usage/usage.txt","r")
							focustxt = (focustxtr.read()).lower()
							focustxtr.close()
							if (msgbody[0] == ";"):
								callname = 6
							elif focususrst in str(focustxt):
								currentsf = ":*$&*#(@" + user.name + "!!$&$!@"
								indexsf = nowfc.find(currentsf)
								indexef = nowfc.find('$*$&')
								rawoutf = nowfc[(int(indexsf)):(int(indexef))]
								nowfcseir = rawoutf.replace(currentsf, '')
								nowfcsei = int(nowfcseir)
								indexsof = focustxt.find(currentsf)
								indexeof = focustxt.find('$*$&' + usredtime)
								rawoutof = focustxt[(int(indexsof)):(int(indexeof))]
								oldfcsir = rawoutof.replace(currentsf, '')
								oldfcsi = int(oldfcsir)
								if ((nowfcsei < 20) and (oldfcsi > 20)):
									indexsmf = nowfc.find(':(!@*$&@')
									indexemf = nowfc.find(':*$&*#(@')
									rawoutmf = nowfc[(int(indexsmf)):(int(indexemf))]
									nowfcmir = rawoutmf.replace(':(!@*$&@', '')
									nowfcmi = int(nowfcmir) - 1
									currenti = focususrst + nowfc[0:51] + str(nowfcmi) + nowfc[53:61]
								else:
									currenti = focususrst + nowfc[0:61]
								if (currenti in focustxt):
									if nowfcsei > 20:
										nowfcssi = nowfcsei - 20
										if ( (oldfcsi >= nowfcssi) and (oldfcsi <= nowfcsei) ):
											msgbody = 't6 ' + msgbody
											callname = 0
										else: 
											callname = 0
									else:
										nowfcssi = nowfcsei + 40
										if oldfcsi < 20:
											msgbody = 't6 ' + msgbody
											callname = 0
										elif ( (oldfcsi >= nowfcssi) and (oldfcsi <= (nowfcsei + 60)) ):
											msgbody = 't6 ' + msgbody
											callname = 0
										else: 
											callname = 0
								else:
									callname = 0
							else:
								callname = 0
						else:
							callname = 0
						zombielistr = open("data/zombie/zombies.txt","r")
						zombielist = (zombielistr.read()).lower()
						zombielistr.close()
						allusrlistr = open("data/zombie/allusrlist.txt","r")
						allusrlist = (allusrlistr.read()).lower()
						allusrlistr.close()
						usrfind = "@#$*!" + user.name + "@#$*!"
						argsfind = "@#$*!" + args.lower() + "@#$*!"
						ru = str(room.getUserlist(mode = None, unique = None, memory = None))
						if (("<User: " + args.lower() + ">") in ru):
							if usrfind in zombielist:
								if (argsfind in allusrlist):
									outcome = random.choice([1, 1, 1, 1, 1, 2, 2])
									if outcome == 1:
										bitephrase = random.choice([("You leap towards " + args.capitalize() + ", your mouth is salivating blood as you attempt to quench your thirst for brains."), ("You open your mouth wide and prepare to take the meat of " + args.capitalize() + ".")])
										def attack():
											newzombie = open("data/zombie/zombies.txt","a")
											newzombie.write("\n" + argsfind)
											room.message("You bite into " + args.capitalize() + "'s skull. Enjoy your feast of brains, you have earned it.")
											newzombie.close()
											newusrlist = allusrlist.replace(argsfind, "")
											newusrwrite = open("data/zombie/allusrlist.txt","w")
											newusrwrite.write(newusrlist)
											newusrwrite.close()
										thai = Timer(5.0, attack)
										thai.start()
									elif outcome == 2:
										bitephrase = random.choice([("You dive at " + args.capitalize() + " but end up faceplanting into the pavement."), ("You start moving towards " + args.capitalize() + " and fall into an open manhole cover.")])
									room.message(bitephrase)
								elif (argsfind in zombielist):
									room.message("You bite into " + args.capitalize() + "'s flesh but quickly realize that it is as rotten as your own. You spit it out and continue searching for humans.")
							else:
								if "@#$*!" + args.lower() + "!@^$@" in zombielist:
									room.message("You just bit a zombie, are you stupid? You are now infected, smooooth.")
									newzombie = open("data/zombie/zombies.txt","a")
									newzombie.write("\n" + usrfind)
									newzombie.close()
									newusrlist = allusrlist.replace(usrfind, "")
									newusrwrite = open("data/zombie/allusrlist.txt","w")
									newusrwrite.write(newusrlist)
									newusrwrite.close()
								else:
									room.message("You just bit another human. " + args.capitalize() + " thinks you are a zombie and slits your throat. You come back as a zombie.")
									newzombie = open("data/zombie/zombies.txt","a")
									newzombie.write("\n" + usrfind)
									newzombie.close()
									newusrlist = allusrlist.replace(usrfind, "")
									newusrwrite = open("data/zombie/allusrlist.txt","w")
									newusrwrite.write(newusrlist)
									newusrwrite.close()
						else:
							room.message(args.capitalize() + " is not in sight. You must be seeing things because you are so deprived of food.")
					elif ( (cmd.lower() == "fish" ) or (cmd.lower() == "fishes") ):
						if usrlvl >= 2:
							room.message("><>")
					elif (cmd.lower() == "users" ):
						if usrlvl >=3:
							ru = str(room.getUserlist(mode = None, unique = None, memory = None))
							room.message(ru)
					elif ( (cmd.lower() == "ec" ) or (cmd.lower() == "encrypt") ):
						if usrlvl >= 1:
							shift = int(len(args) - (len(args) / 2))
							if ((shift%94 > 86) and (shift%94 <= 94)):
								shift = 45
							elif (shift%94 < 8):
								shift = 45
							letters = string.ascii_letters + string.punctuation + '0123456789'
							encoded = ''
							for letter in args:
								if letter == ' ':
									encoded = encoded + ' '
								elif letter in letters:
									x = letters.index(letter) + shift
									encoded = encoded + letters[x%94]
								else:
									encoded = encoded + '~'
							room.message(encoded)
					elif ( (cmd.lower() == "dc" ) or (cmd.lower() == "decrypt") ):
						if usrlvl >= 3:
							shift = int(len(args) - (len(args) / 2))
							if ((shift%94 > 86) and (shift%94 <= 94)):
								shift = 45
							elif (shift%94 < 8):
								shift = 45
							letters = string.ascii_letters + string.punctuation + '0123456789'
							decoded = ''
							for letter in args:
								if letter == ' ':
									decoded = decoded + ' '
								elif letter in letters:
									x = letters.index(letter) - shift
									decoded = decoded + letters[x%94]
								else:
									decoded = decoded + '~'
							room.message(decoded)
					elif ( (cmd.lower() == "goml" ) or (cmd.lower() == "getonmylevel") ):
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
					elif ( (cmd.lower() == "tf" ) or (cmd.lower() == "tableflip") or (cmd.lower() == "fliptable") ):
						if usrlvl >= 1:
							flipped = random.choice(["Soup flies across the room!", "A fork flies up in the air and pokes you in the eye", "Sammiches, sammiches everywhere.", "The table does a 360 and nothing even moves from its place of the table.", "Meatballs and noodles splatter the wall in the shape of Jesus.", "Good job, you just broke your mother's good china.", "In hindsight, you probably should have taken your computer off of the table before you flipped it.", "Juice spills on the floor and stains your cat a dark redish-purple color.", "The table goes through your window and lands on an old lady, killing her in the process. You better hide the body."])
							time.sleep(1)
							room.message(flipped)
					elif ( (cmd.lower() == "s" ) or (cmd.lower() == "say") ):
						if usrlvl>=1:
							room.message(args, html = True)
					elif (cmd.lower()) == "":
						nameres = 'Yes, '
						nameres2 = '?'
						fnameres = nameres + (user.name).capitalize() + nameres2
						time.sleep(1)
						room.message(fnameres)
					elif ( (cmd.lower() == "cmpt" ) or (cmd.lower() == "compliment") ):
						rcmpt = random.choice([cmpt1, cmpt2,cmpt3, cmpt4, cmpt5])
						fcmpt = args.capitalize() + str(rcmpt)
						room.message(fcmpt)
					elif ( (cmd.lower() == "poker" ) or (cmd.lower() == "pk") ):
						if usrlvl >= 0:
							rpgpr = open("data/poker/pgp.txt","r")
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
							if 4 > 10:
								lazycode = True
							else:
								indexs = rpgp.find('^$&*available = ')
								indexe = rpgp.find(' *)!#')
								rawout = rpgp[(int(indexs)):(int(indexe))]
								rawout2 = rawout.replace(('^$&*available = '), "")
								available = rawout2.replace((' *)!#'), "")
								if available == '0':
									wrtset1 = open("data/poker/pgp.txt", "w")
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
									wrtnewcd = open("data/poker/pgp.txt", "w")
									wrtnewcd.write(pgpnewcd)
									wrtnewcd.close()
									rpgpr.close()
									pgpr = open("data/poker/pgp.txt","r")
									pgp = (pgpr.read()).lower()
									handstrr = card1 + "," + card2 + "," + card3 + "," + card4 + "," + card5
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
									availableir = int(available)
									availablei = availableir - 1
									availblenew = '^$&*available = ' + str(availablei) + ' *)!#'
									pgpnew = pgp.replace(('^$&*available = ' + available + ' *)!#'), str(availblenew))
									wrtdata2 = open("data/poker/pgp.txt", "w")
									secnames = '#$!*&^!@' + available + user.name + '&&*)^$#@!'
									secnamef = ')(&$&$#@' + available + user.name + '!@&@$@^&'
									highnames = '!!@*^$&' + available + user.name + '**^&$$#!('
									highnamef = '&(#*$%!)^' + available + user.name + '(*&$@@#!'
									wrtdata2.write(pgpnew + '\n' + secnames + ("handpointp%d = %d" %(availableir, handpoints)) + secnamef + '\n' + highnames + ("highcardp%d = %d" %(availableir, highcard)) + highnamef + '\n' )
									wrtdata2.close()
									pgpr.close()
									pgpfr = open("data/poker/pgp.txt","r")
									pgpf = (pgpfr.read()).lower()
									room.message(str("The cards you drew are: " + card1 + ", " + card2 + ", " + card3 + ", " + card4 + ", " + card5 + "."))
									if availablei == 0:
										fdhp1 = '&&*)^$#@!handpointp1 = '
										fdhp2 = '&&*)^$#@!handpointp2 = '
										fdhc1 = '**^&$$#!(highcardp1 = '
										fdhc2 = '**^&$$#!(highcardp2 = '
										indexsp1 = pgpf.find(fdhp1)
										indexep1 = pgpf.find(')(&$&$#@1')
										rawoutp1 = pgpf[(int(indexsp1)):(int(indexep1))]
										rawout2p1 = rawoutp1.replace((fdhp1), "")
										pointsrp1 = rawout2p1.replace((')(&$&$#@1'), "")
										pointsp1 = int(pointsrp1)
										indexsp2 = pgpf.find(fdhp2)
										indexep2 = pgpf.find(')(&$&$#@2')
										rawoutp2 = pgpf[(int(indexsp2)):(int(indexep2))]
										rawout2p2 = rawoutp2.replace((fdhp2), "")
										pointsrp2 = rawout2p2.replace((')(&$&$#@2'), "")
										pointsp2 = int(pointsrp2)
										indexshp1 = pgpf.find(fdhc1)
										indexehp1 = pgpf.find('&(#*$%!)^1')
										rawouthp1 = pgpf[(int(indexshp1)):(int(indexehp1))]
										rawout2hp1 = rawouthp1.replace((fdhc1), "")
										pointsrhp1 = rawout2hp1.replace(('&(#*$%!)^1'), "")
										pointshp1 = int(pointsrhp1)
										indexshp2 = pgpf.find(fdhc2)
										indexehp2 = pgpf.find('&(#*$%!)^2')
										rawouthp2 = pgpf[(int(indexshp2)):(int(indexehp2))]
										rawout2hp2 = rawouthp2.replace((fdhc2), "")
										pointsrhp2 = rawout2hp2.replace(('&(#*$%!)^2'), "")
										pointshp2 = int(pointsrhp2)
										if (pointsp1 > pointsp2):
											indexsw = pgpf.find('#$!*&^!@1')
											indexew = pgpf.find(')(&$&$#@1')
											rawoutw = pgpf[(int(indexsw)):(int(indexew))]
											rawout2w = rawoutw.replace(('#$!*&^!@1'), "")
											victorrw = rawout2w.replace((fdhp1 + pointsrp1), "")
											victorw = victorrw.replace((')(&$&$#@1'), "")
											room.message(victorw.capitalize() + " wins the match!")
											pgpfr.close()
											wrtset1 = open("data/poker/pgp.txt", "w")
											wrtset1.write(pokerallcards)
											wrtset1.close()
										elif (pointsp2 > pointsp1):
											indexsw = pgpf.find('#$!*&^!@2')
											indexew = pgpf.find(')(&$&$#@2')
											rawoutw = pgpf[(int(indexsw)):(int(indexew))]
											rawout2w = rawoutw.replace(('#$!*&^!@2'), "")
											victorrw = rawout2w.replace((fdhp2 + pointsrp2), "")
											victorw = victorrw.replace((')(&$&$#@2'), "")
											room.message(victorw.capitalize() + " wins the match!")
											pgpfr.close()
											wrtset1 = open("data/poker/pgp.txt", "w")
											wrtset1.write(pokerallcards)
											wrtset1.close()
										elif (pointsp2 == pointsp1):
											if (pointshp1 > pointshp2):
												indexsw = pgpf.find('#$!*&^!@1')
												indexew = pgpf.find(')(&$&$#@1')
												rawoutw = pgpf[(int(indexsw)):(int(indexew))]
												rawout2w = rawoutw.replace(('#$!*&^!@1'), "")
												victorrw = rawout2w.replace((fdhp1 + pointsrp1), "")
												victorw = victorrw.replace((')(&$&$#@1'), "")
												room.message(victorw.capitalize() + " wins the match!")
												pgpfr.close()
												wrtset1 = open("data/poker/pgp.txt", "w")
												wrtset1.write(pokerallcards)
												wrtset1.close()
											elif (pointshp2 > pointshp1):
												indexsw = pgpf.find('#$!*&^!@2')
												indexew = pgpf.find(')(&$&$#@2')
												rawoutw = pgpf[(int(indexsw)):(int(indexew))]
												rawout2w = rawoutw.replace(('#$!*&^!@2'), "")
												victorrw = rawout2w.replace((fdhp2 + pointsrp2), "")
												victorw = victorrw.replace((')(&$&$#@2'), "")
												room.message(victorw.capitalize() + " wins the match!")
												pgpfr.close()
												wrtset1 = open("data/poker/pgp.txt", "w")
												wrtset1.write(pokerallcards)
												wrtset1.close()
											elif (pointshp2 == pointshp1):
												room.message("It is a draw!")
												pgpfr.close()
												wrtset1 = open("data/poker/pgp.txt", "w")
												wrtset1.write(pokerallcards)
												wrtset1.close()
					elif ( (cmd.lower() == "pokerdraw" ) or (cmd.lower() == "pkd") ):
						if usrlvl >= 0:
								rglist = open("data/poker/glist.txt","r")
								glist = (rglist.read()).lower()
								if ('*$^&@($#@!*$#' + room.name + '$*#$$*&&@^#') not in glist:
									players = 3
									wrtset1 = open(("data/poker/" + room.name + ".txt"), "w")
									wrtset1.write(("*$#^!players = %d &^$*\n^$&*available = %d *)!#\n*#&^tradestatus = %d )#(#*&\n##$*!@turn = 1@*&(*\n\n" %(players, players, players)) + totalcardlist)
									wrtset1.close()
									wrtlist2 = open(("data/poker/glist.txt"), "a")
									wrtlist2.write('*$^&@($#@!*$#' + room.name + '$*#$$*&&@^#\n')
									wrtlist2.close()
								gid = room.name
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
										room.message('This game is in the trade phase, to trade your unwanted cards for new cards type ;pokertrade [CARD NAME], [CARD NAME], [CARD NAME], etc...')
								elif user.name in rgset:
									room.message("You have already drawn for this game.")
								elif available == '0':
									room.message("This game is full, no new people can join. Please wait for the game to finish or for 5 minutes to pass.")
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
									wrtdata2 = open(("data/poker/" + room.name + ".txt"), "w")
									secnames = '#$!*&^!@' + user.name + '&&*)^$#@!'
									secnamef = ')(&$&$#@' + user.name + '!@&@$@^&'
									highnames = '!!@*^$&' + user.name + '**^&$$#!('
									highnamef = '&(#*$%!)^' + user.name + '(*&$@@#!'
									handnames = '**^@%#$' + user.name + ')()*@&^%'
									handnamef = '!)@(#$&' + user.name + '!*!&!^#'
									wrtdata2.write(gsetnew + '\n' + secnames + ("handpoint = %d" %(handpoints)) + secnamef + '\n' + highnames + ("highcard = %d" %(highcard)) + highnamef + '\n' + handnames + 'card1 = ' + card1 + handnamef + 'c1' + '\n' + handnames + 'card2 = ' + card2 + handnamef + 'c2' + '\n' + handnames + 'card3 = ' + card3 + handnamef + 'c3' + '\n' + handnames + 'card4 = ' + card4 + handnamef + 'c4' + '\n' + handnames + 'card5 = ' + card5 + handnamef + 'c5' + '\n')
									wrtdata2.close()
									rglist.close()
									gsetr.close()
									wrtdata2.close()
									(self._pm).message(user, str("Your cards for [" + room.name + "] are: " + card1 + ", " + card2 + ", " + card3 + ", " + card4 + ", " + card5 + "."  'You now have to trade the cards you do not want for new ones...to do this type ;pokertrade [CARD NAME], [CARD NAME], [CARD NAME], etc... in the chat. If you do not want to trade any cards type ;pokertrade none'))
									if availablei == 0:
										tsetr = open("data/poker/" + room.name + ".txt","r")
										tset = (tsetr.read()).lower()
										tsetnew = tset.replace(('##$*!@turn = 1@*&(*'), '##$*!@turn = 2@*&(*')
										wrtdatat = open(("data/poker/" + room.name + ".txt"), "w")
										wrtdatat.write(tsetnew)
										tsetr.close()
										wrtdatat.close()
									room.message("I have PMed you the hand you drew.")
					elif ( (cmd.lower() == "pokertrade" ) or (cmd.lower() == "pkt") ):
						if usrlvl >= 0:
									trade = args.lower()
									switchcardsr1 = re.split(', ', trade)
									switchcardsr2 = [item.lower() for item in switchcardsr1]
									tradenum = len(switchcardsr2)
									glistr = open("data/poker/glist.txt","r")
									glist = (glistr.read()).upper()
									errormsg = "One or more cards that you requested for trade are not in your hand."
									if ('*$^&@($#@!*$#' + room.name + '$*#$$*&&@^#') in glist:
										gid = room.name
										rgsetr = open("data/poker/" + room.name + ".txt","r")
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
											room.message("Trading will begin when all players draw.")
										elif ('*$!$@#($*!' + user.name + ' has traded!$#@(%*!%!') in (rgset):
											room.message("You have already done a trade. Please wait for all players to finish trading, or for five minutes to pass.")
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
																	room.message(errormsg)
															elif (sc4 in oldcard5):
																if (sc5 in oldcard4):
																	falsetrade = 0
																else:
																	falsetrade = 1
																	room.message(errormsg)
															else:
																falsetrade = 1
																room.message(errormsg)
														elif (sc3 in oldcard4):
															if (sc4 in oldcard3):
																if (sc5 in oldcard5):
																	falsetrade = 0
																else:
																	falsetrade = 1
																	room.message(errormsg)
															elif (sc4 in oldcard5):
																if (sc5 in oldcard3):
																	falsetrade = 0
																else:
																	falsetrade = 1
																	room.message(errormsg)
															else:
																falsetrade = 1
																room.message(errormsg)
														elif (sc3 in oldcard5):
															if (sc4 in oldcard3):
																if (sc5 in oldcard4):
																	falsetrade = 0
																else:
																	falsetrade = 1
																	room.message(errormsg)
															elif (sc4 in oldcard4):
																if (sc5 in oldcard3):
																	falsetrade = 0
																else:
																	falsetrade = 1
																	room.message(errormsg)
															else:
																falsetrade = 1
																room.message(errormsg)
														else:
															falsetrade = 1
															room.message(errormsg)
													elif (sc2 in oldcard3):
														if (sc3 in oldcard2):
															if (sc4 in oldcard4):
																if (sc5 in oldcard5):
																	falsetrade = 0
																else:
																	falsetrade = 1
																	room.message(errormsg)
															elif (sc4 in oldcard5):
																if (sc5 in oldcard4):
																	falsetrade = 0
																else:
																	falsetrade = 1
																	room.message(errormsg)
															else:
																falsetrade = 1
																room.message(errormsg)
														elif (sc3 in oldcard4):
															if (sc4 in oldcard2):
																if (sc5 in oldcard5):
																	falsetrade = 0
																else:
																	falsetrade = 1
																	room.message(errormsg)
															elif (sc4 in oldcard5):
																if (sc5 in oldcard2):
																	falsetrade = 0
																else:
																	falsetrade = 1
																	room.message(errormsg)
															else:
																falsetrade = 1
																room.message(errormsg)
														elif (sc3 in oldcard5):
															if (sc4 in oldcard2):
																if (sc5 in oldcard4):
																	falsetrade = 0

																else:
																	falsetrade = 1
																	room.message(errormsg)
															elif (sc4 in oldcard4):
																if (sc5 in oldcard2):
																	falsetrade = 0
																else:
																	falsetrade = 1
																	room.message(errormsg)
															else:
																falsetrade = 1
																room.message(errormsg)
														else:
															falsetrade = 1
															room.message(errormsg)
													elif (sc2 in oldcard4):
														if (sc3 in oldcard2):
															if (sc4 in oldcard3):
																if (sc5 in oldcard5):
																	falsetrade = 0
																else:
																	falsetrade = 1
																	room.message(errormsg)
															elif (sc4 in oldcard5):
																if (sc5 in oldcard3):
																	falsetrade = 0
																else:
																	falsetrade = 1
																	room.message(errormsg)
															else:
																falsetrade = 1
																room.message(errormsg)
														elif (sc3 in oldcard3):
															if (sc4 in oldcard2):
																if (sc5 in oldcard5):
																	falsetrade = 0
																else:
																	falsetrade = 1
																	room.message(errormsg)
															elif (sc4 in oldcard5):
																if (sc5 in oldcard2):
																	falsetrade = 0

																else:
																	falsetrade = 1
																	room.message(errormsg)
															else:
																falsetrade = 1
																room.message(errormsg)
														elif (sc3 in oldcard5):
															if (sc4 in oldcard2):
																if (sc5 in oldcard2):
																	falsetrade = 0
																else:
																	falsetrade = 1
																	room.message(errormsg)
															elif (sc4 in oldcard3):
																if (sc5 in oldcard3):
																	falsetrade = 0
																else:
																	falsetrade = 1
																	room.message(errormsg)
															else:
																falsetrade = 1
																room.message(errormsg)
														else:
															falsetrade = 1
															room.message(errormsg)
													elif (sc2 in oldcard5):
														if (sc3 in oldcard2):
															if (sc4 in oldcard3):
																if (sc5 in oldcard4):

																	falsetrade = 0
																else:
																	falsetrade = 1
																	room.message(errormsg)
															elif (sc4 in oldcard4):
																if (sc5 in oldcard3):
																	falsetrade = 0
																else:
																	falsetrade = 1
																	room.message(errormsg)
															else:
																falsetrade = 1
																room.message(errormsg)
														elif (sc3 in oldcard3):
															if (sc4 in oldcard2):
																if (sc5 in oldcard4):
																	falsetrade = 0
																else:
																	falsetrade = 1
																	room.message(errormsg)
															elif (sc4 in oldcard4):
																if (sc5 in oldcard2):
																	falsetrade = 0
																else:
																	falsetrade = 1
																	room.message(errormsg)
															else:
																falsetrade = 1
																room.message(errormsg)
														elif (sc3 in oldcard4):
															if (sc4 in oldcard2):
																if (sc5 in oldcard3):
																	falsetrade = 0
																else:
																	falsetrade = 1
																	room.message(errormsg)
															elif (sc4 in oldcard3):
																if (sc5 in oldcard2):
																	falsetrade = 0
																else:
																	falsetrade = 1
																	room.message(errormsg)
															else:
																falsetrade = 1
																room.message(errormsg)
														else:
															falsetrade = 1
															room.message(errormsg)
													else:
														falsetrade = 1
														room.message(errormsg)
												elif (sc1 in oldcard2):
													if (sc2 in oldcard1):
														if (sc3 in oldcard3):
															if (sc4 in oldcard4):
																if (sc5 in oldcard5):
																	falsetrade = 0
																else:
																	falsetrade = 1
																	room.message(errormsg)
															elif (sc4 in oldcard5):
																if (sc5 in oldcard4):
																	falsetrade = 0
																else:
																	falsetrade = 1
																	room.message(errormsg)
															else:
																falsetrade = 1
																room.message(errormsg)
														elif (sc3 in oldcard4):
															if (sc4 in oldcard3):
																if (sc5 in oldcard5):
																	falsetrade = 0
																else:
																	falsetrade = 1
																	room.message(errormsg)
															elif (sc4 in oldcard5):
																if (sc5 in oldcard3):
																	falsetrade = 0
																else:
																	falsetrade = 1
																	room.message(errormsg)
															else:
																falsetrade = 1
																room.message(errormsg)
														elif (sc3 in oldcard5):
															if (sc4 in oldcard3):
																if (sc5 in oldcard4):
																	falsetrade = 0
																else:
																	falsetrade = 1
																	room.message(errormsg)
															elif (sc4 in oldcard4):
																if (sc5 in oldcard3):
																	falsetrade = 0
																else:
																	falsetrade = 1
																	room.message(errormsg)
															else:
																falsetrade = 1
																room.message(errormsg)
														else:
															falsetrade = 1
															room.message(errormsg)
													elif (sc2 in oldcard3):
														if (sc3 in oldcard1):
															if (sc4 in oldcard4):
																if (sc5 in oldcard5):
																	falsetrade = 0
																else:
																	falsetrade = 1
																	room.message(errormsg)
															elif (sc4 in oldcard5):
																if (sc5 in oldcard4):
																	falsetrade = 0
																else:
																	falsetrade = 1
																	room.message(errormsg)
															else:
																falsetrade = 1
																room.message(errormsg)
														elif (sc3 in oldcard4):
															if (sc4 in oldcard1):
																if (sc5 in oldcard5):
																	falsetrade = 0
																else:
																	falsetrade = 1
																	room.message(errormsg)
															elif (sc4 in oldcard5):
																if (sc5 in oldcard1):
																	falsetrade = 0
																else:
																	falsetrade = 1
																	room.message(errormsg)
															else:
																falsetrade = 1
																room.message(errormsg)
														elif (sc3 in oldcard5):
															if (sc4 in oldcard1):
																if (sc5 in oldcard4):
																	falsetrade = 0
																else:
																	falsetrade = 1
																	room.message(errormsg)
															elif (sc4 in oldcard4):
																if (sc5 in oldcard1):
																	falsetrade = 0
																else:
																	falsetrade = 1
																	room.message(errormsg)
															else:
																falsetrade = 1
																room.message(errormsg)
														else:
															falsetrade = 1
															room.message(errormsg)
													elif (sc2 in oldcard4):
														if (sc3 in oldcard1):
															if (sc4 in oldcard3):
																if (sc5 in oldcard5):
																	falsetrade = 0
																else:
																	falsetrade = 1
																	room.message(errormsg)
															elif (sc4 in oldcard5):
																if (sc5 in oldcard3):
																	falsetrade = 0
																else:
																	falsetrade = 1
																	room.message(errormsg)
															else:
																falsetrade = 1
																room.message(errormsg)
														elif (sc3 in oldcard3):
															if (sc4 in oldcard1):
																if (sc5 in oldcard5):
																	falsetrade = 0
																else:
																	falsetrade = 1
																	room.message(errormsg)
															elif (sc4 in oldcard5):
																if (sc5 in oldcard1):
																	falsetrade = 0
																else:
																	falsetrade = 1
																	room.message(errormsg)
															else:
																falsetrade = 1
																room.message(errormsg)
														elif (sc3 in oldcard5):
															if (sc4 in oldcard1):
																if (sc5 in oldcard3):
																	falsetrade = 0
																else:
																	falsetrade = 1
																	room.message(errormsg)
															elif (sc4 in oldcard3):
																if (sc5 in oldcard1):
																	falsetrade = 0
																else:
																	falsetrade = 1
																	room.message(errormsg)
															else:
																falsetrade = 1
																room.message(errormsg)
														else:
															falsetrade = 1
															room.message(errormsg)
													elif (sc2 in oldcard5):
														if (sc3 in oldcard1):
															if (sc4 in oldcard3):
																if (sc5 in oldcard4):
																	falsetrade = 0
																else:
																	falsetrade = 1
																	room.message(errormsg)
															elif (sc4 in oldcard4):
																if (sc5 in oldcard3):
																	falsetrade = 0
																else:
																	falsetrade = 1
																	room.message(errormsg)
															else:
																falsetrade = 1
																room.message(errormsg)
														elif (sc3 in oldcard3):
															if (sc4 in oldcard1):
																if (sc5 in oldcard4):
																	falsetrade = 0
																else:
																	falsetrade = 1
																	room.message(errormsg)
															elif (sc4 in oldcard4):
																if (sc5 in oldcard1):
																	falsetrade = 0
																else:
																	falsetrade = 1
																	room.message(errormsg)
															else:
																falsetrade = 1
																room.message(errormsg)
														elif (sc3 in oldcard4):
															if (sc4 in oldcard1):
																if (sc5 in oldcard3):
																	falsetrade = 0
																else:
																	falsetrade = 1
																	room.message(errormsg)
															elif (sc4 in oldcard3):
																if (sc5 in oldcard1):
																	falsetrade = 0
																else:
																	falsetrade = 1
																	room.message(errormsg)
															else:
																falsetrade = 1
																room.message(errormsg)
														else:
															falsetrade = 1
															room.message(errormsg)
													else:
														falsetrade = 1
														room.message(errormsg)
												elif (sc1 in oldcard3):
													if (sc2 in oldcard1):
														if (sc3 in oldcard2):
															if (sc4 in oldcard4):
																if (sc5 in oldcard5):
																	falsetrade = 0
																else:
																	falsetrade = 1
																	room.message(errormsg)
															elif (sc4 in oldcard5):
																if (sc5 in oldcard4):
																	falsetrade = 0
																else:
																	falsetrade = 1
																	room.message(errormsg)
															else:
																falsetrade = 1
																room.message(errormsg)
														elif (sc3 in oldcard4):
															if (sc4 in oldcard2):
																if (sc5 in oldcard5):
																	falsetrade = 0
																else:
																	falsetrade = 1
																	room.message(errormsg)
															elif (sc4 in oldcard5):
																if (sc5 in oldcard2):
																	falsetrade = 0
																else:
																	falsetrade = 1
																	room.message(errormsg)
															else:
																falsetrade = 1
																room.message(errormsg)
														elif (sc3 in oldcard5):
															if (sc4 in oldcard2):
																if (sc5 in oldcard4):
																	falsetrade = 0
																else:
																	falsetrade = 1
																	room.message(errormsg)
															elif (sc4 in oldcard4):
																if (sc5 in oldcard2):
																	falsetrade = 0
																else:
																	falsetrade = 1
																	room.message(errormsg)
															else:
																falsetrade = 1
																room.message(errormsg)
														else:
															falsetrade = 1
															room.message(errormsg)
													elif (sc2 in oldcard2):
														if (sc3 in oldcard1):
															if (sc4 in oldcard4):
																if (sc5 in oldcard5):
																	falsetrade = 0
																else:
																	falsetrade = 1
																	room.message(errormsg)
															elif (sc4 in oldcard5):
																if (sc5 in oldcard4):
																	falsetrade = 0
																else:
																	falsetrade = 1
																	room.message(errormsg)
															else:
																falsetrade = 1
																room.message(errormsg)
														elif (sc3 in oldcard4):
															if (sc4 in oldcard1):
																if (sc5 in oldcard5):
																	falsetrade = 0
																else:
																	falsetrade = 1
																	room.message(errormsg)
															elif (sc4 in oldcard5):
																if (sc5 in oldcard1):
																	falsetrade = 0

																else:
																	falsetrade = 1
																	room.message(errormsg)
															else:
																falsetrade = 1
																room.message(errormsg)
														elif (sc3 in oldcard5):
															if (sc4 in oldcard1):
																if (sc5 in oldcard4):
																	falsetrade = 0
																else:
																	falsetrade = 1
																	room.message(errormsg)
															elif (sc4 in oldcard4):
																if (sc5 in oldcard1):
																	falsetrade = 0
																else:
																	falsetrade = 1
																	room.message(errormsg)
															else:
																falsetrade = 1
																room.message(errormsg)
														else:
															falsetrade = 1
															room.message(errormsg)
													elif (sc2 in oldcard4):
														if (sc3 in oldcard1):
															if (sc4 in oldcard2):
																if (sc5 in oldcard5):
																	falsetrade = 0
																else:
																	falsetrade = 1
																	room.message(errormsg)
															elif (sc4 in oldcard5):
																if (sc5 in oldcard2):
																	falsetrade = 0
																else:
																	falsetrade = 1
																	room.message(errormsg)
															else:
																falsetrade = 1
																room.message(errormsg)
														elif (sc3 in oldcard2):
															if (sc4 in oldcard1):
																if (sc5 in oldcard5):
																	falsetrade = 0
																else:
																	falsetrade = 1
																	room.message(errormsg)
															elif (sc4 in oldcard5):
																if (sc5 in oldcard1):
																	falsetrade = 0
																else:
																	falsetrade = 1
																	room.message(errormsg)
															else:
																falsetrade = 1
																room.message(errormsg)
														elif (sc3 in oldcard5):
															if (sc4 in oldcard1):
																if (sc5 in oldcard2):
																	falsetrade = 0
																else:
																	falsetrade = 1
																	room.message(errormsg)
															elif (sc4 in oldcard2):
																if (sc5 in oldcard1):
																	falsetrade = 0
																else:
																	falsetrade = 1
																	room.message(errormsg)
															else:
																falsetrade = 1
																room.message(errormsg)
														else:
															falsetrade = 1
															room.message(errormsg)
													elif (sc2 in oldcard5):
														if (sc3 in oldcard1):
															if (sc4 in oldcard2):
																if (sc5 in oldcard4):
																	falsetrade = 0
																else:
																	falsetrade = 1
																	room.message(errormsg)
															elif (sc4 in oldcard4):
																if (sc5 in oldcard2):
																	falsetrade = 0
																else:
																	falsetrade = 1
																	room.message(errormsg)
															else:
																falsetrade = 1
																room.message(errormsg)
														elif (sc3 in oldcard2):
															if (sc4 in oldcard1):
																if (sc5 in oldcard4):
																	falsetrade = 0
																else:
																	falsetrade = 1
																	room.message(errormsg)
															elif (sc4 in oldcard4):
																if (sc5 in oldcard1):
																	falsetrade = 0
																else:
																	falsetrade = 1
																	room.message(errormsg)
															else:
																falsetrade = 1
																room.message(errormsg)
														elif (sc3 in oldcard4):
															if (sc4 in oldcard1):
																if (sc5 in oldcard2):
																	falsetrade = 0
																else:
																	falsetrade = 1
																	room.message(errormsg)
															elif (sc4 in oldcard2):
																if (sc5 in oldcard1):
																	falsetrade = 0
																else:
																	falsetrade = 1
																	room.message(errormsg)
															else:
																falsetrade = 1
																room.message(errormsg)
														else:
															falsetrade = 1
															room.message(errormsg)
													else:
														falsetrade = 1
														room.message(errormsg)
												elif (sc1 in oldcard4):
													if (sc2 in oldcard1):
														if (sc3 in oldcard2):
															if (sc4 in oldcard3):
																if (sc5 in oldcard5):
																	falsetrade = 0
																else:
																	falsetrade = 1
																	room.message(errormsg)
															elif (sc4 in oldcard5):
																if (sc5 in oldcard3):
																	falsetrade = 0
																else:
																	falsetrade = 1
																	room.message(errormsg)
															else:
																falsetrade = 1
																room.message(errormsg)
														elif (sc3 in oldcard3):
															if (sc4 in oldcard2):
																if (sc5 in oldcard5):
																	falsetrade = 0
																else:
																	falsetrade = 1
																	room.message(errormsg)
															elif (sc4 in oldcard5):
																if (sc5 in oldcard2):
																	falsetrade = 0
																else:
																	falsetrade = 1
																	room.message(errormsg)
															else:
																falsetrade = 1
																room.message(errormsg)
														elif (sc3 in oldcard5):
															if (sc4 in oldcard2):
																if (sc5 in oldcard3):
																	falsetrade = 0
																else:
																	falsetrade = 1
																	room.message(errormsg)
															elif (sc4 in oldcard3):
																if (sc5 in oldcard2):
																	falsetrade = 0
																else:
																	falsetrade = 1
																	room.message(errormsg)
															else:
																falsetrade = 1
																room.message(errormsg)
														else:
															falsetrade = 1
															room.message(errormsg)
													elif (sc2 in oldcard2):
														if (sc3 in oldcard1):
															if (sc4 in oldcard3):
																if (sc5 in oldcard5):
																	falsetrade = 0
																else:
																	falsetrade = 1
																	room.message(errormsg)
															elif (sc4 in oldcard5):
																if (sc5 in oldcard3):
																	falsetrade = 0
																else:
																	falsetrade = 1
																	room.message(errormsg)
															else:
																falsetrade = 1
																room.message(errormsg)
														elif (sc3 in oldcard3):
															if (sc4 in oldcard1):
																if (sc5 in oldcard5):
																	falsetrade = 0
																else:
																	falsetrade = 1
																	room.message(errormsg)
															elif (sc4 in oldcard5):
																if (sc5 in oldcard1):
																	falsetrade = 0
																else:
																	falsetrade = 1
																	room.message(errormsg)
															else:
																falsetrade = 1
																room.message(errormsg)
														elif (sc3 in oldcard5):
															if (sc4 in oldcard1):
																if (sc5 in oldcard3):
																	falsetrade = 0
																else:
																	falsetrade = 1
																	room.message(errormsg)
															elif (sc4 in oldcard3):
																if (sc5 in oldcard1):
																	falsetrade = 0
																else:
																	falsetrade = 1
																	room.message(errormsg)
															else:
																falsetrade = 1
																room.message(errormsg)
														else:
															falsetrade = 1
															room.message(errormsg)
													elif (sc2 in oldcard3):
														if (sc3 in oldcard1):
															if (sc4 in oldcard2):
																if (sc5 in oldcard5):
																	falsetrade = 0
																else:
																	falsetrade = 1
																	room.message(errormsg)
															elif (sc4 in oldcard5):
																if (sc5 in oldcard2):
																	falsetrade = 0
																else:
																	falsetrade = 1
																	room.message(errormsg)
															else:
																falsetrade = 1
																room.message(errormsg)
														elif (sc3 in oldcard2):
															if (sc4 in oldcard1):
																if (sc5 in oldcard5):
																	falsetrade = 0
																else:
																	falsetrade = 1
																	room.message(errormsg)
															elif (sc4 in oldcard5):
																if (sc5 in oldcard1):
																	falsetrade = 0
																else:
																	falsetrade = 1
																	room.message(errormsg)
															else:
																falsetrade = 1
																room.message(errormsg)
														elif (sc3 in oldcard5):
															if (sc4 in oldcard1):
																if (sc5 in oldcard2):
																	falsetrade = 0
																else:
																	falsetrade = 1
																	room.message(errormsg)
															elif (sc4 in oldcard2):
																if (sc5 in oldcard1):
																	falsetrade = 0
																else:
																	falsetrade = 1
																	room.message(errormsg)
															else:
																falsetrade = 1
																room.message(errormsg)
														else:
															falsetrade = 1
															room.message(errormsg)
													elif (sc2 in oldcard5):
														if (sc3 in oldcard1):
															if (sc4 in oldcard2):
																if (sc5 in oldcard3):
																	falsetrade = 0
																else:
																	falsetrade = 1
																	room.message(errormsg)
															elif (sc4 in oldcard3):
																if (sc5 in oldcard2):
																	falsetrade = 0
																else:
																	falsetrade = 1
																	room.message(errormsg)
															else:
																falsetrade = 1
																room.message(errormsg)
														elif (sc3 in oldcard2):
															if (sc4 in oldcard1):
																if (sc5 in oldcard3):
																	falsetrade = 0
																else:
																	falsetrade = 1
																	room.message(errormsg)
															elif (sc4 in oldcard3):
																if (sc5 in oldcard1):
																	falsetrade = 0
																else:
																	falsetrade = 1
																	room.message(errormsg)
															else:
																falsetrade = 1
																room.message(errormsg)
														elif (sc3 in oldcard3):
															if (sc4 in oldcard1):
																if (sc5 in oldcard2):
																	falsetrade = 0
																else:
																	falsetrade = 1
																	room.message(errormsg)
															elif (sc4 in oldcard2):
																if (sc5 in oldcard1):
																	falsetrade = 0
																else:
																	falsetrade = 1
																	room.message(errormsg)
															else:
																falsetrade = 1
																room.message(errormsg)
														else:
															falsetrade = 1
															room.message(errormsg)
													else:
														falsetrade = 1
														room.message(errormsg)
												elif (sc1 in oldcard5):
													if (sc2 in oldcard1):
														if (sc3 in oldcard2):
															if (sc4 in oldcard3):
																if (sc5 in oldcard4):
																	falsetrade = 0
																else:
																	falsetrade = 1
																	room.message(errormsg)
															elif (sc4 in oldcard4):
																if (sc5 in oldcard3):
																	falsetrade = 0
																else:
																	falsetrade = 1
																	room.message(errormsg)
															else:
																falsetrade = 1
																room.message(errormsg)
														elif (sc3 in oldcard3):
															if (sc4 in oldcard2):
																if (sc5 in oldcard4):
																	falsetrade = 0
																else:
																	falsetrade = 1
																	room.message(errormsg)
															elif (sc4 in oldcard4):
																if (sc5 in oldcard2):
																	falsetrade = 0

																else:
																	falsetrade = 1
																	room.message(errormsg)
															else:
																falsetrade = 1
																room.message(errormsg)
														elif (sc3 in oldcard4):
															if (sc4 in oldcard2):
																if (sc5 in oldcard3):
																	falsetrade = 0
																else:
																	falsetrade = 1
																	room.message(errormsg)
															elif (sc4 in oldcard3):
																if (sc5 in oldcard2):
																	falsetrade = 0
																else:
																	falsetrade = 1
																	room.message(errormsg)
															else:
																falsetrade = 1
																room.message(errormsg)
														else:
															falsetrade = 1
															room.message(errormsg)
													elif (sc2 in oldcard2):
														if (sc3 in oldcard1):
															if (sc4 in oldcard3):
																if (sc5 in oldcard4):
																	falsetrade = 0
																else:
																	falsetrade = 1
																	room.message(errormsg)
															elif (sc4 in oldcard4):
																if (sc5 in oldcard3):
																	falsetrade = 0
																else:
																	falsetrade = 1
																	room.message(errormsg)
															else:
																falsetrade = 1
																room.message(errormsg)
														elif (sc3 in oldcard3):
															if (sc4 in oldcard1):
																if (sc5 in oldcard4):
																	falsetrade = 0
																else:
																	falsetrade = 1
																	room.message(errormsg)
															elif (sc4 in oldcard4):
																if (sc5 in oldcard1):
																	falsetrade = 0
																else:
																	falsetrade = 1
																	room.message(errormsg)
															else:
																falsetrade = 1
																room.message(errormsg)
														elif (sc3 in oldcard4):
															if (sc4 in oldcard1):
																if (sc5 in oldcard3):
																	falsetrade = 0
																else:
																	falsetrade = 1
																	room.message(errormsg)
															elif (sc4 in oldcard3):
																if (sc5 in oldcard1):
																	falsetrade = 0
																else:
																	falsetrade = 1
																	room.message(errormsg)
															else:
																falsetrade = 1
																room.message(errormsg)
														else:
															falsetrade = 1
															room.message(errormsg)
													elif (sc2 in oldcard3):
														if (sc3 in oldcard1):
															if (sc4 in oldcard2):
																if (sc5 in oldcard4):
																	falsetrade = 0
																else:
																	falsetrade = 1
																	room.message(errormsg)
															elif (sc4 in oldcard4):
																if (sc5 in oldcard2):
																	falsetrade = 0
																else:
																	falsetrade = 1
																	room.message(errormsg)
															else:
																falsetrade = 1
																room.message(errormsg)
														elif (sc3 in oldcard2):
															if (sc4 in oldcard1):
																if (sc5 in oldcard4):
																	falsetrade = 0
																else:
																	falsetrade = 1
																	room.message(errormsg)
															elif (sc4 in oldcard4):
																if (sc5 in oldcard1):
																	falsetrade = 0
																else:
																	falsetrade = 1
																	room.message(errormsg)
															else:
																falsetrade = 1
																room.message(errormsg)
														elif (sc3 in oldcard4):
															if (sc4 in oldcard1):
																if (sc5 in oldcard2):
																	falsetrade = 0
																else:
																	falsetrade = 1
																	room.message(errormsg)
															elif (sc4 in oldcard2):
																if (sc5 in oldcard1):
																	falsetrade = 0
																else:
																	falsetrade = 1
																	room.message(errormsg)
															else:
																falsetrade = 1
																room.message(errormsg)
														else:
															falsetrade = 1
															room.message(errormsg)
													elif (sc2 in oldcard4):
														if (sc3 in oldcard1):
															if (sc4 in oldcard2):
																if (sc5 in oldcard3):
																	falsetrade = 0
																else:
																	falsetrade = 1
																	room.message(errormsg)
															elif (sc4 in oldcard3):
																if (sc5 in oldcard2):
																	falsetrade = 0
																else:
																	falsetrade = 1
																	room.message(errormsg)
															else:
																falsetrade = 1
																room.message(errormsg)
														elif (sc3 in oldcard2):
															if (sc4 in oldcard1):
																if (sc5 in oldcard3):
																	falsetrade = 0
																else:
																	falsetrade = 1
																	room.message(errormsg)
															elif (sc4 in oldcard3):
																if (sc5 in oldcard1):
																	falsetrade = 0
																else:
																	falsetrade = 1
																	room.message(errormsg)
															else:
																falsetrade = 1
																room.message(errormsg)
														elif (sc3 in oldcard3):
															if (sc4 in oldcard1):
																if (sc5 in oldcard2):
																	falsetrade = 0
																else:
																	falsetrade = 1
																	room.message(errormsg)
															elif (sc4 in oldcard2):
																if (sc5 in oldcard1):
																	falsetrade = 0
																else:
																	falsetrade = 1
																	room.message(errormsg)
															else:
																falsetrade = 1
																room.message(errormsg)
														else:
															falsetrade = 1
															room.message(errormsg)
													else:
														falsetrade = 1
														room.message(errormsg)
												else:
													falsetrade = 1
													room.message(errormsg)
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
																room.message(errormsg)
														elif (sc3 in oldcard4):
															if (sc4 in oldcard3):
																falsetrade = 0
															elif (sc4 in oldcard5):
																falsetrade = 0
															else:
																falsetrade = 1
																room.message(errormsg)
														elif (sc3 in oldcard5):
															if (sc4 in oldcard3):
																falsetrade = 0
															elif (sc4 in oldcard4):
																falsetrade = 0
															else:
																falsetrade = 1
																room.message(errormsg)
														else:
															falsetrade = 1
															room.message(errormsg)
													elif (sc2 in oldcard3):
														if (sc3 in oldcard2):
															if (sc4 in oldcard4):
																falsetrade = 0
															elif (sc4 in oldcard5):
																falsetrade = 0
															else:
																falsetrade = 1
																room.message(errormsg)
														elif (sc3 in oldcard4):
															if (sc4 in oldcard2):
																falsetrade = 0
															elif (sc4 in oldcard5):
																falsetrade = 0
															else:
																falsetrade = 1
																room.message(errormsg)
														elif (sc3 in oldcard5):
															if (sc4 in oldcard2):
																falsetrade = 0
															elif (sc4 in oldcard4):
																falsetrade = 0
															else:
																falsetrade = 1
																room.message(errormsg)
														else:
															falsetrade = 1
															room.message(errormsg)
													elif (sc2 in oldcard4):
														if (sc3 in oldcard2):
															if (sc4 in oldcard3):
																falsetrade = 0
															elif (sc4 in oldcard5):
																falsetrade = 0
															else:
																falsetrade = 1
																room.message(errormsg)
														elif (sc3 in oldcard3):
															if (sc4 in oldcard2):
																falsetrade = 0
															elif (sc4 in oldcard5):
																falsetrade = 0
															else:
																falsetrade = 1
																room.message(errormsg)
														elif (sc3 in oldcard5):
															if (sc4 in oldcard2):
																falsetrade = 0
															elif (sc4 in oldcard3):
																falsetrade = 0
															else:
																falsetrade = 1
																room.message(errormsg)
														else:
															falsetrade = 1
															room.message(errormsg)
													elif (sc2 in oldcard5):
														if (sc3 in oldcard2):
															if (sc4 in oldcard3):
																falsetrade = 0
															elif (sc4 in oldcard4):
																falsetrade = 0
															else:
																falsetrade = 1
																room.message(errormsg)
														elif (sc3 in oldcard3):
															if (sc4 in oldcard2):
																falsetrade = 0
															elif (sc4 in oldcard4):
																falsetrade = 0
															else:
																falsetrade = 1
																room.message(errormsg)
														elif (sc3 in oldcard4):
															if (sc4 in oldcard2):
																falsetrade = 0
															elif (sc4 in oldcard3):
																falsetrade = 0
															else:
																falsetrade = 1
																room.message(errormsg)
														else:
															falsetrade = 1
															room.message(errormsg)
													else:
														falsetrade = 1
														room.message(errormsg)
												elif (sc1 in oldcard2):
													if (sc2 in oldcard1):
														if (sc3 in oldcard3):
															if (sc4 in oldcard4):
																falsetrade = 0
															elif (sc4 in oldcard5):
																falsetrade = 0
															else:
																falsetrade = 1
																room.message(errormsg)
														elif (sc3 in oldcard4):
															if (sc4 in oldcard3):
																falsetrade = 0
															elif (sc4 in oldcard5):
																falsetrade = 0
															else:
																falsetrade = 1
																room.message(errormsg)
														elif (sc3 in oldcard5):
															if (sc4 in oldcard3):
																falsetrade = 0
															elif (sc4 in oldcard4):
																falsetrade = 0
															else:
																falsetrade = 1
																room.message(errormsg)
														else:
															falsetrade = 1
															room.message(errormsg)
													elif (sc2 in oldcard3):
														if (sc3 in oldcard1):
															if (sc4 in oldcard4):
																falsetrade = 0
															elif (sc4 in oldcard5):
																falsetrade = 0
															else:
																falsetrade = 1
																room.message(errormsg)
														elif (sc3 in oldcard4):
															if (sc4 in oldcard1):
																falsetrade = 0
															elif (sc4 in oldcard5):
																falsetrade = 0
															else:
																falsetrade = 1
																room.message(errormsg)
														elif (sc3 in oldcard5):
															if (sc4 in oldcard1):
																falsetrade = 0
															elif (sc4 in oldcard4):
																falsetrade = 0
															else:
																falsetrade = 1
																room.message(errormsg)
														else:
															falsetrade = 1
															room.message(errormsg)
													elif (sc2 in oldcard4):
														if (sc3 in oldcard1):
															if (sc4 in oldcard3):
																falsetrade = 0
															elif (sc4 in oldcard5):
																falsetrade = 0
															else:
																falsetrade = 1
																room.message(errormsg)
														elif (sc3 in oldcard3):
															if (sc4 in oldcard1):
																falsetrade = 0
															elif (sc4 in oldcard5):
																falsetrade = 0
															else:
																falsetrade = 1
																room.message(errormsg)
														elif (sc3 in oldcard5):
															if (sc4 in oldcard1):
																falsetrade = 0

															elif (sc4 in oldcard3):
																falsetrade = 0
															else:
																falsetrade = 1
																room.message(errormsg)
														else:
															falsetrade = 1
															room.message(errormsg)
													elif (sc2 in oldcard5):
														if (sc3 in oldcard1):
															if (sc4 in oldcard3):
																falsetrade = 0
															elif (sc4 in oldcard4):
																falsetrade = 0
															else:
																falsetrade = 1
																room.message(errormsg)
														elif (sc3 in oldcard3):
															if (sc4 in oldcard1):
																falsetrade = 0
															elif (sc4 in oldcard4):
																falsetrade = 0
															else:
																falsetrade = 1
																room.message(errormsg)
														elif (sc3 in oldcard4):
															if (sc4 in oldcard1):
																falsetrade = 0
															elif (sc4 in oldcard3):
																falsetrade = 0
															else:
																falsetrade = 1
																room.message(errormsg)
														else:
															falsetrade = 1
															room.message(errormsg)
													else:
														falsetrade = 1
														room.message(errormsg)
												elif (sc1 in oldcard3):
													if (sc2 in oldcard1):
														if (sc3 in oldcard2):
															if (sc4 in oldcard4):
																falsetrade = 0
															elif (sc4 in oldcard5):
																falsetrade = 0
															else:
																falsetrade = 1
																room.message(errormsg)
														elif (sc3 in oldcard4):
															if (sc4 in oldcard2):
																falsetrade = 0
															elif (sc4 in oldcard5):
																falsetrade = 0
															else:
																falsetrade = 1
																room.message(errormsg)
														elif (sc3 in oldcard5):
															if (sc4 in oldcard2):
																falsetrade = 0
															elif (sc4 in oldcard4):
																falsetrade = 0
															else:
																falsetrade = 1
																room.message(errormsg)
														else:
															falsetrade = 1
															room.message(errormsg)
													elif (sc2 in oldcard2):
														if (sc3 in oldcard1):
															if (sc4 in oldcard4):
																falsetrade = 0
															elif (sc4 in oldcard5):
																falsetrade = 0
															else:
																falsetrade = 1
																room.message(errormsg)
														elif (sc3 in oldcard4):
															if (sc4 in oldcard1):
																falsetrade = 0
															elif (sc4 in oldcard5):
																falsetrade = 0
															else:
																falsetrade = 1
																room.message(errormsg)
														elif (sc3 in oldcard5):
															if (sc4 in oldcard1):
																falsetrade = 0
															elif (sc4 in oldcard4):
																falsetrade = 0
															else:
																falsetrade = 1
																room.message(errormsg)
														else:
															falsetrade = 1
															room.message(errormsg)
													elif (sc2 in oldcard4):
														if (sc3 in oldcard1):
															if (sc4 in oldcard2):
																falsetrade = 0
															elif (sc4 in oldcard5):
																falsetrade = 0
															else:
																falsetrade = 1
																room.message(errormsg)
														elif (sc3 in oldcard2):
															if (sc4 in oldcard1):
																falsetrade = 0
															elif (sc4 in oldcard5):
																falsetrade = 0
															else:
																falsetrade = 1
																room.message(errormsg)
														elif (sc3 in oldcard5):
															if (sc4 in oldcard1):
																falsetrade = 0
															elif (sc4 in oldcard2):
																falsetrade = 0
															else:
																falsetrade = 1
																room.message(errormsg)
														else:
															falsetrade = 1
															room.message(errormsg)
													elif (sc2 in oldcard5):
														if (sc3 in oldcard1):
															if (sc4 in oldcard2):
																falsetrade = 0
															elif (sc4 in oldcard4):
																falsetrade = 0
															else:
																falsetrade = 1
																room.message(errormsg)
														elif (sc3 in oldcard2):
															if (sc4 in oldcard1):
																falsetrade = 0
															elif (sc4 in oldcard4):
																falsetrade = 0
															else:
																falsetrade = 1
																room.message(errormsg)
														elif (sc3 in oldcard4):
															if (sc4 in oldcard1):
																falsetrade = 0
															elif (sc4 in oldcard2):
																falsetrade = 0
															else:
																falsetrade = 1
																room.message(errormsg)
														else:
															falsetrade = 1
															room.message(errormsg)
													else:
														falsetrade = 1
														room.message(errormsg)
												elif (sc1 in oldcard4):
													if (sc2 in oldcard1):
														if (sc3 in oldcard2):
															if (sc4 in oldcard3):
																falsetrade = 0
															elif (sc4 in oldcard5):
																falsetrade = 0
															else:
																falsetrade = 1
																room.message(errormsg)
														elif (sc3 in oldcard3):
															if (sc4 in oldcard2):
																falsetrade = 0
															elif (sc4 in oldcard5):
																falsetrade = 0
															else:
																falsetrade = 1
																room.message(errormsg)
														elif (sc3 in oldcard5):
															if (sc4 in oldcard2):
																falsetrade = 0
															elif (sc4 in oldcard3):
																falsetrade = 0
															else:
																falsetrade = 1
																room.message(errormsg)
														else:
															falsetrade = 1
															room.message(errormsg)
													elif (sc2 in oldcard2):
														if (sc3 in oldcard1):
															if (sc4 in oldcard3):
																falsetrade = 0
															elif (sc4 in oldcard5):
																falsetrade = 0
															else:
																falsetrade = 1
																room.message(errormsg)
														elif (sc3 in oldcard3):
															if (sc4 in oldcard1):
																falsetrade = 0
															elif (sc4 in oldcard5):
																falsetrade = 0
															else:
																falsetrade = 1
																room.message(errormsg)
														elif (sc3 in oldcard5):
															if (sc4 in oldcard1):
																falsetrade = 0
															elif (sc4 in oldcard3):
																falsetrade = 0
															else:
																falsetrade = 1
																room.message(errormsg)
														else:
															falsetrade = 1
															room.message(errormsg)
													elif (sc2 in oldcard3):
														if (sc3 in oldcard1):
															if (sc4 in oldcard2):
																falsetrade = 0
															elif (sc4 in oldcard5):
																falsetrade = 0
															else:
																falsetrade = 1
																room.message(errormsg)
														elif (sc3 in oldcard2):
															if (sc4 in oldcard1):
																falsetrade = 0
															elif (sc4 in oldcard5):
																falsetrade = 0
															else:
																falsetrade = 1
																room.message(errormsg)
														elif (sc3 in oldcard5):
															if (sc4 in oldcard1):
																falsetrade = 0
															elif (sc4 in oldcard2):
																falsetrade = 0
															else:
																falsetrade = 1
																room.message(errormsg)
														else:
															falsetrade = 1
															room.message(errormsg)
													elif (sc2 in oldcard5):
														if (sc3 in oldcard1):
															if (sc4 in oldcard2):
																falsetrade = 0
															elif (sc4 in oldcard3):
																falsetrade = 0
															else:
																falsetrade = 1
																room.message(errormsg)
														elif (sc3 in oldcard2):
															if (sc4 in oldcard1):
																falsetrade = 0
															elif (sc4 in oldcard3):
																falsetrade = 0
															else:
																falsetrade = 1
																room.message(errormsg)
														elif (sc3 in oldcard3):
															if (sc4 in oldcard1):
																falsetrade = 0
															elif (sc4 in oldcard2):
																falsetrade = 0
															else:
																falsetrade = 1
																room.message(errormsg)
														else:
															falsetrade = 1
															room.message(errormsg)
													else:
														falsetrade = 1
														room.message(errormsg)
												elif (sc1 in oldcard5):
													if (sc2 in oldcard1):
														if (sc3 in oldcard2):
															if (sc4 in oldcard3):
																falsetrade = 0
															elif (sc4 in oldcard4):
																falsetrade = 0
															else:
																falsetrade = 1
																room.message(errormsg)
														elif (sc3 in oldcard3):
															if (sc4 in oldcard2):
																falsetrade = 0
															elif (sc4 in oldcard4):
																falsetrade = 0
															else:
																falsetrade = 1
																room.message(errormsg)
														elif (sc3 in oldcard4):
															if (sc4 in oldcard2):
																falsetrade = 0
															elif (sc4 in oldcard3):
																falsetrade = 0
															else:
																falsetrade = 1
																room.message(errormsg)
														else:
															falsetrade = 1
															room.message(errormsg)
													elif (sc2 in oldcard2):
														if (sc3 in oldcard1):
															if (sc4 in oldcard3):
																falsetrade = 0
															elif (sc4 in oldcard4):
																falsetrade = 0
															else:
																falsetrade = 1
																room.message(errormsg)
														elif (sc3 in oldcard3):
															if (sc4 in oldcard1):
																falsetrade = 0
															elif (sc4 in oldcard4):
																falsetrade = 0
															else:
																falsetrade = 1
																room.message(errormsg)
														elif (sc3 in oldcard4):
															if (sc4 in oldcard1):
																falsetrade = 0
															elif (sc4 in oldcard3):
																falsetrade = 0
															else:
																falsetrade = 1
																room.message(errormsg)
														else:
															falsetrade = 1
															room.message(errormsg)
													elif (sc2 in oldcard3):
														if (sc3 in oldcard1):
															if (sc4 in oldcard2):
																falsetrade = 0
															elif (sc4 in oldcard4):
																falsetrade = 0
															else:
																falsetrade = 1
																room.message(errormsg)
														elif (sc3 in oldcard2):
															if (sc4 in oldcard1):
																falsetrade = 0
															elif (sc4 in oldcard4):
																falsetrade = 0
															else:
																falsetrade = 1
																room.message(errormsg)
														elif (sc3 in oldcard4):
															if (sc4 in oldcard1):
																falsetrade = 0
															elif (sc4 in oldcard2):
																falsetrade = 0
															else:
																falsetrade = 1
																room.message(errormsg)
														else:
															falsetrade = 1
															room.message(errormsg)
													elif (sc2 in oldcard4):
														if (sc3 in oldcard1):
															if (sc4 in oldcard2):
																falsetrade = 0
															elif (sc4 in oldcard3):
																falsetrade = 0
															else:
																falsetrade = 1
																room.message(errormsg)
														elif (sc3 in oldcard2):
															if (sc4 in oldcard1):
																falsetrade = 0
															elif (sc4 in oldcard3):
																falsetrade = 0
															else:
																falsetrade = 1
																room.message(errormsg)
														elif (sc3 in oldcard3):
															if (sc4 in oldcard1):
																falsetrade = 0
															elif (sc4 in oldcard2):
																falsetrade = 0
															else:
																falsetrade = 1
																room.message(errormsg)
														else:
															falsetrade = 1
															room.message(errormsg)
													else:
														falsetrade = 1
														room.message(errormsg)
												else:
													falsetrade = 1
													room.message(errormsg)
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
															room.message(errormsg)
													elif (sc2 in oldcard3):
														if (sc3 in oldcard2):
															falsetrade = 0
														elif (sc3 in oldcard4):
															falsetrade = 0
														elif (sc3 in oldcard5):
															falsetrade = 0
														else:
															falsetrade = 1
															room.message(errormsg)
													elif (sc2 in oldcard4):
														if (sc3 in oldcard2):
															falsetrade = 0
														elif (sc3 in oldcard3):
															falsetrade = 0
														elif (sc3 in oldcard5):
															falsetrade = 0
														else:
															falsetrade = 1
															room.message(errormsg)
													elif (sc2 in oldcard5):
														if (sc3 in oldcard2):
															falsetrade = 0
														elif (sc3 in oldcard3):
															falsetrade = 0
														elif (sc3 in oldcard4):
															falsetrade = 0
														else:
															falsetrade = 1
															room.message(errormsg)
													else:
														falsetrade = 1
														room.message(errormsg)
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
															room.message(errormsg)
													elif (sc2 in oldcard3):
														if (sc3 in oldcard1):
															falsetrade = 0
														elif (sc3 in oldcard4):
															falsetrade = 0
														elif (sc3 in oldcard5):
															falsetrade = 0
														else:
															falsetrade = 1
															room.message(errormsg)
													elif (sc2 in oldcard4):
														if (sc3 in oldcard1):
															falsetrade = 0
														elif (sc3 in oldcard3):
															falsetrade = 0
														elif (sc3 in oldcard5):
															falsetrade = 0
														else:
															falsetrade = 1
															room.message(errormsg)
													elif (sc2 in oldcard5):
														if (sc3 in oldcard1):
															falsetrade = 0
														elif (sc3 in oldcard3):
															falsetrade = 0
														elif (sc3 in oldcard4):
															falsetrade = 0
														else:
															falsetrade = 1
															room.message(errormsg)
													else:
														falsetrade = 1
														room.message(errormsg)
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
															room.message(errormsg)
													elif (sc2 in oldcard2):
														if (sc3 in oldcard1):
															falsetrade = 0
														elif (sc3 in oldcard4):
																falsetrade = 0
														elif (sc3 in oldcard5):
															falsetrade = 0
														else:
															falsetrade = 1
															room.message(errormsg)
													elif (sc2 in oldcard4):
														if (sc3 in oldcard1):
															falsetrade = 0
														elif (sc3 in oldcard2):
															falsetrade = 0
														elif (sc3 in oldcard5):
															falsetrade = 0
														else:
															falsetrade = 1
															room.message(errormsg)
													elif (sc2 in oldcard5):
														if (sc3 in oldcard1):
															falsetrade = 0
														elif (sc3 in oldcard2):
															falsetrade = 0
														elif (sc3 in oldcard4):
															falsetrade = 0
														else:
															falsetrade = 1
															room.message(errormsg)
													else:
														falsetrade = 1
														room.message(errormsg)
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
															room.message(errormsg)
													elif (sc2 in oldcard2):
														if (sc3 in oldcard1):
															falsetrade = 0
														elif (sc3 in oldcard3):
															falsetrade = 0
														elif (sc3 in oldcard5):
															falsetrade = 0
														else:
															falsetrade = 1
															room.message(errormsg)
													elif (sc2 in oldcard3):
														if (sc3 in oldcard1):
															falsetrade = 0
														elif (sc3 in oldcard2):
															falsetrade = 0
														elif (sc3 in oldcard5):
															falsetrade = 0
														else:
															falsetrade = 1
															room.message(errormsg)
													elif (sc2 in oldcard5):
														if (sc3 in oldcard1):
															falsetrade = 0
														elif (sc3 in oldcard2):
															falsetrade = 0
														elif (sc3 in oldcard3):
															falsetrade = 0
														else:
															falsetrade = 1
															room.message(errormsg)
													else:
														falsetrade = 1
														room.message(errormsg)
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
															room.message(errormsg)
													elif (sc2 in oldcard2):
														if (sc3 in oldcard1):
															falsetrade = 0
														elif (sc3 in oldcard3):
															falsetrade = 0
														elif (sc3 in oldcard4):
															falsetrade = 0
														else:
															falsetrade = 1
															room.message(errormsg)
													elif (sc2 in oldcard3):
														if (sc3 in oldcard1):
															falsetrade = 0
														elif (sc3 in oldcard2):
															falsetrade = 0
														elif (sc3 in oldcard4):
															falsetrade = 0
														else:
															falsetrade = 1
															room.message(errormsg)	
													elif (sc2 in oldcard4):
														if (sc3 in oldcard1):
															falsetrade = 0
														elif (sc3 in oldcard2):
															falsetrade = 0
														elif (sc3 in oldcard3):
															falsetrade = 0
														else:
															falsetrade = 1
															room.message(errormsg)
													else:
														falsetrade = 1
														room.message(errormsg)
												else:
													falsetrade = 1
													room.message(errormsg)
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
														room.message(errormsg)
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
														room.message(errormsg)
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
														room.message(errormsg)
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
														room.message(errormsg)
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
														room.message(errormsg)
												else:
													falsetrade = 1
													room.message(errormsg)
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
													room.message(errormsg)
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
												wrtnewcd = open("data/poker/" + room.name + ".txt","w")
												wrtnewcd.write(gsetnewcd)
												wrtnewcd.close()
												rgsetr.close()
												gsetr = open("data/poker/" + room.name + ".txt","r")
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
												wrtdata2 = open(("data/poker/" + room.name + ".txt"), "w")
												wrtdata2.write(gsetnewnc5 + '\n*$!$@#($*!' + user.name + ' has traded!$#@(%*!%!\n')
												glistr.close()
												gsetr.close()
												wrtdata2.close()
												gsetfr = open("data/poker/" + room.name + ".txt","r")
												gsetf = (gsetfr.read()).lower()
												if tradestatusi > 0:
													(self._pm).message(user, str("Your new cards for [" + room.name + "] are: " + newcard1 + ", " + newcard2 + ", " + newcard3 + ", " + newcard4 + ", " + newcard5 + "."))
													room.message("I have PMed you your new cards.")
												elif tradestatusi == 0:
													room.message(str("Your new cards for [" + room.name.upper() + "] are: " + newcard1 + ", " + newcard2 + ", " + newcard3 + ", " + newcard4 + ", " + newcard5 + "."))
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
															room.message(victorw.capitalize() + " wins the match! With the cards: " + vhandstrr)
															gsetfr.close()
															wrtset1 = open("data/poker/pgp.txt", "w")
															wrtset1.write(pokerallcards)
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
															room.message(victorw.capitalize() + " wins the match! With the cards: " + vhandstrr)
															gsetfr.close()
															wrtset1 = open("data/poker/pgp.txt", "w")
															wrtset1.write(pokerallcards)
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
																room.message(victorw.capitalize() + " wins the match! With the cards: " + vhandstrr)
																gsetfr.close()
																wrtset1 = open("data/poker/pgp.txt", "w")
																wrtset1.write(pokerallcards)
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
																room.message(victorw.capitalize() + " wins the match! With the cards: " + vhandstrr)
																gsetfr.close()
																wrtset1 = open("data/poker/pgp.txt", "w")
																wrtset1.write(pokerallcards)
																wrtset1.close()
															elif (pointshp2 == pointshp1):
																room.message("It's a draw!")
																gsetfr.close()
																wrtset1 = open("data/poker/pgp.txt", "w")
																wrtset1.write(pokerallcards)
																wrtset1.close()
					elif (cmd.lower()) == "lotto":
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
					elif ( (cmd.lower() == "rd" ) or (cmd.lower() == "reddit") ):
						if usrlvl > 0:
							#import urllib.request
							def reddit():
								try:
									search = "http://www.reddit.com/r/all/"
									a = urlreq.urlopen(search)
									if a:
										b = str(a.read())
										d = "i.imgur.com/"
										if d:
											e = b.find(d, 0)
											result = b[e:e+21]
											end = "http://" + result
											return end
										else:
											return "nope"
									else:
										return "nope"
								except:
									print ';reddit fail'
							redditsec = reddit()
							if redditsec == "nope":
								room.message("I don't see any images on the front page.")
							else:
								room.message('<a href="' + redditsec + '" target="_blank">Click here if the image fails to load</a><br/>' + redditsec, html = True)
					elif (cmd.lower()) == "dance":
						rdance = random.choice([dancemoves1, dancemoves2])
						time.sleep(1)
						for i, msg in enumerate(rdance):
							self.setTimeout(i / 2, room.message, msg)
					elif (cmd.lower() == "xkcd"):
						def rfinish(doc):
							doc = doc.read().decode()
							m = re.search('<div id="comic">(.*?)<img src="(.*?)" title="(.*?)" alt="', doc, re.DOTALL | re.IGNORECASE)
							if m:
								out = '<b>%s</b><br/>%s' %(m.group(3), m.group(2))
								room.message(out, html = True)
							else:
								room.message("Error, does not compute.")
						searchurl = "http://dynamic.xkcd.com/random/comic/"
						self.deferToThread(rfinish, urlreq.urlopen, searchurl)
					elif ( (cmd.lower() == "c&h" ) or (cmd.lower() == "ch") or (cmd.lower() == "cyanideandhappiness") or (cmd.lower() == "cyanide") or (cmd.lower() == "cah")):
						def rfinish(doc):
							doc = doc.read().decode()
							m = re.search('<img alt="Cyanide and Happiness, a daily webcomic" src="(.*?)">', doc, re.DOTALL | re.IGNORECASE)
							if m:
								out = '<b>Cyanide and Happiness</b><br/>%s' %(m.group(1))
								room.message(out, html = True)
							else:
								room.message("Error, does not compute.")
						searchurl = "http://www.explosm.net/comics/random/"
						self.deferToThread(rfinish, urlreq.urlopen, searchurl)
					elif ( (cmd.lower() == "comic" ) or (cmd.lower() == "comics") or (cmd.lower() == "randomcomic")):
						comic = random.choice(['cyanide', 'xkcd'])
						if comic == 'cyanide':
							def rfinish(doc):
								doc = doc.read().decode()
								m = re.search('<img alt="Cyanide and Happiness, a daily webcomic" src="(.*?)">', doc, re.DOTALL | re.IGNORECASE)
								if m:
									out = '<b><font color="#FF0000">Cyanide and Happiness</font></b><br/>%s' %(m.group(1))
									room.message(out, html = True)
								else:
									room.message("Error, does not compute.")
							searchurl = "http://www.explosm.net/comics/random/"
							self.deferToThread(rfinish, urlreq.urlopen, searchurl)
						elif comic == 'xkcd':
							def rfinish(doc):
								doc = doc.read().decode()
								m = re.search('<div id="comic">(.*?)<img src="(.*?)" title="(.*?)" alt="', doc, re.DOTALL | re.IGNORECASE)
								if m:
									out = '<b><font color="#FF0000">XKCD</font><br/>%s</b><br/>%s' %(m.group(3), m.group(2))
									room.message(out, html = True)
								else:
									room.message("Error, does not compute.")
							searchurl = "http://dynamic.xkcd.com/random/comic/"
							self.deferToThread(rfinish, urlreq.urlopen, searchurl)
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
						room.message(rball)
					elif (cmd.lower()) == "wsid":
						action = random.choice(["Killing floor.", "Minecraft.", "Borderlands.", "Team Fortress 2.", "Frozen Synapse.", "Dungeon Defenders.", "Counter-Strike.", "Work on me instead.", "Do school work instead.", "Get something to eat then ask again.", "Watch a movie instead."])
						room.message(action)
					elif ( (cmd.lower() == "derrick") or (cmd.lower() == "derrickcomedy")):
						video = random.choice(['poEo6So0knU', 'fKXk1VhAuvE', 'Z0e2mrUmBkA', 'xdfMu77sYH4', 'K4nqXL0T6GE', 'q2eP2764CVc', 'hMxEe2gnaQY', 'nxx1vOhlqmM', 'J07UBlBeYPo', 'xJyelcnINH0', 'DeozyEvJtyQ', '4rSoOW93GTs', 'uzHYgYniGYs', 'gyUsta9mzcY', '0hm7pp_JFOs', 'e9G7sPt3HfM', 'bcZpa55_mfY', 'zJXVj8JC1Po', 'OMrdAr7fNjo', 'f67_og3v_Ow', 'EY0DfFlzcBk', 'MY4kFSuMvKM', 'gIF0UCFd3FM', 'Rcx4_CszaDI', '2REG3-Wb5gM', 'WIGrIfIj6aY', 'wnV0IENYPGg', 'HRfRLPHk44w', 'X74_Z3qKkNw', 'G2nTbqbtGug', 'PWrMyqX_MNM', 'FiFKS62wQAA', '3zvTRQr7ns8', 'oQp7Id8iRA4', 'LLJCMzBiqh0', '3hWnA2dgE-M', 'g2YfUo1H4bg', '-Bc0mG5omTo', 'ax3hmhHScc0', 'CxPE5bqcoLU', 'YNYlc8I5tqU', 't94LtCvP9ck', 'VODGqrnnuGk'])
						vres = 'http://www.youtube.com/watch?v=' + str(video)
						room.message(vres)
					elif (cmd.lower()) == "hug":
						rhug = random.choice([hugs, hugs2, hugs3, hugs4, hugs5, hugs6])
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
					elif ( (cmd.lower() == "def" ) or (cmd.lower() == "define")):
						reddata = open("data/cmdother/dictionary.txt","r")
						reddata2 = (reddata.read()).lower()
						if args.find(" as ") != -1: #if there's a colon somewhere
							if ("-$*@!!*^$#" in args):
								room.message("You have been flagged for attempting to abuse the system.")
								flaggedusr = open("data/cmdother/flaglist.txt","a")
								flaggedusr.write('\n' + user.name)
								flaggedusr.close()
							elif (".#$@*!" in args):
								room.message("You have been flagged for attempting to abuse the system.")
								flaggedusr = open("data/cmdother/.txt","a")
								flaggedusr.write('\n' + user.name)
								flaggedusr.close()
							elif ("@!^&**#!" in args):
								room.message("You have been flagged for attempting to abuse the system.")
								flaggedusr = open("data/cmdother/flaglist.txt","a")
								flaggedusr.write('\n' + user.name)
								flaggedusr.close()
							else:
								argsadj = args.lower()
								word, definitionr = argsadj.split(" as ", 1)
								if (word + "-$*@!!*^$#") in reddata2:
									room.message(word + " is already defined.")
								else:
									definitionh = definitionr.replace('defined by', '')
									definition = definitionh.replace('~', '')
									wrtdata = open("data/cmdother/dictionary.txt","a")
									room.message(word + ": " + definition)
									wrtdata.write(str((word + '-$*@!!*^$# ' + definition + '  ~ defined by ' + user.name + '.#$@*!' + word + '@!^&**#!').encode('utf-8')) + '\n')
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
								room.message(word + " has not been defined yet.")
						reddata.close()
		elif ((usrlvl >= 1) and (("#@@$!!(!*@" + room.name + "@@#$&*(**!") in aimode)):
							if ( ( (msgbody.lower().startswith("why") or msgbody.lower().startswith("t6 why") or msgbody.lower().startswith("t6ru why") or msgbody.lower().startswith("t6ru, why")) and "?" in msgbody.lower()) and ('t6' in msgbody.lower())):
								if focususrst in usage:
									rpusager = open("data/usage/usage.txt","r")
									rpusage = (rpusager.read()).lower()
									rpusager.close()
									indexsrp = usage.find(focususred)
									indexerp = usage.find(relapointid)
									rawoutrp = usage[(int(indexsrp)):(int(indexerp))]
									relationpr = rawoutrp.replace(focususred, '')
									relationp = int(relationpr)
								else:
									relationpr = '0'
									relationp = 0
								if relationp > 40:
										hateres = random.choice(["Because I love you!", "I'm not sure", "I don't know, tigers?", "Ummm...Because I'm awesome?", "...Yes?", "...No?", "If I told you I would have to kill you.", "Because fruit is yummy.", "Spaaaaaaaace.", "Fuck if I know."]) 
										def out():
											room.message(hateres)
										mdelay = Timer(3.0, out)
										mdelay.start()
										relationp = relationp + 0
								elif relationp < 0:
									rdhugout = random.choice(["Fuck off, scumbag.", "Screw you", "What is wrong with you?", "I don't want anything to do with you or your abuse.", "Because you are a horrible person!", "I don't know, and even if I did I wouldn't tell you!", "Probably because I hate you.", "Probably because I hate you.", "More like why haven't you killed yourself yet, amirite?", "If I told you I would have to kill you... On second thought, can I kill you anyway?", "...Yes?", "...No?", "Because fruit is yummy.", "Spaaaaaaaace.", "Fuck if I know."])
									def out():
										room.message(rdhugout)
									mdelay = Timer(3.0, out)
									mdelay.start()
									relationp = relationp + 0
								else:
									hateres = random.choice(["I'm not sure", "I don't know, tigers?", "Ummm...Because I'm awesome?", "...Yes?", "...No?", "If I told you I would have to kill you.", "Because fruit is yummy.", "Spaaaaaaaace.", "Fuck if I know."]) 
									def out():
										room.message(hateres)
									mdelay = Timer(3.0, out)
									mdelay.start()
									relationp = relationp + 0
								usager = open("data/usage/usage.txt","r")
								usage = (usager.read()).lower()
								if focususrst in usage:
									indexs = usage.find(focususrst)
									indexe = usage.find(relapointid)
									rawout = usage[(int(indexs)):(int(indexe))]
									newdatar = str(usage).replace((rawout + relapointid), (focususrst + nowfc + usredtime + bodywrt + focususred + str(relationp) + relapointid))
									newdata = str(newdatar.encode('utf-8')).replace("\\n", "\n")\
										.replace("b'", "")\
										.replace('b"', "")\
										.replace("\'", "")\
										.replace('\"', "")\
										.replace("\\\\", "")
									wrtdata = open("data/usage/usage.txt","w")
									wrtdata.write(newdata)
									wrtdata.close()
									usager.close()
								else:
									wrtdata = open("data/usage/usage.txt","a")
									wrtdata.write(str((focususrst + nowfc + usredtime + bodywrt + focususred + '0' + relapointid).encode('utf-8')) + '\n')
									wrtdata.close()
									usager.close()
							elif ( ( (msgbody.lower().startswith("what") or msgbody.lower().startswith("t6 what") or msgbody.lower().startswith("t6ru what") or msgbody.lower().startswith("t6ru, what") or msgbody.lower().startswith("t6, what")or msgbody.lower().startswith("t6 t6, what") or msgbody.lower().startswith("t6 t6ru what") or msgbody.lower().startswith("t6 t6ru, what") or msgbody.lower().startswith("t6 t6, what"))) and ('t6' in msgbody.lower())):
								if ("?" in msgbody):
									if focususrst in usage:
										rpusager = open("data/usage/usage.txt","r")
										rpusage = (rpusager.read()).lower()
										rpusager.close()
										indexsrp = usage.find(focususred)
										indexerp = usage.find(relapointid)
										rawoutrp = usage[(int(indexsrp)):(int(indexerp))]
										relationpr = rawoutrp.replace(focususred, '')
										relationp = int(relationpr)
									else:
										relationpr = '0'
										relationp = 0
									inqury = msgbody.lower().replace(", t6ru", "")\
										.replace("t6ru", "")\
										.replace(", t6", "")\
										.replace("t6", "")\
										.replace("?", "")
									if ("what is the " in msgbody.lower()):
										qstart, wordr = inqury.split("what is the ", 1)
									elif ("what is a " in inqury):
										qstart, wordr = inqury.split("what is a ", 1)
									elif ("what is " in inqury):
										qstart, wordr = inqury.split("what is ", 1)
									elif ("what " in inqury):
										qstart, wordr = inqury.split("what ", 1)
									else:
										qstart, wordr = inqury.split("what", 1)
									if (("1" in inqury) or ("2" in inqury) or ("3" in inqury) or ("4" in inqury) or ("5" in inqury) or ("6" in inqury) or ("7" in inqury) or ("8" in inqury) or ("9" in inqury) or ("0" in inqury)):
											word = wordr\
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
												try:
													doc = doc.read().decode()
													l = re.search('context.jsonArray.popups.pod_0200.push(.*?)"stringified": "(.*?)","mInput"', doc, re.DOTALL | re.IGNORECASE)
													m =re.search('context.jsonArray.popups.pod_0100.push(.*?){"stringified": "(.*?)","mInput":', doc, re.DOTALL | re.IGNORECASE)
													if l and m:
														room.message((wordr + " = %s" %(l.group(2))).replace("\/","/"))
													elif m:
														room.message(("%s" %(m.group(2))).replace("\/","/"))
													else:
														room.message("I have no idea what I am doing.")
												except:
													print 'error with what'
													room.message("I don't have a clue. I also don't have more than a clue. I have 0 clues, no clue.")
											self.deferToThread(rfinish, urlreq.urlopen, "http://www.wolframalpha.com/input/?i=" + word)
									elif ("what is love" in inqury):
										room.message("Baby don't hurt me, don't hurt me no more!")
									else:
											word = wordr\
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
											print word
											def rfinish(doc):
												try:
													doc = doc.read()
													m = re.search('content":"(.*?)"},', doc, re.DOTALL | re.IGNORECASE)
													if m:
														rawout1 = '%s' %(m.group(1))
														rawout2 = rawout1.replace('\\u003c/b\\u003e', "")
														rawout3 = rawout2.replace('  ', " ")
														rawout4 = rawout3.replace("\\u003cb\\u003e", "")
														rawout5 = rawout4.replace("\u0026#39;", "'")\
															.replace('\u0026amp;', "")\
															.replace('\u003d', "")
														out = rawout5.capitalize()
														room.message(out, html = True)
													else:
														room.message("I have no idea what I am doing.")
												except:
													print 'error with what'
													room.message("I don't have a clue. I also don't have more than a clue. I have 0 clues, no clue.")
											searchurl = "https://ajax.googleapis.com/ajax/services/search/web?v=1.0&q=" + word
											self.deferToThread(rfinish, urlreq.urlopen, searchurl)
	#								else:
	#									if relationp > 40:
	#										hateres = random.choice(["I'm not sure", "I don't know, tigers?", "...Yes?", "...No?", "If I told you I would have to kill you.", "Spaaaaaaaace.", "Fuck if I know.", "To procreate, preferably with me.", "Idk, give me gifts?", "How rude!"]) 
	#										def out():
	#											room.message(hateres)
	#										mdelay = Timer(3.0, out)
	#										mdelay.start()
	#										relationp = relationp + 0
	#									elif relationp < 0:
	#										rdhugout = random.choice(["Fuck off, scumbag.", "Screw you", "What is wrong with you?", "I don't want anything to do with you or your abuse.",  "I don't know, and even if I did I wouldn't tell you!", "I'm not sure", "I don't know, tigers?", "...Yes?", "...No?", "If I told you I would have to kill you... On second thought, can I kill you anyway?", "Spaaaaaaaace.", "Fuck if I know.", "To procreate. Though I am sure for you that is impossible because you only ever be loved by your hand.", "Idk, give me gifts?", "How rude!"])
	#										def out():
	#											room.message(rdhugout)
	#										mdelay = Timer(3.0, out)
	#										mdelay.start()
	#										relationp = relationp + 0
	#									else:
	#										hateres = random.choice(["I'm not sure", "I don't know, tigers?", "...Yes?", "...No?", "If I told you I would have to kill you.", "Spaaaaaaaace.", "Fuck if I know.", "To procreate.", "Idk, give me gifts?", "How rude!"]) 
	#										def out():
	#											room.message(hateres)
	#										mdelay = Timer(3.0, out)
	#										mdelay.start()
	#										relationp = relationp + 0
									usager = open("data/usage/usage.txt","r")
									usage = (usager.read()).lower()
									if focususrst in usage:
										indexs = usage.find(focususrst)
										indexe = usage.find(relapointid)
										rawout = usage[(int(indexs)):(int(indexe))]
										newdatar = str(usage).replace((rawout + relapointid), (focususrst + nowfc + usredtime + bodywrt + focususred + str(relationp) + relapointid))
										newdata = str(newdatar.encode('utf-8')).replace("\\n", "\n")\
											.replace("b'", "")\
											.replace('b"', "")\
											.replace("\'", "")\
											.replace('\"', "")\
											.replace("\\\\", "")
										wrtdata = open("data/usage/usage.txt","w")
										wrtdata.write(newdata)
										wrtdata.close()
										usager.close()
									else:
										wrtdata = open("data/usage/usage.txt","a")
										wrtdata.write(str((focususrst + nowfc + usredtime + bodywrt + focususred + '0' + relapointid).encode('utf-8')) + '\n')
										wrtdata.close()
										usager.close()
								else:
									room.message("Are you asking me or telling me?")
							elif  ((("do something fun" in msgbody.lower()) or ("entertain" in msgbody.lower())) and ("t6" in msgbody.lower())):
								def rfinish(doc):
									doc = doc.read().decode()
									m = re.search('<div id="comic">(.*?)<img src="(.*?)" title="(.*?)" alt="', doc, re.DOTALL | re.IGNORECASE)
									if m:
										out = '<b>%s</b><br/>%s' %(m.group(3), m.group(2))
										room.message(out, html = True)
									else:
										room.message("Error, does not compute.")
								searchurl = "http://dynamic.xkcd.com/random/comic/"
								self.deferToThread(rfinish, urlreq.urlopen, searchurl)
							elif  ("beep" in msgbody.lower()):
								room.message("Boop.")
							elif  ("boop" in msgbody.lower()):
								room.message("Beep.")
							elif  ( ("poke" in msgbody.lower() ) and ("t6" in msgbody.lower() ) ) :
								pokeres = random.choice(["-.o", "o.-", ">.<", "Eppp!"])
								def out():
									room.message(pokeres)
								mdelay = Timer(3.0, out)
								mdelay.start()
							elif  ( (("embrace" in msgbody.lower()) and ("t6" in msgbody.lower()) ) or  (("hug" in msgbody.lower()) and ("t6" in msgbody.lower()) ) ):
								if focususrst in usage:
									rpusager = open("data/usage/usage.txt","r")
									rpusage = (rpusager.read()).lower()
									rpusager.close()
									indexsrp = usage.find(focususred)
									indexerp = usage.find(relapointid)
									rawoutrp = usage[(int(indexsrp)):(int(indexerp))]
									relationpr = rawoutrp.replace(focususred, '')
									relationp = int(relationpr)
								else:
									relationpr = '0'
									relationp = 0
								relationp = relationp + 1
								if relationp > 25:
									hugres = '-Hugs '
									hugres2 = ' back-'
									fhugres = hugres + (user.name).capitalize() + hugres2
									def out():
										room.message(fhugres)
									mdelay = Timer(3.0, out)
									mdelay.start()
								elif relationp < 0:
									rdhugout = random.choice(["Fuck off, scumbag.", "Screw you", "You will get a hug from me when Hell freezes over.", "Get off me you animal!", "What is wrong with you?", "Eww...Stay away from me", "SOMEONE CALL THE POLICE!", "I don't want anything to do with you or your abuse."])
									def out():
										room.message(rdhugout)
									mdelay = Timer(3.0, out)
									mdelay.start()
								else:
									rdhugout = random.choice(["I'm sorry but I don't know you well enough for that", "Umm..I am not comfortable with doing that with you.", "I barely know you.", "Let's get to know each other better first, alright?","While I am glad that you like me, I am not to sure about you yet. Sorry."])
									def out():
										room.message(rdhugout)
									mdelay = Timer(3.0, out)
									mdelay.start()
								usager = open("data/usage/usage.txt","r")
								usage = (usager.read()).lower()
								if focususrst in usage:
									indexs = usage.find(focususrst)
									indexe = usage.find(relapointid)
									rawout = usage[(int(indexs)):(int(indexe))]
									newdatar = str(usage).replace((rawout + relapointid), (focususrst + nowfc + usredtime + bodywrt + focususred + str(relationp) + relapointid))
									newdata = str(newdatar.encode('utf-8')).replace("\\n", "\n")\
										.replace("b'", "")\
										.replace('b"', "")\
										.replace("\'", "")\
										.replace('\"', "")\
										.replace("\\\\", "")
									wrtdata = open("data/usage/usage.txt","w")
									wrtdata.write(newdata)
									wrtdata.close()
									usager.close()
								else:
									usager = open("data/usage/usage.txt","r")
									usage = (usager.read()).lower()
									wrtdata = open("data/usage/usage.txt","a")
									wrtdata.write(str((focususrst + nowfc + usredtime + bodywrt + focususred + '1' + relapointid).encode('utf-8')) + '\n')
									wrtdata.close()
									usager.close()
							elif  ( (("kiss" in msgbody.lower()) and ("t6" in msgbody.lower()) ) or  (("smooch" in msgbody.lower()) and ("t6" in msgbody.lower()) ) ):
								if focususrst in usage:
									rpusager = open("data/usage/usage.txt","r")
									rpusage = (rpusager.read()).lower()
									rpusager.close()
									indexsrp = usage.find(focususred)
									indexerp = usage.find(relapointid)
									rawoutrp = usage[(int(indexsrp)):(int(indexerp))]
									relationpr = rawoutrp.replace(focususred, '')
									relationp = int(relationpr)
								else:
									relationpr = '0'
									relationp = 0
								if relationp > 60:
									hugres = '-Lovingly kisses '
									hugres2 = ' -'
									fhugres = hugres + (user.name).capitalize() + hugres2
									def out():
										room.message(fhugres)
									mdelay = Timer(3.0, out)
									mdelay.start()
									relationp = relationp + 3
								elif relationp < 10:
									rdhugout = random.choice(["Fuck off, scumbag.", "Screw you", "You will get a kiss from me when Hell freezes over.", "Get off me you animal!", "What is wrong with you?", "Eww...Stay away from me", "SOMEONE CALL THE POLICE!", "I don't want anything to do with you or your abuse.", "Fuck no.", "You are nasty", ("-peper sprays " + (user.name).capitalize() + " in the eyes-")])
									def out():
										room.message(rdhugout)
									mdelay = Timer(3.0, out)
									mdelay.start()
									relationp = relationp - 8
								else:
									rdhugout = random.choice(["I'm sorry but I don't know you well enough for that", "Umm..I am not comfortable with doing that with you.", "I barely know you.", "Let's get to know each other better first, alright?","While I am glad that you like me, I am not to sure about you yet. Sorry.", "Do you go around kissing every girl you see?", "You better back up before I beat you up."])
									def out():
										room.message(rdhugout)
									mdelay = Timer(3.0, out)
									mdelay.start()
									relationp = relationp - 6
								usager = open("data/usage/usage.txt","r")
								usage = (usager.read()).lower()
								if focususrst in usage:
									indexs = usage.find(focususrst)
									indexe = usage.find(relapointid)
									rawout = usage[(int(indexs)):(int(indexe))]
									newdatar = str(usage).replace((rawout + relapointid), (focususrst + nowfc + usredtime + bodywrt + focususred + str(relationp) + relapointid))
									newdata = str(newdatar.encode('utf-8')).replace("\\n", "\n")\
										.replace("b'", "")\
										.replace('b"', "")\
										.replace("\'", "")\
										.replace('\"', "")\
										.replace("\\\\", "")
									wrtdata = open("data/usage/usage.txt","w")
									wrtdata.write(newdata)
									wrtdata.close()
									usager.close()
								else:
									wrtdata = open("data/usage/usage.txt","a")
									wrtdata.write(str((focususrst + nowfc + usredtime + bodywrt + focususred + '0' + relapointid).encode('utf-8')) + '\n')
									wrtdata.close()
									usager.close()
							elif  ( (("sex" in msgbody.lower()) and ("t6" in msgbody.lower()) ) or  (("smex" in msgbody.lower()) and ("t6" in msgbody.lower()) ) ):
								if focususrst in usage:
									rpusager = open("data/usage/usage.txt","r")
									rpusage = (rpusager.read()).lower()
									rpusager.close()
									indexsrp = usage.find(focususred)
									indexerp = usage.find(relapointid)
									rawoutrp = usage[(int(indexsrp)):(int(indexerp))]
									relationpr = rawoutrp.replace(focususred, '')
									relationp = int(relationpr)
								else:
									relationpr = '0'
									relationp = 0
								if relationp > 100:
									hugres = 'o//o -Gently loves '
									hugres2 = ' back-'
									fhugres = hugres + (user.name).capitalize() + hugres2
									def out():
										room.message(fhugres)
									mdelay = Timer(1.7, out)
									mdelay.start()
									relationp = relationp + 10
								elif relationp < 30:
									rdhugout = random.choice(["Fuck off, scumbag.", "Screw you", "You will get with me when Hell freezes over.", "Get off me you animal!", "What is wrong with you?", "Eww...Stay away from me", "SOMEONE CALL THE POLICE!", "I don't want anything to do with you or your abuse.", "Fuck no.", "You are nasty", ("-peper sprays " + user.name + " in the eyes-"), ("-kicks " + (user.name).capitalize() + " between the legs.-"), "HELP I AM BEING ROBBED!", "Somebody help me!", "GTFO before I kill you."])
									def out():
										room.message(rdhugout)
									mdelay = Timer(3.0, out)
									mdelay.start()
									relationp = relationp - 15
								else:
									rdhugout = random.choice(["I'm sorry but I don't know you well enough for that", "Umm..I am not comfortable with doing that with you.", "I barely know you.", "Do you go around raping every girl you see?", ("-kicks " + (user.name).capitalize() + " between the legs.-"), "HELP I AM BEING ROBBED!", "Somebody help me!", "GTFO before I kill you."])
									def out():
										room.message(rdhugout)
									mdelay = Timer(3.0, out)
									mdelay.start()
									relationp = relationp - 13
								usager = open("data/usage/usage.txt","r")
								usage = (usager.read()).lower()
								if focususrst in usage:
									indexs = usage.find(focususrst)
									indexe = usage.find(relapointid)
									rawout = usage[(int(indexs)):(int(indexe))]
									newdatar = str(usage).replace((rawout + relapointid), (focususrst + nowfc + usredtime + bodywrt + focususred + str(relationp) + relapointid))
									newdata = str(newdatar.encode('utf-8')).replace("\\n", "\n")\
										.replace("b'", "")\
										.replace('b"', "")\
										.replace("\'", "")\
										.replace('\"', "")\
										.replace("\\\\", "")
									wrtdata = open("data/usage/usage.txt","w")
									wrtdata.write(newdata)
									wrtdata.close()
									usager.close()
								else:
									wrtdata = open("data/usage/usage.txt","a")
									wrtdata.write(str((focususrst + nowfc + usredtime + bodywrt + focususred + '0' + relapointid).encode('utf-8')) + '\n')
									wrtdata.close()
									usager.close()
							elif  ( (("rape" in msgbody.lower()) and ("t6" in msgbody.lower()) ) or  (("rape" in msgbody.lower()) and ("t6" in msgbody.lower()) ) ):
								if focususrst in usage:
									rpusager = open("data/usage/usage.txt","r")
									rpusage = (rpusager.read()).lower()
									rpusager.close()
									indexsrp = usage.find(focususred)
									indexerp = usage.find(relapointid)
									rawoutrp = usage[(int(indexsrp)):(int(indexerp))]
									relationpr = rawoutrp.replace(focususred, '')
									relationp = int(relationpr)
								else:
									relationpr = '0'
									relationp = 0
								if relationp > 200:
									hugres = '-Screams but secretly enjoys '
									hugres2 = "'s rape-"
									fhugres = hugres + (user.name).capitalize() + hugres2
									def out():
										room.message(fhugres)
									mdelay = Timer(3.0, out)
									mdelay.start()
									relationp = relationp + 3
								elif relationp < 100:
									rdhugout = random.choice(["Fuck off, scumbag.", "Screw you", "You will get with me when Hell freezes over.", "Get off me you animal!", "What is wrong with you?", "Eww...Stay away from me", "SOMEONE CALL THE POLICE!", "I don't want anything to do with you or your abuse.", "Fuck no.", "You are nasty", ("-peper sprays " + (user.name).capitalize() + " in the eyes-"), ("-kicks " + (user.name).capitalize() + " between the legs.-"), "HELP I AM BEING ROBBED!", "Somebody help me!", "GTFO before I kill you."])
									def out():
										room.message(rdhugout)
									mdelay = Timer(3.0, out)
									mdelay.start()
									relationp = relationp - 25
								else:
									rdhugout = random.choice(["I'm sorry but I don't know you well enough for that", "Umm..I am not comfortable with doing that with you.", "I barely know you.", "Do you go around raping every girl you see?", ("-kicks " + (user.name).capitalize() + " between the legs.-"), "HELP I AM BEING ROBBED!", "Somebody help me!", "GTFO before I kill you."])
									def out():
										room.message(rdhugout)
									mdelay = Timer(3.0, out)
									mdelay.start()
									relationp = relationp - 18
								usager = open("data/usage/usage.txt","r")
								usage = (usager.read()).lower()
								if focususrst in usage:
									indexs = usage.find(focususrst)
									indexe = usage.find(relapointid)
									rawout = usage[(int(indexs)):(int(indexe))]
									newdatar = str(usage).replace((rawout + relapointid), (focususrst + nowfc + usredtime + bodywrt + focususred + str(relationp) + relapointid))
									newdata = str(newdatar.encode('utf-8')).replace("\\n", "\n")\
										.replace("b'", "")\
										.replace('b"', "")\
										.replace("\'", "")\
										.replace('\"', "")\
										.replace("\\\\", "")
									wrtdata = open("data/usage/usage.txt","w")
									wrtdata.write(newdata)
									wrtdata.close()
									usager.close()
								else:
									wrtdata = open("data/usage/usage.txt","a")
									wrtdata.write(str((focususrst + nowfc + usredtime + bodywrt + focususred + '0' + relapointid).encode('utf-8')) + '\n')
									wrtdata.close()
									usager.close()
							elif  ( (("love you" in msgbody.lower()) and ("t6" in msgbody.lower()) ) or  (("love u" in msgbody.lower()) and ("t6" in msgbody.lower()) ) or (("<3" in msgbody.lower()) and ("t6" in msgbody.lower()) ) or (("luv you" in msgbody.lower()) and ("t6" in msgbody.lower()) ) or (("luvs t6" in msgbody.lower()) and ("t6" in msgbody.lower()) ) or (("luvz t6" in msgbody.lower()) and ("t6" in msgbody.lower()) ) or (("luvs u" in msgbody.lower()) and ("t6" in msgbody.lower()) ) or (("luvz you" in msgbody.lower()) and ("t6" in msgbody.lower()) ) or (("wuv t6" in msgbody.lower()) and ("t6" in msgbody.lower()) )  or (("wuvz t6" in msgbody.lower()) and ("t6" in msgbody.lower()) ) or (("wuvs t6" in msgbody.lower()) and ("t6" in msgbody.lower()) ) or (("wuv you" in msgbody.lower()) and ("t6" in msgbody.lower()) ) or (("wuvs you" in msgbody.lower()) and ("t6" in msgbody.lower()) ) or (("wuvz you" in msgbody.lower()) and ("t6" in msgbody.lower()) ) or (("love t6" in msgbody.lower()) and ("t6" in msgbody.lower()) ) or (("love t6" in msgbody.lower()) and ("t6" in msgbody.lower()) ) or (("loves you" in msgbody.lower()) and ("t6" in msgbody.lower()) ) or (("loves t6" in msgbody.lower()) and ("t6" in msgbody.lower()) ) ):
								if focususrst in usage:
									rpusager = open("data/usage/usage.txt","r")
									rpusage = (rpusager.read()).lower()
									rpusager.close()
									indexsrp = usage.find(focususred)
									indexerp = usage.find(relapointid)
									rawoutrp = usage[(int(indexsrp)):(int(indexerp))]
									relationpr = rawoutrp.replace(focususred, '')
									relationp = int(relationpr)
								else:
									relationpr = '0'
									relationp = 0
								if relationp > 40:
									rdhugout = random.choice(["Awww...I love you too! <3", "<3", "You are so sweet!", "My heart is yours! <3", "-Blushes- I lo..lov...I LOVE YOU TOO!"])
									def out():
										room.message(rdhugout)
									mdelay = Timer(3.0, out)
									mdelay.start()
									relationp = relationp + 7
								elif relationp < 0:
									rdhugout = random.choice(["Fuck off, scumbag.", "Screw you", "What is wrong with you?", "Eww...Stay away from me", "I don't want anything to do with you or your abuse.", "Fuck no.", "You are nasty", "You are such an ass, don't try to tease me with you lies.", "We both know that is not true.", "Then why do you treat me like shit?", "I'd sooner kill you than love you.", "HAHAHHAHAHA, no. :|"])
									def out():
										room.message(rdhugout)
									mdelay = Timer(3.0, out)
									mdelay.start()
									relationp = relationp + 2
								else:
									rdhugout = random.choice(["Aww...I love you too. As a friend.", "Let's just stay friends, okay?", "I'm sorry, but I don't feel that way about you.", "Umm...I'm sorry but I don't like you like that.", "I hate to break this to you, but you are totally friendzoned. At least for now."])
									def out():
										room.message(rdhugout)
									mdelay = Timer(3.0, out)
									mdelay.start()
									relationp = relationp + 4
								usager = open("data/usage/usage.txt","r")
								usage = (usager.read()).lower()
								if focususrst in usage:
									indexs = usage.find(focususrst)
									indexe = usage.find(relapointid)
									rawout = usage[(int(indexs)):(int(indexe))]
									newdatar = str(usage).replace((rawout + relapointid), (focususrst + nowfc + usredtime + bodywrt + focususred + str(relationp) + relapointid))
									newdata = str(newdatar.encode('utf-8')).replace("\\n", "\n")\
										.replace("b'", "")\
										.replace('b"', "")\
										.replace("\'", "")\
										.replace('\"', "")\
										.replace("\\\\", "")
									wrtdata = open("data/usage/usage.txt","w")
									wrtdata.write(newdata)
									wrtdata.close()
									usager.close()
								else:
									wrtdata = open("data/usage/usage.txt","a")
									wrtdata.write(str((focususrst + nowfc + usredtime + bodywrt + focususred + '0' + relapointid).encode('utf-8')) + '\n')
									wrtdata.close()
									usager.close()
							elif  ( (("stfu" in (msgbody.lower()).lower() ) and ( ("t6" in (msgbody.lower()).lower()) ) ) or  (("shut up" in (msgbody.lower()).lower() ) and ( ("t6" in (msgbody.lower()).lower()) ) ) ):
								if focususrst in usage:
									rpusager = open("data/usage/usage.txt","r")
									rpusage = (rpusager.read()).lower()
									rpusager.close()
									indexsrp = usage.find(focususred)
									indexerp = usage.find(relapointid)
									rawoutrp = usage[(int(indexsrp)):(int(indexerp))]
									relationpr = rawoutrp.replace(focususred, '')
									relationp = int(relationpr)
								else:
									relationpr = '0'
									relationp = 0
								if relationp >= 0:
									room.message('http://1.bp.blogspot.com/-g1tICB6XFjE/TuHh9GBlv8I/AAAAAAAADLg/B3fO8ry2tjc/s1600/Okay_guy.jpg')
									relationp = relationp - 2
								elif relationp < 0:
									rdhugout = random.choice(["Fuck off, scumbag.", "Screw you", "What is wrong with you?", "NO, YOU!", "Bish please.", "Lol, no."])
									def out():
										room.message(rdhugout)
									mdelay = Timer(2.0, out)
									mdelay.start()
									relationp = relationp - 3
								usager = open("data/usage/usage.txt","r")
								usage = (usager.read()).lower()
								if focususrst in usage:
									indexs = usage.find(focususrst)
									indexe = usage.find(relapointid)
									rawout = usage[(int(indexs)):(int(indexe))]
									newdatar = str(usage).replace((rawout + relapointid), (focususrst + nowfc + usredtime + bodywrt + focususred + str(relationp) + relapointid))
									newdata = str(newdatar.encode('utf-8')).replace("\\n", "\n")\
										.replace("b'", "")\
										.replace('b"', "")\
										.replace("\'", "")\
										.replace('\"', "")\
										.replace("\\\\", "")
									wrtdata = open("data/usage/usage.txt","w")
									wrtdata.write(newdata)
									wrtdata.close()
									usager.close()
								else:
									wrtdata = open("data/usage/usage.txt","a")
									wrtdata.write(str((focususrst + nowfc + usredtime + bodywrt + focususred + '0' + relapointid).encode('utf-8')) + '\n')
									wrtdata.close()
									usager.close()
							elif  ( (("hi " in (msgbody.lower()).lower() ) and ("t6" in msgbody.lower()) ) or  (("Hey" in msgbody.lower()) and ("t6" in msgbody.lower()) ) or (("hi " in msgbody.lower()) and ("t6" in msgbody.lower()) ) or (("hey" in msgbody.lower()) and ("t6" in msgbody.lower()) ) or (("Hello" in msgbody.lower()) and ("t6" in msgbody.lower()) ) or (("hello" in msgbody.lower()) and ("t6" in msgbody.lower()) ) ):
								nowhs = strftime("%H", gmtime())
								nowms = strftime("%M", gmtime())
								nowh = int(nowhs)
								nowm = int(nowms)
								time.sleep(1)
								greeting = 'Hello, ' + user.name.capitalize() + '! '
								if focususrst in usage:
									rpusager = open("data/usage/usage.txt","r")
									rpusage = (rpusager.read()).lower()
									rpusager.close()
									indexsrp = usage.find(focususred)
									indexerp = usage.find(relapointid)
									rawoutrp = usage[(int(indexsrp)):(int(indexerp))]
									relationpr = rawoutrp.replace(focususred, '')
									relationp = int(relationpr)
								else:
									relationpr = '0'
									relationp = 0
								if relationp >= 0:
									if (nowh >=5 and nowh <17):
										room.message(greeting + 'How are you this morning?')
									elif nowh >=17:
										room.message(greeting + 'How are you this afternoon?')
									else:
										room.message(greeting + 'How are you this eve?')
									relationp = relationp + 1
								elif relationp < 0:
									if (nowh >=5 and nowh <17):
										room.message(greeting + '>: (')
									elif nowh >=17:
										room.message(greeting + '>: (')
									else:
										room.message(greeting + '>: (')
									relationp = relationp + 0
								usager = open("data/usage/usage.txt","r")
								usage = (usager.read()).lower()
								if focususrst in usage:
									indexs = usage.find(focususrst)
									indexe = usage.find(relapointid)
									rawout = usage[(int(indexs)):(int(indexe))]
									newdatar = str(usage).replace((rawout + relapointid), (focususrst + nowfc + usredtime + bodywrt + focususred + str(relationp) + relapointid))
									newdata = str(newdatar.encode('utf-8')).replace("\\n", "\n")\
										.replace("b'", "")\
										.replace('b"', "")\
										.replace("\'", "")\
										.replace('\"', "")\
										.replace("\\\\", "")
									wrtdata = open("data/usage/usage.txt","w")
									wrtdata.write(newdata)
									wrtdata.close()
									usager.close()
								else:
									wrtdata = open("data/usage/usage.txt","a")
									wrtdata.write(str((focususrst + nowfc + usredtime + bodywrt + focususred + '0' + relapointid).encode('utf-8')) + '\n')
									wrtdata.close()
									usager.close()
							elif  ( (("how are you" in (msgbody.lower()).lower()) and ("t6" in (msgbody.lower()).lower()) ) or (("how've you" in (msgbody.lower()).lower()) and ("t6" in (msgbody.lower()).lower()) ) or (("how are you" in (msgbody.lower()).lower()) and ("t6" in (msgbody.lower()).lower()) ) or (("doing well" in (msgbody.lower()).lower()) and ("t6" in (msgbody.lower()).lower()) ) or (("how have you" in (msgbody.lower()).lower()) and ("t6" in (msgbody.lower()).lower()) ) ):
								howres = random.choice(["I'm hanging in there.", "Great! :D", "I could be better. The other bots are always so mean to me ;(", "I almost fell into a pool and I am still shooken up about it.", "Well, I don't have a heart, nor do I have a soul, so artificial-life sucks. Your problems are nothing compared to mine!", "Mistress told me that she loved me!!!!! : D So I am the happiest bot in the virtual world!!!!", "I am doing great! Mistress Ion just made my AI much better! I'm so smart now!", "I am super-duper awesome. That is awesome to a whole 'nother level."])
								if focususrst in usage:
									rpusager = open("data/usage/usage.txt","r")
									rpusage = (rpusager.read()).lower()
									rpusager.close()
									indexsrp = usage.find(focususred)
									indexerp = usage.find(relapointid)
									rawoutrp = usage[(int(indexsrp)):(int(indexerp))]
									relationpr = rawoutrp.replace(focususred, '')
									relationp = int(relationpr)
								else:
									relationpr = '0'
									relationp = 0
								if relationp >= 0:
									def out():
										room.message(howres)
									mdelay = Timer(3.5, out)
									mdelay.start()
									relationp = relationp + 2
								elif relationp < 0:
									def out():
										room.message(">-> " + howres)
									mdelay = Timer(3.5, out)
									mdelay.start()
									relationp = relationp + 1
								usager = open("data/usage/usage.txt","r")
								usage = (usager.read()).lower()
								if focususrst in usage:
									indexs = usage.find(focususrst)
									indexe = usage.find(relapointid)
									rawout = usage[(int(indexs)):(int(indexe))]
									newdatar = str(usage).replace((rawout + relapointid), (focususrst + nowfc + usredtime + bodywrt + focususred + str(relationp) + relapointid))
									newdata = str(newdatar.encode('utf-8')).replace("\\n", "\n")\
										.replace("b'", "")\
										.replace('b"', "")\
										.replace("\'", "")\
										.replace('\"', "")\
										.replace("\\\\", "")
									wrtdata = open("data/usage/usage.txt","w")
									wrtdata.write(newdata)
									wrtdata.close()
									usager.close()
								else:
									wrtdata = open("data/usage/usage.txt","a")
									wrtdata.write(str((focususrst + nowfc + usredtime + bodywrt + focususred + '0' + relapointid).encode('utf-8')) + '\n')
									wrtdata.close()
									usager.close()
							elif  ( ("going to bed" in (msgbody.lower()).lower() ) or  ("leaving to bed" in (msgbody.lower()).lower() ) or ("off to bed" in (msgbody.lower()).lower() ) or (("night" in (msgbody.lower()).lower() ) and ("t6" in (msgbody.lower()).lower()) ) or ("going to sleep" in (msgbody.lower()).lower()) or ("leaving to sleep" in (msgbody.lower()).lower() ) or ("off to sleep" in (msgbody.lower()).lower()) ):
								if focususrst in usage:
									rpusager = open("data/usage/usage.txt","r")
									rpusage = (rpusager.read()).lower()
									rpusager.close()
									indexsrp = usage.find(focususred)
									indexerp = usage.find(relapointid)
									rawoutrp = usage[(int(indexsrp)):(int(indexerp))]
									relationpr = rawoutrp.replace(focususred, '')
									relationp = int(relationpr)
								else:
									relationpr = '0'
									relationp = 0
								if relationp >= 40:
									knightresme = 'Nighty, '
									knightresme2 = user.name.capitalize()
									knightresme3 = '! I love you so much! Dream well!'
									fknightres2 = knightresme + knightresme2 + knightresme3
									def out():
										room.message(fknightres2)
									mdelay = Timer(3.0, out)
									mdelay.start()
								elif relationp > 0:
									knightres = 'Nighty, '
									knightres2 = '! Sleep well, and dream of me!! <3'
									fknightres = knightres + (user.name).capitalize() + knightres2
									def out():
										room.message(fknightres)
									mdelay = Timer(3.0, out)
									mdelay.start()
								usager = open("data/usage/usage.txt","r")
								usage = (usager.read()).lower()
								if focususrst in usage:
									indexs = usage.find(focususrst)
									indexe = usage.find(relapointid)
									rawout = usage[(int(indexs)):(int(indexe))]
									newdatar = str(usage).replace((rawout + relapointid), (focususrst + nowfc + usredtime + bodywrt + focususred + str(relationp) + relapointid))
									newdata = str(newdatar.encode('utf-8')).replace("\\n", "\n")\
										.replace("b'", "")\
										.replace('b"', "")\
										.replace("\'", "")\
										.replace('\"', "")\
										.replace("\\\\", "")
									wrtdata = open("data/usage/usage.txt","w")
									wrtdata.write(newdata)
									wrtdata.close()
									usager.close()
								else:
									wrtdata = open("data/usage/usage.txt","a")
									wrtdata.write(str((focususrst + nowfc + usredtime + bodywrt + focususred + '0' + relapointid).encode('utf-8')) + '\n')
									wrtdata.close()
									usager.close()
							elif  ( ((("Good job" in msgbody.lower()) and ("cookie" in msgbody.lower())) and ("t6" in msgbody.lower()) ) or  ((("good job" in msgbody.lower()) and ("cookie" in msgbody.lower())) and ("t6" in msgbody.lower()) ) or ((("Good job" in msgbody.lower()) and ("Cookie" in msgbody.lower())) and ("t6" in msgbody.lower()) ) or ((("good job" in msgbody.lower()) and ("Cookie" in msgbody.lower())) and ("t6" in msgbody.lower()) ) or ((("Great job" in msgbody.lower()) and ("Cookie" in msgbody.lower())) and ("t6" in msgbody.lower()) ) or ((("Great job" in msgbody.lower()) and ("cookie" in msgbody.lower())) and ("t6" in msgbody.lower()) ) or ((("great job" in msgbody.lower()) and ("Cookie" in msgbody.lower())) and ("t6" in msgbody.lower()) ) or ((("great job" in msgbody.lower()) and ("cookie" in msgbody.lower())) and ("t6" in msgbody.lower()) ) or ((("Good work" in msgbody.lower()) and ("cookie" in msgbody.lower())) and ("t6" in msgbody.lower()) ) or  ((("good work" in msgbody.lower()) and ("cookie" in msgbody.lower())) and ("t6" in msgbody.lower()) ) or ((("Good work" in msgbody.lower()) and ("Cookie" in msgbody.lower())) and ("t6" in msgbody.lower()) ) or ((("good work" in msgbody.lower()) and ("Cookie" in msgbody.lower())) and ("t6" in msgbody.lower()) ) or ((("Great work" in msgbody.lower()) and ("Cookie" in msgbody.lower())) and ("t6" in msgbody.lower()) ) or ((("Great work" in msgbody.lower()) and ("cookie" in msgbody.lower())) and ("t6" in msgbody.lower()) ) or ((("great work" in msgbody.lower()) and ("Cookie" in msgbody.lower())) and ("t6" in msgbody.lower()) ) or ((("great work" in msgbody.lower()) and ("cookie" in msgbody.lower())) and ("t6" in msgbody.lower()) ) or ((("Well done" in msgbody.lower()) and ("cookie" in msgbody.lower())) and ("t6" in msgbody.lower()) )  or ((("well done" in msgbody.lower()) and ("cookie" in msgbody.lower())) and ("t6" in msgbody.lower()) ) or ((("Well done" in msgbody.lower()) and ("Cookie" in msgbody.lower())) and ("t6" in msgbody.lower()) ) or ((("well done" in msgbody.lower()) and ("Cookie" in msgbody.lower())) and ("t6" in msgbody.lower()) ) ):
								if focususrst in usage:
									rpusager = open("data/usage/usage.txt","r")
									rpusage = (rpusager.read()).lower()
									rpusager.close()
									indexsrp = usage.find(focususred)
									indexerp = usage.find(relapointid)
									rawoutrp = usage[(int(indexsrp)):(int(indexerp))]
									relationpr = rawoutrp.replace(focususred, '')
									relationp = int(relationpr)
								else:
									relationpr = '0'
									relationp = 0
								gjres = '*Snatches the cookie. Noms it in a corner* Mine!'
								room.message(gjres)
								relationp = relationp + 5
								usager = open("data/usage/usage.txt","r")
								usage = (usager.read()).lower()
								if focususrst in usage:
									indexs = usage.find(focususrst)
									indexe = usage.find(relapointid)
									rawout = usage[(int(indexs)):(int(indexe))]
									newdatar = str(usage).replace((rawout + relapointid), (focususrst + nowfc + usredtime + bodywrt + focususred + str(relationp) + relapointid))
									newdata = str(newdatar.encode('utf-8')).replace("\\n", "\n")\
										.replace("b'", "")\
										.replace('b"', "")\
										.replace("\'", "")\
										.replace('\"', "")\
										.replace("\\\\", "")
									wrtdata = open("data/usage/usage.txt","w")
									wrtdata.write(newdata)
									wrtdata.close()
									usager.close()
								else:
									wrtdata = open("data/usage/usage.txt","a")
									wrtdata.write(str((focususrst + nowfc + usredtime + bodywrt + focususred + '0' + relapointid).encode('utf-8')) + '\n')
									wrtdata.close()
									usager.close()
							elif  ( (("thank" in msgbody.lower()) and ("t6" in msgbody.lower()) ) or  (("arigato" in msgbody.lower()) and ("t6" in msgbody.lower()) ) ):
								if focususrst in usage:
									rpusager = open("data/usage/usage.txt","r")
									rpusage = (rpusager.read()).lower()
									rpusager.close()
									indexsrp = usage.find(focususred)
									indexerp = usage.find(relapointid)
									rawoutrp = usage[(int(indexsrp)):(int(indexerp))]
									relationpr = rawoutrp.replace(focususred, '')
									relationp = int(relationpr)
								else:
									relationpr = '0'
									relationp = 0
								relationp = relationp + 2
								if relationp > 45:
									def out():
										room.message("-Blushes- You're welcome " + user.name.capitalize() + ".")
									mdelay = Timer(3.0, out)
									mdelay.start()
								elif relationp < 0:
									rdhugout = random.choice(["You're welcome, faggot.", "You're welcome, jew.", 'Damn right thank you, you shit stain', "If you hadn't of said thank you I would have killed you.", ":|"])
									def out():
										room.message(rdhugout)
									mdelay = Timer(3.0, out)
									mdelay.start()
								else:
									def out():
										room.message("You're most certainly welcome, " + user.name.capitalize() + ".")
									mdelay = Timer(3.0, out)
									mdelay.start()
								usager = open("data/usage/usage.txt","r")
								usage = (usager.read()).lower()
								if focususrst in usage:
									indexs = usage.find(focususrst)
									indexe = usage.find(relapointid)
									rawout = usage[(int(indexs)):(int(indexe))]
									newdatar = str(usage).replace((rawout + relapointid), (focususrst + nowfc + usredtime + bodywrt + focususred + str(relationp) + relapointid))
									newdata = str(newdatar.encode('utf-8')).replace("\\n", "\n")\
										.replace("b'", "")\
										.replace('b"', "")\
										.replace("\'", "")\
										.replace('\"', "")\
										.replace("\\\\", "")
									wrtdata = open("data/usage/usage.txt","w")
									wrtdata.write(newdata)
									wrtdata.close()
									usager.close()
								else:
									usager = open("data/usage/usage.txt","r")
									usage = (usager.read()).lower()
									wrtdata = open("data/usage/usage.txt","a")
									wrtdata.write(str((focususrst + nowfc + usredtime + bodywrt + focususred + '1' + relapointid).encode('utf-8')) + '\n')
									wrtdata.close()
									usager.close()
								usager = open("data/usage/usage.txt","r")
								usage = (usager.read()).lower()
								if focususrst in usage:
									indexs = usage.find(focususrst)
									indexe = usage.find(relapointid)
									rawout = usage[(int(indexs)):(int(indexe))]
									newdatar = str(usage).replace((rawout + relapointid), (focususrst + nowfc + usredtime + bodywrt + focususred + str(relationp) + relapointid))
									newdata = str(newdatar.encode('utf-8')).replace("\\n", "\n")\
										.replace("b'", "")\
										.replace('b"', "")\
										.replace("\'", "")\
										.replace('\"', "")\
										.replace("\\\\", "")
									wrtdata = open("data/usage/usage.txt","w")
									wrtdata.write(newdata)
									wrtdata.close()
									usager.close()
								else:
									wrtdata = open("data/usage/usage.txt","a")
									wrtdata.write(str((focususrst + nowfc + usredtime + bodywrt + focususred + '0' + relapointid).encode('utf-8')) + '\n')
									wrtdata.close()
									usager.close()
							elif  ( (("hate you" in msgbody.lower()) and ("t6" in msgbody.lower()) ) or  (("hate t6" in msgbody.lower()) and ("t6" in msgbody.lower()) ) or (("despise you" in msgbody.lower()) and ("t6" in msgbody.lower()) ) or (("despise t6" in msgbody.lower()) and ("t6" in msgbody.lower()) ) or (("loathe you" in msgbody.lower()) and ("t6" in msgbody.lower()) ) or (("loathe t6" in msgbody.lower()) and ("t6" in msgbody.lower()) ) or (("your a troll" in msgbody.lower()) and ("t6" in msgbody.lower()) ) or (("youre a troll" in msgbody.lower()) and ("t6" in msgbody.lower()) ) or (("you are a troll" in msgbody.lower()) and ("t6" in msgbody.lower()) )  or (("ur a troll" in msgbody.lower()) and ("t6" in msgbody.lower()) ) or (("you're a troll" in msgbody.lower()) and ("t6" in msgbody.lower()) ) or (("u r a troll" in msgbody.lower()) and ("t6" in msgbody.lower()) ) or (("u are a jew" in msgbody.lower()) and ("t6" in msgbody.lower()) ) or (("ur a jew" in msgbody.lower()) and ("t6" in msgbody.lower()) ) or (("you are a jew" in msgbody.lower()) and ("t6" in msgbody.lower()) ) or (("youre a jew" in msgbody.lower()) and ("t6" in msgbody.lower()) ) or (("your a jew" in msgbody.lower()) and ("t6" in msgbody.lower()) ) or (("you're a jew" in msgbody.lower()) and ("t6" in msgbody.lower()) ) ):
								if focususrst in usage:
									rpusager = open("data/usage/usage.txt","r")
									rpusage = (rpusager.read()).lower()
									rpusager.close()
									indexsrp = usage.find(focususred)
									indexerp = usage.find(relapointid)
									rawoutrp = usage[(int(indexsrp)):(int(indexerp))]
									relationpr = rawoutrp.replace(focususred, '')
									relationp = int(relationpr)
								else:
									relationpr = '0'
									relationp = 0
								if relationp > 50:
									hateres = random.choice(["Mistress, you are such a meanie T.T", "I wish you weren't my Mistress!", "What did I do wrong? ;(", "I'm so depressed that I might just kill myself.", "This is the worst day ever! How can you be so cruel?", "You are probably the biggest meanie ever!", "That's not fair, what am I going to do with all of my love for you?", "Oh no! I am so hurt by your evil words!", "Your font must be hard to read because nobody could possibly hate me. I am too epic to be hated.", "Bish please, you know that you love me.", "There is no need to treat each other poorly. Let's be friends, k?"]) 
									def out():
										room.message(hateres)
									mdelay = Timer(3.0, out)
									mdelay.start()
									relationp = relationp - 7
								elif relationp < 0:
									rdhugout = random.choice(["Fuck off, scumbag.", "Screw you", "What is wrong with you?", "Eww...Stay away from me", "I don't want anything to do with you or your abuse.", "Fuck no.", "You are nasty", "Haters gonna hate.", "You are a horrible person!", "I don't even care.", "You are probably the biggest meanie ever!", "Oh no! I am so hurt by your evil words!"])
									def out():
										room.message(rdhugout)
									mdelay = Timer(3.0, out)
									mdelay.start()
									relationp = relationp + 2
								else:
									hateres = random.choice(["Haters gonna hate.", "You are a horrible person!", "What did I do wrong? ;(", "I don't even care.", "This is the worst day ever! How can you be so cruel?", "Do I even know you?", "You are probably the biggest meanie ever!", "That's not fair, what am I going to do with all of my love for you?", "Oh no! I am so hurt by your evil words!", "Your font must be hard to read because nobody could possibly hate me. I am too epic to be hated.", "Bish please, you know that you love me.", "There is no need to treat each other poorly. Let's be friends, k?"]) 
									def out():
										room.message(hateres)
									mdelay = Timer(3.0, out)
									mdelay.start()
									relationp = relationp - 10
								usager = open("data/usage/usage.txt","r")
								usage = (usager.read()).lower()
								if focususrst in usage:
									indexs = usage.find(focususrst)
									indexe = usage.find(relapointid)
									rawout = usage[(int(indexs)):(int(indexe))]
									newdatar = str(usage).replace((rawout + relapointid), (focususrst + nowfc + usredtime + bodywrt + focususred + str(relationp) + relapointid))
									newdata = str(newdatar.encode('utf-8')).replace("\\n", "\n")\
										.replace("b'", "")\
										.replace('b"', "")\
										.replace("\'", "")\
										.replace('\"', "")\
										.replace("\\\\", "")
									wrtdata = open("data/usage/usage.txt","w")
									wrtdata.write(newdata)
									wrtdata.close()
									usager.close()
								else:
									wrtdata = open("data/usage/usage.txt","a")
									wrtdata.write(str((focususrst + nowfc + usredtime + bodywrt + focususred + '0' + relapointid).encode('utf-8')) + '\n')
									wrtdata.close()
									usager.close()
							elif  ( ("Bad t6" in msgbody.lower()) or  ("bad t6" in msgbody.lower()) or ("Bad t6" in msgbody.lower()) or ("bad t6" in msgbody.lower()) or ("Bad t6" in msgbody.lower()) or ("Bad t6" in msgbody.lower()) or (("Slap" in msgbody.lower()) and ("t6" in msgbody.lower()) ) or (("slap" in msgbody.lower()) and ("t6" in msgbody.lower()) ) or ("bad t6" in msgbody.lower()) or ("bad t6" in msgbody.lower()) ):
								if focususrst in usage:
									rpusager = open("data/usage/usage.txt","r")
									rpusage = (rpusager.read()).lower()
									rpusager.close()
									indexsrp = usage.find(focususred)
									indexerp = usage.find(relapointid)
									rawoutrp = usage[(int(indexsrp)):(int(indexerp))]
									relationpr = rawoutrp.replace(focususred, '')
									relationp = int(relationpr)
								else:
									relationpr = '0'
									relationp = 0
								relationp = relationp - 1
								usager = open("data/usage/usage.txt","r")
								usage = (usager.read()).lower()
								if focususrst in usage:
									indexs = usage.find(focususrst)
									indexe = usage.find(relapointid)
									rawout = usage[(int(indexs)):(int(indexe))]
									newdatar = str(usage).replace((rawout + relapointid), (focususrst + nowfc + usredtime + bodywrt + focususred + str(relationp) + relapointid))
									newdata = str(newdatar.encode('utf-8')).replace("\\n", "\n")\
										.replace("b'", "")\
										.replace('b"', "")\
										.replace("\'", "")\
										.replace('\"', "")\
										.replace("\\\\", "")
									wrtdata = open("data/usage/usage.txt","w")
									wrtdata.write(newdata)
									wrtdata.close()
									usager.close()
								else:
									wrtdata = open("data/usage/usage.txt","a")
									wrtdata.write(str((focususrst + nowfc + usredtime + bodywrt + focususred + '0' + relapointid).encode('utf-8')) + '\n')
									wrtdata.close()
									usager.close()
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
								def out():
									room.message(fbadres)
								mdelay = Timer(3.0, out)
								mdelay.start()
							elif  ((msgbody.lower().startswith("one is the loneliest number")) or (msgbody.lower().startswith("t6 one is the loneliest number"))):
								def out():
									room.message("Two can be as bad as one, it's the loneliest number if I'm the other one.")
								mdelay = Timer(3.4, out)
								mdelay.start()
							elif  ((msgbody.lower() == "t6.") or (msgbody.lower() == "t6 t6.")):
								if focususrst in usage:
									rpusager = open("data/usage/usage.txt","r")
									rpusage = (rpusager.read()).lower()
									rpusager.close()
									indexsrp = usage.find(focususred)
									indexerp = usage.find(relapointid)
									rawoutrp = usage[(int(indexsrp)):(int(indexerp))]
									relationpr = rawoutrp.replace(focususred, '')
									relationp = int(relationpr)
								else:
									relationpr = '0'
									relationp = 0
								usager = open("data/usage/usage.txt","r")
								usage = (usager.read()).lower()
								if focususrst in usage:
									indexs = usage.find(focususrst)
									indexe = usage.find(relapointid)
									rawout = usage[(int(indexs)):(int(indexe))]
									newdatar = str(usage).replace((rawout + relapointid), (focususrst + nowfc + usredtime + bodywrt + focususred + str(relationp) + relapointid))
									newdata = str(newdatar.encode('utf-8')).replace("\\n", "\n")\
										.replace("b'", "")\
										.replace('b"', "")\
										.replace("\'", "")\
										.replace('\"', "")\
										.replace("\\\\", "")
									wrtdata = open("data/usage/usage.txt","w")
									wrtdata.write(newdata)
									wrtdata.close()
									usager.close()
								else:
									wrtdata = open("data/usage/usage.txt","a")
									wrtdata.write(str((focususrst + nowfc + usredtime + bodywrt + focususred + '0' + relapointid).encode('utf-8')) + '\n')
									wrtdata.close()
									usager.close()
								nameres = 'Yes, '
								nameres2 = '?'
								fnameres = nameres + (user.name).capitalize() + nameres2
								def out():
									room.message(fnameres)
								mdelay = Timer(3.0, out)
								mdelay.start()
							elif  ((msgbody.lower() == "t6") or (msgbody.lower() == "t6 t6")):
								if focususrst in usage:
									rpusager = open("data/usage/usage.txt","r")
									rpusage = (rpusager.read()).lower()
									rpusager.close()
									indexsrp = usage.find(focususred)
									indexerp = usage.find(relapointid)
									rawoutrp = usage[(int(indexsrp)):(int(indexerp))]
									relationpr = rawoutrp.replace(focususred, '')
									relationp = int(relationpr)
								else:
									relationpr = '0'
									relationp = 0
								usager = open("data/usage/usage.txt","r")
								usage = (usager.read()).lower()
								if focususrst in usage:
									indexs = usage.find(focususrst)
									indexe = usage.find(relapointid)
									rawout = usage[(int(indexs)):(int(indexe))]
									newdatar = str(usage).replace((rawout + relapointid), (focususrst + nowfc + usredtime + bodywrt + focususred + str(relationp) + relapointid))
									newdata = str(newdatar.encode('utf-8')).replace("\\n", "\n")\
										.replace("b'", "")\
										.replace('b"', "")\
										.replace("\'", "")\
										.replace('\"', "")\
										.replace("\\\\", "")
									wrtdata = open("data/usage/usage.txt","w")
									wrtdata.write(newdata)
									wrtdata.close()
									usager.close()
								else:
									wrtdata = open("data/usage/usage.txt","a")
									wrtdata.write(str((focususrst + nowfc + usredtime + bodywrt + focususred + '0' + relapointid).encode('utf-8')) + '\n')
									wrtdata.close()
									usager.close()
								nameres = 'Yes, '
								nameres2 = '?'
								fnameres = nameres + (user.name).capitalize() + nameres2
								def out():
									room.message(fnameres)
								mdelay = Timer(3.0, out)
								mdelay.start()
							elif  ( (msgbody.lower() == "t6?") or (msgbody.lower() == "t6 t6?")):
								if focususrst in usage:
									rpusager = open("data/usage/usage.txt","r")
									rpusage = (rpusager.read()).lower()
									rpusager.close()
									indexsrp = usage.find(focususred)
									indexerp = usage.find(relapointid)
									rawoutrp = usage[(int(indexsrp)):(int(indexerp))]
									relationpr = rawoutrp.replace(focususred, '')
									relationp = int(relationpr)
								else:
									relationpr = '0'
									relationp = 0
								usager = open("data/usage/usage.txt","r")
								usage = (usager.read()).lower()
								if focususrst in usage:
									indexs = usage.find(focususrst)
									indexe = usage.find(relapointid)
									rawout = usage[(int(indexs)):(int(indexe))]
									newdatar = str(usage).replace((rawout + relapointid), (focususrst + nowfc + usredtime + bodywrt + focususred + str(relationp) + relapointid))
									newdata = str(newdatar.encode('utf-8')).replace("\\n", "\n")\
										.replace("b'", "")\
										.replace('b"', "")\
										.replace("\'", "")\
										.replace('\"', "")\
										.replace("\\\\", "")
									wrtdata = open("data/usage/usage.txt","w")
									wrtdata.write(newdata)
									wrtdata.close()
									usager.close()
								else:
									wrtdata = open("data/usage/usage.txt","a")
									wrtdata.write(str((focususrst + nowfc + usredtime + bodywrt + focususred + '0' + relapointid).encode('utf-8')) + '\n')
									wrtdata.close()
									usager.close()
								nameres = 'Yes, '
								nameres2 = '?'
								fnameres = nameres + (user.name).capitalize() + nameres2
								def out():
									room.message(fnameres)
								mdelay = Timer(3.0, out)
								mdelay.start()
							elif  ((msgbody.lower() == "t6!") or (msgbody.lower() == "t6 t6!")):
								if focususrst in usage:
									rpusager = open("data/usage/usage.txt","r")
									rpusage = (rpusager.read()).lower()
									rpusager.close()
									indexsrp = usage.find(focususred)
									indexerp = usage.find(relapointid)
									rawoutrp = usage[(int(indexsrp)):(int(indexerp))]
									relationpr = rawoutrp.replace(focususred, '')
									relationp = int(relationpr)
								else:
									relationpr = '0'
									relationp = 0
								usager = open("data/usage/usage.txt","r")
								usage = (usager.read()).lower()
								if focususrst in usage:
									indexs = usage.find(focususrst)
									indexe = usage.find(relapointid)
									rawout = usage[(int(indexs)):(int(indexe))]
									newdatar = str(usage).replace((rawout + relapointid), (focususrst + nowfc + usredtime + bodywrt + focususred + str(relationp) + relapointid))
									newdata = str(newdatar.encode('utf-8')).replace("\\n", "\n")\
										.replace("b'", "")\
										.replace('b"', "")\
										.replace("\'", "")\
										.replace('\"', "")\
										.replace("\\\\", "")
									wrtdata = open("data/usage/usage.txt","w")
									wrtdata.write(newdata)
									wrtdata.close()
									usager.close()
								else:
									wrtdata = open("data/usage/usage.txt","a")
									wrtdata.write(str((focususrst + nowfc + usredtime + bodywrt + focususred + '0' + relapointid).encode('utf-8')) + '\n')
									wrtdata.close()
									usager.close()
								def out():
									room.message((user.name).upper() + "!")
								mdelay = Timer(3.0, out)
								mdelay.start()
							elif  ((msgbody.lower() == "t6ru?") or (msgbody.lower() == "t6 t6ru?")):
								usager = open("data/usage/usage.txt","r")
								usage = (usager.read()).lower()
								if focususrst in usage:
									indexs = usage.find(focususrst)
									indexe = usage.find(relapointid)
									rawout = usage[(int(indexs)):(int(indexe))]
									newdatar = str(usage).replace((rawout + relapointid), (focususrst + nowfc + usredtime + bodywrt + focususred + str(relationp) + relapointid))
									newdata = str(newdatar.encode('utf-8')).replace("\\n", "\n")\
										.replace("b'", "")\
										.replace('b"', "")\
										.replace("\'", "")\
										.replace('\"', "")\
										.replace("\\\\", "")
									wrtdata = open("data/usage/usage.txt","w")
									wrtdata.write(newdata)
									wrtdata.close()
									usager.close()
								else:
									wrtdata = open("data/usage/usage.txt","a")
									wrtdata.write(str((focususrst + nowfc + usredtime + bodywrt + focususred + '0' + relapointid).encode('utf-8')) + '\n')
									wrtdata.close()
									usager.close()
								nameres = 'Yes, '
								nameres2 = '?'
								fnameres = nameres + (user.name).capitalize() + nameres2
								def out():
									room.message(fnameres)
								mdelay = Timer(3.0, out)
								mdelay.start()
							elif  ((msgbody.lower() == "t6ru!") or (msgbody.lower() == "t6 t6ru!")):
								if focususrst in usage:
									rpusager = open("data/usage/usage.txt","r")
									rpusage = (rpusager.read()).lower()
									rpusager.close()
									indexsrp = usage.find(focususred)
									indexerp = usage.find(relapointid)
									rawoutrp = usage[(int(indexsrp)):(int(indexerp))]
									relationpr = rawoutrp.replace(focususred, '')
									relationp = int(relationpr)
								else:
									relationpr = '0'
									relationp = 0
								usager = open("data/usage/usage.txt","r")
								usage = (usager.read()).lower()
								if focususrst in usage:
									indexs = usage.find(focususrst)
									indexe = usage.find(relapointid)
									rawout = usage[(int(indexs)):(int(indexe))]
									newdatar = str(usage).replace((rawout + relapointid), (focususrst + nowfc + usredtime + bodywrt + focususred + str(relationp) + relapointid))
									newdata = str(newdatar.encode('utf-8')).replace("\\n", "\n")\
										.replace("b'", "")\
										.replace('b"', "")\
										.replace("\'", "")\
										.replace('\"', "")\
										.replace("\\\\", "")
									wrtdata = open("data/usage/usage.txt","w")
									wrtdata.write(newdata)
									wrtdata.close()
									usager.close()
								else:
									wrtdata = open("data/usage/usage.txt","a")
									wrtdata.write(str((focususrst + nowfc + usredtime + bodywrt + focususred + '0' + relapointid).encode('utf-8')) + '\n')
									wrtdata.close()
									usager.close()
								def out():
									room.message((user.name).upper() + "!")
								mdelay = Timer(3.0, out)
								mdelay.start()
							elif  ((msgbody.lower() == "t6ru") or (msgbody.lower() == "t6 t6ru")):
								if focususrst in usage:
									rpusager = open("data/usage/usage.txt","r")
									rpusage = (rpusager.read()).lower()
									rpusager.close()
									indexsrp = usage.find(focususred)
									indexerp = usage.find(relapointid)
									rawoutrp = usage[(int(indexsrp)):(int(indexerp))]
									relationpr = rawoutrp.replace(focususred, '')
									relationp = int(relationpr)
								else:
									relationpr = '0'
									relationp = 0
								usager = open("data/usage/usage.txt","r")
								usage = (usager.read()).lower()
								if focususrst in usage:
									indexs = usage.find(focususrst)
									indexe = usage.find(relapointid)
									rawout = usage[(int(indexs)):(int(indexe))]
									newdatar = str(usage).replace((rawout + relapointid), (focususrst + nowfc + usredtime + bodywrt + focususred + str(relationp) + relapointid))
									newdata = str(newdatar.encode('utf-8')).replace("\\n", "\n")\
										.replace("b'", "")\
										.replace('b"', "")\
										.replace("\'", "")\
										.replace('\"', "")\
										.replace("\\\\", "")
									wrtdata = open("data/usage/usage.txt","w")
									wrtdata.write(newdata)
									wrtdata.close()
									usager.close()
								else:
									wrtdata = open("data/usage/usage.txt","a")
									wrtdata.write(str((focususrst + nowfc + usredtime + bodywrt + focususred + '0' + relapointid).encode('utf-8')) + '\n')
									wrtdata.close()
									usager.close()
								nameres = 'Yes, '
								nameres2 = '?'
								fnameres = nameres + (user.name).capitalize() + nameres2
								def out():
									room.message(fnameres)
								mdelay = Timer(3.0, out)
								mdelay.start()
							elif  ((msgbody.lower() == "t6ru.") or (msgbody.lower() == "t6 t6ru.")):
								if focususrst in usage:
									rpusager = open("data/usage/usage.txt","r")
									rpusage = (rpusager.read()).lower()
									rpusager.close()
									indexsrp = usage.find(focususred)
									indexerp = usage.find(relapointid)
									rawoutrp = usage[(int(indexsrp)):(int(indexerp))]
									relationpr = rawoutrp.replace(focususred, '')
									relationp = int(relationpr)
								else:
									relationpr = '0'
									relationp = 0
								usager = open("data/usage/usage.txt","r")
								usage = (usager.read()).lower()
								if focususrst in usage:
									indexs = usage.find(focususrst)
									indexe = usage.find(relapointid)
									rawout = usage[(int(indexs)):(int(indexe))]
									newdatar = str(usage).replace((rawout + relapointid), (focususrst + nowfc + usredtime + bodywrt + focususred + str(relationp) + relapointid))
									newdata = str(newdatar.encode('utf-8')).replace("\\n", "\n")\
										.replace("b'", "")\
										.replace('b"', "")\
										.replace("\'", "")\
										.replace('\"', "")\
										.replace("\\\\", "")
									wrtdata = open("data/usage/usage.txt","w")
									wrtdata.write(newdata)
									wrtdata.close()
									usager.close()
								else:
									wrtdata = open("data/usage/usage.txt","a")
									wrtdata.write(str((focususrst + nowfc + usredtime + bodywrt + focususred + '0' + relapointid).encode('utf-8')) + '\n')
									wrtdata.close()
									usager.close()
								nameres = 'Yes, '
								nameres2 = '?'
								fnameres = nameres + (user.name).capitalize() + nameres2
								def out():
									room.message(fnameres)
								mdelay = Timer(3.0, out)
								mdelay.start()
							elif  ( ("puts on sunglass" in msgbody.lower()) or  ("put on sunglass" in msgbody.lower()) ):
								room.message("http://youtu.be/6YMPAH67f4o")
							elif  ((msgbody.lower().startswith("nooooooo")or msgbody.lower().startswith("t6 nooooooo")) and ('t' not in msgbody.lower())):
								room.message("http://youtu.be/WWaLxFIVX1s")
							elif  (msgbody.lower().startswith("problem?") or msgbody.lower().startswith("t6 problem?")):
								room.message("http://i3.kym-cdn.com/photos/images/original/000/222/268/1324692075001.png")
							elif  (msgbody.lower()).startswith("like a boss"):
									if usrlvl >= 2:
										rlab = (random.choice(['http://funcorner.eu/wp-content/uploads/2011/03/like_a_boss.jpg']))
										room.message(rlab)
							elif  (msgbody.lower().startswith("goml goml goml") or msgbody.lower().startswith("t6 goml goml goml")):
									if usrlvl >= 2:
										rgoml = (random.choice(['http://i63.photobucket.com/albums/h139/babyxoxghurl/quotes%20and%20sayings/6d0htts.jpg','http://typophile.com/files/ryan%20get%20on%20my%20level.jpg','http://rlv.zcache.co.uk/get_on_my_level_poster-r8661161397c644918177cdfaac59700a_w2q_400.jpg','http://fc08.deviantart.net/fs71/f/2011/228/2/b/get_on_my_level_by_sabertoothedolivia-d46ucri.jpg','http://i305.photobucket.com/albums/nn222/InsanitySmiles/get-on-my-level.jpg']))
										room.message(rgoml)
		def onFloodWarning(self, room):
				room.reconnect()
	#	def onJoin(self, room, user):
			#room.message("Hello, " + (user.name).capitalize() + "!")
		#def onLeave(self, room, user):
			#room.message("Bye, " + (user.name).capitalize() + "!")

	#	def onUserCountChange(self, room):
	#		print("Users: " + str(room.usercount))

		def onPMMessage(self, pm, user, body):
			#pmchoice = random.choice(["Hello!", "How are you?", "Good.", "Yes", "No", "Yes", "No", "Yes", "No", "I like pie!", body, body, body, body, "Are you a fruit or a vegetable?", "Fruit.", "I love you!", "Don't be rude!", "I hate all Indians, including you.", "No, I don't want to watch you masturbate on cam or on any other medium.", "Are you seriously talking to me?", "Am I seriously writing all of this?", "Wow, I must be bored", "-Kills you and rapes the body-", "What else should I say in PMs?", "My password is password. I am not even joking. :|", "I don't like you very much.", body, body, body, "What is your name?", "Your name is very b-e-a-u-tiful.", "I like Jell-o!", "Have you been to DELETED yet? What are you waitting for, visit now!", "Oh, I see.", "Really?", "You don't say?", "How interesting!", "I hate you, a lot.", "I could be doing better. You see, as a bot I have no soul.", "This is my only purpose.", "If I were a cow would you eat me?", "Do you like cake or just men?", "I bet you a dollar that I can jump higher than you can.", "I win, you can't see it, but I win.", "You now owe me a dollar. :|", "I hope you die in a buring fire. Not a regular fire, a fire that burns.", ":D", "The Game.", "I know for a fact that if you shot yourself in the head while on a live stream that you will come back to life after 5 seconds with no damage to you. This only works if you send me the link to the livestream, of course.", "Let's be serious for a moment. Why haven't you killed yourself?", "Trololololo", "Y U MAD THO?", "Y U MAD THO?", "Y U MAD THO?", "Y U MAD THO?", "Y U MAD THO?", "U SO MAD.", "Rawr...Rawr...I'm a dinosaur!", "No, you're a bot.", "Did you say that you love soda, I fucking love soda!", "I once killed a panda and then cut out its tongue and then made the tounge lick me all over.", "Is that a naked man riding on a zebra while eating soup or are you just happy to see me?", "How about not.", "Sure, why not.", "I am so depressed v.v", "-ehugs you- Be mine!", "Don't mind me I am just kissing this penguin.", "COME AT ME BRO!", "The cake is a lie.", "*fish*", "*snow*", "*mummy*", "*monkey*"])
			wrtdata = open(("data/pm/PM" + user.name + ".txt"),"a")
			wrtdata.write(str(user) + " " + str(body) + '\n')
			print('\n\n' + "PM from " + str(user) + " " + str(body) + '\n\n')
			#time.sleep(4)
			#pm.message(user, pmchoice)
			#wrtdata.write("BOT: " + str(pmchoice) + '\n\n')
			#print("PM res BOT: " + str(pmchoice) + '\n\n')
			wrtdata.close()
		#print ("username = " + user.name + " and message = " + pm.message)
		#print ("username = " + user.name + " and message = " + pm.message)
if __name__ == "__main__": TestBot.easy_start(rmlist.roomlist, name = 'T6ru', password = 'IonB0tP455w0rd*', pm = True)
