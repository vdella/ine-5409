

#f = [1,0,0,0,0,0,0,0,0,-2];
f = [1,0,-5];
df = polyder(f);

function xj = x_newton (x, f, df)
  xj = x - polyval(f,x) / polyval(df,x);
endfunction

x = 2;
err = 0.001;
fx = polyval(f,x);
i=0;
while (abs(fx)>err) & (i < 100)
  x = x_newton(x, f, df);
  fx = polyval(f,x);
  i++;
endwhile

x
i