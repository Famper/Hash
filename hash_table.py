class HashTable:
    def __init__(self) -> None:
        """
        HashTable initialization class
        """
        self.__hash_table: dict = {0: {}, 1: {}, 2: {}, 3: {}, 4: {}}
        self.count_values: int = 0
        self.divider: int = len(self.__hash_table)

        print("\n[SYSTEM] - Init hash table!")

    def get_hash_table(self) -> dict:
        """
        Get HashSet
        :return:
        """
        return self.__hash_table

    def set_hash_table(self, new_hash_table: dict) -> None:
        """
        Set new HashSet
        :param new_hash_table:
        """
        self.__hash_table: dict = new_hash_table

    def hash_code(self, value) -> int:
        """
        Get code from value
        :param value:
        :return:
        """
        result = 0

        for letter in list(value):
            result += ord(letter)

        return result % self.divider

    def existence(self, key: str) -> bool:
        """
        Check key in HashTable
        :param key:
        :return:
        """
        bucket = self.hash_code(key)

        return key in self.get_hash_table()[bucket].keys()

    def generate_new_dict(self, _type: int = 1):
        """
        Update count buckets in HashSet and update position elements in buckets
        :param _type: 1 = Positive, other = Negative
        """
        if _type == 1:
            self.divider = len(self.get_hash_table()) * 2
        else:
            self.divider = len(self.get_hash_table()) / 2

        new_hash_set = dict()

        for start in range(0, self.divider):
            new_hash_set[start] = set()

        for start in range(0, len(self.get_hash_table())):
            for _value in self.get_hash_table()[start]:
                bucket = self.hash_code(_value)
                new_hash_set[bucket].add(_value)

        self.set_hash_table(new_hash_set)

    def append(self, key: str, value: any):
        """
        Add new value in HashSet
        :param key:
        :param value:
        """
        if not self.existence(key):
            if self.count_values == len(self.get_hash_table()):
                self.generate_new_dict()

            bucket = self.hash_code(key)
            self.__hash_table[bucket][key] = value
            self.count_values += 1

    def remove(self, key: str):
        """
        Remove value in HashSet
        :param key:
        """
        if self.existence(key):
            if self.count_values == round(len(self.get_hash_table()) / 2):
                self.generate_new_dict(_type=0)

            bucket = self.hash_code(key)
            del self.__hash_table[bucket][key]
            self.count_values -= 1

    def get_value(self, key: str):
        if self.existence(key):
            bucket = self.hash_code(key)

            return self.get_hash_table()[bucket].get(key, '[SYSTEM] - Not found!')
