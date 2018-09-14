from search import binary_search
import tests.data as data

def test_binary_search_find_23():
    assert(binary_search(data.good_data, 23) == 23)

def test_binary_search_find_777():
    assert(binary_search(data.good_data, 777) is None)