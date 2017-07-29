import unittest

import techlabreactor
import sc2reader


class TestCreep(unittest.TestCase):

    def test_creep(self):
        replay = sc2reader.load_replay("test_replays/frugs_vs_ai.SC2Replay")
        result = techlabreactor.creep_tumours_built_before_second(420, replay.players[0], replay)

        self.assertEqual(result, 8)