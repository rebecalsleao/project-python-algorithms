import pytest
from challenges.challenge_encrypt_message import encrypt_message



def test_encrypt_message():
    with pytest.raises(TypeError):
        encrypt_message(123, 6)

    with pytest.raises(TypeError):
        encrypt_message("abobrinha", "one")

    assert encrypt_message(message = 'beca', key = 4) == 'aceb'

    assert encrypt_message(message ='beca', key = 2) == 'ac_eb'

    assert encrypt_message(message = 'beca', key = -1) == 'aceb'

    assert encrypt_message(message = 'beca', key = 3) == 'ceb_a'