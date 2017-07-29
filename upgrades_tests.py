import unittest

import sc2reader

import techlabreactor


class TestUpgrades(unittest.TestCase):

    def test_upgrades(self):
        replay = sc2reader.load_replay("test_replays/frugs.SC2Replay")

        result = techlabreactor.first_upgrade_started_timing(replay.players[0], replay)
        self.assertEqual(result, 400)