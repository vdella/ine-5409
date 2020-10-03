#f = [1,0,0,0,0,0,0,0,0,-2];
#f = [1,0,-5];
f = @(x)7*(2-0.9^x)-10;
#df = polyder(f);
df = @(x)-7*(0.9^x)*log(0.9);

function xj = x_newton (x, f, df)
  #xj = x - polyval(f,x) / polyval(df,x);
  xj = x - f(x) / df(x);
endfunction

x = 6; #não entendi como chegar nesse valor
err = 0.000001;
#fx = polyval(f,x);
fx = f(x)
i=1;
while (abs(fx)>err) & (i < 100)
  x = x_newton(x, f, df);
  #fx = polyval(f,x);
  fx = f(x)
  i++;
endwhile

x
i