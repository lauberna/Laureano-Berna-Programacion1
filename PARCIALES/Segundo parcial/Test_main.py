from functions import is_mutant
import pytest


@pytest.mark.parametrize("dna, expected_result", [
    ([
        "ATGCGA",
        "CAGTGC",
        "TTATTT",
        "AGACGG",
        "GCGTCA",
        "TCACTG"], False),
    ([
        "ATGCAG",
        "CAGTAC",
        "CCAAGT",
        "CGAAGG",
        "CACCGA",
        "TCACTG"], True),
]

)
def test_is_mutant_False(dna, expected_result):
    assert is_mutant(dna) == expected_result

