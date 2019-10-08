#include <iostream>
#include <stdio.h>
#include <conio.h>

using namespace std;

int leitura(){      // ler valores do txt //
	
}

int escrita(){     // escrever novos valores no txt //

}

int main(){
	int equip, forca, crs;    // add = verificar outros inteiros //
	
	equip=leitura(1);      // ler valores do txt //
	forca=leitura(2);
	crs=leitura(3);
	
	if(equip=0){      // Desarmado //
		forca=0;
		crs=0;
	}else if(equip=1){    // HTML //
		forca=1;
		crs=0;
	}else if(equip=2){    // C com cin e cout //
		forca=5;
		crs=1;
	}
	
	escrita(2; forca);
	escrita(3; crs);
	
}
