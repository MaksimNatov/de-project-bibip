from models import Car, CarFullInfo, CarStatus, Model, ModelSaleStats, Sale
from datetime import datetime
from decimal import Decimal

class CarService:
    def __init__(self, root_directory_path: str) -> None:
        self.root_directory_path = root_directory_path

    # Задание 1. Сохранение автомобилей и моделей
    def add_model(self, model: Model) -> Model:
        with open('models_index.txt', 'a'): # Создаем файл, если его нет
            pass
        with open('models.txt', 'a'):  # Создаем файл, если его нет
            pass
        model_str = f'{model.id};{model.name};{model.brand}'
        model_str = model_str.ljust(500) + '\n' # формируем строку
        with open('models_index.txt', 'r') as f: # проверяем наличие записи в файле
            f.seek(0)
            models_list = [row.rstrip('\n').split(';') for row in f.readlines()]
            model_list_id = [int(row[1]) for row in models_list]
        if model.id not in model_list_id:
            with open('models_index.txt', 'r+') as f:
                f.seek(0)
                models_list = f.readlines()
                line = len(models_list)
                empty_flg = False #флаг наличия пустой строки
                for i in range(len(models_list)):
                    if models_list[i].lstrip(' ') =='\n': # если в файле индексов есть пустая строка
                        line = i
                        models_list[line] = f'{line};{model.id}\n' # записываем в нее новый индекс
                        f.seek(0)
                        f.writelines(models_list) # записываем в нее новый индекс
                        empty_flg = True
                        break
                if empty_flg == False: # если нет пустых строк внутри - записываем в конец
                    models_list.append(f'{line};{model.id}\n')
                    f.seek(0)
                    f.writelines(models_list)
            with open('models.txt', 'r+') as f:
                f.seek(line  * 501)
                f.write(model_str)
            return
        else:
            return        

    # Задание 1. Сохранение автомобилей и моделей
    def add_car(self, car: Car) -> Car:
        with open('cars_index.txt', 'a'): # Создаем файл, если его нет
            pass
        with open('cars.txt', 'a'):  # Создаем файл, если его нет
            pass        
        car_str = f'{car.vin};{car.model};{car.price};{car.date_start};{car.status}'
        car_str = car_str.ljust(500) + '\n' # формируем строку
        with open('cars_index.txt', 'r') as f: # проверяем наличие записи в файле
            f.seek(0)
            car_list = [row.rstrip('\n').split(';') for row in f.readlines()]
            car_list_id = [row[1] for row in car_list]
        if car.vin not in car_list_id:   
            with open('cars_index.txt', 'r+') as f: 
                f.seek(0)
                car_list = f.readlines()
                line = len(car_list)
                empty_flg = False # флаг наличия пустой строки
                for i in range(len(car_list)):
                    if car_list[i].lstrip(' ') =='\n': # если в файле индексов есть пустая строка
                        line = i
                        car_list[line] = f'{line};{car.vin}\n' # записываем в нее новый индекс
                        f.seek(0)
                        f.writelines(car_list) # записываем в нее новый индекс
                        empty_flg = True
                        break
                if empty_flg == False: # если нет пустых строк внутри - записываем в конец
                    car_list.append(f'{line};{car.vin}\n')
                    f.seek(0)
                    f.writelines(car_list)
            with open('cars.txt', 'r+') as f:
                f.seek(line  * 501)
                f.write(car_str)
            return
        else:
            return
    # Задание 2. Сохранение продаж.
    def sell_car(self, sale: Sale) -> Car:
        #raise NotImplementedError
        with open('sales_index.txt', 'a'): # Создаем файл, если его нет
            pass
        with open('sales.txt', 'a'):  # Создаем файл, если его нет
            pass         
        sales_str = f'{sale.sales_number};{sale.car_vin};{sale.sales_date};{sale.cost}'
        sales_str = sales_str.ljust(500) + '\n' # формируем строку
        with open('sales_index.txt', 'r') as f: # проверяем наличие продажи в файле
            f.seek(0)
            sale_list = [row.rstrip('\n').split(';') for row in f.readlines()]
            sale_list_id = [row[1] for row in sale_list]
        if sale.sales_number not in sale_list_id:            
            with open('sales_index.txt', 'r+') as f:
                f.seek(0)
                sales_list = f.readlines()
                line = len(sales_list)
                empty_flg = False #флаг наличия пустой строки
                for i in range(len(sales_list)):
                    if sales_list[i].lstrip(' ') =='\n': # если в файле индексов есть пустая строка
                        line = i
                        sales_list[line] = f'{line};{sale.sales_number}\n' # записываем в нее новый индекс
                        f.seek(0)
                        f.writelines(sales_list) # записываем в нее новый индекс
                        empty_flg = True
                        break
                if empty_flg == False: # если нет пустых строк внутри - записываем в конец
                    sales_list.append(f'{line};{sale.sales_number}\n')
                    f.seek(0)
                    f.writelines(sales_list)
            with open('sales.txt', 'r+') as f:
                f.seek(line  * 501)
                f.write(sales_str)
            with open('cars_index.txt', 'r') as f:
                car_list = [row.rstrip('\n').split(';') for row in f.readlines()]
                result_index = int(list(filter(lambda x: x[1] == sale.car_vin, car_list))[0][0]) # ищем index
            with open('cars.txt', 'r+') as f: # меняем значение на sold
                f.seek(result_index * 501)
                val = f.read(501).rstrip('\n')
                val = val.rstrip().split(';')
                val[4] = 'sold'
                val = ';'.join(val)
                val = val.ljust(499) + '\n'
                f.seek(result_index  * 501)
                f.write(val)
            return
        else:
            return
    # Задание 3. Доступные к продаже
    def get_cars(self, status: CarStatus) -> list[Car]:
        with open('cars.txt', 'r') as f:
            car_list = [row.rstrip().split(';') for row in f.readlines()]
            car_list = [Car(
                            vin=row[0],
                            model=int(row[1]),
                            price=Decimal(row[2]),
                            date_start= datetime.strptime(row[3], '%Y-%m-%d %H:%M:%S'),
                            status=CarStatus(row[4])) for row in car_list] # все запаковываем в объекты car
            available_cars = [car for car in car_list if car.status == status] # ищем по статусу нужные
        return available_cars

    # Задание 4. Детальная информация
    def get_car_info(self, vin: str) -> CarFullInfo | None:
        flag_vin_in_index = True # Проверяем что VIN есть в базе
        with open('cars_index.txt', 'r') as f:
            index_list = [row.rstrip().split(';') for row in f.readlines()]
            index_list = [row[0] for row in index_list if row[1] == vin]
        if len(index_list) == 0:
            flag_vin_in_index = False # VIN отсутствуе, т.к. список пустой
        if flag_vin_in_index == True:   
            with open('cars_index.txt', 'r') as f:
                index_list = [row.rstrip().split(';') for row in f.readlines()]
                index_list = [row[0] for row in index_list if row[1] == vin]
                line = int(index_list[0])
            with open('cars.txt', 'r') as f:
                f.seek(line * (501))
                val = f.read(500).rstrip().split(';')
                our_car = Car(
                            vin=val[0],
                            model=int(val[1]),
                            price=Decimal(val[2]),
                            date_start= datetime.strptime(val[3], '%Y-%m-%d %H:%M:%S'),
                            status=CarStatus(val[4])
                            )
            with open('models_index.txt', 'r') as f:
                index_list = [row.rstrip().split(';') for row in f.readlines()]
                index_list = [row[0] for row in index_list if int(row[1]) == our_car.model]
                line = int(index_list[0])
            with open('models.txt', 'r') as f:
                f.seek(line * (501))
                val = f.read(500).rstrip().split(';')
                our_model = Model(
                                id=int(val[0]),
                                name=val[1],
                                brand=val[2]
                                )
            if our_car.status == CarStatus.sold: # проверяем продана ли машина
                with open('sales_index.txt', 'r') as f:    
                    index_list = [row.rstrip().split(';') for row in f.readlines()]
                    index_list = [[row[0]] + row[1].split('#') for row in index_list]
                    index_list = [row[0] for row in index_list if row[2] == our_car.vin]
                    line = int(index_list[0])
                with open('sales.txt', 'r') as f:
                    f.seek(line * (501))
                    val = f.read(500).rstrip().split(';')
                    our_sale = Sale(
                                    sales_number=val[0],
                                    car_vin=val[1],
                                    sales_date=datetime.strptime(val[2], '%Y-%m-%d %H:%M:%S'),
                                    cost=Decimal(val[3])
                                    )
                result = CarFullInfo( # Формируем результат, если продана
                    vin=our_car.vin,
                    car_model_name=our_model.name,
                    car_model_brand=our_model.brand,
                    price=our_car.price,
                    date_start=our_car.date_start,
                    status=our_car.status,
                    sales_date=our_sale.sales_date,
                    sales_cost=our_sale.cost
                )
            else:
                result = CarFullInfo( # Формируем результат, если не продана
                    vin=our_car.vin,
                    car_model_name=our_model.name,
                    car_model_brand=our_model.brand,
                    price=our_car.price,
                    date_start=our_car.date_start,
                    status=our_car.status,
                    sales_date=None,
                    sales_cost=None
                )
            return result
        else:
            return None             
    # Задание 5. Обновление ключевого поля
    def update_vin(self, vin: str, new_vin: str) -> CarFullInfo | None: # Поменял, ожидается CarFullInfo, было 'Car'
        flag_vin_in_index = True
        with open('cars_index.txt', 'r') as f: # Проверка на наличие vin
            index_list = [row.rstrip().split(';') for row in f.readlines()]
            index_list = [row[0] for row in index_list if row[1] == vin]
            if len(index_list) == 0: # Нет нужного vin
                flag_vin_in_index = False
        if flag_vin_in_index == True:
            with open('cars_index.txt', 'r+') as f:
                index_list = [row.rstrip().split(';') for row in f.readlines()]
                new_list = [row if row[1] != vin else [row[0], new_vin] for row in index_list]
                new_list = [';'.join(row) + '\n' for row in new_list]
                index_list = [row[0] for row in index_list if row[1] == vin]
                line = int(index_list[0])
                f.seek(0)
                f.writelines(new_list)
            with open('cars.txt', 'r+') as f:
                f.seek(line * (501))
                val = f.read(500).rstrip().split(';')
                val[0] = new_vin
                val_row = ';'.join(val).ljust(499) + '\n'
                f.seek(line * (501))
                f.write(val_row)
            with open('sales_index.txt', 'r') as f:
                index_list = [row.rstrip().split(';') for row in f.readlines()]
                index_list = [[row[0]] + row[1].split('#') for row in index_list]
                index_list = [row[0] for row in index_list if row[2] == vin]
            if len(index_list) != 0: #значит в БД продаж вин тоже нужно поменять
                line = int(index_list[0])
                with open('sales_index.txt', 'r+') as f:
                    index_list = [row.rstrip().split(';') for row in f.readlines()]
                    index_list = [[row[0]] + row[1].split('#') for row in index_list]
                    new_index_list = [f'{row[0]};{row[1]}#{row[2]}\n' if row[2] != vin else f'{row[0]};{row[1]}#{new_vin}\n' for row in index_list]
                    new_index_sale = [f'{row[1]}#{new_vin}' for row in index_list if row[2] == vin]
                    new_index_sale = new_index_sale[0] # переменная для таблицы sale
                    f.seek(0)
                    f.writelines(new_index_list)                
                with open('sales.txt', 'r+') as f:
                    f.seek(line * (501))
                    val = f.read(500).rstrip().split(';')
                    val[0] = new_index_sale
                    val[1] = new_vin
                    val_row = ';'.join(val).ljust(499) + '\n'
                    f.seek(line * (501))
                    f.write(val_row)
            return self.get_car_info(new_vin)
        else:
            return None
    # Задание 6. Удаление продажи
    def revert_sale(self, sales_number: str) -> Car:
        vin = sales_number.split('#')[1]
        flag_vin_in_index = True # Проверяем что VIN есть в базе
        with open('cars_index.txt', 'r') as f:
            index_list = [row.rstrip().split(';') for row in f.readlines()]
            index_list = [row[0] for row in index_list if row[1] == vin]
        if len(index_list) == 0:
            flag_vin_in_index = False # VIN отсутствуе, т.к. список пустой
        if flag_vin_in_index == True:   
            with open('cars_index.txt', 'r') as f:
                index_list = [row.rstrip().split(';') for row in f.readlines()]
                index_list = [row[0] for row in index_list if row[1] == vin]
                line = int(index_list[0])
            with open('cars.txt', 'r+') as f: # записываем новый статус
                f.seek(line * (501))
                val = f.read(500).rstrip().split(';')
                val[4] = 'available'
                val_row = ';'.join(val).ljust(499) + '\n'
                f.seek(line * (501))
                f.write(val_row)
                our_car = Car(
                            vin=val[0],
                            model=int(val[1]),
                            price=Decimal(val[2]),
                            date_start= datetime.strptime(val[3], '%Y-%m-%d %H:%M:%S'),
                            status=CarStatus(val[4])
                            )
            with open('sales_index.txt', 'r+') as f:
                index_list = [row.rstrip().split(';') for row in f.readlines()]
                row_for_write = [row for row in index_list if row[1] != sales_number]
                row_for_write = [';'.join(row) + '\n' for row in row_for_write] # перезаписываем индексы без найденного
                index_list = [row[0] for row in index_list if row[1] == sales_number]
                line = int(index_list[0])
            with open('sales_index.txt', 'w') as f:
                f.writelines(row_for_write)
            with open('sales.txt', 'r+') as f:
                f.seek(0) 
                item_list = [row for row in f.readlines()]
                val = ' '
                val_row = val.ljust(499) + '\n' # мы меняем значения на пробелы
                item_list[line] = val_row
                f.seek(0)
                f.writelines(item_list)
            return our_car                          
        else:
            return None
    # Задание 7. Самые продаваемые модели
    def top_models_by_sales(self) -> list[ModelSaleStats]:
        with open('sales_index.txt', 'r') as f:
            sales_list = [row.rstrip().split(';') for row in f.readlines()]
            sales_list = [row for row in sales_list if len(row) > 1] # убираем пустые строки если они есть
            vin_list = [row[1].split('#') for row in sales_list]
            vin_list = [row[1] for row in vin_list]
        full_info_list = [self.get_car_info(row) for row in vin_list]
        brand_price_info = [(car.car_model_name, car.car_model_brand) for car in full_info_list]
        temp_dict = {}
        for row in brand_price_info:
            temp_dict[row] = temp_dict.get(row, 0) + 1
        sorted_dict = sorted(temp_dict.items(), key=lambda x: x[1], reverse=True)
        sorted_dict = sorted_dict[:3]
        result = []
        for row in sorted_dict:
            our_model = ModelSaleStats(
                car_model_name=row[0][0],
                brand=row[0][1],
                sales_number=row[1]
            )
            result.append(our_model)
        return result
