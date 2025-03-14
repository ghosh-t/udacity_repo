from tryexcept import divide_vals

def test_divide_vals():
    assert(divide_vals(10,2) == 5)
    assert(divide_vals(5,2) == 2.5)
    assert(divide_vals(-5,2) == -2.5)
    assert(divide_vals(5,-2) == -2.5)
    assert(divide_vals(5,0) == "denominator cannot be zero")

def test_divide_vals_zero(): 
    assert(divide_vals(2,0) == "denominator cannot be zero")
    assert(divide_vals(-9,0) == "denominator cannot be zero")
    assert(divide_vals(21,0) == "denominator cannot be zero") 