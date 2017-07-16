import unittest

import techlabreactor
import sc2reader


class TestInjects(unittest.TestCase):

    def test_inject_pops(self):
        replay = sc2reader.load_replay("test_replays/frugs_vs_ai.SC2Replay")
        result = techlabreactor.get_inject_pops_for_player(replay.players[0], replay)

        self.assertEqual(result, 20)