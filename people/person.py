class Person:
    def __init__(self, imie, nazwisko):
        self.imie = imie
        self.nazwisko = nazwisko

    def report_status(self):
        return f'Nazywam się tak jak ja : {self.imie} {self.nazwisko}.'