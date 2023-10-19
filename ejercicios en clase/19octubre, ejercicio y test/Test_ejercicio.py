import sys
sys.path.append("/Users/mac/Desktop/UTN/Programacion 1 tps/functions")
import pytest
import Functions

@pytest.mark.parametrize("input_number, expected_result", [
    (5, 5),
    (12345, 15),
    (0, 0),
    (987654321, 45),
])
def test_count_digits(input_number, expected_result):
    assert Functions.count_digits(input_number) == expected_result


