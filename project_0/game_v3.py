"""Игра угадай число
Компьютер сам загадывает и сам угадывает число
"""
import numpy as np

def game_core_v3(number: int = 1) -> int:
    """Сначала устанавливаем любое random число, а потом уменьшаем
    или увеличиваем его рандомно в зависимости от того, больше оно или меньше нужного.
       Функция принимает загаданное число и возвращает число попыток
    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    count = 0 # число попыток
    predict = np.random.randint(1, 101) # Устонавливаем рандом число
    predict_min = 1 # Задаем минимальное число
    predict_max = 101 # Задаем максимальное число
    
    while number != predict: # цикл сравнения чисел     
        count += 1 # счет числа попыток 
        
        # сравнение загаданного и найденого числа и уменьшаем промежуток 
        # между максимумом и минимумом рандомного генератора
        if number > predict: 
          predict_min = predict
          predict = np.random.randint(predict_min, predict_max)

        elif number < predict:
          predict_max = predict
          predict = np.random.randint(predict_min, predict_max)

    return count

def score_game(random_predict) -> int:
    """За какое количество попыток в среднем за 10000 подходов угадывает наш алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = []
    np.random.seed(1)  # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(10000))  # загадали список чисел

    for number in random_array:
        count_ls.append(random_predict(number))

    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за: {score} попытки")
    
print('Run benchmarking for game_core_v3: ', end='')
score_game(game_core_v3)