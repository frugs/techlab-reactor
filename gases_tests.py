import unittest

import sc2reader

import techlabreactor


class TestGases(unittest.TestCase):

    def test_gases(self):
        replay = sc2reader.load_replay("test_replays/frugs_vs_ai.SC2Replay")

        result = techlabreactor.second_gas_timing(replay.players[0], replay)
        self.assertEqual(result, 292)