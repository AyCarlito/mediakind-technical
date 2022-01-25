from task import postcodes

def test_for_non_existing_postcode():
    assert(postcodes.get_postcode_data("SFF")) is None

def test_for_existing_postcode():
    assert(postcodes.get_postcode_data("BL4 0QL")) is not None

def test_for_office_postcode():
    assert(postcodes.get_postcode_data("SO30 4DA")) is not None

def test_for_live_postcode():
    assert(postcodes.get_postcode_data("BL4 0QA")[1]) == "live"

def test_for_terminated_postcode():
    assert(postcodes.get_postcode_data("BL4 0YW")[1]) == "terminated"

def test_distance_between_same_postcodes_is_zero():
    assert(postcodes.get_distance(postcodes.get_postcode_data("SO30 4DA"), postcodes.get_postcode_data("SO30 4DA"))) == 0.0

def test_pythagorean_triple_3_4_5():
    assert((postcodes.get_distance([None, None, None, 1, 2], [None, None, None,4, 6]))) == 5.0

def test_pythagorean_triple_5_12_13():
    assert((postcodes.get_distance([None, None, None, 1, 2], [None, None, None,6, 14]))) == 13.0

def test_office_data_no_of_fields():
    assert(len(postcodes.get_postcode_data("SO30 4DA"))) == 17

def test_user_postcode_data_no_of_fields():
    assert(len(postcodes.get_postcode_data("BL4 0YW"))) == 17

def test_negative_difference():
    assert((postcodes.get_distance([None, None, None, 1, 2], [None, None, None,4, 6]))) == 5.0

def test_positive_difference():
    assert((postcodes.get_distance([None, None, None, 4, 6], [None, None, None,1, 2]))) == 5.0
    
