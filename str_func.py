def capital_letters() -> str:
    """Перевод строки на заглавные буквы"""
    user_word = input()
    word_upper = user_word.upper()
    return word_upper


print(capital_letters())
