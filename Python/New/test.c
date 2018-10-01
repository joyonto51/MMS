#include <stdio.h>

void main()
{
      int i, a[12], b[12], k;

      printf("Enter a sample input data: \n");

      scanf("%d", &k);
      printf("Input= %d\n",k);

      for(i = 0;k != 1; i = i + 1)
      {
            a[i] = k;
            printf("i = %d, k = %d,\n",i,k);

            printf("input2 =");
            scanf("%d", &b[i]);

            printf("a[%d] = %d  ", i, a[i]);

            printf(" b[%d] = %d\n\n", i, b[i]);

      }
      printf("\n");
}
