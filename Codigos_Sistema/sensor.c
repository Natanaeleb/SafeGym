#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include<wiringPi.h>

// Define o pino para o sensor
#define SENSOR_SAIDA 22

int qtd_pessoas =0; // entrada = 0, saida = 0
int face_reconhecida =1; // variavel p/ receber o resultado de outra funcao

int main(int argc, char *argv[])
{
	wiringPiSetup();
	pinMode(SENSOR_SAIDA,INPUT);
	
	while(1){
		// face_reconhecida = 1;
		if(face_reconhecida==1)
		{
			if(qtd_pessoas>=0)
			{
				qtd_pessoas = qtd_pessoas + 1;
				printf("%d\n",qtd_pessoas);
				usleep(500000);
			}
			if(digitalRead(SENSOR_SAIDA)==0) // detecta presenca
			{
				
				if(qtd_pessoas>0)
				{
					qtd_pessoas = qtd_pessoas - 1;
					printf("%d\n",qtd_pessoas);
					usleep(500000);
				}
			}

		}
	}
return 0;
}

