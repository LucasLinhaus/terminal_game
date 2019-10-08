#include <iostream>
#include <stdio.h>
#include <conio.h>

using namespace std;

int leitura(int var){      // recebe qual variavel deve ser lida //
	int val;             // valor a ser retornado //
	char txt[100];       // recebe as linhas do txt //
	
	FILE *arq;           // ponteiro pro txt //
	arq=fopen("Player.txt", "rt");
	
	if(arq==NULL){        // verificar a leitura do arquivo //
		cout<<"[ Falha ao executar comando ]\n";
		return 0;
	}
	
	for(int l=1;!feof(arq);l++){     // procura linha da variavel pedida // 
		fgets(txt,100,arq);
		if(l==var){
			val=txt[5];
		}
	}
	
	fclose(arq);      // fecha txt e retorna o valor da variavel //
	return val;
}

int escrita(int var; int val){

}

int main(){
	int eqp, frc, crs;    // add = verificar outros inteiros //
	
	eqp=leitura(1);      // ler valores do txt //
	frc=leitura(2);
	crs=leitura(3);
	
	if(eqp=0){      // Desarmado //
		frc=0;
		crs=0;
	}else if(eqp=1){    // HTML //
		frc=1;
		crs=0;
	}else if(eqp=2){    // C com cin e cout //
		frc=5;
		crs=1;
	}
	
	escrita(2; frc);   //  escreve valores no txt // 
	escrita(3; crs);
	
	return;    // a definir //
}
