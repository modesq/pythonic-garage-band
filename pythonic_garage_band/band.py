from abc import ABC


class Band:
    """
    this class represents a band which can be used to represent all of its memebers in a list alongside some
    methods that can be used to print them or play their solos
    """

    instances = []

    def __init__(self, name, members):
        self.name = name
        self.members = members
        Band.instances.append(self)

    def play_solos(self):
        solos = []
        for i in self.members:
            solos.append(i.play_solo())
        return solos

    def __str__(self):
        return f"{self.name} band"

    def __repr__(self):
        return f"Name = {self.name}"

    @classmethod
    def to_list(cls):
        return cls.instances


class Musician(ABC):
    """
    this the parent abstract class for the classes "Guitarist", "Drummer", and "Bassist". it has the methods that they inherit.
    the abstract methods "play_solos()" and "get_instrument() need to be implemented in the children classes.
    """

    def __init__(self, name):
        self.name = name

    # @abstractmethod
    def play_solos(self):
        return

    # @abstractmethod
    def get_instrument(self):
        return

    def __str__(self):
        return f"My name is {self.name} and I play {self.get_instrument()}"

    def __repr__(self):
        return f"{self.__class__.__name__} instance. Name = {self.name}"

    def play_solo(self):
        return self.play_solos()


class Guitarist(Musician):
    """
    this is a child class that inherits from class "Musician" and it implements its abstract methods as needed for this class
    """

    def __init__(self, name):
        super().__init__(name)

    @staticmethod
    def get_instrument():
        return "guitar"

    @staticmethod
    def play_solo():
        return "face melting guitar solo"


class Drummer(Musician):
    """
    this is a child class that inherits from class "Musician" and it implements its abstract methods as needed for this class
    """

    def __init__(self, name):
        super().__init__(name)

    @staticmethod
    def get_instrument():
        return "drums"

    @staticmethod
    def play_solo():
        return "rattle boom crash"


class Bassist(Musician):
    """
    this is a child class that inherits from class "Musician" and it implements its abstract methods as needed for this class
    """

    def __init__(self, name):
        super().__init__(name)

    @staticmethod
    def get_instrument():
        return "bass"

    @staticmethod
    def play_solo():
        return "bom bom buh bom"
