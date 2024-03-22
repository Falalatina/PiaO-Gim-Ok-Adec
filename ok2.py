from collections import Counter

def find_max_same_words(words, k):
    n = len(words)  # liczba słow
    m = len(words[0])  # liczba liter w słowie

    # Porównanie 2 wierszy i dodanie indeksow liter ktore sie nie powtarzaja
    # column_counts = Counter()
    # for i in range(n - 1):
    #     for j in range(m):
    #         if words[i][j] != words[i + 1][j]:
    #             column_counts[j] += 1

    column_counts = Counter()
    for i in range(n):
        for j in range(m):
            for other_row in range(n):
                if i != other_row and words[i][j] != words[other_row][j]:
                    column_counts[j] += 1

    print(column_counts)
    # Wybranie indeksów kolumn z największą liczbą wystąpień
    removed_columns = [index for index, count in column_counts.most_common(k)]

    return sorted(removed_columns)

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
