#include <stdio.h>
#include <stdlib.h>

/* fputs(file gets): verilerin topluca yazd�r�lmas�

  fputs�n sytnx� 2parametre 
1.parametre de�i�kenin ismi
2.parametre nereye yazd�r�laca��          */

int main() {
	
	FILE *metinbelgesi;
	
	char veri1[20]="Bilgisayar ";
	char veri2[20]="Muhendisligi ";
	char veri3[20]="Bolumu";
	
	metinbelgesi=fopen("C:\\Users\\BEYZA\\Desktop\\YEANI.txt","w");
	
	fputs(veri1,metinbelgesi);
	
	fputs(veri2,metinbelgesi);
	
	fputs(veri3,metinbelgesi);
	
	
	
	
	
	return 0;
}
