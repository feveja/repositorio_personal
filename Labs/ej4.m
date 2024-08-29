% Ejercicio 4: Generar una matriz de la forma especificada
function A = matriz(alpha, epsilon, n)
    I = eye(n); % Matriz identidad de tamaño nxn
    ones_matrix = ones(n, n); % Matriz de unos de tamaño nxn
    A = [alpha * I, epsilon * ones_matrix; epsilon * ones_matrix, alpha * I];
end

alpha = 2;
epsilon = 1;
n = 4;
A = matriz(alpha, epsilon, n);
disp('Matriz generada en el Ejercicio 4:');
disp(A);

