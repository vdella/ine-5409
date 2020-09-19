#include <stdio.h>
#include <stdlib.h>
#include <math.h>

float equacao(char eq, float x){
    if(eq == 'a'){
        return exp(x)+x;
    }
    else if(eq == 'b'){
        return exp(x)-2*cos(x);
    }
    else{
        return exp(x)*sin(x)-1;
    }
    
}

float xk_falsa_pos(float inf, float sup,char eq){
    return inf-equacao(eq,inf)*(sup-inf)/(equacao(eq,sup)-equacao(eq,inf));
}

int main(int argc, char *argv[]){

    float inf,sup,x,fx,p = 0.01f;
    char eq, eqs[3] = {'a','b','c'};
    int it = 0, lim[6] = {-1,0,0,2,0,1};

    for(int i = 0;i<3;i++){
        eq = eqs[i];
        inf = lim[i*2];
        sup = lim[i*2+1];
        it = 0;
        fx = 1;
        while(fabs(fx)>p){
            x = xk_falsa_pos(inf,sup,eq);
            fx = equacao(eq,x);
            if(fx == 0){
                break;
            }
            else if(fx>0){
                sup = x;
            }
            else{
                inf = x;
            }
            it+=1;
        }
        printf("Equacao %c:\n\tx: %.4f\n\tf(x): %.4f\n\titeracoes: %d\n\n",eq,x,fx,it);
    }
	return 0;
}