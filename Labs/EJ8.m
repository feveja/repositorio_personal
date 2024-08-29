% Ejercicio 8: Usar los comandos save y load

% Paso 1: Crear una matriz de ejemplo
A = rand(5); % Crear una matriz 5x5 aleatoria

% Paso 2: Guardar la matriz A en un archivo .mat
save('matrizA.mat', 'A'); % 'save' guarda la variable A en el archivo 'matrizA.mat'

% Paso 3: Limpiar las variables de la memoria
clear; % 'clear' elimina todas las variables del espacio de trabajo

% Paso 4: Cargar la matriz A desde el archivo
load('matrizA.mat'); % 'load' carga la variable A desde el archivo 'matrizA.mat'

% Verificar que la matriz ha sido cargada correctamente
disp('La matriz A cargada desde el archivo es:');
disp(A);
