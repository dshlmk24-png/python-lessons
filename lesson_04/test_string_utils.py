import pytest

from string_utils import StringUtils


@pytest.fixture
def string_utils():
    return StringUtils()


# =========================
# Тесты capitalize
# =========================

def test_capitalize_positive(string_utils):
    assert string_utils.capitalize("test") == "Test"


def test_capitalize_with_numbers(string_utils):
    assert string_utils.capitalize("123") == "123"


def test_capitalize_empty_string(string_utils):
    assert string_utils.capitalize("") == ""


def test_capitalize_with_spaces(string_utils):
    assert string_utils.capitalize(" тест") == " тест"


# =========================
# Тесты trim
# =========================

def test_trim_positive(string_utils):
    assert string_utils.trim(" test") == "test"


def test_trim_multiple_spaces(string_utils):
    assert string_utils.trim("   test") == "test"


def test_trim_string_without_spaces(string_utils):
    assert string_utils.trim("test") == "test"


def test_trim_empty_string(string_utils):
    assert string_utils.trim("") == ""


def test_trim_only_spaces(string_utils):
    assert string_utils.trim("   ") == ""


# =========================
# Тесты contains
# =========================

def test_contains_positive(string_utils):
    assert string_utils.contains("Test", "e") is True


def test_contains_negative(string_utils):
    assert string_utils.contains("Test", "U") is False


def test_contains_empty_string(string_utils):
    assert string_utils.contains("", "a") is False


def test_contains_number_as_string(string_utils):
    assert string_utils.contains("123", "2") is True


def test_contains_space(string_utils):
    assert string_utils.contains("Test Test", " ") is True


# =========================
# Тесты delete_symbol
# =========================

def test_delete_symbol_positive(string_utils):
    assert string_utils.delete_symbol("Testing", "i") == "Testng"


def test_delete_symbol_word(string_utils):
    assert string_utils.delete_symbol("TestProgr", "Progr") == "Test"


def test_delete_symbol_multiple_occurrences(string_utils):
    assert string_utils.delete_symbol("banana", "a") == "bnn"


def test_delete_symbol_not_found(string_utils):
    assert string_utils.delete_symbol("Test", "x") == "Test"


def test_delete_symbol_empty_string(string_utils):
    assert string_utils.delete_symbol("", "a") == ""


def test_delete_symbol_spaces(string_utils):
    assert string_utils.delete_symbol("a b c", " ") == "abc"
