% Definir los coeficientes de las ecuaciones
A = [1.0001 1.0000; 1.0000 1.0000];
b = [2; 2];

% Crear un rango de valores para x
x = linspace(-10, 10, 100);

% Obtener y de cada ecuación en función de x
y1 = (b(1) - A(1, 1) * x) / A(1, 2);
y2 = (b(2) - A(2, 1) * x) / A(2, 2);

% Graficar las dos ecuaciones
plot(x, y1, 'r', 'LineWidth', 2); % Línea roja para la primera ecuación
hold on;
plot(x, y2, 'b', 'LineWidth', 2); % Línea azul para la segunda ecuación

% Añadir etiquetas y leyenda
xlabel('x');
ylabel('y');
title('Gráfico lineal de las dos ecuaciones');
legend('1.0001x + 1.0000y = 2', '1.0000x + 1.0000y = 2');
grid on;
hold off;
