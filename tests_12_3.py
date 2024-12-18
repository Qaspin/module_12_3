import runner
import unittest
from runner import Runner, Tournament

class RunnerTest(unittest.TestCase):
    is_frozen = False
    @unittest.skipIf(is_frozen , 'Тесты в этом кейсе заморожены')
    def test_walk(self):
        walker = runner.Runner('Евгений')
        for i in range(10):
            walker.walk()
        self.assertEqual(walker.distance, 50)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_run(self):
        runer = runner.Runner('Елизаветта')
        for i in range(10):
            runer.run()
        self.assertEqual(runer.distance, 100)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_challenge(self):
        walker2 = runner.Runner('Катя')
        runer2 = runner.Runner('Саша')
        for i in range(10):
            walker2.walk()
            runer2.run()
        self.assertNotEqual(runer2.distance, walker2.distance)



class TournamentTest(unittest.TestCase):
    is_frozen = True
    @classmethod
    def setUpClass(cls):
        cls.all_results = []

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def setUp(self):
        self.usein = Runner('Усейн', 10)
        self.andrey = Runner('Андрей', 9)
        self.nik = Runner('Ник', 3)

    @classmethod
    def tearDownClass(cls):
        for i, elem in enumerate(cls.all_results):
            print(elem)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_fist_tur(self):
        tur = Tournament(90, self.usein, self.nik)
        result = {k: str(v) for k, v in tur.start().items()}
        TournamentTest.all_results.append(result)
        self.assertTrue(result[2], 'Ник')

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_second_tur(self):
        tur = Tournament(90, self.andrey, self.nik)
        result = {k: str(v) for k, v in tur.start().items()}
        TournamentTest.all_results.append(result)
        self.assertTrue(result[2], 'Ник')

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_third_tur(self):
        tur = Tournament(90, self.usein, self.andrey, self.nik)
        result = {k: str(v) for k, v in tur.start().items()}

        TournamentTest.all_results.append(result)
        self.assertTrue(result[3], 'Ник')