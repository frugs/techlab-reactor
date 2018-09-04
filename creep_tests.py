import unittest

import techlabreactor
import sc2reader


class TestCreep(unittest.TestCase):

    def test_creep_1(self):
        replay = sc2reader.load_replay("test_replays/frugs.SC2Replay")
        result = techlabreactor.creep_tumours_built_before_second(420, replay.players[0], replay)

        self.assertEqual(result, 8)

    def test_creep_2(self):
        replay = sc2reader.load_replay("test_replays/picur.SC2Replay")
        result = techlabreactor.creep_tumours_built_before_second(420, replay.players[0], replay)

        self.assertEqual(result, 23)

    def test_creep_3(self):
        replay = sc2reader.load_replay("test_replays/snute.SC2Replay")
        result = techlabreactor.creep_tumours_built_before_second(420, replay.players[1], replay)

        self.assertEqual(result, 27)

    def test_creep_states_1(self):
        replay = sc2reader.load_replay("test_replays/frugs.SC2Replay")
        result = techlabreactor.creep_tumour_state_changes(replay.players[0], replay)

        self.assertEqual(sum([x[1] for x in result]), 0)
        self.assertEqual(len(result), 24)

    def test_creep_states_2(self):
        replay = sc2reader.load_replay("test_replays/picur.SC2Replay")
        result = techlabreactor.creep_tumour_state_changes(replay.players[0], replay)

        self.assertEqual(sum([x[1] for x in result]), 0)
        self.assertEqual(len(result), 170)

    def test_creep_states_3(self):
        replay = sc2reader.load_replay("test_replays/snute.SC2Replay")
        result = techlabreactor.creep_tumour_state_changes(replay.players[1], replay)

        self.assertEqual(sum([x[1] for x in result]), 0)
        self.assertEqual(len(result), 170)