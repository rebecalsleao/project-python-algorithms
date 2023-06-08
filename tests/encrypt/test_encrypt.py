# from challenges.challenge_encrypt_message import encrypt_message


def test_encrypt_message():
    pass


def soma(a, b):
    assert isinstance(a, int) and isinstance(
        b, int
    ), "Os argumentos devem ser números inteiros"
    return a + b


resultado = soma(2, 3)
assert resultado == 5, "A soma está incorreta"
