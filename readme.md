## Висновки до завдання № 2

Обчислення визначеного інтеграла функції `f(x) = x²` на відрізку `[0, 2]` методом Монте-Карло дало результат, який дуже близький до точного аналітичного значення, отриманого за допомогою функції `quad` з модуля `scipy.integrate`. Абсолютна похибка була мінімальною, що підтверджує правильність реалізації та ефективність імовірнісного підходу.

## Отримані результати:

- Інтеграл методом Монте-Карло: `2.654480`  
- Аналітичне значення (quad): `2.666666666666667`  
- Оцінка похибки quad: `2.960594732333751e-14`  
- Абсолютна похибка Монте-Карло: `0.012187`

Ці результати підтверджують ефективність методу Монте-Карло навіть при простій реалізації. Точність обчислень покращується зі збільшенням кількості випадкових точок, що узгоджується з законом великих чисел.

Таким чином, метод Монте-Карло є надійним інструментом для наближеного чисельного інтегрування, особливо в задачах, де аналітичне вирішення є складним або неможливим. Побудова графіка допомогла візуально проаналізувати область під кривою та переконатися в правильності розрахунків.
