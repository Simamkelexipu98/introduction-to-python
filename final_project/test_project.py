from project import get_energy_consumption , get_solar_production, calculate_energy_balance

def test_calculate_energy_balance():
    assert calculate_energy_balance(100,150) == 50
    assert calculate_energy_balance(200,100) == -100
    assert calculate_energy_balance(0,0) == 0

import pytest

def test_get_energy_consumption(monkeypatch):
    monkeypatch.setattr("builtins.input",lambda _:"200")
    assert get_energy_consumption() == 200.0


def test_get_solar_production(monkeypatch):
    monkeypatch.setattr("builtins.input",lambda _:"5")
    monkeypatch.setattr("builtins.input",lambda _:"10")
    assert get_solar_production() == 50.0

