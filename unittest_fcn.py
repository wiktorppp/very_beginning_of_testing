import unittest

class MojTest(unittest.TestCase):
    #metoda przygotowujca test
    def setUp(self):
        #warunki wstepne
        print("Przygotowanie testu")

    #metody testowe zaczynaja sie od slowa test
    def testPierwszy(self):
        print("Robie test nr 1")
        napis_faktyczny ="To pole jest wymaganesfa" #required parameter
        napis_oczekiwany = "To pole jest wymagane" #not required parameter
        self.assertEqual(napis_oczekiwany,napis_faktyczny) #add unittest test for checking two parameters

    def testDrugi(self):
        print("Robie test nr 2")

    def tearDown(self):
        print("Koniec testow")

