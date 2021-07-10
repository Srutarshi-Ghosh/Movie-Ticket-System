
from models.MovieShow import MovieShow
from models.Group import Group
from models.MovieTicketSystem import MovieTicketSystem


def main():
    movie_system = MovieTicketSystem()

    show1 = MovieShow(1)
    show1.set_available_seats(['A1', 'A2', 'A3', 'A4'])
    movie_system.set_show(show1)

    show2 = MovieShow(2)
    show2.set_available_seats(['A1', 'A2', 'A3', 'A4', 'B1', 'B2', 'B3'])
    movie_system.set_show(show2)

    group1 = Group(1)
    group1.set_requested_show_number(1)
    group1.set_requested_seats(['A3', 'A4', 'B3'])
    movie_system.alott_seats(group1)

    group2 = Group(2)
    group2.set_requested_show_number(2)
    group2.set_requested_seats(['A1', 'A4', 'B2'])
    movie_system.alott_seats(group2)


main()

