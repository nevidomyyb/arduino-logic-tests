def count_letters(string: str, char: str) -> int:
    return string.count(char)

sensor_input = "ABCDabcAAAdddEEEFgjkl1233251aAÇçsl23"
info_to_search = 'k'

print(f"O sensor recebeu a informação: {sensor_input}")
print(f"A informação '{info_to_search}' apareceu {count_letters(sensor_input, info_to_search)} vezes")