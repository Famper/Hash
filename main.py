import json
import re

from hash_set import HashSet


def set_default(obj):
    """
    set replace to list type

    :param obj:
    :return:
    """
    if isinstance(obj, set):
        return list(obj)
    raise TypeError


if __name__ == '__main__':
    print(f"\n[System] - Start")

    hash_object = HashSet()

    with open('lorem_ipsum.txt', encoding='UTF-8') as file:
        contents = file.read()

        for word in contents.split():
            hash_object.append(
                re.sub("['\"!@#$%^&*()-_=+/\\,.|]", '', word)
            )

    with open('output.json', 'w', encoding='UTF-8') as file:
        json.dump(
            obj=hash_object.get_hash_set(),
            default=set_default,
            fp=file
        )

    print(f"\n[System] - End!")
