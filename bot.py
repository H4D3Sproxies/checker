from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters
import traceback

from database import get_user_action, add_update_action
from cc_killer import CC_killer
from proxy import Proxy
from database import initialize_tables

TOKEN = '7553835081:AAEm5w5DE--GA2lBDyNz1YETTb9wsM5ISRM' #'8053702073:AAEjF9xD_GoycTy3FOpwCsuhJg0xYUmgFGE'

class Bot():
    _instance = None
    
    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance

    def __init__(self):
        self.cc_killer = CC_killer()
        self.proxy = Proxy()
        
    ################ Commands
    
    async def start(self, update: Update, context):
        user = update.message.from_user
        
        add_update_action(user.id, 'start')
        
        await update.message.reply_text(f'Please insert card details in the format of: number|month|year|cvv\n\n example: 5874589654125968|06|27|584')

    async def proxies(self, update: Update, context):
        user = update.message.from_user
        
        add_update_action(user.id, 'proxies')

        await update.message.reply_text(f'Please insert proxies in the format of: ip:port\nip:port\n\n example: 111.111.111.111:1111\n222.222.222.222:2222')


    ################ Methods
    
    async def upload_proxies(self, update, user_id, msg):
        proxies = msg.split('\n')
        
        for proxy in proxies:
                ip, port = proxy.split(':')
                
                if not self.proxy.insert_proxy(user_id, ip, port):
                    
                    await update.message.reply_text(f'proxy with ip: {ip}, is a bad proxy -- not saved')
    
    ################ Handlers
    
    async def handle_message(self, update: Update, context):
        user_id = update.message.from_user.id
        msg = update.message.text
        user_action = get_user_action(user_id)
        
        print(user_action)
        
        if user_action == 'start':
            try:                
                self.cc_killer.cc_kill(msg)
            
            except:
                await update.message.reply_text('Something went wrong when cc killing please contact admin')
                
        elif user_action == 'proxies':
            try:
                await self.upload_proxies(update, user_id, msg)
            
                await update.message.reply_text('proxies uploading proccess finished successfully')
                
            except Exception as err:
                traceback.print_exc()
                await update.message.reply_text('Something went wrong when uploading proxies please contact admin')
            
    def main(self):
        app = Application.builder().token(TOKEN).build()
        
        app.add_handler(CommandHandler('start', self.start))
        app.add_handler(CommandHandler('proxies', self.proxies))
        app.add_handler(MessageHandler(filters.TEXT, self.handle_message))

        print('Bot is running...')
        app.run_polling(1)

if __name__ == '__main__':
    initialize_tables()
    
    bot = Bot()
    bot.main()