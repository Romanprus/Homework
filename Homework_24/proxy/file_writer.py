from Homework_24.proxy.writer import Writer


class FileWriter(Writer):

    def __init__(self, file_path):
        self.file_path = file_path

    def write_file(self, new_data):
        with open(self.file_path, 'a') as file:
            text = file.write(new_data)
        return text