import unittest

import sc2reader

import techlabreactor


class TestResearches(unittest.TestCase):

    def test_zergling_speed(self):
        replay = sc2reader.load_replay("test_replays/frugs.SC2Replay")

        result = techlabreactor.research_finished_timing("zerglingmovementspeed", replay.players[0], replay)
        self.assertEqual(result, 208)

    def test_overlord_speed(self):
        replay = sc2reader.load_replay("test_replays/frugs.SC2Replay")

        result = techlabreactor.overlord_speed_research_started_timing(replay.players[0], replay)
        self.assertEqual(result, 478)
