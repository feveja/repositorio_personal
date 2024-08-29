function A=matriz(n)
B=[zeros(n-1,1) eye(n-1);zeros(1,n)];
A=2*eye(n)-B-B';
end
%
n=4;
A=matriz(n);
b=ones(n,1);
x= A\b; %Sale de Ax=b
y=A*x-b;
