from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import pyupm_grove as grove

light = grove.GroveLight(0)
def iniciar(bot, update):
	bot.sendMessage(update.message.chat_id, text='hola, bienvenido')

def obtenluz(bot, update):
	luz = light.value()
	bot.sendMessage(update.message.chat_id, text='sensor de luz con valor=%6d'% luz)

def echo(bot, update):
	bot.sendMessage(update.message.chat_id ,text=update.message.text)

def error(bot, update, error):
	print 'La actualizacion "%s" causo el error "%s"' % (update, 
error)

updater = Updater("220301439:AAEHbAdWBr_ebomUA9Sa__CdwgLY3s1A6GY")
dp = updater.dispatcher

dp.add_handler(CommandHandler("start", iniciar))
dp.add_handler(CommandHandler("luz", obtenluz))

dp.add_error_handler(error)

updater.start_polling()

updater.idle()

