// 단어 개수 C언어 풀이

#include <stdio.h>

int		strlen(char *s)
{
	int len;
	
	len = 0;
	while (s[len] != '\0')
		len++;
	return (len);
}

int		main()
{
	char	*str[1000000];
	int		cnt = 0;

	gets(str);
	for (int i = 0; i < strlen(str); i++)
	{
		if (str[i] != ' ')
		{
			if (i > 0 && str[i - 1] != ' ')
				continue ;
			else
				cnt++;
		}
	}
	printf("%d\n", cnt);
	return (0);
}