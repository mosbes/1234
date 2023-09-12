def counter_sin(word):
    word = word.lower()
    counter = 0
    for symbol in set(word):
        symbol = symbol.lower()
        if word.count(symbol)> 1:
            counter+=1
    return counter
print(counter_sin(input()))
