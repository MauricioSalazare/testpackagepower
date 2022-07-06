import pytest
from testpackagepower import compute_function

def test_compute_correct_answer():
    assert compute_function(1, 1) == 12

def test_incorrect_type_input_in_compute_raises_assertion_error():
    with pytest.raises(AssertionError):
        compute_function("a", 2)
