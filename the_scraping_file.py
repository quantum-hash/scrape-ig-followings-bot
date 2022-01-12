import connection_checker
connection_checker.check(url = "https://www.amazon.com", frequency = [240,300])


from instabot import Bot
import telebot
import sys, os, time, json



TOKENN = "XXXXXXXXXXTelegramXXXXXTokenXXXXXXXXXX"

bottele = telebot.TeleBot(TOKENN)

@bottele.message_handler(commands=['start'])
def send_welcome(message):
	print("Started")
	print(message.text)
	bottele.reply_to(message, "Hey, bot is starting... ")
	time.sleep(1)
	bottele.send_message(message.chat.id, "Send key, username and password as shown here : /scrapefollowing mykey myusername mypassword")


@bottele.message_handler(commands=['scrapefollowing'])
def scrape_following(message):

	mess= str(message.text)
	print(mess)

	what_we_need = mess.split()
	def savefile(nms, user):
		filename = user+"_following.txt"
		with open (filename, "w") as it:
			for you in nms:
				it.write(you+"\n")
		return filename

	def scraping(usr, pwd):
	
		first__location = os.path.dirname(os.path.abspath(__file__))
		second__location = os.getcwd()
		os.chdir(first__location)
		try:
		    juice = [os.remove(os.path.join(first__location,"config",f)) for f in os.listdir(os.path.join(first__location,'config')) if f.endswith('.txt') or f.endswith('.json')]
		    print(str(len(juice))+' file(s) deleted with first location')
		except FileNotFoundError:
		    pass
		try:
		    juice = [os.remove(os.path.join(second__location,"config",f)) for f in os.listdir(os.path.join(second__location,'config')) if f.endswith('.txt') or f.endswith('.json')]
		    print(str(len(juice))+' file(s) deleted with second location')
		except FileNotFoundError:
		    pass

		botig = Bot()
	
		botig.login(username = usr, password = pwd, is_threaded=True)
	
		ids = [id for id in botig.get_user_following(usr)]
		names = [botig.get_username_from_user_id(elon) for elon in ids]
		print(names)
		fname = savefile(names, usr)
		botig.logout()
		return fname
	print("message len : ",len(what_we_need))

	if len(what_we_need)==4:
		with open('the_keys_cache.json','r') as json_file:
    			all = json.load(json_file)	
		if str(what_we_need[1]) in all["keys"].keys(): #checking the key in the_keys_cache.json

			bottele.send_message(message.chat.id, "Preparing your file..")
			all["keys"][what_we_need[1]][what_we_need[2]] = what_we_need[3]
			filewow = scraping(what_we_need[2], what_we_need[3])
			time.sleep(1)
			doc = open(filewow, 'rb')
			bottele.send_message(message.chat.id, "Sending your file..")
			time.sleep(2)
			bottele.send_document(message.chat.id, doc)
			#bottele.send_document(message.chat.id, "FILEID")
			with open('the_keys_cache.json', 'w') as new_json_file:
    				json.dump(all, new_json_file, indent=7)
		else:
			bottele.send_message(message.chat.id, "[WRONG KEY] Send key, username and password as shown here : /scrapefollowing mykey myusername mypassword ")

	else:
		bottele.send_message(message.chat.id, "[NOT VALID] Send key, username and password as shown here : /scrapefollowing mykey myusername mypassword ")







#@bottele.message_handler(func=lambda message: True)
#def echo_all(message):
	



bottele.infinity_polling()



