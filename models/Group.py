

class Group:

    def __init__(self, group_no):
        self.group_number = group_no
        self.requested_show_number = None
        self.requested_seats = []

    def get_group_number(self):
        return self.group_number

    def set_requested_show_number(self, show_no):
        self.requested_show_number = show_no

    def get_requested_show_number(self):
        return self.requested_show_number

    def set_requested_seats(self, requested_seats):
        self.requested_seats = requested_seats

    def get_requested_seats(self):
        return self.requested_seats