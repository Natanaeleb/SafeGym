#-- coding: utf-8 --
import requests
import telebot
from telebot import types
import pymysql #biblioteca de conexão com o MySQL

conn = pymysql.connect(host='127.0.0.1',
unix_socket='/opt/lampp/var/mysql/mysql.sock', #qual base ele deve se conectar
user='root', #usuario
passwd=None, #vazio
db='alunos_safegym') #nome do banco de dados

#127.0.0.1 é igual localhost
cur = conn.cursor() #conexao com o xampp

API_TOKEN = '1752787298:AAHuFGnIH4gar_cMpTc-sJjwwwCe22mEO5A' #@botfather
 
bot = telebot.TeleBot(API_TOKEN) #telebot-sumario e TeleBot(comando) aplicando token

user_dict = {} #variaveis unicas

class User:
	def __init__(self,name):
		self.name = name
		self.age = None
		self.treino = None
		self.mail = None

@bot.message_handler(commands=['start'])
def send_welcome(message):
	msg = bot.reply_to(message, 'Bem vindo ao bot de treinos SafeGym')
	cid = message.chat.id #numero
	bot.send_message(cid, "Nosso id é: " + str(cid) + "Este bot serve para enviar seus treinos em caso de dúvidas, \nQual seu nome?")
	bot.register_next_step_handler(msg,process_name_step)

def process_name_step(message):
	try:
		chat_id = message.chat.id
		name = message.text #nome digitado a variavel name
		user = User(name) #alocando o nome dele na variavel user
		user_dict[chat_id] = user #armazenando o chat_id desta conversa, unico
		msg = bot.reply_to(message, 'Quantos anos você tem?')
		bot.register_next_step_handler(msg,process_age_step)
	except Exception as e:
		bot.reply_to(message,e)

def process_age_step(message):
	try:
		chat_id = message.chat.id
		age = message.text
		if not age.isdigit():
			msg = bot.reply_to(message,'Você precisa digitar um número! Quantos anos você tem?')
			bot.register_next_step_handler(msg,process_age_step)			
			return			  				
		user = user_dict[chat_id]  
		user.age = age
		markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
		markup.add('Superiores', 'Inferiores') #quais categorias
		msg = bot.reply_to(message, 'Qual treino você tem duvidas?',reply_markup=markup)
		bot.register_next_step_handler(msg, process_treino_step)
	except Exception as e:
		bot.reply_to(message,'Ops, algo deu errado')
		print(e)

def process_treino_step(message):
	try:
		chat_id = message.chat.id
		treino = message.text
		user = user_dict[chat_id]
		if (treino == u'Superiores') or (treino == u'Inferiores'):
			user.treino = treino
		else:
			raise Exception()
		msg = bot.reply_to(message, 'Qual o seu email?')
		bot.register_next_step_handler(msg,process_mail_step)
	except Exception as e:
		bot.reply_to(message,e)

def process_mail_step(message):
	try:
		chat_id = message.chat.id
		mail = message.text #nome digitado a variavel name
		user = user_dict[chat_id] #alocando o nome dele na variavel user

		#nome da base
		cur.execute("USE alunos_safegym")#executando base a ser usada
		sql = "INSERT INTO usuario (nome_usuario,chatid_usuario,treino_usuario, email_usuario,idade_usuario) VALUES(%s,%s,%s,%s,%s)"
		val = (user.name,str(chat_id),user.treino,mail,str(user.age))
		cur.execute(sql,val)#comando insert+valores
		print(val)
		conn.commit()#açao do comando digitado
		cur.close()
		conn.close()
		
		msg = bot.reply_to(message, "Tenha um otimo treino!")
		
	except Exception as e:
		bot.reply_to(message,e)

bot.enable_save_next_step_handlers(delay=2)
bot.load_next_step_handlers()

bot.polling()





