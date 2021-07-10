

class MovieShow:

    def __init__(self, show_no):
        self.show_number = show_no
        self.available_seats = []

    def set_available_seats(self, seat_list):
        self.available_seats = seat_list

    def get_show_number(self):
        return self.show_number

    def get_available_seats(self):
        return self.available_seats