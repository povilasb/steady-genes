from hamcrest import assert_that, is_, calling, raises

from src.main import SubstringIterator


def describe_substring_iterator():
    def describe_has_next():
        def describe_when_starting_from_initial_position_fits_substring_size():
            def it_returns_true():
                it = SubstringIterator('CGAAGCCA', 0, 2)
                assert_that(it.has_next(), is_(True))

    def describe_next():
        def describe_when_position_is_0():
            def it_returns_first_substring_size_bytes():
                it = SubstringIterator('abcdef', 0, 3)
                assert_that(it.__next__(), is_('abc'))

            def describe_when_used_in_list_comprehension():
                def it_returns_all_the_substrings():
                    it = SubstringIterator('abcde', 0, 3)

                    substrings = [substr for substr in it]

                    assert_that(substrings, is_(['abc', 'bcd', 'cde']))

        def it_increases_position():
            it = SubstringIterator('abcdef', 0, 3)
            it.__next__()

            assert_that(it.position, is_(1))

        def describe_when_position_is_0():
            def it_returns_first_substring_size_bytes():
                it = SubstringIterator('abcdef', 0, 3)
                assert_that(it.__next__(), is_('abc'))

        def describe_when_position_above_0():
            def it_returns_string_with_substring_size_characters_starting_from_the_current_position():
                it = SubstringIterator('abcdef', 0, 3)
                it.__next__()

                assert_that(it.__next__(), is_('bcd'))

            def describe_when_last_substring_reached():
                def it_raises_iterator_stop_if_we_iterate_more():
                    it = SubstringIterator('abcd', 0, 3)
                    it.__next__()
                    it.__next__()

                    assert_that(calling(it.__next__).with_args(),
                        raises(StopIteration))
