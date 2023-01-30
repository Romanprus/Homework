class CustomIterator:
    def __init__(self, sequence, start_index, end_index):
        self.sequence = sequence
        self.start_index = start_index
        self.end_index = end_index
        self.current_index = start_index

    def __iter__(self):
        return self

    def __next__(self):
        if self.current_index >= self.end_index:
            raise StopIteration
        else:
            current_value = self.sequence[self.current_index]
            self.current_index += 1
            return current_value


if __name__ == '__main__':
    sequence = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
    start_index = 2
    end_index = 13

    for value in CustomIterator(sequence, start_index, end_index):
        print(value)