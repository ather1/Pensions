from django.test import TestCase

# Create your tests here.
from  .models import  Airport, Passenger, Flight

class ModelsTestCase(TestCase):
    def setUp(self):
        #create airports
        a1 = Airport.objects.create(code="AAA", city= "City A")
        a2 = Airport.objects.create(code="BBB", city= "City B")

        p1 = Passenger.objects.create(first="Pass1", last ="Pass1-Surname")
        p2 = Passenger.objects.create(first="Pass2", last ="Pass1-Surname")

        f1 = Flight.objects.create(origin = a1, destination =a2, duration = 512)
        f1 = Flight.objects.create(origin = a2, destination = a2, duration = 512)
        f1 = Flight.objects.create(origin = a1, destination = a2, duration = -100 )


    def test_airport_count(self):
        a= Airport.objects.get(code="AAA")
        self.assertEquals(a.departures.count(),2)

    def test_flight_count(self):
        a = Flight.objects.get(origin = a2)
        self.assertEqual(a.count(),1)

    def test_isflightvalid(self):
        a1  = Airport.objects.get(code ="AAA")
        a2 = Airport.objects.get(code="BBB")

        f1 = Flight.objects.get(origin = a1, destination = a2,duration = 512)

        self.assertTrue(f1.isValidFlight())

    def test_isFlightNotvalid(self):
        a1= Airport.objects.get(code ="AAA")
        a2 = Airport.objects.get(code="BBB")

        f1 = Flight.objects.get(origin = a1, destination = a2, duration = -100)

        self.assertFalse(fl.isValidFlight())
