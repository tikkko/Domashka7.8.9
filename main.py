def middle_(word):  # ДЗ 7. Знайти середиину рядка.
    if len(word) == 1:
        return word
    i = len(word) // 2
    if len(word) % 2 == 0:
        l: str = word[i - 1:-i + 1]
        return l
    else:
        m: str = word[i:-i]
        return m


def palindrome(slovo: str):  # ДЗ 8. Знайти паліндром.
    a = ''.join(reversed(slovo))
    if slovo == a:
        print(slovo, "is palindrome")
    else:
        print(slovo, "is NOT palindrome")


def century_converter(year):  # ДЗ 9. Порахувати номер століття.
    if year % 100 > 0:
        cent = year // 100 + 1
    else:
        cent = year // 100
    return cent


if __name__ == '__main__':
    print(middle_("middle"))
    palindrome("python")
    print(century_converter(777))

