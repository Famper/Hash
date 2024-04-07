class HashSet:
    """Hash set example."""

    def __init__(self) -> None:
        """
        HashSet initialization class
        """
        self.hash_set: dict = {0: set()}
        self.count_values: int = 0
        self.divider: int = len(self.hash_set)
        self.bucket: int | None = None

        print("\n[SYSTEM] - Init hash set!")

    def existence(self, value: any) -> bool:
        """
        Check key in HashSet
        :param value:
        :return:
        """
        self.bucket: int = hash(value) % self.divider

        return value in self.hash_set[self.bucket]

    def generate_new_dict(self, _type: int = 1) -> None:
        """
        Update count buckets in HashSet and update position elements in buckets
        :param _type: 1 = Positive, other = Negative
        """
        if _type == 1:
            self.divider: int = self.divider * 2
        else:
            self.divider: int = round(self.divider / 2)

        new_hash_set = {}

        for start in range(0, self.divider):
            new_hash_set[start]: set = set()

        for start in range(0, len(self.hash_set)):
            for _value in self.hash_set[start]:
                bucket: int = hash(_value) % self.divider
                new_hash_set[bucket].add(_value)

        self.hash_set = new_hash_set

    def append(self, value: any) -> None:
        """
        Add new value in HashSet
        :param value:
        """
        if not self.existence(value):
            if self.count_values == len(self.hash_set):
                self.generate_new_dict()

            self.hash_set[self.bucket].add(value)
            self.count_values += 1

    def remove(self, value: any) -> None:
        """
        Remove value in HashSet
        :param value:
        """
        if self.existence(value):
            if self.count_values == round(len(self.hash_set) / 2):
                self.generate_new_dict(_type=0)

            self.hash_set[self.bucket].remove(value)
            self.count_values -= 1
