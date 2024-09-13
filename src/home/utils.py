from openpyxl import load_workbook
from .models import Passenger

field_mapper = {'PassengerId': 'id', 'Survived': 'survived', 'Pclass': 'pclass',
                'Name': 'name', 'Sex': 'sex', 'Age': 'age', 'SibSp': 'sibsp',
                'Parch': 'parch', 'Ticket': 'ticket', 'Fare': 'fare',
                'Cabin': 'cabin', 'Embarked': 'embarked'}


def insert_data_from_dataset(dataset_file):
    workbook = load_workbook(filename=dataset_file)
    sheet = workbook.active
    passengers = []

    for value in sheet.iter_rows(min_row=1, max_row=1, values_only=True):
        first_row = value
    fields = [field_mapper[cell] for cell in first_row]

    for row_values in sheet.iter_rows(min_row=2, values_only=True):
        kwargs = dict(zip(fields, row_values))
        kwargs['age'] = None if kwargs['age'] == '' else float(kwargs['age'])
        passengers.append(Passenger(**kwargs))

    return Passenger.objects.bulk_create(passengers)



