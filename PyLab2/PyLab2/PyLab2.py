def shift_list_right(lst, k):
    if not lst:
        return lst
    k %= len(lst)
    return lst[-k:] + lst[:-k]

def shift_list_left(lst, k):
    if not lst:
        return lst
    k %= len(lst)
    return lst[k:] + lst[:k]

def swap_first_last(word):
    if len(word) <= 1:
        return word
    return word[-1] + word[1:-1] + word[0]

def caesar_cipher(text, m):
    result = []
    for char in text:
        if 'a' <= char <= 'z':
            result.append(chr((ord(char) - ord('a') + m) % 26 + ord('a')))
        elif 'A' <= char <= 'Z':
            result.append(chr((ord(char) - ord('A') + m) % 26 + ord('A')))
        else:
            result.append(char)
    return "".join(result)

def generate_cipher_dict(text):
    unique_chars = []
    for char in text:
        if char not in unique_chars:
            unique_chars.append(char)
    cipher_dict = {}
    current_code = 52
    for char in unique_chars:
        cipher_dict[char] = str(current_code)
        current_code += 1
    return cipher_dict

def encrypt_to_numbers(text, cipher_dict):
    return "".join(cipher_dict[char] for char in text)

def decrypt_from_numbers(num_str, cipher_dict):
    dec_dict = {v: k for k, v in cipher_dict.items()}
    result = []
    for i in range(0, len(num_str), 2):
        code = num_str[i:i+2]
        result.append(dec_dict[code])
    return "".join(result)

def run_cipher_system():
    input_string = input("Введите строку: ")
    k = int(input("Введите число k (сдвиг списка): "))
    m = int(input("Введите число m (шаг Цезаря): "))
    
    print("\n--- АЛГОРИТМ ШИФРОВАНИЯ ---")
    print(f"Шаг 0. Исходная строка: '{input_string}'")
    
    words = input_string.split(" ")
    print(f"Шаг 1. Разбиение на список слов: {words}")
    
    words_reversed = words[::-1]
    print(f"Шаг 2. Переворот списка слов: {words_reversed}")
    
    words_shifted = shift_list_right(words_reversed, k)
    print(f"Шаг 3. Циклический сдвиг списка вправо на {k}: {words_shifted}")
    
    words_swapped = [swap_first_last(w) for w in words_shifted]
    print(f"Шаг 4. Перестановка первой и последней буквы в словах: {words_swapped}")
    
    words_caesar = [caesar_cipher(w, m) for w in words_swapped]
    print(f"Шаг 5. Шифр Цезаря с шагом {m}: {words_caesar}")
    
    encrypted_string = " ".join(words_caesar)
    print(f"Шаг 6. Сборка списка обратно в строку: '{encrypted_string}'")
    
    cipher_dict = generate_cipher_dict(encrypted_string)
    print(f"Шаг 7. Создание словаря уникальных символов: {cipher_dict}")
    
    numeric_result = encrypt_to_numbers(encrypted_string, cipher_dict)
    print(f"Шаг 8. Преобразование строки в числовой код: {numeric_result}")
    
    print("\n--- АЛГОРИТМ ДЕШИФРОВАНИЯ ---")
    print(f"Шаг 0. Исходный числовой код: {numeric_result}")
    
    dec_string = decrypt_from_numbers(numeric_result, cipher_dict)
    print(f"Шаг 1. Декодирование по словарю в строку: '{dec_string}'")
    
    dec_words = dec_string.split(" ")
    print(f"Шаг 2. Разбиение строки на слова: {dec_words}")
    
    dec_caesar = [caesar_cipher(w, -m) for w in dec_words]
    print(f"Шаг 3. Обратный шифр Цезаря (шаг {-m}): {dec_caesar}")
    
    dec_swapped = [swap_first_last(w) for w in dec_caesar]
    print(f"Шаг 4. Обратная перестановка первой и последней буквы: {dec_swapped}")
    
    dec_shifted = shift_list_left(dec_swapped, k)
    print(f"Шаг 5. Циклический сдвиг списка слов влево на {k}: {dec_shifted}")
    
    dec_reversed = dec_shifted[::-1]
    print(f"Шаг 6. Переворот списка слов в исходный порядок: {dec_reversed}")
    
    final_string = " ".join(dec_reversed)
    print(f"Шаг 7. Итоговая дешифрованная строка: '{final_string}'")

run_cipher_system()
