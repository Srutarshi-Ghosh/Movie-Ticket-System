
from models.MovieShow import MovieShow
from models.Group import Group
from models.MovieTicketSystem import MovieTicketSystem
from models.InputValidator import InputValidator
from models.Message import Message

class Driver:

    def __init__(self):
        self.movie_system = MovieTicketSystem()
        self.validator = InputValidator()
        self.set_movvie_ticket_system()
        self.message = Message()


    def set_movvie_ticket_system(self):
        show1 = MovieShow(1, ['A1', 'A2', 'A3', 'A4'])
        self.movie_system.set_show(show1)

        show2 = MovieShow(2, ['A1', 'A2', 'A3', 'A4', 'B1', 'B2', 'B3'])
        self.movie_system.set_show(show2)


    def create_group(self):
        show_number = input("Enter the show you want to watch: ")
        if not self.validator.validate_show_number(show_number):
            self.message.invalid_input_message()
            return False, None

        show_number = int(show_number)
        print("Enter the seats you want to book: ")
        seat_list = list(input().strip().split())
        group = Group(show_number, seat_list)
        return True, group


    def exit_booking(self):
        while True:
            choice = input("Do you wish to book more seats (Y/N): ").strip().upper()
            if choice == "N":
                return True
            if choice == "Y":
                return False
            self.message.invalid_input_message()


    def book_seats(self):
        success, group = self.create_group()
        if not success:
            self.message.error_message()
            return

        self.movie_system.alott_seats(group)


    def main(self):
        exited = False
        while not exited:
            self.book_seats()
            exited = self.exit_booking()



driver = Driver()
driver.main()

