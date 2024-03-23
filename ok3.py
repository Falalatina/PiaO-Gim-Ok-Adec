from ortools.linear_solver import pywraplp

def max_rows_same_words(words, k):
    solver = pywraplp.Solver.CreateSolver('SCIP')

    # Dla każdej kolumny definiuję zmienną decyzyjną boolvar w celu dalszego określenia co ma się z nią dziać
    columns = []
    for j in range(len(words[0])):
        column_var = solver.BoolVar(f'column_{j}')
        columns.append(column_var)

    # ilośc kolumn jako ich suma
    solver.Add(sum(columns) == k)

    # Definiowanie zmiennych pomocniczych - liczba wierszy zawierających te same słowa
    rows_with_same_words = []
    for word in set(words):
        word_count = 0
        for i, row in enumerate(words):
            if all(row[j] == word[j] or not columns[j].solution_value() for j in range(len(row))):
                word_count += 1
        rows_with_same_words.append(word_count)

    # Maksymalizacja liczby wierszy z tymi samymi słowami
    solver.Maximize(sum(rows_with_same_words))

    # Rozwiązanie problemu
    status = solver.Solve()

    if status == pywraplp.Solver.OPTIMAL:
        optimal_solution = [j for j in range(len(columns)) if columns[j].solution_value() == 1]
        return optimal_solution
    else:
        return None

# Przykładowe dane
k = 7
words = [
    "LQCGAPPJAIQNNKHJNFFE",
    "LHCGAPPJABQNNKHJBFAE",
    "RQCGSPPJAIQNNKHJNFFE",
    "LQCGAPPJAIQNNKHJNFFE",
    "LQCGAPDJFIQNNKHJNFFE"
]

# Rozwiązanie
solution = max_rows_same_words(words, k)
print("Usunięte kolumny:", solution)
