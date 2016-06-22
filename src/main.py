from collections import Counter


def desired_letter_count(text):
    return int(len(text) / 4)


def excessive_letters(text, letter_occurances):
    letters = {'A': 0, 'C': 0, 'G': 0, 'T': 0}
    letters.update({l: freq - letter_occurances for l, freq in Counter(text).items()
        if freq > letter_occurances})
    return letters


def excessive_genes(genes):
    return excessive_letters(genes, desired_letter_count(genes))


def gene_stabilized(replace_me):
    for freq in replace_me.values():
        if freq > 0:
            return False

    return True


def there_is_more_symbols_in(text, position):
    return position < len(text)


def expand_substring(text, right_position, exessive_symbols):
    while there_is_more_symbols_in(text, right_position) and \
            not gene_stabilized(exessive_symbols):
        symbol = text[right_position]
        exessive_symbols[symbol] -= 1
        right_position += 1

    return right_position, exessive_symbols


def reduce_substring(text, left_position, exessive_symbols):
    while gene_stabilized(exessive_symbols):
        symbol = text[left_position]
        exessive_symbols[symbol] += 1
        left_position += 1

    return left_position, exessive_symbols


def min_stabilizer(text):
    """Finds minimum substring that stabilizes gene.

    Args:
        text (str): string made of A, G, C, T symbols representing gene.

    Returns:
        int: minimum substring to be replaced so that gene would be stable.
    """
    replace_me = excessive_genes(text)
    if sum(replace_me.values()) == 0:
        return 0

    pos_r = 0
    pos_l = 0
    min_length = len(text)

    while there_is_more_symbols_in(text, pos_r):
        pos_r, replace_me = expand_substring(text, pos_r, replace_me)
        pos_l, replace_me = reduce_substring(text, pos_l, replace_me)

        if pos_r - pos_l + 1 < min_length:
            min_length = pos_r - pos_l + 1

    return min_length


def main():
    int(input()) # Reads the gene length, but in python we don't need that.
    s = input()

    print(min_stabilizer(s))


if __name__ == '__main__':
    main()
