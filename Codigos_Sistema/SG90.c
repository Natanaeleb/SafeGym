#include <wiringPi.h>
#include <unistd.h>
#include <stdio.h>
#include <stdlib.h>

#define SAIDA 1

int face_reconhecida = 1;

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
	
	return 0;
}
