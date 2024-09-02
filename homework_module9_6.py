def all_variants(text):
    """Генерирует все возможные подпоследовательности заданной строки.

    Args:
        text (str): Исходная строка.

    Yields:
        str: Следующая подпоследовательность.
    """

    for start_index in range(len(text)):
        for end_index in range(start_index + 1, len(text) + 1):
            yield text[start_index:end_index]

# Пример использования
a = all_variants("abc")
for subsequence in a:
    print(subsequence)