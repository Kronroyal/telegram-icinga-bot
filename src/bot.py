import telebot
import sys
import yaml
import argparse
# in telebot.TeleBot("TOKEN") one should specify the Token which was received by @BotFather from Telegram
with open("whitelist.yaml") as f:
    data=yaml.load(f, Loader=yaml.FullLoader)
    token=data['token']
    print(token)
    bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start'])
def send_welcome(m): #get chat_id of chats
    cid=m.chat.id 
    bot.send_message(chat_id=cid,text="Hello! 🧑 ' I am a Notifier-Bot for TOP-Net👁️ Project")
    msg="Your UID is: " + str(cid)
    bot.send_message(chat_id=cid,text=msg)
    with open("whitelist.yaml") as f:
        data=yaml.load(f,Loader=yaml.FullLoader)
        whitelisted=data['receivers']
        if str(cid) in whitelisted:
            bot.send_message(chat_id=cid,text="You are already whitelisted!")
        else:
            bot.send_message(chat_id=cid,text="Please add yourself to the receivers in whitelist! -> whitelist.yaml")

def bot_send_warning(cid,message):
    #try:
    messagelist=message[0]
    msgcontent= ' '.join(messagelist[0:])
    
    if(len(msgcontent)>=5000):
        print("Passed message content must be less than 5000 chars!\n")
    else:
        bot.send_message(chat_id=cid,text=msgcontent)
        print("message sent to",cid,":",msgcontent)

if __name__=="__main__":
    parser=argparse.ArgumentParser()
    parser.add_argument("-d", "--daemon",action="store_true",help="Spawn Bot as daemon")
    parser.add_argument("-m", "--message",nargs="+",action="append",help="Send Message to User!")
    args=parser.parse_args()
    if args.daemon is True:
        print("now running in daemon mode 👹 [...]")
        
        bot.polling()
    elif args.message is not None:
        with open("whitelist.yaml") as f:
            data=yaml.load(f, Loader=yaml.FullLoader)
            whitelisted=data['receivers']
            for receiver in whitelisted:
                bot_send_warning(receiver,args.message)      
    else:
        print("Specify either -m or -d!")
        exit(1)
    