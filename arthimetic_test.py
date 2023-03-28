import pytest
from arthimetic import arthimetic

# test class to test artimetic operations in arthimetic file
class Test_arithmetic:

    # test to add function
    def test_add(self ):
        x, y = 1.0, 2.0
        expected_output = 3.0
        actual_output = arthimetic.add(x, y)
        assert expected_output == actual_output
        
    # test to subtract function
    def test_sub(self ):
        x, y = 1.0, 2.0
        expected_output = -1.0
        actual_output = arthimetic.subtract(x, y)
        assert expected_output == actual_output
    
    # # test to multiply function
    def test_mul(self ):
        x, y = 1.0, 2.0
        expected_output = 2.0
        actual_output = arthimetic.multiply(x, y)
        assert expected_output == actual_output

    # test to divide function  
    def test_divide(self ):
        x, y = 1.0, 2.0
        expected_output = 0.5
        actual_output = arthimetic.divide(x, y)
        assert expected_output == actual_output


