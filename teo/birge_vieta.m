#f = [1,0,-5];
f = [1,0,2,-1];

x = 1;
err = 0.1;
fx = polyval(f,x);
i=1;
while (abs(fx)>err) & (i<10)
    b = f(1);
    cj = b;
    for j = f(2:end)
        b = j + (b*x)
        ci = cj
        cj = b +  ci*x;
    endfor
    x = x - b / ci
    fx=polyval(f,x);
    i++;
endwhile

x
fx
i