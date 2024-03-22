from collections import defaultdict

def find_max_same_words(words, k):
    n = len(words)  # liczba słow
    m = len(words[0])  # liczba liter w słowie

    # Liczenie różnych liter w każdej kolumnie
    column_diffs = defaultdict(int)
    for i in range(m):
        for j in range(n):
            column_diffs[i] += len(set(words[j][i] for j in range(n)))

    print('Posotowane kolumny wg ilosci slow:',sorted(column_diffs,  key=column_diffs.get, reverse=True))
    
    # Usunięcie kolumn z największą liczbą liter
    removed_columns = sorted(column_diffs, key=column_diffs.get, reverse=True)[:k]

    return removed_columns

# Przykładowe dane
k = 7
words = [
    "LQCGAPPJAIQNNKHJNFFE",
    "LHCGAPPJABQNNKHJBFAE",
    "RQCGSPPJAIQNNKHJNFFE",
    "LQCGAPPJAIQNNKHJNFFE",
    "LQCGAPDJFIQNNKHJNFFE"
]

# Rozwiązanie problemu
removed_columns = find_max_same_words(words, k)
print("Usunięte kolumny:", removed_columns)
