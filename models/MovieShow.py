

class MovieShow:

    def __init__(self, show_no, available_seats):
        self.show_number = show_no
        self.available_seats = available_seats

    def get_show_number(self):
        return self.show_number

    def get_available_seats(self):
        return self.available_seats