
from .table import Table
import random


class OpenSpace:
    def __init__(self, number_of_tables: int, number_of_seats: int):
        self.number_of_tables = number_of_tables
        self.number_of_seats = number_of_seats
        self.tables = [Table(self.number_of_seats)
                       for i in range(number_of_tables)]

    def organize(self, names):
        shuffle_names = names[:]
        random.shuffle(shuffle_names)
        wait_list = []

        for name in shuffle_names:
            for table in self.tables:
                if table.has_free_spot() == True:
                    table.assign_seat(name)
                    break
            else:
                print(
                    f"Nao há acentos na mesa para voce {name}! para vc e nem para ninguem! vai ter que esperar na fila!\n")
                wait_list.append(name)

        if wait_list:
            print(str(len(wait_list))+" pessoas na lista de espera ")

    def display(self):
        table_number = 1
        count_empty = 0
        for table in self.tables:
            print(f"Table {table_number}")
            seat_number = 1
            for seat in table.seats:
                occupant = seat.occupant
                if seat.free == False:
                    print(f"  Seat {seat_number} : {occupant}")
                else:
                    count_empty += 1
                    print(f"  Seat {seat_number} : Empty")

                seat_number += 1
            table_number += 1

        print(f"We have {count_empty} empty seats in our class")
