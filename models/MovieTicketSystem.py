
from models.Message import Message


class MovieTicketSystem:

    def __init__(self):
        self.show_list = {}

    def set_show(self, show):
        show_number = show.get_show_number()
        self.show_list[show_number] = set(show.available_seats)


    def get_available_seats(self, show_number):
        return self.show_list.get(show_number, [])


    def check_show_availability(self, requested_show):
        return requested_show in self.show_list


    @staticmethod
    def check_seat_availability(available_seats, requested_seats):
        for seat in requested_seats:
            if seat not in available_seats:
                return False
        return True


    @staticmethod
    def update_available_seats(booked_seats, available_seats):
        for seat in booked_seats:
            available_seats.remove(seat)


    def alott_seats(self, group):
        requested_show = group.get_requested_show_number()
        available_seats = self.get_available_seats(requested_show)
        requested_seats = group.get_requested_seats()
        message = Message()

        are_seats_available = self.check_seat_availability(available_seats, requested_seats)

        if not are_seats_available:
            message.seat_not_available_message()
            return None

        self.update_available_seats(requested_seats, available_seats)
        message.booking_successful_message()



