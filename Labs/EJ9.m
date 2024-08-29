% Ejercicio 9: Interpretar y calcular con líneas de código dadas

% Paso 1: Crear una matriz A de ejemplo
A = rand(3, 3); % Matriz 3x3 aleatoria para ilustración

% Paso 2: Calcular el máximo de la suma de valores absolutos por columna
resultado1 = max(sum(abs(A'))); 
% 'A'' ' es la transpuesta de A. 'abs' toma el valor absoluto. 
% 'sum' suma los elementos de cada columna y 'max' toma el valor máximo.

% Paso 3: Calcular la norma infinito de la matriz A
resultado2 = norm(A, inf); 
% 'norm(A, inf)' calcula la norma infinito, que es la máxima suma de valores absolutos de cada fila.

% Mostrar los resultados
disp(['Resultado de max(sum(abs(A''))) = ', num2str(resultado1)]);
disp(['Resultado de norm(A, inf) = ', num2str(resultado2)]);
