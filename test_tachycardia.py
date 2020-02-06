import pytest


@pytest.mark.parametrize("a, expected", [
    ('tachycardic', True),
    ('Tachycardic', True),
    ('tachycardic ', True),
    (' tachycardic', True),
    ('TACHYCARDIC', True),
    ('tachycardic;', True),
])
def test_is_tachycardic(a, expected):
    from tachycardic import is_tachycardic
    answer = is_tachycardic(a)
    assert answer == expected
