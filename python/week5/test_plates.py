import plates

def test_is_valid():
    assert plates.is_valid("CS50") == True
    assert plates.is_valid("CS50P") == False

def test_is_valid_edge_cases():
    assert plates.is_valid("AB") == True
    assert plates.is_valid("A1") == False
    assert plates.is_valid("A12") == False
    assert plates.is_valid("A123") == False
    assert plates.is_valid("A1234") == False
    assert plates.is_valid("A12345") == False
    assert plates.is_valid("A123456") == False
    assert plates.is_valid("AB1") == True
    assert plates.is_valid("AB12") == True
    assert plates.is_valid("AB123") == True
    assert plates.is_valid("AB1234") == True
    assert plates.is_valid("AB12345") == False

def test_is_valid_special_characters():
    assert plates.is_valid("CS50!") == False
    assert plates.is_valid("CS50@") == False

def test_is_valid_lowercase():
    assert plates.is_valid("cs50") == True
    assert plates.is_valid("cs50p") == False

def test_is_valid_mixed_case():
    assert plates.is_valid("Cs50") == True
    assert plates.is_valid("cS50") == True
    assert plates.is_valid("CS50p") == False

def test_is_valid_numbers_only():
    assert plates.is_valid("123456") == False
    assert plates

def test_is_valid_empty_string():
    assert plates.is_valid("") == False

def test_is_valid_whitespace():
    assert plates.is_valid(" ") == False
    assert plates.is_valid(" CS50 ") == False

def test_zero_placement():
    assert plates.is_valid("CS05") == False
    assert plates.is_valid("AA01") == False