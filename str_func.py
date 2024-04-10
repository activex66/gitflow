def capital_letters() -> str:
    """"Изменяет строку на заглавные,
     поступившей на вход функции"""
    user_word = input()
    word_upper = user_word.upper()
    return word_upper


print(capital_letters())


def words_title(word) -> str:
    """Изменяет первые буквы каждого слова в строке,
     поступившей на вход функции"""
    return word.title()
