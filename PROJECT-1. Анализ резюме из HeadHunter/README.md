<center> <img src = https://raw.githubusercontent.com/AndreyRysistov/DatasetsForPandas/main/hh%20label.jpg alt="drawing" style="width:400px;">

# <center> Проект 1: Анализ резюме из HeadHunter

#### Python 3.9.13
# Огловление

[1. Описание проекта](https://github.com/alexey273-27/sf_data_sciense/blob/master/PROJECT-1.%20%D0%90%D0%BD%D0%B0%D0%BB%D0%B8%D0%B7%20%D1%80%D0%B5%D0%B7%D1%8E%D0%BC%D0%B5%20%D0%B8%D0%B7%20HeadHunter/README.md#Описание-проекта)
## Описание проекта
Нам необходимо иследовать структуру данных, затем преобразовать данные, иследовать зависемости в данных и в итоге очистить данные от пустых значений, выбросов дубликатов

[1.1 Исследование структуры данных](https://github.com/alexey273-27/sf_data_sciense/blob/master/PROJECT-1.%20%D0%90%D0%BD%D0%B0%D0%BB%D0%B8%D0%B7%20%D1%80%D0%B5%D0%B7%D1%8E%D0%BC%D0%B5%20%D0%B8%D0%B7%20HeadHunter/README.md#Исследование-структуры-данных)

[1.2 Преобразование данных](https://github.com/alexey273-27/sf_data_sciense/blob/master/PROJECT-1.%20%D0%90%D0%BD%D0%B0%D0%BB%D0%B8%D0%B7%20%D1%80%D0%B5%D0%B7%D1%8E%D0%BC%D0%B5%20%D0%B8%D0%B7%20HeadHunter/README.md#Преобразование-данных)

[1.3 Исследование зависимостей в данных](https://github.com/alexey273-27/sf_data_sciense/blob/master/PROJECT-1.%20%D0%90%D0%BD%D0%B0%D0%BB%D0%B8%D0%B7%20%D1%80%D0%B5%D0%B7%D1%8E%D0%BC%D0%B5%20%D0%B8%D0%B7%20HeadHunter/README.md#Исследование-зависимостей-в-данных)

[1.4 Очистка данных](https://github.com/alexey273-27/sf_data_sciense/blob/master/PROJECT-1.%20%D0%90%D0%BD%D0%B0%D0%BB%D0%B8%D0%B7%20%D1%80%D0%B5%D0%B7%D1%8E%D0%BC%D0%B5%20%D0%B8%D0%B7%20HeadHunter/README.md#Очистка-данных)



###  Исследование структуры данных
Импортируем библиотеки
``` Python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
```

Прочитаем данные с помощью библиотеки Pandas

``` Python
# Читаем данные с помощью библиотеки Pandos
hh_database = pd.read_csv('data/dst-3.0_16_1_hh_database.csv', sep= ';')
```  
Выведим несколько первых (последних) строк таблицы чтобы убедиться в том, что ваши данные не повреждены
``` Python
print(hh_database.head())
print(hh_database.tail())
```

Выведем основную информацию о числе непустых значений в столбцах и их типах в таблице.
``` Python
hh_database.info() 
```
видно что таблица class 'pandas.core.frame.DataFrame'имеет 44744 строки и  12 столбцов типа   
dtypes: object(12) и занимает memory usage: 4.1+ MB  

Обратим внимание на информацию о числе непустых значений
``` Python
hh_database.count() 
```
из таблицы видно что в трех столбцах есть пропуски   
Опыт работы                        44576  
Последнее/нынешнее место работы    44743  
Последняя/нынешняя должность       44742

расмотрим основную статистическую информацию о столбцах.
``` Python
hh_database.describe() 
```
из таблицы видно что очень много уникальных значений  
:arrow_up:[к оглавлению](https://github.com/alexey273-27/sf_data_sciense/blob/master/PROJECT-1.%20%D0%90%D0%BD%D0%B0%D0%BB%D0%B8%D0%B7%20%D1%80%D0%B5%D0%B7%D1%8E%D0%BC%D0%B5%20%D0%B8%D0%B7%20HeadHunter/README.md#Огловление)
### Преобразование данных
Создадим с помощью функции-преобразования новый признак **"Образование"**, который должен иметь 4 категории: "высшее", "неоконченное высшее", "среднее специальное" и "среднее". 
Удалим признак "Образование и ВУЗ".
``` Python
# На вход данной функции поступает строка с образованием.
def level_education(educat):
    # Метод split() разбивает строку на слова по пробелу.
    # В результате получаем список слов в строке и заносим его в переменную educat_list.
    educat_list = educat.split(' ')
    # Обрезаем список, оставляя в нём только первые два  элемента и преобразуем его в строку ,
    educat_type = ' '.join(educat_list[0:2])
    # Делаем проверку на уровень образования.
    if 'Высшее' in educat_type :
        educat_type = 'высшее'
    elif 'Неоконченное высшее' in educat_type:
        educat_type = 'неоконченное высшее' 
    elif 'Среднее специальное' in educat_type:
        educat_type = 'среднее специальное'  
    elif 'Среднее' in educat_type:
        educat_type = 'среднее'      
    #Возвращаем переменную street_type, в которой хранится уровень образования.
    return educat_type

#создаем новый признак Образование методом apply
hh_database['Образование'] = hh_database['Образование и ВУЗ'].apply(level_education)


print(hh_database['Образование'].value_counts())

# удоляем столбец Образование и ВУЗ
hh_database = hh_database.drop('Образование и ВУЗ', axis=1)
```


:arrow_up:[к оглавлению](https://github.com/alexey273-27/sf_data_sciense/blob/master/PROJECT-1.%20%D0%90%D0%BD%D0%B0%D0%BB%D0%B8%D0%B7%20%D1%80%D0%B5%D0%B7%D1%8E%D0%BC%D0%B5%20%D0%B8%D0%B7%20HeadHunter/README.md#Огловление)
### Исследование зависимостей в данных
:arrow_up:[к оглавлению](https://github.com/alexey273-27/sf_data_sciense/blob/master/PROJECT-1.%20%D0%90%D0%BD%D0%B0%D0%BB%D0%B8%D0%B7%20%D1%80%D0%B5%D0%B7%D1%8E%D0%BC%D0%B5%20%D0%B8%D0%B7%20HeadHunter/README.md#Огловление)
### Очистка данных

![](../images/boxplot.png):arrow_up:[к оглавлению](https://github.com/alexey273-27/sf_data_sciense/blob/master/PROJECT-1.%20%D0%90%D0%BD%D0%B0%D0%BB%D0%B8%D0%B7%20%D1%80%D0%B5%D0%B7%D1%8E%D0%BC%D0%B5%20%D0%B8%D0%B7%20HeadHunter/README.md#Огловление)

### Алгоритм метода:

1. Вычислить 25-ую и 75-ую квантили (1 и 3 квартили) - $Q_{25}$ и $Q_{75}$ для признака, который мы исследуем
2. Вычислить межквартильное расстояние:  
    * $IQR=Q_{75}-Q_{25}$
3. Определить верхнюю и нижнюю границы Тьюки: 

    * $bound_{upper} = Q_{75} + 1.5*IQR$
    
    * $bound_{lower} = Q_{25} - 1.5*IQR$
4. Найти наблюдения, которые выходят за пределы границ


### **Недостатки метода:**

Метод требует, чтобы признак, на основе которого происходит поиск выбросов, был распределен нормально.

### **Модификация метода:**

Можно попробовать воспользоваться методами преобразования данных, например, логарифмированием, чтобы попытаться свести распределение к нормальному или хотя бы к симметричному. 

Также можно добавить вариативности количеству квартильных размахов в левую и правую сторону распределений.


## Метод z-отклонений (метод сигм)

Правило трех сигм гласит: что, если распределение данных является нормальным, то 99.73% лежат в интервале: $(\mu-3 \sigma$ , $\mu+3 \sigma)$, 
где  
* $\mu$ - математическое ожидание (для выборки это среднее значение)
* $\sigma$ - стандартное отклонение. 

Наблюдения, которые лежат за пределами этого интервала будут считаться выбросами.

![](../images/method_sigm.png)

### **Алгоритм метода:**

1. Вычислить среднее и стандартное отклонение $\mu$ и $\sigma$ для признака, который мы исследуем
2. Определить верхнюю и нижнюю границы:
    * $bound_{upper} = \mu - 3 * \sigma$
    
    * $bound_{lower} = \mu + 3 * \sigma$
3. Найти наблюдения, которые выходят за пределы границ

### **Недостатки метода:**
Метод требует, чтобы признак, на основе которого происходит поиск выбросов, был распределен нормально.

### **Модификация метода:**

Можно попробовать воспользоваться методами преобразования данных, например, логарифмированием, чтобы попытаться свести распределение к нормальному или хотя бы к симметричному. 

Также можно добавить вариативности количеству стандартных отклонений в левую и правую сторону распределений.

## Реализация методов

Методы реализованы в виде функций find_outliers_iqr() и find_outliers_z_score(). Функции представлены в файле find_outliers.py. К функциям предоставлена документация.

## Пример использования

Обязательными аргументами функций, реализующих методы поиска выбросов являются:
* data (pandas.DataFrame): набор данных (таблица)
* feature (str): имя признака, на основе которого происходит поиск выбросов

Использование классических подходов без модификаций:
```python
# Метод межквартильного размаха
from outliers_lib.find_outliers import find_outliers_iqr

outliers_iqr, cleaned_iqr = find_outliers_iqr(data, feature)

# Метод z-отклонений
from outliers_lib.find_outliers import find_outliers_z_score

find_outliers_z_score
outliers_z_score, cleaned_z_score = find_outliers_z_score(data, feature)
```
Использование методов с предварительным логарифмированием:
```python
outliers_iqr, cleaned_iqr = find_outliers_iqr(data, feature, log=True)
outliers_z_score, cleaned_z_score = find_outliers_z_score(data, feature, log=True)
```
Использование методов с предварительным логарифмированием и добавлением вариативности разброса:
```python
outliers_iqr, cleaned_iqr = find_outliers_iqr(data, feature, log=True, left=2, right=2)
outliers_z_score, cleaned_z_score = find_outliers_z_score(data, feature, log=True, left=2, right=2)
```


## Использованные инструменты и библиотеки
* numpy (1.20.3)
* pandas (1.3.4)

## Дополнительные источники:
* [Нормальное распределение](https://ru.wikipedia.org/wiki/Нормальное_распределение)
* [Метод межквартильного размаха](https://recture.ru/common/chto-takoe-pravilo-mezhkvartilnogo-razmaha/)
* [Правило трех сигм](https://wiki.loginom.ru/articles/3-sigma-rule.html)



