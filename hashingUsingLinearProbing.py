class HashTable:

    def __init__(self, size = 10):
        self.table_size = size
        self.table = [None] * size
        self.count = 0

    def __str__(self):
        return str(self.table)

    def resize_table(self):
    # 1. Lets grab a deep copy of the old table
    # 2. Lets initialze our self.table = a new list thats bigger(2 x table_size) and empty
    # 3. Re-put all the old values in our copy (#1) back into the hash table by calling self.put(value)

        # self.new_size = 2 * self.table_size
        # self.table_size = self.new_size
        # self.table = [None] * self.new_size

        # for i in range(self.new_size):
        #     for j in range(10): #old table size
        #        val = self.get(i)
        #        self.put(val)

        old = []
        for bucket in self.table:
            if bucket is not None:
                old.append(bucket)

        self.table = 2 * self.table_size * [None]
        for items in old:
            self.put(items)

        # pass






    def put(self, value):

        self.count += 1

        # check the load factor. Will the table exceed the acceptable load factor
        # Load factor = 0.66
        # load factor = #items in the table / total number of slots
        load_factor = self.count / len(self.table)
        if load_factor > 0.66:
            # print("Need to resize the table.")
            self.resize_table()

        index = self.hash(value)

        if self.table[index] is None or self.table[index] == value:
            # slot is empty or same --> save the value
            self.table[index] = value
        else:
            # print("Hash Collision")
            i=1
            done = False
            while not done:
                # Linear Probing: increment i until next empty slot is found
                new_index = (index + i) % len(self.table)

                # check whether the table is full or not
                if new_index == index:
                    raise ValueError("Hash Table is Full! No room for further elements to be inserted")

                # add element to new_index
                if self.table[new_index] is None or self.table[new_index] == value:
                    self.table[new_index] = value
                    done = True
                else:
                    i += 1




    def get(self, value):
        index = self.hash(value)
        if self.table[index] is None or self.table[index] == value:
            return '{} is present at index {}'.format(self.table[index], index)
        else:
            # we need to probe in order to be sure that the value is not in the hash table.
            i = 1
            done = False
            while not done:
                # Linear Probing: increment i until value is found
                new_index = (index + i) % len(self.table)

                if new_index == index:
                    return "{} is not present in the hash table.".format(value)

                if self.table[new_index] == value:
                    done = True
                    return '{} is present at index {}'.format(self.table[new_index], new_index)
                else:
                    i += 1

            # return "OOPS! Value not what i expected"

    def hash(self, value):
        return value % len(self.table)

if __name__ == "__main__":
    ht = HashTable()
    ht.put(2)
    ht.put(33)
    ht.put(222)
    ht.put(303)
    ht.put(1)
    ht.put(0)
    ht.put(10)
    ht.put(12)
    print(ht.get(2))
    print(ht.get(222))
    print(ht.get(13))
    print(ht)

