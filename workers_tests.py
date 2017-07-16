import unittest

import sc2reader

import techlabreactor


class TestWorkers(unittest.TestCase):

    def test_worker_saturation(self):
        replay = sc2reader.load_replay("test_replays/frugs_vs_ai.SC2Replay")

        two_base_saturation = techlabreactor.two_base_saturation_timing(replay.players[0], replay)
        self.assertEqual(two_base_saturation, 278)

        three_base_saturation = techlabreactor.three_base_saturation_timing(replay.players[0], replay)
        self.assertEqual(three_base_saturation, 428)