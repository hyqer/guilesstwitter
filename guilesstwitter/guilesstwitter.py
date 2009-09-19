import sys
import win32con
import ctypes
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
	def __init__(self,name,password):
		self.twitter=Twitter('hyqer','111111')
		self.tl=self.twitter.statuses.friends_timeline()
		hotkey={'hotkey' : win32con.MOD_CONTROL|win32con.MOD_SHIFT, 'modifiers': ord('N')}
		key1 = KeyHook(hotkey)
		hotkey={'hotkey' : win32con.MOD_CONTROL|win32con.MOD_SHIFT, 'modifiers': ord('P')}
		key2 = KeyHook(hotkey)
		hotkey={'hotkey' : win32con.MOD_CONTROL|win32con.MOD_SHIFT, 'modifiers': ord('R')}
		key3 = KeyHook(hotkey)
		hotkey={'hotkey' : win32con.MOD_CONTROL|win32con.MOD_SHIFT, 'modifiers': ord('Z')}
		key4 = KeyHook(hotkey)
		hotkey={'hotkey' : win32con.MOD_CONTROL|win32con.MOD_SHIFT, 'modifiers': ord('C')}
		key4 = KeyHook(hotkey)
		self.index=0
	def show_next():
		print "next"
	

	def show_prev():
		print "prev"

	def refresh():
		print "refresh"

	def restore():
		print "restore"




#hTop=win32gui.GetForegroundWindow()
#twitter=Twitter('hyqer','111111')
#tl=twitter.statuses.friends_timeline()
#for a in range(len(tl)):print tl[a]['user']['screen_name'],":",tl[a]['text']
#conf={"update_to":"title"}

#if hTop>0:
#	win32gui.SetWindowText(hTop,tl[a]['user']['screen_name']+":"+tl[a]['text'])
t=Guiless('hyqer','111111')
from ctypes import wintypes
msg = wintypes.MSG()
lpmsg = ctypes.byref(msg)
user32 = ctypes.windll.user32
while user32.GetMessageW(lpmsg, 0, 0, 0):
	if (msg.message == win32con.WM_HOTKEY):
		print "WM_HOTKEY received\n"  
		break







from getpass import getpass
getpass("press enter to exit.")






#hTop=win32gui.GetForegroundWindow()
#twitter=Twitter('hyqer','111111')
#tl=twitter.statuses.friends_timeline()
#for a in range(len(tl)):print tl[a]['user']['screen_name'],":",tl[a]['text']
#conf={"update_to":"title"}

#if hTop>0:
#	win32gui.SetWindowText(hTop,tl[a]['user']['screen_name']+":"+tl[a]['text'])
	
	