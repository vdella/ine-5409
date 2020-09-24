#f = [1,0,0,0,0,0,0,0,0,-2];
f = [1,0,-5];

function xj = x_newton (x, f)
  xj = x - polyval(f,x) / polyval(df,x);
endfunction

x = 2; #não entendi como chegar nesse valor
err = 0.001;
fx = polyval(f,x);
i=1;
while (abs(fx)>err) & (i < 100)
  x = x_newton(x, f, df);
  fx = polyval(f,x);
  i++;
endwhile

x
i