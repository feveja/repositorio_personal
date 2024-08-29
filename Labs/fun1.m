function y=fun1(x)
    n=length(x);
    for i=1:n
        if x(i)<=0
            y(i)=2*(sin(2*x(i)))^2;
        else
            y(i)=1-exp(-x(i));
        end
    end
%Grafico
%x = -10:.01:10;
%plot(x,fun1(x))
