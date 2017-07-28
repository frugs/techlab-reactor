import unittest

import sc2reader

import techlabreactor


class TestTiers(unittest.TestCase):

    def test_tiers_1(self):
        replay = sc2reader.load_replay("test_replays/frugs_vs_ai.SC2Replay")

        result = techlabreactor.lair_started_timing(replay.players[0], replay)
        self.assertEqual(result, 328)

    def test_tiers_2(self):
        replay = sc2reader.load_replay("test_replays/picur.SC2Replay")

        result = techlabreactor.lair_started_timing(replay.players[0], replay)
        self.assertEqual(result, 336)
