#-- coding: utf-8 --
import telebot #importando a biblioteca pyTelegramBotAPI
from telebot import types #esta selecionando a lib types que faz parte do telebot

API_TOKEN = '1752787298:AAHuFGnIH4gar_cMpTc-sJjwwwCe22mEO5A' #@botfather

bot = telebot.TeleBot(API_TOKEN) #telebot-sumario e TeleBot(comando aplicando token)

#inicio

@bot.message_handler(commands=['start']) #recebo mensagem /start
def send_welcome(message):
	cid = message.chat.id #pegar id da conversa
	msg = bot.reply_to(message,"Olá, bem vindo a SafeGym, \n Nosso id é: " + str(cid)) #mensagem enviada para o usuario
	bot.send_message(cid, "Caso precise de ajuda, use a função /ajuda")

#ajuda

@bot.message_handler(commands=['ajuda'])
def send_help(message):
	cid = message.chat.id
	msg_help = bot.reply_to(message,"O que você deseja? \n Opção 1: /cadastro \n Opção 2: /treino \n Opção 3 : /Quantidade") 
	bot.send_message(cid, "Caso ainda encontre dificuldades, fale conosco pelo email: safegym@gmail.com")

#categorias

@bot.message_handler(commands=['treino'])
def send_category(message):
	cid = message.chat.id
	markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)#crio o layout de opçoes, digo para ele que só pode selecionar uma opção
	markup.add('Superiores', 'Inferiores')#opções que devem aparecer para o cliente
	msg_cat = bot.reply_to(message,"Escolha o treino que você deseja:", reply_markup = markup)#qual das categorias voce quer		
bot.polling() #escuta o usuario

