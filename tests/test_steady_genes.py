from hamcrest import assert_that, is_

import src.main as steady_genes


def describe_desired_letter_count():
    def it_returns_how_many_times_every_letter_should_appear_in_text():
        assert_that(steady_genes.desired_letter_count('GAAATAAA'), is_(2))

def describe_excessive_letters():
    def describe_with_given_desired_repetetive_letter_count():
        def it_returns_map_of_how_much_each_letter_is_excessive_in_the_specified_word():
            excessive_letters = steady_genes.excessive_letters('GAAATAAA', 2)

            assert_that(excessive_letters, is_({'A': 4, 'C': 0, 'G': 0, 'T': 0}))

def describe_min_stabilizer():
    def describe_when_the_replaced_substring_is_at_position_0():
        def describe_when_substring_to_replace_length_is_exactly_the_exessive_letters_count():
            def it_returns_the_first_n_letters_of_the_string():
                assert_that(steady_genes.min_stabilizer('AAAAAATG'), is_(4))

        def describe_when_first_letters_has_symbols_that_should_not_be_replaced():
            def it_returns_substring_that_is_as_long_as_it_needs_to_contain_all_letters_to_replace():
                assert_that(steady_genes.min_stabilizer('AAATAAAG'), is_(5))

    def describe_when_the_replaced_substring_starts_at_random_position():
        def describe_when_first_letters_has_symbols_that_should_not_be_replaced():
            def it_returns_substring_that_is_as_long_as_it_needs_to_contain_all_letters_to_replace():
                assert_that(steady_genes.min_stabilizer('GAAATAAA'), is_(5))

        def describe_when_first_found_substring_is_not_the_shortest_solution():
            def it_continues_to_search_for_the_shortest_substring():
                assert_that(steady_genes.min_stabilizer('CGAAGCCA'), is_(2))

    def describe_when_the_replaced_substring_is_at_the_end_of_the_gene():
        def it_returns_satisfying_substring():
            assert_that(steady_genes.min_stabilizer('AATCTCTT'), is_(2))

    def describe_when_the_specified_gene_is_already_steady():
        def it_returns_empty_substring():
            assert_that(steady_genes.min_stabilizer('AACCGGTT'), is_(0))
