% Ejercicio 5: Generar una matriz con 2n en la diagonal y 1 fuera de la diagonal

function A = matriz_diagonal_ones(n)
    % Paso 1: Crear una matriz de 2n x 2n llena de unos
    A = ones(2*n, 2*n); % 'ones' crea una matriz de unos de tamaño 2n x 2n
    
    % Paso 2: Colocar 2n en la diagonal principal
    A = A + (2*n - 1) * eye(2*n); % 'eye' genera una matriz identidad de 2n x 2n
    % y la multiplicamos por (2n - 1) para ajustar los valores de la diagonal
end

% Ejemplo de uso:
n = 3; % Puedes cambiar el valor de n para probar diferentes tamaños

% Llamada a la función para generar la matriz A
A = matriz_diagonal_ones(n);

% Mostrar la matriz resultante
disp('La matriz A generada en el Ejercicio 5 es:');
disp(A);
