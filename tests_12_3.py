import runner_and_tournament
import unittest
import runner

class RunnerTest(unittest.TestCase):
    is_frozen = False

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены.')
    def test_walk(self):
        runner_1 = runner.Runner('Danil')
        for i in range(10):
            runner_1.walk()
        self.assertEqual(runner_1.distance, 50)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены.')
    def test_run(self):
        runner_2 = runner.Runner('Alex')
        for i in range(10):
            runner_2.run()
        self.assertEqual(runner_2.distance, 100)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены.')
    def test_challenge(self):
        runner_1 = runner.Runner('Danil')
        runner_2 = runner.Runner('Alex')
        for i in range(10):
            runner_1.walk()
            runner_2.run()
        self.assertNotEqual(runner_1.distance, runner_2.distance)

class TournamentTest(unittest.TestCase):
    is_frozen = True

    @classmethod
    def setUpClass(cls):
        TournamentTest.all_results = {}

    def setUp(self):
        self.usein = runner_and_tournament.Runner('Усэйн', 10)
        self.andre = runner_and_tournament.Runner('Андрей', 9)
        self.nic = runner_and_tournament.Runner('Ник', 3)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены.')
    def testing_1(self):
        tourn_1 = runner_and_tournament.Tournament(90, self.usein, self.nic)
        TournamentTest.all_results = tourn_1.start()
        self.assertTrue(TournamentTest.all_results[2], 'Ник')

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены.')
    def testing_2(self):
        tourn_2 = runner_and_tournament.Tournament(90, self.andre, self.nic)
        TournamentTest.all_results = tourn_2.start()
        self.assertTrue(TournamentTest.all_results[2], 'Ник')

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены.')
    def testing_3(self):
        tourn_3 = runner_and_tournament.Tournament(90, self.usein, self.andre, self.nic)
        TournamentTest.all_results = tourn_3.start()
        self.assertTrue(TournamentTest.all_results[2], 'Ник')

    @classmethod
    def tearDowmClass(cls):
        for key, value in TournamentTest.all_results.items():
            print(f'{key} - {value}')

if __name__ == '__main__':
    unittest.main()
