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

float xi_newton(float x,char eq, char der){
    return x-equacao(eq,x)/equacao(der,x);
}

int main(int argc, char *argv[]){
    float x = 2,fx,p = 0.001f;
    char eqs[2] = {'f','d'};
    int it = 1;
    fx = equacao(eqs[0],x);
    while(fabs(fx)>p){
        x = xi_newton(x,eqs[0],eqs[1]);
        fx = equacao(eqs[0],x);
        it+=1;
    }
    printf("Aprox de sqrt(5):\n\tx: %.4f\n\tf(x): %.4f\n\titeracoes: %d\n\n",x,fx,it);
	return 0;
}
