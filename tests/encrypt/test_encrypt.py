from challenges.challenge_encrypt_message import encrypt_message
import pytest


def test_encrypt_message():
    with pytest.raises(TypeError, match="tipo inválido para key"):
        encrypt_message("message", "olá")
    with pytest.raises(TypeError, match="tipo inválido para message"):
        encrypt_message(123, 1)
    assert encrypt_message("message", 1) == "m_egasse"

    assert encrypt_message("message", 18) == "egassem"
