def merge(word, start=0, end=None):
    if end is None:
        end = len(word)
    if (end - start) > 1:
        # calcula o meio da palavra
        middle = (start + end) // 2
        # metade esquerda
        merge(word, start, middle)
        # metade direita
        merge(word, middle, end)
        # mescla as duas metades
        sort(word, start, middle, end)
    # retorna a "palavra" como uma string    
    return "".join(word)


def sort(word, start, middle, end):
    left = word[start:middle]
    rigth = word[middle:end]
    # divide a palavra em duas metades "left" e "rigth"

    left_index, rigth_index = 0, 0

    for i in range(start, end):
        # se a parte left já foi inserida, adiciona a parte rigth
        if left_index >= len(left):
            word[i] = rigth[rigth_index]
            rigth_index += 1
        # se a parte rigth já foi inserida, adiciona a parte left
        elif rigth_index >= len(rigth):
            word[i] = left[left_index]
            left_index += 1
        # se left for menor, adiciona a parte left
        elif left[left_index] < rigth[rigth_index]:
            word[i] = left[left_index]
            left_index += 1
        # caso não, adiciona a parte rigth
        else:
            word[i] = rigth[rigth_index]
            rigth_index += 1


def is_anagram(first_string, second_string):
    """Faça o código aqui."""
    first_str = merge(list(first_string.lower()))
    second_str = merge(list(second_string.lower()))
    true_or_false = first_str == second_str

    if first_string == "" and second_string == "":
        return (first_string, second_string, False)

    return (first_str, second_str, true_or_false)
