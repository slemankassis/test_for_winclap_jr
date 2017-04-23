def thousands_with_commas(i):
    THOUSAND = 1000
    value = i
    groups = []

    while(value % THOUSAND):
        groups.append((value % THOUSAND))
        value = value // THOUSAND

    # Reverse, change to str and add commas.
    return ','.join([str(j) for j in groups[::-1]])


if __name__ == '__main__':
    assert thousands_with_commas(1234) == '1,234'
    assert thousands_with_commas(123456789) == '123,456,789'
    assert thousands_with_commas(12) == '12'

