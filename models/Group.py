

class Group:

    def __init__(self, requested_show_number, requested_seats):
        self.requested_show_number = requested_show_number
        self.requested_seats = requested_seats


    def get_requested_show_number(self):
        return self.requested_show_number


    def get_requested_seats(self):
        return self.requested_seats