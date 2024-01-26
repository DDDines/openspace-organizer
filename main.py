from src.openspace import OpenSpace

if __name__ == "__main__":

    def get_collegues_list(file_path):

        content = open(file_path, "r")
        collegues = content.read().split("\n")

        collegues_filtrado = [
            collegue for collegue in collegues if collegue.strip()]

        return collegues_filtrado

    def display_menu():

        answer = input(
            "Wold you like to run the default sistem ? Y/N ").upper()
        if answer == "Y" or answer == "":

            file_path = r"C:\Users\julio\Desktop\openspace-organizer\collegues.txt"
            Tables = OpenSpace(4, 6)
            Tables.organize(get_collegues_list(file_path))
            Tables.display()
            display_menu()

        elif answer == "N":
            print("\n" * 100 +
                  "Well, lets customise then! \nI'll let you know if you just fill in blank the parameter the sistem can use the Default")

            number_of_tables = int(input("Put the number of tables: "))
            if number_of_tables == "":
                number_of_tables = int(4)
            print("\n" * 100)

            number_of_seats = int(input("Put the number of seats: "))
            if number_of_seats == "":
                number_of_seats = int(6)
            print("\n" * 100)

            path = input("Put the path to the File: ")
            if path == "":
                path = r"C:\Users\julio\Desktop\openspace-organizer\collegues.txt"

            Tables = OpenSpace(number_of_tables, number_of_seats)

            Tables.organize(get_collegues_list(path))
            Tables.display()
            display_menu()
        else:
            display_menu()

    print("Hello, this sistem allow you to distribute ramdonly a list of people on seats, at a table on a room")
    print(
        f"Deafault Sistema creates 4 tables whith 6 seats each, and use the list collegues.txt")

    display_menu()
