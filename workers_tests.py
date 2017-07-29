import unittest

import sc2reader

import techlabreactor


class TestWorkers(unittest.TestCase):

    def test_worker_saturation(self):
        replay = sc2reader.load_replay("test_replays/frugs.SC2Replay")

        two_base_saturation = techlabreactor.two_base_saturation_timing(replay.players[0], replay)
        self.assertEqual(two_base_saturation, 278)

        three_base_saturation = techlabreactor.three_base_saturation_timing(replay.players[0], replay)
        self.assertEqual(three_base_saturation, 428)

    def test_worker_supply_1(self):
        replay = sc2reader.load_replay("test_replays/frugs.SC2Replay")

        worker_supply = techlabreactor.worker_supply_at(270, replay.players[0], replay)
        self.assertEqual(worker_supply, 52)

    def test_worker_supply_2(self):
        replay = sc2reader.load_replay("test_replays/snute.SC2Replay")

        worker_supply = techlabreactor.worker_supply_at(270, replay.players[1], replay)
        self.assertEqual(worker_supply, 56)
