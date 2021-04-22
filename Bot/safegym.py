#-- coding: utf-8 --
import telebot #importando a biblioteca pyTelegramBotAPI
from telebot import types #esta selecionando a lib types que faz parte do telebot

API_TOKEN = '1752787298:AAHuFGnIH4gar_cMpTc-sJjwwwCe22mEO5A' #@botfather

bot = telebot.TeleBot(API_TOKEN) #telebot-sumario e TeleBot(comando aplicando token)

#inicio

class User:
	def __init__(self,name):
		self.name = name
		self.age = None
		self.treino = None
		self.mail = None

@bot.message_handler(commands=['start'])
def send_welcome(message):
	msg = bot.reply_to(message, 'Bem vindo ao bot de treinos SafeGym!')
	cid = message.chat.id #numero
	bot.send_message(cid, "Este bot serve para enviar seus treinos caso tenha dúvidas. Para escolher seu treino digite: /treino")
	#bot.register_next_step_handler(msg,process_name_step)

@bot.message_handler(commands=['treino'])
def process_name_step(message):
	try:
		cid = message.chat.id #numero
		msg = bot.reply_to(message, 'Qual o treino de hoje? \nTreino A (Superior), digite 1 \nTreino B (Inferiores), digite 2 \nTreino C (Cardio), digite 3')
		bot.register_next_step_handler(msg,process_tipo_step)
	except Exception as e:
		bot.reply_to(message,e)


		#bot.send_message(cid, "Você quer o documento impresso ou o documento digital?. Para obter o digital, escreva: /digital \n  Para obter o impresso escreva: /impresso")
def process_tipo_step(message):
		try:
			chat_id = message.chat.id
			cid = message.chat.id #numero
			treino = message.text
			#user = user_dict[chat_id]
			if (treino == u'1') or (treino == u'2') or (treino == u'3'):
				msg = bot.reply_to(message, 'Você quer o documento impresso ou o documento digital? \nPara obter o digital, digite: D \nPara obter o impresso digite: I')
				#bot.send_message(cid, "Você quer o documento impresso ou o documento digital? \n Para obter o digital, digite: D \n Para obter o impresso digite: I")
			else:
				raise Exception()
			bot.register_next_step_handler(msg,process_escolha_step)
		except Exception as e:
			bot.reply_to(message,e)

def process_escolha_step(message):
		try:
			chat_id = message.chat.id
			cid = message.chat.id #numero
			escolha = message.text
			if (escolha == u'I'):
				msg = bot.reply_to(message, 'Retire seu treino na impressora e tenha um ótimo treino!')
			if (escolha == u'D'):
				msg = bot.reply_to(message, 'Aqui esta, tenha um ótimo treino!')
			else:
				raise Exception()
		except Exception as e:
			bot.reply_to(message,e)

bot.polling() #escuta o usuario


