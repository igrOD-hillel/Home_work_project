# 1. Загружаете исходний json
# 2. Преобразовиваете его в словарь
# 3. Органицовиваете цикл для итерации исходного списка словорей
# 4. В списке словорей по ключам собираете полное ими персони.
# 5. Припомощи метода items из ключей и значений генерируете список кортежей пари ключ-значение.
# 6. По занчению определяете тип и сортируете по типу согласно результирующему json-ну.
# 7. Генерируете все в новий словарь
# 8. Словарь записиваете в новий файл.
# ======================================================================================================================
import json


def load_jsn(file1):
    with open(file1, 'r') as json_data:
        dict_data = json.load(json_data)
    print(dict_data, type(dict_data))
    return dict_data


def save_jsn(file2, dict_data):
    with open(file2, 'w') as file:
        json.dump(dict_data, file)
    print(dict_data, type(dict_data))

def main(load):
    new_dict = {}
    for employee in load['employee']:
        f_name = f"{employee['firstName']} {employee['lastName']}"
        list_value = {'int': [], 'float': [], 'string': [], 'bool': [], 'none_type': []}
        for item in employee.items():
            if type(item[1]) == int:
                list_value['int'].append(item[0])
            elif type(item[1]) == float:
                list_value['float'].append(item[0])
            elif type(item[1]) == str:
                list_value['string'].append(item[0])
            elif type(item[1]) == bool:
                list_value['bool'].append(item[0])
            else:
                list_value['none_type'].append(item[0])
        new_dict.update({f_name: list_value})
    return {'employee': new_dict}


file1 = 'HW.json'
file2 = 'HW_result_Domushchei.json'

dict_data = load_jsn(file1)
task = main(dict_data)
save_jsn(file2, task)
