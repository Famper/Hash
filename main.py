import json
import re

from hash_set import HashSet
from hash_table import HashTable


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
    print(f"\n[SYSTEM] - Start")

    hash_object: HashSet = HashSet()
    hash_table: HashTable = HashTable()

    with open('lorem_ipsum.txt', encoding='UTF-8') as file:
        contents = file.read()

        for word in contents.split():
            word = re.sub("['\"!@#$%^&*()-_=+/\\,.|]", '', word)

            hash_object.append(word)
            hash_table.append(
                key=word,
                value=hash(word)
            )

    with open('output_set.json', 'w', encoding='UTF-8') as file:
        json.dump(
            obj=hash_object.get_hash_set(),
            default=set_default,
            fp=file
        )

    with open('output_table.json', 'w', encoding='UTF-8') as file:
        json.dump(
            obj=hash_table.get_hash_table(),
            default=set_default,
            fp=file
        )

    print(f"\n[SYSTEM] - End!")
