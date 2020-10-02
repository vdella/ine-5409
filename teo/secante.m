#f = [1,0,0,0,0,0,0,0,0,-2];
f = [1,0,-5];
                      #xi = xk-1; xj = xk
function xk = x_newton (xi, xj, f)
  xk = xj - ((xj - xi) * polyval(f,xj)) / (polyval(f,xj) - polyval(f,xi));
endfunction

# pensando na ordem alfabetica k,i,j
xi = 3; #não entendi como chegar nesse valor
xj = 2;
err = 0.001;
fx = polyval(f,xj);
i=1;
while (abs(fx)>err) & (i < 100)
  temp = xj;
  xj = x_newton(xi, xj, f);
  xi = temp;
  fx = polyval(f,xj);
  i++;
endwhile

xj
i