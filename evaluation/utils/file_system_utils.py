import csv


def get_dict_of_posts_from_csv(file):
    """
    returns a dictionary of dictionaries with the postId as the key
    :param file:
    :return:
    """
    posts = {}
    with open(file, "r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            posts[int(row['postId'])] = {k: int(v) for k, v in row.items()}
        return posts
