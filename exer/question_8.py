'''
Will be tested with letters a string of DISTINCT UPPERCASE letters only.
'''

from collections import Counter

def f(letters):
    '''
    >>> f('ABCDEFGH')
    There is no solution
    >>> f('GRIHWSNYP')
    The pairs of words using all (distinct) letters in "GRIHWSNYP" are:
    ('SPRING', 'WHY')
    >>> f('ONESIX')
    The pairs of words using all (distinct) letters in "ONESIX" are:
    ('ION', 'SEX')
    ('ONE', 'SIX')
    >>> f('UTAROFSMN')
    The pairs of words using all (distinct) letters in "UTAROFSMN" are:
    ('AFT', 'MOURNS')
    ('ANT', 'FORUMS')
    ('ANTS', 'FORUM')
    ('ARM', 'FOUNTS')
    ('ARMS', 'FOUNT')
    ('AUNT', 'FORMS')
    ('AUNTS', 'FORM')
    ('AUNTS', 'FROM')
    ('FAN', 'TUMORS')
    ('FANS', 'TUMOR')
    ('FAR', 'MOUNTS')
    ('FARM', 'SNOUT')
    ('FARMS', 'UNTO')
    ('FAST', 'MOURN')
    ('FAT', 'MOURNS')
    ('FATS', 'MOURN')
    ('FAUN', 'STORM')
    ('FAUN', 'STROM')
    ('FAUST', 'MORN')
    ('FAUST', 'NORM')
    ('FOAM', 'TURNS')
    ('FOAMS', 'RUNT')
    ('FOAMS', 'TURN')
    ('FORMAT', 'SUN')
    ('FORUM', 'STAN')
    ('FORUMS', 'NAT')
    ('FORUMS', 'TAN')
    ('FOUNT', 'MARS')
    ('FOUNT', 'RAMS')
    ('FOUNTS', 'RAM')
    ('FUR', 'MATSON')
    ('MASON', 'TURF')
    ('MOANS', 'TURF')
    '''
    dictionary = 'dictionary.txt'
    solutions = []
    # Insert your code here
    with open(dictionary, 'r') as file:
        all_words = file.readlines()
    all_words = [_.strip() for _ in all_words]
    list_a = [item for item in letters]

    letters_count = Counter(letters)
    for dic_word in all_words:
        dic_word_count = Counter(dic_word)
        isResult = True
        for i in dic_word:
            if i not in letters_count or dic_word_count.get(i) > letters_count.get(i):
                isResult = False
        if isResult:
            other_pair_of_words = "".join([_ for _ in list_a if _ not in dic_word])
            other_pair_of_words_count = Counter(other_pair_of_words)

            for word in all_words:
                new_word_count = Counter(word)
                if new_word_count == other_pair_of_words_count and (word, dic_word) not in solutions:
                    solutions.append((dic_word, word))

    if not solutions:
        print('There is no solution')
    else:
        print(f'The pairs of words using all (distinct) letters in "{letters}" are:')
        for solution in solutions:
            print(solution)



if __name__ == '__main__':
    import doctest
    doctest.testmod()
