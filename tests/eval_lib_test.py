import pytest

from evaluation.eval_lib import array_diff, tally_followers


def test_array_diff():
    current = [1, 3, 5, 6, 8, 9]
    target = [1, 2, 5, 7, 9]
    addition, deletion = array_diff(current, target)
    assert addition == [2, 7]
    assert deletion == [3, 6, 8]


def test_array_diff_empty():
    addition, deletion = array_diff([], [])
    assert addition == []
    assert deletion == []


def test_array_diff_one_list_empty():
    current = []
    target = [1, 2, 5, 7, 9]
    addition, deletion = array_diff(current, target)
    assert addition == [1, 2, 5, 7, 9]
    assert deletion == []


def test_array_diff_strings():
    current = ['cow', 'moose', 'monkey']
    target = ['monkey', 'dog', 'jackalope']
    addition, deletion = array_diff(current, target)
    assert addition == ['dog', 'jackalope']
    assert deletion == ['cow', 'moose']


def test_tally_followers(dictionary_of_csv_records):
    assert tally_followers(dictionary_of_csv_records) == {1: 350, 7: 480}


def test_tally_followers_empty(dictionary_of_csv_records_empty_dictionary):
    assert tally_followers(dictionary_of_csv_records_empty_dictionary) == {}


@pytest.fixture()
def dictionary_of_csv_records():
    return {
        1: {
            'postId': 1,
            'repostId': -1,
            'followers': 120
        },
        2: {
            'postId': 2,
            'repostId': 1,
            'followers': 60
        },
        3: {
            'postId': 3,
            'repostId': 1,
            'followers': 30
        },
        4: {
            'postId': 4,
            'repostId': 2,
            'followers': 90
        },
        5: {
            'postId': 5,
            'repostId': 3,
            'followers': 40
        },
        6: {
            'postId': 6,
            'repostId': 4,
            'followers': 10
        },
        7: {
            'postId': 7,
            'repostId': -1,
            'followers': 240
        },
        8: {
            'postId': 8,
            'repostId': 7,
            'followers': 190
        },
        9: {
            'postId': 9,
            'repostId': 7,
            'followers': 50
        }
    }


@pytest.fixture()
def dictionary_of_csv_records_empty_dictionary():
    return {}
