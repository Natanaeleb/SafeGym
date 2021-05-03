#include <csignal>
#include <cstdio>
#include <cstdlib>
#include <exception>
#include <string>

#include <tgbot/tgbot.h>

using namespace std;
using namespace TgBot;

#define TOKEN "1651736494:AAEI-uA6dMDnn8pPLH-10vfbSMyzzGBlsvc"

int main(int argc, char *argv[])
{
	Bot bot(TOKEN);
	
    const string photoMimeType = "image/jpeg";
	
	bot.getEvents().onCommand("start", [&bot](Message::Ptr message) {
        bot.getApi().sendMessage(message->chat->id, "Bem vindo ao bot de treinos SafeGym!");
		bot.getApi().sendMessage(message->chat->id, "Este bot serve para enviar seus treinos caso tenha dúvidas. Para escolher seu treino digite: /treino");
	});	
	
	bot.getEvents().onCommand("treino",[&bot](TgBot::Message::Ptr message ){
		bot.getApi().sendMessage(message->chat->id,"Qual será o treino de hoje?	Treino A (Superior) = /1, Treino B (Inferior) = /2 e  Treino C (Cardio) = /3");
    });
	
	bot.getEvents().onCommand("1",[&bot](Message::Ptr message){
		bot.getApi().sendMessage(message->chat->id, "Você quer o documento impresso ou o documento digitalizado? Impresso = /IA e Digitalizado = /DA");
	});
	
	bot.getEvents().onCommand("IA",[&bot](Message::Ptr message){
		system("./treino superior");
		bot.getApi().sendMessage(message->chat->id, "Retire seu treino na impressora e tenha um ótimo treino!");
	});
	
	bot.getEvents().onCommand("DA",[&bot](Message::Ptr message){
		bot.getApi().sendMessage(message->chat->id, "Aqui está o seu treino. Tenha um ótimo treino!");
		bot.getApi().sendPhoto(message->chat->id, InputFile::fromFile("treinoA.jpg", photoMimeType));
	});
	
	bot.getEvents().onCommand("2",[&bot](Message::Ptr message){
		bot.getApi().sendMessage(message->chat->id, "Você quer o documento impresso ou o documento digitalizado? Impresso = /IB e Digitalizado = /DB");
	});
	
	bot.getEvents().onCommand("IB",[&bot](Message::Ptr message){
		system("./treino inferior");
		bot.getApi().sendMessage(message->chat->id, "Retire seu treino na impressora e tenha um ótimo treino!");
	});
	
	bot.getEvents().onCommand("DB",[&bot](Message::Ptr message){
		bot.getApi().sendMessage(message->chat->id, "Aqui está o seu treino. Tenha um ótimo treino!");
		bot.getApi().sendPhoto(message->chat->id, InputFile::fromFile("treinoB.jpg", photoMimeType));
	});
	
	bot.getEvents().onCommand("3",[&bot](Message::Ptr message){
		bot.getApi().sendMessage(message->chat->id, "Você quer o documento impresso ou o documento digitalizado? Impresso = /IC e Digitalizado = /DC");
	});
	
	bot.getEvents().onCommand("IC",[&bot](Message::Ptr message){
		system("./treino cardio");
		bot.getApi().sendMessage(message->chat->id, "Retire seu treino na impressora e tenha um ótimo treino!");
	});
	
	bot.getEvents().onCommand("DC",[&bot](Message::Ptr message){
		bot.getApi().sendMessage(message->chat->id, "Aqui está o seu treino. Tenha um ótimo treino!");
		bot.getApi().sendPhoto(message->chat->id, InputFile::fromFile("treinoC.jpg", photoMimeType));
	}); 

    try {
        printf("Bot username: %s\n", bot.getApi().getMe()->username.c_str());
        bot.getApi().deleteWebhook();

        TgLongPoll longPoll(bot);
        while (true) {
            printf("Long poll started\n");
            longPoll.start();
        }
    } catch (exception& e) {
        printf("error: %s\n", e.what());
    }

    return 0;
}