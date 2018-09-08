import unittest

import techlabreactor
import sc2reader


class TestLarvae(unittest.TestCase):

    def test_larvae_blocks(self):
        replay = sc2reader.load_replay("test_replays/frugs.SC2Replay")
        result = techlabreactor.larvae_blocks_per_hatchery_for_player(replay.players[0], replay)

        self.assertEqual(len(result), 5)
        self.assertEqual(len(result[0]), 22)

