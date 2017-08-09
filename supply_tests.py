import unittest

import sc2reader

import techlabreactor


class TestSupply(unittest.TestCase):

    def test_supply_blocks(self):
        replay = sc2reader.load_replay("test_replays/frugs.SC2Replay")
        result = techlabreactor.get_supply_blocks_till_time_for_player(420, replay.players[0], replay)

        blocked = False
        blocked_since = 0
        time_supply_blocked = 0
        for time, blocked_state in result:

            if blocked:
                time_supply_blocked += time - blocked_since

            if blocked_state:
                blocked_since = time

            blocked = blocked_state

        self.assertGreater(time_supply_blocked, 35)
        self.assertLess(time_supply_blocked, 36)
