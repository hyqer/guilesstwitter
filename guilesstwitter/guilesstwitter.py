import sys
import win32con
import ctypes
import re,os
keyid=1002
class KeyHook:
    '''Key hook to catch global Hotkey.

    '''
    def __init__(self,
            hotkey={'hotkey' : win32con.MOD_ALT, 'modifiers': ord('R')}):
        global keyid
        self.register_hotkey(keyid, hotkey)
        keyid+=1

    def register_hotkey(self, id, hotkey):
        byref = ctypes.byref
        user32 = ctypes.windll.user32

        if not user32.RegisterHotKey(None,
                                    id,
                                    hotkey['hotkey'],
                                    hotkey['modifiers']):
            print"Unable to register hotkey",hotkey['modifiers']
        else: print "register hotkey",hotkey['modifiers'],"ok" 







from twitter import *
import win32gui
import time
class Guiless:
	def __init__(self,name,password,domain="twitter.com"):
		self.twitter=Twitter(name,password,domain=domain)
		self.tl=self.twitter.statuses.friends_timeline()
		hotkey={'hotkey' : win32con.MOD_CONTROL|win32con.MOD_SHIFT, 'modifiers': win32con.VK_DOWN}
		key1 = KeyHook(hotkey)
		hotkey={'hotkey' : win32con.MOD_CONTROL|win32con.MOD_SHIFT, 'modifiers': win32con.VK_UP}
		key2 = KeyHook(hotkey)
		hotkey={'hotkey' : win32con.MOD_CONTROL|win32con.MOD_SHIFT, 'modifiers': ord('R')}
		key3 = KeyHook(hotkey)
		hotkey={'hotkey' : win32con.MOD_CONTROL|win32con.MOD_SHIFT, 'modifiers': ord('Z')}
		key4 = KeyHook(hotkey)
		hotkey={'hotkey' : win32con.MOD_CONTROL|win32con.MOD_SHIFT, 'modifiers': ord('C')}
		key5 = KeyHook(hotkey)
		hotkey={'hotkey' : win32con.MOD_CONTROL|win32con.MOD_SHIFT, 'modifiers': win32con.VK_RIGHT}
		key6 = KeyHook(hotkey)
		hotkey={'hotkey' : win32con.MOD_CONTROL|win32con.MOD_SHIFT, 'modifiers': win32con.VK_LEFT}
		key7 = KeyHook(hotkey)
		hotkey={'hotkey' : win32con.MOD_CONTROL|win32con.MOD_SHIFT, 'modifiers': ord('O')}
		KeyHook(hotkey)
		self.index=0
		self.hLast = win32gui.GetForegroundWindow()
		self.sLast = win32gui.GetWindowText(self.hLast)
		win32gui.SetWindowText(self.hLast,self.tl[0]['user']['screen_name']+":"+self.tl[0]['text'])
		self.pos = 0
		self.page = 1
	def show_next(self):
		if(self.index+1<len(self.tl)):
			self.index+=1
		else:
			self.page += 1
			newpg = self.twitter.statuses.friends_timeline(page=self.page)
			#print len(newpg)
			if len(newpg)==0:
				return
			else:
				self.tl = self.tl+newpg
				self.index+=1
				
		self.pos = 0
		self.show_tweet()
		#print "next"
	
	def show_tweet(self):
		hTop=win32gui.GetForegroundWindow()
		if hTop != self.hLast:
			if win32gui.IsWindow(self.hLast):
				win32gui.SetWindowText(self.hLast,self.sLast)
			self.hLast = hTop
			self.sLast = win32gui.GetWindowText(self.hLast)
		#print "index",self.index,"len",len(self.tl)
		win32gui.SetWindowText(hTop,self.tl[self.index]['user']['screen_name']+":"+self.tl[self.index]['text'][self.pos:].replace("\n",' '))
	def show_prev(self):
		if(self.index>0):
			self.index-=1
		else:
			return
		self.pos = 0
		self.show_tweet()
		#print "prev"

	def refresh(self):
		self.tl = self.twitter.statuses.friends_timeline()
		self.index=0
		self.pos = 0
		self.page = 1
		self.show_tweet()
		#print "refresh"

	def restore(self):
		if win32gui.IsWindow(self.hLast):
			win32gui.SetWindowText(self.hLast,self.sLast)
	def more(self):
		if((self.pos+1)<len(self.tl[self.index]['text'])):
			self.pos +=1
			self.show_tweet()
	def less(self):
		if(self.pos>0):
			self.pos -=1
			self.show_tweet()
	def open_url(self):
		url_pat = re.compile(r'[a-zA-z]+://[^\s]*')
		urls=url_pat.findall(self.tl[self.index]['text'])
		for url in urls:
			os.system("start "+url)




#hTop=win32gui.GetForegroundWindow()
#twitter=Twitter('','')
#tl=twitter.statuses.friends_timeline()
#for a in range(len(tl)):print tl[a]['user']['screen_name'],":",tl[a]['text']
#conf={"update_to":"title"}

#if hTop>0:
#	win32gui.SetWindowText(hTop,tl[a]['user']['screen_name']+":"+tl[a]['text'])
from getpass import getpass
if len(sys.argv)<2:
	#print "usage:%s <usrname>"%sys.argv[0]
	#sys.exit()
	sys.argv.append(raw_input("input you twitter account:"))
pas = getpass("Twitter password: ")
gui=Guiless(sys.argv[1],pas,domain="javatweet.appspot.com/api")
#search 'Twitter API proxy list' to find more

from ctypes import wintypes
msg = wintypes.MSG()
lpmsg = ctypes.byref(msg)
user32 = ctypes.windll.user32
while user32.GetMessageW(lpmsg, 0, 0, 0):
	if (msg.message == win32con.WM_HOTKEY):
		#print "WM_HOTKEY received\n"
		#print "wParam", msg.wParam
		#print "lParam", msg.lParam
		#print "time", msg.time
		#print "pt", msg.pt
		if msg.wParam == 1002:#NPRZCML
			gui.show_next()
		if msg.wParam == 1003:
			gui.show_prev()
		if msg.wParam == 1004:
			gui.refresh()
		if msg.wParam == 1005:
			gui.restore()
		if msg.wParam == 1006:
			gui.restore()
			break
		if msg.wParam == 1007:
			gui.more()
		if msg.wParam == 1008:
			gui.less()
		if msg.wParam == 1009:
			gui.open_url()







print "bye."






#hTop=win32gui.GetForegroundWindow()
#twitter=Twitter('','')
#tl=twitter.statuses.friends_timeline()
#for a in range(len(tl)):print tl[a]['user']['screen_name'],":",tl[a]['text']
#conf={"update_to":"title"}

#if hTop>0:
#	win32gui.SetWindowText(hTop,tl[a]['user']['screen_name']+":"+tl[a]['text'])
	
	
