#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include<wiringPi.h>

// Define o pino para o sensor
#define SENSOR_SAIDA 22
// Define o pino para o servo
#define SAIDA 1

int qtd_pessoas =0; // entrada = 0, saida = 0 
int face_reconhecida =1; // variavel p/ receber o resultado de outra funcao


void sqwv(float d, int pin_out, int N)
{
	int high_us = (int)(d*50.0/9.0 + 1500);
	int low_us  = 20000 - high_us;
	int i ;
	for(i = 0;i <N;i ++)
	{
		digitalWrite(pin_out, HIGH);
		usleep(high_us);
		digitalWrite(pin_out, LOW);
		usleep(low_us);
	}
}

int main(int argc, char *argv[])
{
	wiringPiSetup();
	pinMode(SAIDA, OUTPUT);
	pinMode(SENSOR_SAIDA,INPUT);
	
	pid_t pid1 ;
	pid1 = fork();
	
	// Filho cuida da contagem
	// Pai cuida da catraca
	
	if(pid1==0)
	{
		while(1){
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
	}else{
		while(1){
			if(face_reconhecida==1)
			{
				sqwv(0, SAIDA, 40);
				usleep(250000);
				sqwv(180, SAIDA, 1100);
			}
			else if(face_reconhecida==0)
			{
				sqwv(0, SAIDA, 40);
			}
		}	
	}
	return 0;
}
