from hash_set import HashSet

if __name__ == '__main__':
    hash_object = HashSet()

    print(f"\nHash object: {hash_object.get_hash_set()}")

    with open('lorem_ipsum.txt') as f:
        contents = f.read()

        for word in contents.split():
            hash_object.append(word)

    print(f"\nHash object: {hash_object.get_hash_set()}")