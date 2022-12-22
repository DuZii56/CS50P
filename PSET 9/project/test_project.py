import project
from project import damage, Character, get_name, alive
import pytest


def main():
    test_invalid_name()
    test_alive()
    test_heal()


def test_alive():
    player = Character(get_name(), 25, int(damage())) #Test player is still alive
    assert alive(player) == True

    player = Character(get_name(), 0, int(damage())) #Test player has died
    assert alive(player) == False


def test_invalid_name(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: "David") #Test valid player name
    assert get_name() == "David"

    monkeypatch.setattr('builtins.input', lambda _: '') #Test invalid player name
    with pytest.raises(TypeError):
        get_name('') == "\nInvalid name"


def test_heal():
    player = Character(get_name(), 25, int(damage())) #Test healing function
    player.heal(player)
    assert player.hp == 50


if __name__ == "__main__":
    main()
