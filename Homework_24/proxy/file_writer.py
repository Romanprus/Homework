from Homework_24.proxy.writer import Writer


class FileWriter(Writer):

    def __init__(self, file_path):
        self.file_path = file_path

    def append_to_file(self, *args):
        with open(self.file_path, 'a') as file:
            text = file.write(*args)
        return text

    def rewrite_file(self, *args):
        with open(self.file_path, 'w') as file:
            text = file.write(*args)
        return text