def title(string):
    for i in range(0, len(string)):
        if string[i-1] in "\t, " or i == 0:
            if "a" <= string[i] <= "z" or "а" <= string[i] <= "я":  # Работает только для английского и русского языков
                string = string[:i] + chr(ord(string[i])-32) + string[i + 1:]
    return string


# Тестовая строка
input_str = "тесТОвое задание   для pt"

# Вызов переопределённой функции title
print(title(input_str))
