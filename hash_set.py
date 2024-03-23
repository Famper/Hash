class HashSet:
    def __init__(self) -> None:
        """
        HashSet initialization class
        """
        self.__hash_set: dict = {0: set(), 1: set(), 2: set(), 3: set(), 4: set()}
        self.count_values: int = 0
        self.divider: int = len(self.__hash_set)

        print("\n[System] - Init hash set!")

    def get_hash_set(self) -> dict:
        """
        Get HashSet
        :return:
        """
        return self.__hash_set

    def set_hash_set(self, new_hash_set: dict) -> None:
        """
        Set new HashSet
        :param new_hash_set:
        """
        self.__hash_set: dict = new_hash_set
    
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
    
    def existence(self, value: str) -> bool:
        """
        Check key in HashSet
        :param value:
        :return:
        """
        bucket = self.hash_code(value)

        return value in self.get_hash_set()[bucket]

    def generate_new_dict(self, _type: int = 1):
        """
        Update count buckets in HashSet and update position elements in buckets
        :param _type: 1 = Positive, other = Negative
        """
        if _type == 1:
            self.divider = len(self.get_hash_set()) * 2
        else:
            self.divider = len(self.get_hash_set()) / 2

        new_hash_set = dict()

        for start in range(0, self.divider):
            new_hash_set[start] = set()

        for start in range(0, len(self.get_hash_set())):
            for _value in self.get_hash_set()[start]:
                bucket = self.hash_code(_value)
                new_hash_set[bucket].add(_value)

        self.set_hash_set(new_hash_set)
    
    def append(self, value: str):
        """
        Add new value in HashSet
        :param value:
        """
        if not self.existence(value):
            if self.count_values == len(self.get_hash_set()):
                self.generate_new_dict()

            bucket = self.hash_code(value)
            self.__hash_set[bucket].add(value)
            self.count_values += 1
    
    def remove(self, value):
        """
        Remove value in HashSet
        :param value:
        """
        if self.existence(value):
            if self.count_values == round(len(self.get_hash_set()) / 2):
                self.generate_new_dict(_type=0)
            
            bucket = self.hash_code(value)
            self.__hash_set[bucket].remove(value)
            self.count_values -= 1
