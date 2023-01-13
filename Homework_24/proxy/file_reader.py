from Homework_24.proxy.reader import Reader


class FileReader(Reader):

    def __init__(self, file_path):
        self.file_path = file_path

    def read_file(self):
        with open(self.file_path, 'r') as file:
            text = file.read()
        return text