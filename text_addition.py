from addition import add
def text_add_positive_numbers():
    assert add(2, 3) == 5
    
def text_add_negative_numbers():
    assert add(-4, -6) == -10
    
def text_add_zero():
    assert add(0, 5) == 5
  