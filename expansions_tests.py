import unittest

import sc2reader

import techlabreactor


class TestExpansions(unittest.TestCase):

    def test_worker_saturation(self):
        replay = sc2reader.load_replay("test_replays/frugs_vs_ai.SC2Replay")

        natural_timing = techlabreactor.natural_expansion_timing(replay.players[0], replay)
        self.assertEqual(natural_timing, 49)

        third_timing = techlabreactor.natural_expansion_timing(replay.players[0], replay)
        self.assertEqual(third_timing, 161)
