# from evaluation.utils.benchmark_utils import time_this
from evaluation.utils.file_system_utils import get_dict_of_posts_from_csv


# @time_this
def array_diff(current, target):
    """
     2 arrays of integers, "current" and "target", and produce 2 arrays
     representing an additions list and a deletions list such that applying
     the additions and deletions to the "current" array will yield the "target"
     array.
    :param current: list
    :param target: list
    :return: additions: list, deletions: list
    """
    if not isinstance(current, (list,)) and not isinstance(target, (list,)):
        return None, None
    # e-05 seconds sorted or e-06 seconds if unsorted
    # a = set(current)
    # b = set(target)
    #
    # return sorted(list(a - b)), sorted(list(b - a))

    # e-06 seconds
    additions = [x for x in target if x not in current]
    deletions = [x for x in current if x not in target]
    return additions, deletions


def tally_followers(posts):
    """
    tally the total number of followers from original and reposts
    :param posts:
    :return:
    """
    tally = {}
    for key, post in posts.items():
        original_post_id = post['postId']

        while posts[original_post_id]['repostId'] != -1:
            original_post_id = posts[original_post_id]['repostId']

        if original_post_id in tally:
            tally[original_post_id] += post['followers']
        else:
            tally[original_post_id] = post['followers']
    return tally


def social_network_analysis(filename):
    """ loads a csv file into a dictionary of dictionaries and tallies the
    total number of followers"""
    posts = get_dict_of_posts_from_csv(filename)
    return tally_followers(posts)


if __name__ == "__main__":
    list_a = [1, 3, 5, 6, 8, 9]
    list_b = [1, 2, 5, 7, 9]
    additions_example, deletions_example = array_diff(list_a, list_b)

    print(additions_example)
    print(deletions_example)

    print(social_network_analysis('../data/test_data.csv'))
