#include <stdio.h>
#include <stdlib.h>
#include <math.h>

float equacao(char eq, float x){
    if(eq == 'f'){
        return x*x-5;
    }
    else{
        return 2*x;
    }
    
}

float xi_secante(float x1, float x0,char eq){
    return x1-((x1-x0)*equacao(eq,x1))/(equacao(eq,x1)-equacao(eq,x0));
}

int main(int argc, char *argv[]){
    float x1 = 2, x0=3,fx=1, temp,p = 0.001f;
    char eqs[2] = {'f','d'};
    int it = 1;
    while(fabs(fx)>p){
        temp = x1;
        x1 = xi_secante(x1,x0,eqs[0]);
        x0 = temp;
        fx = equacao(eqs[0],x0);
        it+=1;
    }
    printf("Aprox de sqrt(5):\n\tx: %.4f\n\tf(x): %.4f\n\titeracoes: %d\n\n",x1,fx,it);
	return 0;
}