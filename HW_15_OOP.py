# Задачу из “Homework 11. Paбота с json обектом.” перевести в формат ООП.
# Класс должен содержать отрибути и методи. Отрибутами будут пути к исходному и результирующему файлам.
# И как миниму 4 метода:
#     конструктор должен на вход принимать возможние альтернативние варианти путей к исходному и результирующему файлам,
#     но и иметь дефолтние значения, которими и будут отрибути класса;
#     метод для загрузки исходного json обекта из исходного файла;
#     метод для оброботки словаря полученного из исходного json обекта;
#     метод для загрузки полученного результата в новий результирующий json файл.
# Если придумаете еще больше методов будет хорошо. Помните о принципе “Единственной ответственности”.
# Екземпляр класса визивать через определенную точку входа python скрипта.

import json


class MyClass:
    # we start our attributes from __ to indicate that it is private values
    def __init__(self, src_path='HW.json', dest_path='HW_result_Domushchei.json'):
        self.__src_path = src_path
        self.__dest_path = dest_path
        self.__data = {}

    # load json file to python dict
    def load(self):
        with open(self.__src_path, 'r') as json_file:
            self.__data = json.load(json_file)

    # save dict to json file
    def dump(self):
        with open(self.__dest_path, 'w') as json_file:
            json.dump(self.__data, json_file, indent=4)

    # define "magick" method to convert data to string
    def __str__(self):
        return json.dumps(self.__data, indent=4)

    # define "magick" method to be able to print data
    def __repr__(self):
        return self.__str__()

    def create_task(self):
        # loop thrhoug keys in dict from json file
        result = {}
        data = self.__data
        for key, lst in data.items():
            dict_intitial = {}
            # loop through elements in list of employee
            for el in lst:
                # el is a dict with info for employee
                firstName = el.get('firstName')
                lastName = el.get('lastName')
                fullName = '{} {}'.format(firstName, lastName)
                d_types = {
                    'int': 'int',
                    'str': 'string',
                    'float': 'float',
                    'NoneType': 'none_type',
                    'bool': 'bool'
                }
                d_res = dict.fromkeys(d_types.values(), [])
                # generate list of tuples
                lst_tpl =  [(tpl[0], tpl[1].__class__.__name__) for tpl in el.items()]
                for tpl in lst_tpl:
                    value, typeValye = tpl
                    # value = str(value)
                    custom_value = d_types.get(typeValye)
                    d_res[custom_value] = d_res.get(custom_value, []) + [value]
                dict_intitial[fullName] = d_res
            result[key] = dict_intitial
        self.__data = result


def main():
    obj = MyClass()
    obj.load()
    print(obj)
    obj.create_task()
    print(obj)
    obj.dump()


if __name__ == '__main__':
    main()
