#-- coding: utf-8 --
import telebot  #biblioteca bot
import json #valores em json - xml
import urllib #tratar urls
from urllib2 import urlopen
 
 
API_TOKEN = '1752787298:AAHuFGnIH4gar_cMpTc-sJjwwwCe22mEO5A' #@botfather
 
bot = telebot.TeleBot(API_TOKEN) #telebot-sumario e TeleBot(comando) aplicando token
 
@bot.message_handler(commands=['cep']) #mensagem digitada
 
def send_cep(message):
    msg = bot.reply_to(message," Digite o cep que deseja consultar: ") #responde o comando /cep com uma ação
    cid = message.chat.id #pega o id da conversa
    bot.register_next_step_handler(msg, send_cep_step) #armazena a informação digitada e joga para o próximo passo(mensagem digitada -> próximo passo)
 
def send_cep_step(message):
    cid = message.chat.id #pegar o id da conversa
    mensagem_cep = message.text #mensagem digitada
    url = "https://viacep.com.br/ws/" + mensagem_cep + "/json/"

#-------------------- 
# A partir daqui, ou seja, acrescentando essas linhas abaixo, aí sim a busca por CEP funcionou, exibindo tudo abaixo do "print(data)". Sem isso, o código não exibe informações sobre o CEP que solicita do usuário.
#-------------------- 
 
#    response = urllib.urlopen(url) #[não funcionou para urllib.urlopen(...), apresentando a mensagem de erro: "AttributeError: module 'urllib' has no attribute 'urlopen' "
 
    response = urllib.urlopen(url) #abrir a url que nós colocamos, que seria o json
 
    data = json.loads(response.read()) #carregar o json e ler os valores do json
 
    print(data)
    cep = data['cep']
    logradouro = data['logradouro']
    bairro = data['bairro']
    localidade = data['localidade']
    uf = data['uf']
 
    bot.send_message(cid,"\nCEP: " + cep + "\nLogradouro: " + logradouro + "\nBairro: " + bairro + "\nLocalidade: " + localidade + "\nUF: " + uf )
 
bot.polling() #escuta usuário
