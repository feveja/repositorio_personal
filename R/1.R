n=1000000
X=runif(n,min=0, max = 1)
Y = 1:n
for (i in 1:n)(if(X(i)>5) (Y(i)=1) else(Y(i)=0))
Z= which(Y==0)
p_rel= NROW(Z)/n
abs(0.5-p_rel)