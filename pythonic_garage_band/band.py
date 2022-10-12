from abc import ABC


class Band:
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
    def __init__(self, name):
        super().__init__(name)

    @staticmethod
    def get_instrument():
        return "guitar"

    @staticmethod
    def play_solo():
        return "face melting guitar solo"


class Drummer(Musician):
    def __init__(self, name):
        super().__init__(name)

    @staticmethod
    def get_instrument():
        return "drums"

    @staticmethod
    def play_solo():
        return "rattle boom crash"


class Bassist(Musician):
    def __init__(self, name):
        super().__init__(name)

    @staticmethod
    def get_instrument():
        return "bass"

    @staticmethod
    def play_solo():
        return "bom bom buh bom"

# class Keyboardist(Musician):
#     def __init__(self, name):
#         super().__init__(name)

#     # @staticmethod
#     def get_instrument():
#         return "keyboard"

#     # @staticmethod
#     def play_solo():
#         return "clickity clack"