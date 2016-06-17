from hamcrest import assert_that, is_

import src.main as steady_genes


def describe_desired_letter_count():
    def it_returns_how_many_times_every_letter_should_appear_in_text():
        assert_that(steady_genes.desired_letter_count('GAAATAAA'), is_(2))

def describe_excessive_letters():
    def describe_with_given_desired_repetetive_letter_count():
        def it_returns_map_of_how_much_each_letter_is_excessive_in_the_specified_word():
            excessive_letters = steady_genes.excessive_letters('GAAATAAA', 2)

            assert_that(excessive_letters, is_({'A': 4}))

def describe_starting_search_window_size():
    def it_sums_all_excessive_letters():
        window_size = steady_genes.starting_search_window_size(
            steady_genes.excessive_genes('GAAATAAC'))

        assert_that(window_size, is_(3))

def describe_min_substring():
    def describe_when_the_replaced_substring_is_at_position_0():
        def describe_when_substring_to_replace_length_is_exactly_the_exessive_letters_count():
            def it_returns_the_first_n_letters_of_the_string():
                assert_that(steady_genes.min_substring('AAAAAATG'), is_('AAAA'))

        def describe_when_first_letters_has_symbols_that_should_not_be_replaced():
            def it_returns_substring_that_is_as_long_as_it_needs_to_contain_all_letters_to_replace():
                assert_that(steady_genes.min_substring('AAATAAAG'), is_('AAATA'))

    def describe_when_the_replaced_substring_starts_at_random_position():
        def describe_when_first_letters_has_symbols_that_should_not_be_replaced():
            def it_returns_substring_that_is_as_long_as_it_needs_to_contain_all_letters_to_replace():
                assert_that(steady_genes.min_substring('GAAATAAA'), is_('AAATA'))

        def describe_when_first_found_substring_is_not_the_shortest_solution():
            def it_continues_to_search_for_the_shortest_substring():
                assert_that(steady_genes.min_substring('CGAAGCCA'), is_('CA'))

    def describe_when_the_replaced_substring_is_at_the_end_of_the_gene():
        def it_returns_satisfying_substring():
            assert_that(steady_genes.min_substring('AATCTCTT'), is_('TT'))

    def describe_when_the_specified_gene_is_already_steady():
        def it_returns_empty_substring():
            assert_that(steady_genes.min_substring('AACCGGTT'), is_(''))

def describe_stabilizes_gene():
    def describe_when_substring_characters_are_repeated_as_much_as_characters_that_need_to_be_replaced():
        def it_returns_true():
            assert_that(
                steady_genes.stabilizes_gene(
                    {'A': 1, 'B': 2},
                    {'A': 1, 'B': 2},
                ),
                is_(True)
            )

    def describe_when_substring_characters_are_not_repeated_enough():
        def it_returns_false():
            assert_that(
                steady_genes.stabilizes_gene(
                    {'A': 1, 'B': 1},
                    {'A': 1, 'B': 2},
                ),
                is_(False)
            )

    def describe_when_substring_characters_are_repeated_more_than_the_ones_that_need_to_be_replaced():
        def it_returns_true():
            assert_that(
                steady_genes.stabilizes_gene(
                    {'A': 2, 'B': 2},
                    {'A': 1, 'B': 2},
                ),
                is_(True)
            )

    def describe_when_there_are_less_characters_specified_than_need_to_be_replaced():
        def it_returns_false():
            assert_that(
                steady_genes.stabilizes_gene(
                    {'B': 2},
                    {'A': 1, 'B': 2},
                ),
                is_(False)
            )

    def describe_when_subdstring_doesnt_containt_all_characters_to_replace():
        def it_returns_false():
            assert_that(
                steady_genes.stabilizes_gene(
                    {'B': 2, 'C': 1},
                    {'A': 1, 'B': 2},
                ),
                is_(False)
            )

def describe_genes_replacement():
    def describe_when_substring_includes_excessive_characters_to_replace():
        def it_returns_the_substring():
            text = 'CCCAGTTT'
            replace_me = steady_genes.excessive_genes(text)

            replacement = steady_genes.genes_replacement(text, replace_me, 5)

            assert_that(replacement, is_('CCAGT'))
