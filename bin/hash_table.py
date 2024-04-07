class HashTable:
    """Hash Table Implementation"""

    def __init__(self) -> None:
        """
        HashTable initialization class
        """
        self.hash_table: dict = {0: {}}
        self.count_values: int = 0
        self.divider: int = len(self.hash_table)
        self.bucket: int | None = None

        print("\n[SYSTEM] - Init hash table!")

    def existence(self, key: any) -> bool:
        """
        Check key in HashTable
        :param key:
        :return:
        """
        self.bucket: int = hash(key) % self.divider

        return key in self.hash_table[self.bucket].keys()

    def generate_new_dict(self, _type: int = 1):
        """
        Update count buckets in HashSet and update position elements in buckets
        :param _type: 1 = Positive, other = Negative
        """
        if _type == 1:
            self.divider: int = self.divider * 2
        else:
            self.divider: int = round(self.divider / 2)

        new_hash_set: dict = {}

        for start in range(0, self.divider):
            new_hash_set[start]: dict = {}

        for start in range(0, len(self.hash_table)):
            for key, _value in self.hash_table[start].items():
                bucket: int = hash(key) % self.divider

                new_hash_set[bucket][key] = _value

        self.hash_table: dict = new_hash_set

    def append(self, key: any, value: any):
        """
        Add new value in HashSet
        :param key:
        :param value:
        """
        if not self.existence(key):
            if self.count_values == self.divider:
                self.generate_new_dict()

            self.hash_table[self.bucket][key] = value
            self.count_values += 1

    def remove(self, key: any):
        """
        Remove value in HashSet
        :param key:
        """
        if self.existence(key):
            if self.count_values == round(self.divider / 2):
                self.generate_new_dict(_type=0)

            del self.hash_table[self.bucket][key]
            self.count_values -= 1

    def get_value(self, key: any):
        if self.existence(key):
            bucket: int = hash(key) % self.divider

            return self.hash_table[bucket].get(key, None)
