from django.test import TestCase, Client
from django.db.models import Max

# Create your tests here.
from  .models import  Airport, Passenger, Flight

class ModelsTestCase(TestCase):
    def setUp(self):
        #create airports
        a1 = Airport.objects.create(code="AAA", city= "City A")
        a2 = Airport.objects.create(code="BBB", city= "City B")

        p1 = Passenger.objects.create(first="Pass1", last ="Pass1-Surname")
        p2 = Passenger.objects.create(first="Pass2", last ="Pass1-Surname")

        f1 = Flight.objects.create(origin = a1, destination = a2, duration = 512)
        f1 = Flight.objects.create(origin = a2, destination = a2, duration = 512)
        f1 = Flight.objects.create(origin = a1, destination = a2, duration = -100 )
        f1 = Flight.objects.create(origin = a1, destination = a1, duration = 100)

    def test_airport_count(self):
        a= Airport.objects.get(code="AAA")
        self.assertEqual(a.code,"AAA")

    def test_flight_count(self):
        a2= Airport.objects.get(code="AAA")
        f1 = Flight.objects.filter(origin = a2)
        self.assertEqual(f1.count(),3)

    def test_isflightvalid(self):
        a1  = Airport.objects.get(code ="AAA")
        a2 = Airport.objects.get(code="BBB")

        f1 = Flight.objects.filter(origin = a1, destination = a2,duration = 512)

        self.assertEqual(f1.count(),1)

    def test_isFlightDurationNotvalid(self):
        a1  = Airport.objects.get(code ="AAA")
        a2 = Airport.objects.get(code="BBB")

        f1 = Flight.objects.get(origin = a1, destination = a2,duration = -100)
        self.assertFalse(f1.isValidFlight())

    def test_isFlightOriginDestinationNotValid(self):
        a1= Airport.objects.get(code="AAA")
        a2 = Airport.objects.get(code="BBB")

        f1 = Flight.objects.get(origin = a1, destination = a1, duration = 100)
        self.assertFalse(f1.isValidFlight())

    def test_Index(self):
        c = Client()
        response = c.get("/")
        self.assertEqual(response.status_code , 200)
        self.assertEqual(response.context["flights"].count(),4)


    def test_valid_flight_page(self):
        c = Client()
        a2 = Airport.objects.get(code = "BBB")
        f1 = Flight.objects.get(origin = a2 , destination = a2)

        response = c.get(f"/{f1.id}")
        self.assertEqual(response.status_code , 200)

    def test_invalid_flight_id_page(self):
        maxNo = Flight.objects.all().aggregate(Max("id"))["id__max"]

        c = Client()
        response = c.get(f"/{maxNo + 1 }")
        self.assertEqual(response.status_code , 404)

    def test_flight_passenger_count(self):
        f1 = Flight.objects.get(pk=1)
        p1 = Passenger.objects.create(first = "Jaone", last = "Smith")
        p2 = Passenger.objects.create(first = "John", last = "Jones")
        c = Client()
        f1.passengers.add(p1)
        f1.passengers.add(p2)
        response = c.get(f"/{f1.id}")
        self.assertEqual(response.context["passengers"].count() , 2)

    def test_flight_non_passenger_count(self):
        f1 = Flight.objects.get(pk=1)
        p1 = Passenger.objects.create(first= "abid", last = "second")
        # p2 = Passenger.objects.create(first="Simon", last = "Singh")
        # p3 = Passenger.objects.create(first="Atif", last="Khan")
        c = Client()
        # f1.passengers.add(p1)
        response = c.get(f"/{f1.id}")
        for passenger in response.context["non_passengers"].all():
            print(passenger)

        self.assertEqual(response.status_code , 200)
        # The setup has created 2 additional non passengers . For testing purposes 
        # this has meant this test is not atomic. But on the other hand if there is a 
        # a setup function then tests cant be atomic. If I wanted to test this function 
        # then I have to check if non passengers already exist in the database and then
        # add 1 more and then check to see if that has been added.

        self.assertEqual(response.context["non_passengers"].count() , 3)

