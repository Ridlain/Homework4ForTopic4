def find_owner(doc_number):
    for doc in documents:
        if doc['number'] == doc_number:
            return f"Владелец документа: {doc['name']}"
    return "Документ с таким номером не найден."

documents = [
    {'type': 'passport', 'number': '2207 876234', 'name': 'Василий Гупкин'},
    {'type': 'invoice', 'number': '11-2', 'name': 'Геннадий Покемонов'},
    {'type': 'insurance', 'number': '10006', 'name': 'Аристарх Павлов'}
]

directories = {
    '1': ['2207 876234', '11-2'],
    '2': ['10006'],
    '3': []
}

while True:
    print("Введите команду:")
    command = input().strip().lower()

    if command == 'q':
        break
    elif command == 'p':
        print("Введите номер документа:")
        doc_number = input().strip()
        result = find_owner(doc_number)
        print("Результат:")
        print(result)