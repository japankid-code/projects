class Game:
    def __init__(self):
        self.won = False
        self.items = []
        self.floor_level = 0
        self.current_floor = None

    def start_game(cls):
        g = Game()
        cls.intro()
        while not g.won:
            g.ride_elevator()
            g.enter_floor()


    def ride_elevator(self):
        floor = input("Please enter the number for the floor you would like to visit:")
        self.floor_level = int(floor)
        while not Floor().valid_floor(int(floor)):
            floor = self.ride_again()
            self.floor_level = int(floor)

    def ride_again(self):
        print("The floor you entered is invalid, please choose another")
        Floor().print_options()
        return input("Choose a floor:")


    def intro(cls):
        for msg in cls.intro_messages():
            print(msg)
        Floor().print_options()

    def enter_floor(self):
        floor_name = self.parse_current_floor()
        class_name = globals()[floor_name.replace(' ', '')]
        floor = class_name()
        if floor.can_enter(self.items):
            self.current_floor = floor
            self.get_items_from_floor()
        else:
            floor.missing_required_msg

    def get_items_from_floor(self):
        if self.item_exist():
            self.current_floor.contains_message()
            return
        self.current_floor.recieved_message()
        self.items.append(self.current_floor.ITEM)

    def item_exist(self):
        return(self.current_floor.ITEM in self.items)

    def parse_current_floor(self):
        return(Floor().LEVELS[self.floor_level])

    def intro_messages(cls):
        return ['Humanity as it was once has ceased to exist.',
        'You are a robot and have just arrived to start your new assignment at the human generator plant.',
         'You make your way directly to the elevator and find several buttons.']


class Floor:
    LEVELS = {
        1: 'Lobby',
        2: 'Robot Resources'
    }

    def valid_floor(cls, floor):
        return(floor in cls.LEVELS.keys())

    def print_options(cls):
        for opt in cls.options():
            print(opt)

    def options(cls):
        opts = cls.LEVELS.items()
        return([f"{k} - {v}" for k,v in opts])

    def enter_floor(self):
        for msg in self.INTRO:
            print(msg)

    def can_enter(self, items):
        return(items == self.ITEMS_REQUIRED)

class Lobby(Floor):
    INTRO = [
        'The door closes and then opens. Your circuity computes...',
        'You are now in the lobby...'
    ]

    ITEM = 'ID Chip'

    def __init__(self):
        super().__init__()

    def can_enter(self, items = None):
        return True

    def contains_message(self):
        print("The clerk greets you, but she has already given you your \n"
              "ID chip, so there is nothing more to do here now")

    def recieved_message(self):
        print("The clerk greets you and gives you your ID chip.")

class RobotResources(Floor):
    INTRO = [
        'After a moment, you find yourself in the Robot Resources department',
        'The administrator of the floor greets you'
    ]

    ITEM = 'Handbook'
    ITEMS_REQUIRED = [Lobby.ITEM]

    def __init__(self):
        super().__init__()

    def contains_message(self):
        print("But she has already given you your handbook");

    def recieved_message(self):
        print("She looks at your ID chip, she hands you a datachip containg"
              " the employee handbook")

    def missing_required_msg(self):
        print(f"The administrator has something for you, but says she can't give it to you until you go get your {ITEMS_REQUIRED[0]}")

Game().start_game()
