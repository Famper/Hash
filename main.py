from hash_set import HashSet

if __name__ == '__main__':
    hash_object = HashSet()

    print(f"\nHash object: {hash_object.get_hash_set()}")

    hash_object.append('1')
    hash_object.append('2')
    hash_object.append('3')
    hash_object.append('4')
    hash_object.append('5')
    hash_object.append('6')
    hash_object.append('7')
    hash_object.append('8')
    hash_object.append('9')
    hash_object.append('10')
    hash_object.append('11')

    print(f"\nHash object: {hash_object.get_hash_set()}")

    hash_object.remove('1')
    hash_object.remove('0')
    hash_object.remove('2')
    hash_object.remove('10')

    print(f"\nHash object: {hash_object.get_hash_set()}")