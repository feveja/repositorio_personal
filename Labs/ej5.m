% Ejercicio 5: Generar una matriz de la forma especificada
function A = matriz_ej5(n)
    % Genera una matriz de la forma especificada
    A = 2 * n * eye(2*n) + diag(ones(2*n-1, 1), 1) + diag(ones(2*n-1, 1), -1);
end

n = 4;
A = matriz_ej5(n);
disp('Matriz del Ejercicio 5:');
disp(A);

% Ejercicio 5: Generar una matriz con 2n en la diagonal y 1 fuera de la diagonal
function A = matriz_diagonal_ones(n)
    A = 2 * n * eye(2 * n) + diag(ones(2 * n - 1, 1), 1) + diag(ones(2 * n - 1, 1), -1);
end

n = 4;
A = matriz_diagonal_ones(n);
disp('Matriz generada en el Ejercicio 5:');
disp(A);
