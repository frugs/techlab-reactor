import unittest

import sc2reader

import techlabreactor


class TestExpansions(unittest.TestCase):

    def test_expansions_1(self):
        replay = sc2reader.load_replay("test_replays/frugs.SC2Replay")

        natural_timing = techlabreactor.natural_expansion_timing(replay.players[0], replay)
        self.assertEqual(natural_timing, 49)

        third_timing = techlabreactor.third_expansion_timing(replay.players[0], replay)
        self.assertEqual(third_timing, 161)

    def test_expansions_2(self):
        replay = sc2reader.load_replay("test_replays/picur.SC2Replay")

        natural_timing = techlabreactor.natural_expansion_timing(replay.players[0], replay)
        self.assertEqual(natural_timing, 54)

        third_timing = techlabreactor.third_expansion_timing(replay.players[0], replay)
        self.assertEqual(third_timing, 209)
