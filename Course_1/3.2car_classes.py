import os
import csv


class CarBase:

    def __init__(self, brand, photo_file_name, carrying):
        self.brand = brand
        self.photo_file_name = photo_file_name
        self.carrying = float(carrying) if carrying is not None else carrying

    def get_photo_file_ext(self):
        _, path = os.path.splitext(self.photo_file_name)
        if path in ('.jpg', '.jpeg', '.png', '.gif'):
            return path
        else:
            return False


class Car(CarBase):

    def __init__(self, brand=None, photo_file_name=None, carrying=None, passenger_seats_count=None):
        super().__init__(brand, photo_file_name, carrying)
        self.passenger_seats_count = int(passenger_seats_count) if carrying is not None else carrying
        self.car_type = 'car'


class Truck(CarBase):

    def __init__(self, brand=None, photo_file_name=None, carrying=None, body_whl=None):
        super().__init__(brand, photo_file_name, carrying)
        self.car_type = 'truck'
        self.body_whl = body_whl

        if body_whl:
            self.body_whl = body_whl.split('x')

        if (self.body_whl is None) or (len(self.body_whl) != 3):
            self.body_length = 0.0
            self.body_width = 0.0
            self.body_height = 0.0

        else:
            self.body_length, self.body_width, self.body_height = map(float, self.body_whl)

    def get_body_volume(self):
        return float(self.body_length) * float(self.body_width) * float(self.body_height)


class SpecMachine(CarBase):

    def __init__(self, brand=None, photo_file_name=None, carrying=None, extra=None):
        super().__init__(brand, photo_file_name, carrying)
        self.car_type = 'spec_machine'
        self.extra = extra


def get_car_list(csv_filename):
    car_list = []
    try:
        with open(csv_filename) as csv_fd:
            reader = csv.reader(csv_fd, delimiter=';')
            next(reader)
            for row in reader:
                try:
                    if row[0] != '':
                        if row[0] == Car().car_type:
                            if (row[1] != '') and (row[2] != '') and (row[5] != ''):

                                obj = Car(brand=row[1], photo_file_name=row[3], carrying=row[5],
                                          passenger_seats_count=row[2])
                                if obj.get_photo_file_ext():
                                    car_list.append(obj)

                        elif row[0] == Truck().car_type:
                            if (row[1] != '') and (row[5] != ''):
                                obj = Truck(brand=row[1], photo_file_name=row[3], carrying=row[5],
                                            body_whl=row[4])
                                if obj.get_photo_file_ext():
                                    car_list.append(obj)

                        elif row[0] == SpecMachine().car_type:
                            if (row[1] != '') and (row[5] != '') and (row[6] != ''):
                                obj = SpecMachine(brand=row[1], photo_file_name=row[3], carrying=row[5],
                                                  extra=row[6])
                                if obj.get_photo_file_ext():
                                    car_list.append(obj)

                except IndexError:
                    pass
    except FileNotFoundError:
        print("Error. File not found")
    else:
        return car_list
