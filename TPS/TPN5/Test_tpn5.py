import sys
sys.path.append("/Users/mac/Desktop/UTN/Programacion 1 tps/functions")
import pytest
import Functions

@pytest.mark.parametrize("input_number, expected_result", [
    ("44538355", True),
    ("1234567", True),
    ("12345", False),
    ("0", False),
    ("abcd", False),
])
def test_validate_dni(input_number, expected_result):
    assert Functions.validar_dni(input_number) == expected_result

@pytest.mark.parametrize("input, expected_result", [
    ("  hola como  estas ", 5),
    ("1234567", 7)

])
def test_validate_count_digits(input, expected_result):
    assert Functions.count_letters(input) == expected_result    

@pytest.mark.parametrize("a, b, expected_result", [
    (4,2, True),
    (7,2, False)
    

])
def test_validate_multip(a,b, expected_result):
    assert Functions.mult(a,b) == expected_result  