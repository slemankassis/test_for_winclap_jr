with open('c-input.in', 'rb') as file_in, open('answers.txt', 'wb') as file_out:
    lines = file_in.read().splitlines()
    case = 1

    for l in lines[1:]:
        digits = []
        result = 'INSOMNIA'

        for mult in xrange(1, 1000):
            n = str(int(l) * mult)
            for d in n:
                if d not in digits:
                    digits.append(d)
            if len(digits) == 10:
                result = n
                break

        file_out.write('Case #%d: %s\n' % (case, result))
        case += 1

