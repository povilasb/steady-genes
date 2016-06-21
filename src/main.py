from collections import Counter


def desired_letter_count(text):
    return int(len(text) / 4)


def excessive_letters(text, letter_occurances):
    return {l: freq - letter_occurances for l, freq in Counter(text).items()
        if freq > letter_occurances}


def excessive_genes(genes):
    return excessive_letters(genes, desired_letter_count(genes))


def starting_search_window_size(excessive_genes):
    return sum(excessive_genes.values())


def stabilizes_gene(char_frequencies, replace_me):
    if len(char_frequencies) < len(replace_me):
        return False

    for symbol, freq in replace_me.items():
        if symbol not in char_frequencies or freq > char_frequencies[symbol]:
            return False

    return True


def expand_substring(substr, text, position, replace_me):
    while position + 1< len(text) and not stabilizes_gene(Counter(substr), replace_me):
        position += 1
        substr += text[position]

    return (substr, position)


def reduce_substring(substr, replace_me):
    last_removed_letter = ''

    while len(substr) > 0 and stabilizes_gene(Counter(substr), replace_me):
        last_removed_letter = substr[0]
        substr = substr[1:]

    return substr, last_removed_letter


def min_substring(text):
    min_substring = text
    replace_me = excessive_genes(text)

    if len(replace_me) == 0:
        return ''

    pos = 0
    substr = text[0]
    while pos + 1 < len(text):
        substr, pos = expand_substring(substr, text, pos, replace_me)
        substr, last_removed = reduce_substring(substr, replace_me)

        if len(substr) + 1 < len(min_substring):
            min_substring = last_removed + substr

    return min_substring


def main():
    n = int(input())
    s = input()

    print(len(min_substring(s)))


if __name__ == '__main__':
    main()
