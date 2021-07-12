import unittest
from models.MovieTicketSystem import MovieTicketSystem
from models.MovieShow import MovieShow


class MyTestCase(unittest.TestCase):

    def test_should_return_available_seats_of_as_set_when_show_number_is_passed(self):
        movie_ticket_system = MovieTicketSystem()
        show_number = 1
        available_seats = ['A1', 'A2', 'A3', 'A4']
        show = MovieShow(1, available_seats)
        movie_ticket_system.set_show(show)
        self.assertEqual(set(available_seats), movie_ticket_system.get_available_seats(show_number))

    def test_should_return_empty_set_when_invalid_show_number_is_passed(self):
        movie_ticket_system = MovieTicketSystem()
        show_number = 1
        self.assertEqual(set(), movie_ticket_system.get_available_seats(show_number))



if __name__ == '__main__':
    unittest.main()
