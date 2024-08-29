function y=fun2(x)
n=length(x);
for i=1:n
    if x(i)<=-2
        y(i)=x(i)-1;
    elseif (x(i)>-2 & x(i)<0)
        y(i)=1-x(i).^2;
    else
        y(i)=-1/(x(i)+1);
    end
end

%Grafico
%x = -10:.01:10;
%plot(x,fun2(x))
