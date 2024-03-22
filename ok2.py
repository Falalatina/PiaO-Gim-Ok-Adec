from collections import Counter

def find_max_same_words(words, k):
    n = len(words)  # liczba słow
    m = len(words[0]) # liczba liter w słowie
    
    # Porównanie 2 wierszy i dodanie indeksow liter ktore sie nie powtarzaja
    # column_counts = Counter()
    # for i in range(n - 1):
    #     for j in range(m):
    #         if words[i][j] != words[i + 1][j]:
    #             column_counts[j] += 1

    column_counts = Counter()
    for i in range(n):
        for j in range(m):
            for other_row in range(  n):
               # print('wiersz', i, 'kolumna', j, 'porownuje z wierszem', other_row)
                if i != other_row and words[i][j] != words[other_row][j]:
                    column_counts[j] += 1
                   # print('wierszi:',i,'kolumna j:',j,words[i][j] , 'porow z', words[other_row][j] )

    print(column_counts)
    # Wybranie indeksów kolumn z największą liczbą wystąpień
    # removed_columns = [index for index, count in column_counts.most_common(k)]
    removed_columns = [index for index, count in column_counts.most_common(k)]


    return sorted(removed_columns)


def print_words_after_removal(words, removed_columns):
    for word in words:
        new_word = ''.join(word[j] for j in range(len(word)) if j not in removed_columns)
        print(new_word)

# Przykładowe dane
k = 7
words = [
    "LQCGAPPJAIQNNKHJNFFE",
    "LHCGAPPJABQNNKHJBFAE",
    "RQCGSPPJAIQNNKHJNFAE",
    "LQCGAPPJAIQNNKHJNFFE",
    "LQCGAPDJFIQNNKHJNFFE"
]

wynik=[1,4,6,8,9,16,18]


# Rozwiązanie problemu
removed_columns = find_max_same_words(words, k)
print("Usunięte kolumny:", removed_columns)
print("Słowa po usunięciu wskazanych kolumn:")
print_words_after_removal(words, removed_columns)
