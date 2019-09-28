import unittest

import techlabreactor
import sc2reader


class TestProduction(unittest.TestCase):

    def test_production_used_out_of_capacity_0(self):
        replay = sc2reader.load_replay("test_replays/picur.SC2Replay")
        production_used, production_capacity = techlabreactor.production_used_out_of_capacity_for_player(
            420, replay.players[1], replay)

        for structure_type, capacities in production_capacity.items():
            for time, capacity in capacities:
                used_before_times = [used for used_time, used in production_used[structure_type] if used_time <= time]
                used_at_time = used_before_times[-1] if used_before_times else 0

                self.assertGreaterEqual(capacity, used_at_time)
                self.assertGreaterEqual(capacity, 0)

        for structure_type, used_values in production_used.items():
            for time, used in used_values:
                self.assertGreaterEqual(used, 0)

    def test_production_used_out_of_capacity_1(self):
        replay = sc2reader.load_replay("test_replays/lambo_vs_soul.SC2Replay")
        for player in replay.players:
            production_used, production_capacity = techlabreactor.production_used_out_of_capacity_for_player(
                600, player, replay)

            for structure_type, capacities in production_capacity.items():
                for time, capacity in capacities:
                    used_before_times = [used for used_time, used in production_used[structure_type] if
                                         used_time <= time]
                    used_at_time = used_before_times[-1] if used_before_times else 0

                    self.assertGreaterEqual(capacity, used_at_time)
                    self.assertGreaterEqual(capacity, 0)

            for structure_type, used_values in production_used.items():
                for time, used in used_values:
                    self.assertGreaterEqual(used, 0)

    def test_production_used_out_of_capacity_2(self):
        replay = sc2reader.load_replay("test_replays/lambo_vs_barcode.SC2Replay")
        for player in replay.players:
            production_used, production_capacity = techlabreactor.production_used_out_of_capacity_for_player(
                600, player, replay)

            for structure_type, capacities in production_capacity.items():
                for time, capacity in capacities:
                    used_before_times = [used for used_time, used in production_used[structure_type] if
                                         used_time <= time]
                    used_at_time = used_before_times[-1] if used_before_times else 0

                    self.assertGreaterEqual(capacity, used_at_time)
                    self.assertGreaterEqual(capacity, 0)

            for structure_type, used_values in production_used.items():
                for time, used in used_values:
                    self.assertGreaterEqual(used, 0)

    def test_production_used_out_of_capacity_3(self):
        replay = sc2reader.load_replay("test_replays/avilo_1.SC2Replay")
        for player in replay.players:
            production_used, production_capacity = techlabreactor.production_used_out_of_capacity_for_player(
                6000, player, replay)

            for structure_type, capacities in production_capacity.items():
                for time, capacity in capacities:
                    used_before_times = [used for used_time, used in production_used[structure_type] if
                                         used_time <= time]
                    used_at_time = used_before_times[-1] if used_before_times else 0

                    self.assertGreaterEqual(capacity, used_at_time)
                    self.assertGreaterEqual(capacity, 0)

            for structure_type, used_values in production_used.items():
                for time, used in used_values:
                    self.assertGreaterEqual(used, 0)

    def test_production_used_out_of_capacity_4(self):
        replay = sc2reader.load_replay("test_replays/avilo_2.SC2Replay")
        for player in replay.players:
            production_used, production_capacity = techlabreactor.production_used_out_of_capacity_for_player(
                6000, player, replay)

            for structure_type, capacities in production_capacity.items():
                for time, capacity in capacities:
                    used_before_times = [used for used_time, used in production_used[structure_type] if
                                         used_time <= time]
                    used_at_time = used_before_times[-1] if used_before_times else 0

                    self.assertGreaterEqual(capacity, used_at_time)
                    self.assertGreaterEqual(capacity, 0)
                    self.assertGreaterEqual(time, 0)

            for structure_type, used_values in production_used.items():
                for time, used in used_values:
                    self.assertGreaterEqual(used, 0)
                    self.assertGreaterEqual(time, 0)

    def test_production_used_out_of_capacity_5_viking(self):
        replay = sc2reader.load_replay("test_replays/Ephemeron_LE_33.SC2Replay")
        for player in replay.players:
            production_used, production_capacity = techlabreactor.production_used_out_of_capacity_for_player(
                6000, player, replay)

            for structure_type, capacities in production_capacity.items():
                for time, capacity in capacities:
                    used_before_times = [used for used_time, used in production_used[structure_type] if
                                         used_time <= time]
                    used_at_time = used_before_times[-1] if used_before_times else 0

                    self.assertGreaterEqual(capacity, used_at_time)
                    self.assertGreaterEqual(capacity, 0)
                    self.assertGreaterEqual(time, 0)

            for structure_type, used_values in production_used.items():
                for time, used in used_values:
                    self.assertGreaterEqual(used, 0)
                    self.assertGreaterEqual(time, 0)
