import pytest


@pytest.mark.parametrize("a, expected", [
    ('tachycardic', True),
    ('Tachycardic', True),
    ('tachycardic ', True),
    (' tachycardic', True),
    ('TACHYCARDIC', True),
    ('tachycardic;', True),
    ('tachyrdic', True),
    ('tachycard1c', True),
    ('tachycsrd1c', True),
    ('tachyrdi', False),
    ('tachycsmd1c', False),
    ('tachycd1c', False),
    ('tachycard1cc', False),
])
def test_is_tachycardic(a, expected):
    from tachycardic import is_tachycardic
    answer = is_tachycardic(a)
    assert answer == expected
