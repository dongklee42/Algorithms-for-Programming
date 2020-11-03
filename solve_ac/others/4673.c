#include<stdio.h>

int main()
{
	int i, j, k, tmp;
	for(i = 1; i < 10000; i++)
	{
		for(j = 0; j < i; j++)
		{
			tmp = j;
			for(k = j; k != 0; k /= 10)
				tmp += k % 10;

			if(tmp == i)
				break ;
				
			if(j == (i - 1))
				printf("%d\n", i);
		}
	}
	return (0);
}