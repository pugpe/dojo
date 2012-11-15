# coding: utf-8
# tests

import unittest
from problem import jogo

class TestsDojo(unittest.TestCase):

    def test_empate(self):
        self.assertEqual(
            jogo('spock', 'spock'), 'Uhhhh'
        )

    def test_pedra_tesoura(self):
        self.assertEqual(
            jogo('pedra', 'tesoura'),
            'pedra esmaga tesoura'
        )

    def test_pedra_lagarto(self):
        self.assertEqual(
            jogo('pedra', 'lagarto'),
            'pedra esmaga lagarto'
        )

    def test_lagarto_spock(self):
        self.assertEqual(
            jogo('lagarto', 'spock'),
            'lagarto envenena spock'
        )

    def test_tesoura_papel(self):
        self.assertEqual(
            jogo('tesoura', 'papel'),
            'tesoura corta papel'
            )
    def test_spock_tesoura(self):
        self.assertEqual(
            jogo('spock','tesoura'),
            'spock esmaga tesoura'

            )

    def test_tesoura_spock(self):
        self.assertEqual(
            jogo('tesoura', 'spock'),
            'spock esmaga tesoura'
            )

    def test_spock_pedra(self):
        self.assertEqual(
            jogo('spock', 'pedra'),
            'spock vaporiza pedra'
            )

    def test_lagarto_papel(self):
        self.assertEqual(jogo('lagarto', 'papel'),
            'lagarto come papel')

if __name__ == '__main__':
    unittest.main()
