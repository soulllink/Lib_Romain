
letters = ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX', 'X']

def romanize_dec(num):
    return letters[num-1]

def romanize_beyond(num, temp=[]):
    if num >= 1000:
        return romanize_beyond(num - 1000, temp + ['M'])
    if num <= 1000 and num - 500 > 0:
        return romanize_beyond(num - 500, temp + ['D'])
    if num <= 500 and num - 100 > 0:
        return romanize_beyond(num - 100, temp + ['C'])
    if num <= 100 and num - 50 > 0:
        return romanize_beyond(num - 50, temp + ['L'])
    if num <= 50 and num - 10 > 0:
        return romanize_beyond(num - 10, temp + ['X'])
    if num < 10 and num != 0:
        return temp + [romanize_dec(num)]
    if num == 0:
        return temp

def rocollect(romalist):
    return ''.join(romalist)

def main():
    print(romanize_collect(romanize_beyond(1337)))

if __name__ == '__main__':
    main()
