# goit-algo-hw-09
 
Виведення виконання (копія с терміналу)

Жадібний алгоритм: {50: 2, 10: 1, 2: 1, 1: 1}
Алгоритм динамічного програмування: {50: 2, 10: 1, 2: 1, 1: 1}

amount_big = 1000:

Жадібний алгоритм виконується за 0.000001 секунд
Алгоритм динамічного програмування виконується за 0.000655 секунд
 
amount_big = 10000:

 Жадібний алгоритм виконується за 0.000001 секунд
Алгоритм динамічного програмування виконується за 0.006621 секунд

amount_big = 100000:

Жадібний алгоритм виконується за 0.000001 секунд
Алгоритм динамічного програмування виконується за 0.073524 секунд

Висновок: Отже, виведені результати показують, наскільки жадібний алгоритм є швидшим (при заданій начальній великій сумі і послідовних двох збільшеннях на х10 цієї суми, час виконання не змінюється), і як зменшується час виконання у випадках великих сум при використанні алгоритму динамічного програмування (чим більша сума, тим помітно довший час виконання). Тому, жадібний алгоритм по часу виконання безперечно є швидшим, ніж алгоритм динамічного програмування.

Жадібний алгоритм
Складність: O(n), де n — кількість номіналів монет.
Переваги: Швидкість виконання, проста реалізація.
Недоліки: Не завжди знаходить оптимальне рішення (мінімальну кількість монет).

Алгоритм динамічного програмування
Складність: O(n * m), де n — кількість номіналів монет, m — сума.
Переваги: Гарантоване знаходження оптимального рішення.
Недоліки: Більш висока обчислювальна складність, потреба в більшій пам'яті.
