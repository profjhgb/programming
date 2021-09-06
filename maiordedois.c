#include<stdio.h>
int main(){
  int n1, n2;
  //
  // Este trehco de software não possui nenhum tipo de otimização
  // e é destinado aos alunos iniciantes nas disciplinas de programação
  // em linguagem C
  //
  printf("##########################################################\n");
  printf("# Define o maior entre dois números inteiros e distintos #\n");
  printf("##########################################################\n\n\n");
  printf("Digite o primeiro número: ");
  scanf("%d",&n1);
  printf("Digite o segundo número:  ");
  scanf("%d",&n2);
  if(n1 == n2){
    printf("Os valores DEVEM ser distintos!\n");
    printf("Programa encerrado...\n\n");
    return 0;
  }else{
    if(n1 > n2){
      printf("===> Maior número: %d\n\n",n1);
    }else
      printf("===> Maior número: %d\n\n",n2);
  }
  return 0;
}
