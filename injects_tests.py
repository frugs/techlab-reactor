import unittest

import techlabreactor
import sc2reader


class TestInjects(unittest.TestCase):

    def test_inject_pops(self):
        replay = sc2reader.load_replay("test_replays/frugs.SC2Replay")
        result = techlabreactor.get_inject_pops_for_player(replay.players[0], replay)

        self.assertEqual(result, 20)

    def test_inject_pops_full(self):
        replay = sc2reader.load_replay("test_replays/frugs.SC2Replay")
        result = techlabreactor.get_inject_pops_for_player(replay.players[0], replay, 0)

        self.assertEqual(result, 49)

    def test_inject_before_hatchery_finished(self):
        replay = sc2reader.load_replay("test_replays/ZvP_AcidPlant_HydraLurker_with_Drops.SC2Replay")
        result = techlabreactor.get_hatchery_inject_states_for_player(replay.players[0], replay, 0)

        self.assertEqual(result[2][0], (5151, False))
