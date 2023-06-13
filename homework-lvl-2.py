# Задача 2.1. 

# Создайте две функции maximum и minimum,
# которые получают список целых чисел в качестве входных данных 
# и возвращают наибольшее и наименьшее число в этом списке соответственно.
# Например,
# * [4,6,2,1,9,63,-134,566]         -> max = 566, min = -134
# * [-52, 56, 30, 29, -54, 0, -110] -> min = -110, max = 56
# * [42, 54, 65, 87, 0]             -> min = 0, max = 87
# * [5]                             -> min = 5, max = 5
# функции sorted, max и min использовать нельзя!

def maximum(lst):
    max_num = lst[0]
    for num in lst:
        if num > max_num:
            max_num = num
    return max_num

def minimum(lst):
    min_num = lst[0]
    for num in lst:
        if num < min_num:
            min_num = num
    return min_num

numbers1 = [4, 6, 2, 1, 9, 63, -134, 566]
print(f"max = {maximum(numbers1)}, min = {minimum(numbers1)}")
numbers2 = [-52, 56, 30, 29, -54, 0, -110]
print(f"max = {maximum(numbers2)}, min = {minimum(numbers2)}")
numbers3 = [42, 54, 65, 87, 0]
print(f"max = {maximum(numbers3)}, min = {minimum(numbers3)}")
numbers4 = [5]
print(f"max = {maximum(numbers4)}, min = {minimum(numbers4)}")

# Задача 2.2. 

# Напишите функцию, которая возвращает номер квартал по номеру месяца
# Например: 
# месяц 2 (февраль) является частью первого квартала; 
# месяц 6 (июнь) является частью второго квартала; 
# месяц 11 (ноябрь) является частью четвертого квартала.

def quarter_of(month):
    if month in range(1, 4):
        return 1
    elif month in range(4, 7):
        return 2
    elif month in range(7, 10):
        return 3
    elif month in range(10, 13):
        return 4
    else:
        return "Неверный номер месяца"

month1 = 2
print(f"Месяц {month1} относится к {quarter_of(month1)} кварталу")
month2 = 6
print(f"Месяц {month2} относится к {quarter_of(month2)} кварталу")
month3 = 11
print(f"Месяц {month3} относится к {quarter_of(month3)} кварталу")



# Задача 2.3.

# Напишите функцию, которая принимает цифры от 0 до 9 и возвращает значение прописью.
# Например,
# switch_it_up(1) -> 'One'
# switch_it_up(3) -> 'Three'
# switch_it_up(10000) -> None
# Использовать условный оператор if-elif-else нельзя!

def switch_it_up(number):
    num_dict = {
        0: 'Zero',
        1: 'One',
        2: 'Two',
        3: 'Three',
        4: 'Four',
        5: 'Five',
        6: 'Six',
        7: 'Seven',
        8: 'Eight',
        9: 'Nine'
    }

    return num_dict.get(number)

print(switch_it_up(1))      
print(switch_it_up(3))      
print(switch_it_up(7))      
print(switch_it_up(9))      
print(switch_it_up(10000))  


# Задача 2.4.

# Пункт A.
# Напишите функцию, которая удаляет все восклицательные знаки из заданной строк.
# Например,
# foo("Hi! Hello!") -> "Hi Hello"
# foo("") -> ""
# foo("Oh, no!!!") -> "Oh, no"

def remove_exclamation_marks(s):
    return s.replace("!", "")

print(remove_exclamation_marks("Hi! Hello!"))    
print(remove_exclamation_marks(""))              
print(remove_exclamation_marks("Oh, no!!!"))     

# Пункт B.
# Удалите восклицательный знак из конца строки. 
# remove("Hi!") == "Hi"
# remove("Hi!!!") == "Hi!!"
# remove("!Hi") == "!Hi"

def remove_last_em(s):
    if s.endswith("!"):
        return s[:len(s) - 1]
    return s

print(remove_last_em("Hi!"))       
print(remove_last_em("Hi!!!"))     
print(remove_last_em("!Hi"))       

# Дополнительно

# Пункт С.
# Удалите слова из предложения, если они содержат ровно один восклицательный знак.
# Слова разделены одним пробелом.
# Например,
# remove("Hi!") === ""
# remove("Hi! Hi!") === ""
# remove("Hi! Hi! Hi!") === ""
# remove("Hi Hi! Hi!") === "Hi"
# remove("Hi! !Hi Hi!") === ""
# remove("Hi! Hi!! Hi!") === "Hi!!"
# remove("Hi! !Hi! Hi!") === "!Hi!"

def remove_word_with_one_em(s):
    words = s.split()
    result = []
    for word in words:
        if word.count("!") != 1:
            result.append(word)
    return " ".join(result)

print(remove_word_with_one_em("Hi!"))            
print(remove_word_with_one_em("Hi! Hi!"))        
print(remove_word_with_one_em("Hi! Hi! Hi!"))   
print(remove_word_with_one_em("Hi Hi! Hi!"))     
print(remove_word_with_one_em("Hi! !Hi Hi!"))    
print(remove_word_with_one_em("Hi! Hi!! Hi!"))   
print(remove_word_with_one_em("Hi! !Hi! Hi!"))   
