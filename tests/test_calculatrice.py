import unittest
from calculatrice import division, puissance, moyenne
class TestCalculatrice(unittest.TestCase):
    def test_division_simple(self):
        self.assertEqual(division(10, 2), 5)
    def test_division_decimale(self):
        self.assertEqual(division(5, 2), 2.5)
    def test_division_par_zero(self):
        with self.assertRaises(ZeroDivisionError):
            division(10, 0)
    def test_puissance_2_3(self):
        self.assertEqual(puissance(2, 3), 8)
    def test_puissance_exposant_zero(self):
        self.assertEqual(puissance(5, 0), 1)
    def test_puissance_exposant_negatif(self):
        with self.assertRaises(ValueError):
            puissance(2, -1)
    def test_moyenne_valeurs(self):
        self.assertEqual(moyenne([10, 20, 30]), 20)
    def test_moyenne_liste_vide(self):
        with self.assertRaises(ValueError):
            moyenne([])
