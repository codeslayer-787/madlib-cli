import pytest

from madlib_cli.madlib import read_template, parse_template

def test_read_template_returns_stripped_string():
  actual = read_template("assets/video_game.txt")
  expected = "I the {Adjective} and {Adjective} {A First Name}"
  assert actual == expected

def test_parse_template():
    actual_stripped, actual_parts = parse_template(
        "I the {Adjective} and {Adjective} {A First Name}"
    )
    expected_stripped = "I the {} and {} {}"
    expected_parts = ("Adjective", "Adjective", "A First Name")

    assert actual_stripped == expected_stripped
    assert actual_parts == expected_parts

# @pytest.mark.skip("pending")
# def test_merge():
#     actual = merge("It was a {} and {} {}.", ("dark", "stormy", "night"))
#     expected = "It was a dark and stormy night."
#     assert actual == expected

# @pytest.mark.skip("pending")
# def test_read_template_raises_exception_with_bad_path():

#     with pytest.raises(FileNotFoundError):
#         path = "missing.txt"
#         read_template(path)