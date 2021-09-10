#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ---------------------
# Telegram : @DIBIBl , @TDTDI ,@ruks3
# Coded by ruks
# YouTube : https://youtube.com/channel/UCUNbzQRjfAXGCKI1LY72DTA
# Instagram : https://instagram.com/_v_go?utm_medium=copy_link
# ---------------------
import requests,time,random
from user_agent import generate_user_agent
def send_uesr(uesr):
	tt=time.asctime()
	req = requests.post(f'https://api.telegram.org/bot{tok}/sendMessage?chat_id={id}&text=⌯  ʜɪ ѕɪʀ  ⌯\n. — — — — —  — — — — — . \n⌯ ᴜѕᴇʀɴᴀᴍᴇ : @{uesr}\n⌯ {tt} \n. — — — — —  — — — — —\n• Tele : @DIBIBl . @RUKS3 .')
def run(uest):
	try:	
		ruks=requests.get(f"https://m.twitch.tv/{uesr}",headers={
	'Host': 'm.twitch.tv','Connection': 'keep-alive','sec-ch-ua': '"Google Chrome";v="93", " Not;A Brand";v="99", "Chromium";v="93"','sec-ch-ua-mobile': '?1','sec-ch-ua-platform': '"Android"','Save-Data': 'on','Upgrade-Insecure-Requests': '1','User-Agent': generate_user_agent(),'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','Sec-Fetch-Site': 'none','Sec-Fetch-Mode': 'navigate','Sec-Fetch-User': '?1','Sec-Fetch-Dest': 'document'}).status_code
		return ruks
	except:
		pass
ruks_ = '\033[1;36m'	
ruks__ = '\033[1;36m'
jruks = '\033[1;33m'
_ruks  = '\033[1;31m'
BGreen='\033[1;32m'
BRed ='\033[1;31m'
Number =0
T=("="*60)
print(f"""{BRed}{T}
{BGreen}


	 ______  __    __  ____  ______    __  __ __ 
	|      T|  T__T  Tl    j|      T  /  ]|  T  T
	|      ||  |  |  | |  T |      | /  / |  l  |
	l_j  l_j|  |  |  | |  | l_j  l_j/  /  |  _  |
	  |  |  l  `  '  ! |  |   |  | /   \_ |  |  |
	  |  |   \      /  j  l   |  | \     ||  |  |
	  l__j    \_/\_/  |____j  l__j  \____jl__j__j
                                             
	        __          __       __             
	 ____  / /  __ __  / /___ __/ /__ ___   ____
	/___/ / _ \/ // / / __/ // /  '_/(_-<  /___/
	     /_.__/\_, /  \__/\_,_/_/\_\/___/       
	          /___/                             
	            

{BRed}{T}""")

tok = input(jruks+'['+_ruks+'+'+jruks+']'+ruks__+' TOKEN BOT ! -> ; '+BGreen)
id = input(jruks+'['+_ruks+'+'+jruks+']'+ruks__+' ID ! -> ; '+BGreen)
try:
	count = int(input(jruks+'['+_ruks+'+'+jruks+']'+ruks__+' Character count ! -> ; '+BRed))
except:
	print("="*30)
	print("Please put numbers only")
	exit(0)
if count >10: print("="*30),print("Please write a number less than 10"),exit()	
			
	
if __name__ == '__main__':
	print(T)	
	while True:
		Number+=1
		uesr = str("".join(random.choice( 'poiuytrewqasdfghjklmnbvcxz1234567890_')for i in range(count)))
		ruks3=run(uesr)
		print(ruks3)	
		if ruks3 == 404:
			print(jruks+'['+BGreen+f'{Number}'+jruks+'] Available'+BGreen+f' [{uesr}]')
			send_uesr(uesr)
		elif ruks3 == 200:
			print(jruks+'['+BRed+f'{Number}'+jruks+'] Unavailable'+BRed+f'-[{uesr}]')
		else: 
			print(jruks+'['+BRed+f'{Number}'+jruks+'] Unavailable'+BRed+f'-[False]')
			
			