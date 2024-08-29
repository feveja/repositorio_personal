% Ejercicio 6: Generar una matriz en bloques

function A = matriz_bloques(n)
    % Paso 1: Crear la matriz identidad I de tamaño nxn
    I = eye(n); % 'eye(n)' genera una matriz identidad de tamaño nxn
    
    % Paso 2: Crear las matrices bloque
    % La matriz A se crea usando la función 'blkdiag' que construye matrices bloque
    A = blkdiag(2*I, 2*I, 2*I) + blkdiag(-I, -I, zeros(n)); % 2I en la diagonal principal
    A = A + blkdiag(zeros(n), -I, -I); % -I en las posiciones adyacentes a la diagonal principal
end

% Ejemplo de uso:
n = 3; % Puedes cambiar el valor de n para probar diferentes tamaños

% Llamada a la función para generar la matriz A
A = matriz_bloques(n);

% Mostrar la matriz resultante
disp('La matriz A generada en el Ejercicio 6 es:');
disp(A);
