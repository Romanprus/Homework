import configparser


abs_path = '/Homework_QAA/home_work/configurations/configuration.ini'
config = configparser.RawConfigParser()
config.read(abs_path)


class ReadConfig:
    @staticmethod
    def get_base_url():
        return config.get('app_info', 'base_url')

    @staticmethod
    def get_user_name():
        return config.get('user_data', 'user_name')

    @staticmethod
    def get_password():
        return config.get('user_data', 'password')

    @staticmethod
    def get_driver_id():
        return config.get('browser', 'browser_id')
