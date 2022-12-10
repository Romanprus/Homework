from Homework_QAA.data_classes.user import User
from Homework_QAA.home_work.utilities.API.BaseAPI import BaseAPI


class Users(BaseAPI):
    def __init__(self):
        super().__init__()
        self.__url = "/api/users"
        self.__page_url = "/api/users?page"

    def get_user_by_id(self, user_id, headers=None):
        return self.get(f'{self.__url}/{user_id}', headers=headers)

    def get_users_page(self, page_number):
        return self.get(f'{self.__page_url}={page_number}')

    def create_user(self, body=None):
        user_data = User()
        if body is not None:
            user_data.update_dict(**body)
        response = self.post(self.__url, body, None)
        return response

    def delete_user(self, user_id):
        return self.delete(f'{self.__url}/{user_id}')

    def put_user_data(self, user_id, body=None):
        user_data = User()
        if body is not None:
            user_data.update_dict(**body)
        response = self.put(f'{self.__url}/{user_id}', body)
        return response



