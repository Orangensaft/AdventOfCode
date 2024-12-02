from year2024.day2 import Day2


def test_is_monotonic_asc():
    assert Day2.is_monotonic([1, 2, 3, 4, 5])


def test_is_monotonic_desc():
    assert Day2.is_monotonic([5, 4, 3, 2, 1])


def test_is_not_monotonic():
    assert not Day2.is_monotonic([1, 5, 2, 3, 4])


def test_has_valid_gaps():
    assert Day2.has_valid_gaps([1, 2, 3, 4, 5])


def test_has_valid_gaps_same_number():
    assert not Day2.has_valid_gaps([1, 2, 3, 4, 4])


def test_has_valid_gaps_upper_limit():
    assert Day2.has_valid_gaps([1, 4, 7, 10])


def test_has_valid_gaps_too_big():
    assert not Day2.has_valid_gaps([1, 2, 3, 4, 8])


def test_is_safe_report():
    assert Day2.is_safe_report([7, 6, 4, 2, 1])


def test_is_not_safe_report():
    assert not Day2.is_safe_report([1, 2, 7, 8, 9])


def test_is_safe_without_dropping():
    assert Day2.is_safe_by_optional_dropping([7, 6, 4, 2, 1])


def test_is_safe_with_dropping():
    assert Day2.is_safe_by_optional_dropping([1, 3, 2, 4, 5])


def test_is_unsafe_with_dropping():
    assert not Day2.is_safe_by_optional_dropping([1, 2, 7, 8, 9])
