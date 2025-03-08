from entities.rocket import Rocket
from people.person import Person
from people.student_engineer import StudentEngineer
#from utilities.mission_member import MissionMember

rocket = Rocket(fuel_level= '50%', thrust_power=1000)

person = Person(imie= 'Emilia', nazwisko= 'M')

print(rocket.launch_sequence())
print(person.report_status())