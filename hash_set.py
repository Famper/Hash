class HashSet:
    def __init__(self) -> None:
        self.__hash_set: dict = {0: set(), 1: set(), 2: set(), 3: set(), 4: set()}
        self.count_values: int = 0
        self.divider: int = len(self.__hash_set)

        print("\n[System] - Init hash set!\n")

    def get_hash_set(self) -> dict:
        return self.__hash_set

    def set_hash_set(self, new_hash_set: dict) -> None:
        self.__hash_set: dict = new_hash_set
    
    def hash_code(self, value) -> int:
        result = 0

        for letter in list(value):
            result += ord(letter)
        
        return result % self.divider
    
    def existence(self, value: str) -> bool:
        bucket = self.hash_code(value)

        return value in self.get_hash_set()[bucket]
    
    def append(self, value: str):
        if not self.existence(value):
            if self.count_values == len(self.get_hash_set()):
                new_hash_set = dict()

                for start in range(0, len(self.get_hash_set()) * 2):
                    new_hash_set[start] = set()
                    self.divider = len(self.get_hash_set()) * 2

                for start in range(0, len(self.get_hash_set())):
                    for _value in self.get_hash_set()[start]:
                        bucket = self.hash_code(_value)
                        new_hash_set[bucket].add(_value)
            
                self.set_hash_set(new_hash_set)

            bucket = self.hash_code(value)
            self.__hash_set[bucket].add(value)
            self.count_values += 1
    
    def remove(self, value):
        if self.existence(value):
            if self.count_values == round(len(self.get_hash_set()) / 2):
                new_hash_set = dict()

                for start in range(0, round(len(self.get_hash_set()) / 2)):
                    new_hash_set[start] = set()
                    self.divider = round(len(self.get_hash_set()) / 2)

                for start in range(0, len(self.get_hash_set())):
                    for _value in self.get_hash_set()[start]:
                        bucket = self.hash_code(_value)
                        new_hash_set[bucket].append(_value)
                
                self.set_hash_set(new_hash_set)
            
            bucket = self.hash_code(value)
            self.__hash_set[bucket].remove(value)
            self.count_values -= 1
