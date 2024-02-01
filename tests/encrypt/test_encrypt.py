from challenges.challenge_encrypt_message import encrypt_message
import pytest


def test_encrypt_message():
    assert encrypt_message('Eric', 2) == 'ci_rE'
    assert encrypt_message('Eric', 3) == 'irE_c'
    assert encrypt_message('Eric', 999) == 'cirE'
    with pytest.raises(TypeError):
        encrypt_message("string", "teste")
    with pytest.raises(TypeError):
        encrypt_message(123, 1)
