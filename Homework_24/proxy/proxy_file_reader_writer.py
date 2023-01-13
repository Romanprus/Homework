from Homework_24.proxy.file_reader import FileReader
from Homework_24.proxy.file_writer import FileWriter


class TxtProxyWriterReader:
    def __init__(self, file_path):
        self.__result = ''
        self.__is_actual = False
        self.__file_reader = FileReader(file_path)
        self.__file_writer = FileWriter(file_path)

    def read_file(self):
        if self.__is_actual:
            return self.__result
        else:
            self.__result = self.__file_reader.read_file()
            self.__is_actual = True
            return self.__result

    def write_file(self):
        self.__result = self.__file_writer.write_file('new_data')
        self.__is_actual = False
        return self.__result


if __name__ == '__main__':
    proxy_reader = TxtProxyWriterReader('some_file.txt')
    print(proxy_reader.read_file())
    proxy_reader.write_file()
    print(proxy_reader.read_file())
