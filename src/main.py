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


class SubstringIterator:
    """Iterates fixed sized substrings within some text."""

    def __init__(self, text, start_position, substring_size):
        self.text = text
        self.position = start_position
        self.substring_size = substring_size

    def __iter__(self):
        return self

    def __next__(self):
        if not self.has_next():
            raise StopIteration()

        position = self.position
        self.position += 1

        return self.text[position:position + self.substring_size]

    def has_next(self):
        return self.position <= len(self.text) - self.substring_size


def stabilizes_gene(char_frequencies, replace_me):
    if len(char_frequencies) < len(replace_me):
        return False

    for symbol, freq in replace_me.items():
        if symbol not in char_frequencies or freq > char_frequencies[symbol]:
            return False

    return True


def genes_replacement(text, replace_me, window_size):
    for substr in SubstringIterator(text, 0, window_size):
        if stabilizes_gene(Counter(substr), replace_me):
            return substr

    return text


def min_substring(text):
    replace_me = excessive_genes(text)
    init_window_size = starting_search_window_size(replace_me)

    for window_size in range(init_window_size, len(text)):
        replacement = genes_replacement(text, replace_me, window_size)
        if len(replacement) < len(text):
            return replacement

    return text


def main():
    n = int(input())
    s = input()

    print(len(min_substring(s)))


if __name__ == '__main__':
    main()
