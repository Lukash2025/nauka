from .person import Person
from utilities.mission_member import MissionMember

class StudentEngineer(Person, MissionMember):
    def show_mro_report_status(self):
        return self.report_status()