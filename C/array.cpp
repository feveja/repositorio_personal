/* Vector de tipo char. */

	#include <cstdio.h>
    #include <conio.h>

	main() /* Rellenamos un vector char */
	{
		char cadena[20];
		int i;
		for (i=0;i<19 && cadena[i-1]!=13;i++)
			cadena[i]=getche( );
		if (i==19) cadena[i]='\0';
		else cadena[i-1]='\0';
		printf("\n%s",cadena);
	}
