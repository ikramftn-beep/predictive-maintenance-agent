from src.utils.scoring import phm_score

def test_perfect_prediction():
    assert phm_score([10, 20], [10, 20]) == 0

def test_late_is_penalized_more():
    assert phm_score([70], [60]) > phm_score([50], [60])
