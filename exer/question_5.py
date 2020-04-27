'''
Will be tested with year between 1913 and 2013.
You might find the reader() function of the csv module useful,
but you can also use the split() method of the str class.
'''

import csv, math

def f(year):
    '''
    >>> f(1914)
    In 1914, maximum inflation was: 2.0
    It was achieved in the following months: Aug
    >>> f(1922)
    In 1922, maximum inflation was: 0.6
    It was achieved in the following months: Jul, Oct, Nov, Dec
    >>> f(1995)
    In 1995, maximum inflation was: 0.4
    It was achieved in the following months: Jan, Feb
    >>> f(2013)
    In 2013, maximum inflation was: 0.82
    It was achieved in the following months: Feb
    '''
    months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    # Insert your code here
    with open('cpiai.csv', 'r') as csvfile:
        reader = csv.reader(csvfile)
        rows = [row for row in reader]

    max_data = str(-math.inf)
    month = []
    for row in rows:
        if row[0].split('-')[0] == str(year):
            if row[2] > max_data:
                month.clear()
                month.append(months[int(row[0].split('-')[1]) - 1])
                max_data = row[2]
            elif row[2] == max_data:
                month.append(months[int(row[0].split('-')[1]) - 1])

    print(f'In {year}, maximum inflation was: {max_data}')
    print(f'It was achieved in the following months: {", ".join(_ for _ in month)}')




if __name__ == '__main__':
    import doctest
    doctest.testmod()
