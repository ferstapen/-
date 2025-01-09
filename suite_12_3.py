import unittest
import tests_12_3

import unittest
import tests_12_3

tournamentST = unittest.TestSuite()
tournamentST.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_3.RunnerTest))
tournamentST.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_3.TournamentTest))

run = unittest.TextTestRunner(verbosity=2)
run.run(tournamentST)
