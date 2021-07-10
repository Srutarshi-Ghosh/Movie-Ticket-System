

class InputValidator:

    @staticmethod
    def validate_input_type(given_input, required_type):
        return type(given_input) is required_type

    @staticmethod
    def validate_show_number(show_no):
        try:
            int(show_no)
        except:
            return False
        return True

