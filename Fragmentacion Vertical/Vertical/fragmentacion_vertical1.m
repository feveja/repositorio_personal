% La matriz de afinidad observada
affinity_matrix_example = [85, 85, 85, 85;
                            85, 320, 190, 320;
                            85, 190, 215, 215;
                            85, 320, 215, 345];

% Función para calcular el valor bond
function b = bond(Ax, Ay, affinity_matrix)
    b = sum(affinity_matrix(:, Ax) .* affinity_matrix(:, Ay));
end

% Función para calcular la contribución
function c = contribution(Ai, Ak, Aj, affinity_matrix)
    bond_ik = bond(Ai, Ak, affinity_matrix);
    bond_kj = bond(Ak, Aj, affinity_matrix);
    bond_ij = bond(Ai, Aj, affinity_matrix);
    c = 2 * (bond_ik + bond_kj) - 2 * bond_ij;
end

% Algoritmo BEA para encontrar el orden óptimo
function [clustered_affinity_matrix, columns_positioned] = bond_energy_algorithm(affinity_matrix)
    n = size(affinity_matrix, 2);
    columns_positioned = []; % Inicializamos el orden de columnas
    unpositioned_columns = 1:n; % Todas las columnas están inicialmente no posicionadas
    
    % Empezamos con la primera columna arbitraria
    columns_positioned = [unpositioned_columns(1)];
    unpositioned_columns(1) = []; % Eliminar la columna posicionada
    
    while ~isempty(unpositioned_columns)
        best_column = [];
        best_position = [];
        best_contribution = -inf;

        % Iteramos sobre las columnas no posicionadas
        for k = unpositioned_columns
            % Evaluamos cada posible posición para insertar la columna k
            for pos = 1:length(columns_positioned) + 1
                if pos == 1
                    % Colocamos al inicio
                    contribution_value = contribution(k, columns_positioned(1), columns_positioned(1), affinity_matrix);
                elseif pos == length(columns_positioned) + 1
                    % Colocamos al final
                    contribution_value = contribution(columns_positioned(end), k, columns_positioned(end), affinity_matrix);
                else
                    % Colocamos entre Ai y Aj
                    Ai = columns_positioned(pos - 1);
                    Aj = columns_positioned(pos);
                    contribution_value = contribution(Ai, k, Aj, affinity_matrix);
                end
                
                % Actualizamos si encontramos una mejor contribución
                if contribution_value > best_contribution
                    best_column = k;
                    best_position = pos;
                    best_contribution = contribution_value;
                end
            end
        end
        
        % Insertamos la mejor columna encontrada en la mejor posición
        columns_positioned = [columns_positioned(1:best_position-1), best_column, columns_positioned(best_position:end)];
        unpositioned_columns(unpositioned_columns == best_column) = []; % Eliminar la columna posicionada
    end
    
    % Reordenamos las filas y columnas en base al nuevo orden de las columnas
    clustered_affinity_matrix = affinity_matrix(:, columns_positioned);
    clustered_affinity_matrix = clustered_affinity_matrix(columns_positioned, :);
end

% Aplicar el BEA con el ejemplo que proporcionaste en la imagen
[clustered_matrix_example, order_example] = bond_energy_algorithm(affinity_matrix_example);
disp('Matriz agrupada:');
disp(clustered_matrix_example);
disp('Orden de columnas:');
disp(order_example);

% Funciones para calcular accesos y maximizar según el punto diagonal (sin cambios)
function [CTQ, CBQ, COQ] = calculate_group_accesses(affinity_matrix, diagonal_point)
    TA = affinity_matrix(1:diagonal_point-1, 1:diagonal_point-1);
    BA = affinity_matrix(diagonal_point:end, diagonal_point:end);
    OQ = affinity_matrix(1:diagonal_point-1, diagonal_point:end);
    
    CTQ = sum(TA(:)); % Accesos de TA
    CBQ = sum(BA(:)); % Accesos de BA
    COQ = sum(OQ(:)); % Accesos cruzados entre TA y BA
end

function [best_point, max_value] = maximize_access(affinity_matrix)
    n = size(affinity_matrix, 1);
    best_point = [];
    max_value = -inf;
    
    for diagonal_point = 2:n
        [CTQ, CBQ, COQ] = calculate_group_accesses(affinity_matrix, diagonal_point);
        
        value = CTQ * CBQ - COQ^2;
        
        if value > max_value
            max_value = value;
            best_point = diagonal_point;
        end
    end
end

% Aplicar el algoritmo a la matriz agrupada (que ya fue reorganizada)
[best_diagonal_point, max_value] = maximize_access(clustered_matrix_example);

disp('Mejor punto en la diagonal:');
disp(best_diagonal_point);
disp('Valor máximo:');
disp(max_value);