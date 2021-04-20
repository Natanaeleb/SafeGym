# SafeGym

Este repositório reúne códigos e documentos do Projeto de sistemas embarcados chamado SafeGym.

## Objetivos

Projetar um sistema capaz de identificar se a pessoa é registrada ou não em uma academia, de modo que, ao coletar os dados identifiquem-se entradas de pessoas não registradas com o propósito de avisar ao gerente sobre o acesso indevido e, também que as pessoas registradas tenham um maior suporte na hora dos treinos. 

##Requisitos

- Uma Raspberry Pi 3b+ que funcionará como unidade central, em que ocorrerá o processamentos dos dados adquiridos;
- Uma WebCam que irá capturar a imagem da pessoa na entrada da academia para detectar se a pessoa é registrada ou não no banco de dados;
- Um bot no Telegram para informar ao gerente se algum indivíduo foi identificado com entrada não autorizada;
- Um bot no Telegram para auxiliar os alunos com os treinos;
- Um sensor detector de presença para contabilizar quando as pessoas estiverem saindo da academia, esse sensor vai auxiliar no balanço diário de alunos;
- Uma impressora térmica integrada ao sistema para imprimir os treinos. Para validação do protótipo, será utilizada uma impressora multifuncional;
- Um monitor para auxiliar o aluno quanto à posição que deve estar para a imagem ser capturada e a quantidade de pessoas na academia em tempo real;
- Um circuito eletrônico totalmente lacrado para não haver desconexão elétrica;
- Uma boa iluminação no local para que não atrapalhe o reconhecimento facial dos indivíduos;

##Linguagens de Porgramação
-C++
-Python




