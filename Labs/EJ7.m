% Ejercicio 7: Evaluar e^x usando la serie de Taylor

function y = miexp(x)
    % Inicializar la suma con el primer término de la serie (1)
    y = 1;
    term = x; % Primer término después de 1
    n = 1; % Contador para el factorial en el denominador
    
    % Calcular la serie de Taylor hasta que el nuevo término sea muy pequeño
    while (y + term ~= y) % Comparar si añadir el término cambia el valor de y
        y = y + term; % Sumar el nuevo término a la suma total
        n = n + 1; % Incrementar n
        term = term * x / n; % Calcular el siguiente término de la serie
    end
end

% Ejemplo de uso:
x = 1; % Valor para el cual se quiere calcular e^x

% Llamada a la función para calcular e^x
resultado = miexp(x);

% Mostrar el resultado
disp(['El valor de miexp(', num2str(x), ') es: ', num2str(resultado)]);
disp(['El valor de exp(', num2str(x), ') (función de MATLAB) es: ', num2str(exp(x))]);
