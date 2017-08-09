import unittest

import techlabreactor
import sc2reader


# def plot_graph(production_used, production_capacity):
#     import matplotlib.dates
#     import matplotlib.pyplot as plt
#     import datetime
#
#     def to_time(seconds):
#         return datetime.datetime.fromtimestamp(0) + datetime.timedelta(milliseconds=int(seconds * 1000))
#
#     offset = 0
#     for structure_type in production_capacity.keys():
#         plt.step([to_time(time) for time, _ in production_used[structure_type]],
#                  [production + offset for _, production in production_used[structure_type]],
#                  where="post", label=structure_type + " Production Used")
#         plt.step([to_time(time) for time, _ in production_capacity[structure_type]],
#                  [production + offset for _, production in production_capacity[structure_type]],
#                  where="post", label=structure_type + " Production Capacity")
#
#         offset += 1 + max(production for _, production in production_capacity[structure_type])
#
#     plt.gca().xaxis.set_major_locator(matplotlib.dates.MinuteLocator())
#     plt.gca().xaxis.set_minor_locator(matplotlib.dates.SecondLocator(interval=10))
#     plt.gca().xaxis.set_major_formatter(matplotlib.dates.DateFormatter("%M:%S"))
#
#     plt.yticks([])
#     plt.legend(loc=2)
#     plt.show()


class TestProduction(unittest.TestCase):

    def test_production(self):
        replay = sc2reader.load_replay("test_replays/picur.SC2Replay")
        production_used = techlabreactor.production_used_till_time_for_player(420, replay.players[1], replay)
        production_capacity = techlabreactor.production_capacity_till_time_for_player(420, replay.players[1], replay)

        for structure_type, capacities in production_capacity.items():
            for time, capacity in capacities:
                used_before_times = [used for used_time, used in production_used[structure_type] if used_time <= time]
                used_at_time = used_before_times[-1] if used_before_times else 0

                self.assertGreaterEqual(capacity, used_at_time)
                self.assertGreaterEqual(capacity, 0)

        for structure_type, used_values in production_used.items():
            for time, used in used_values:
                self.assertGreaterEqual(used, 0)



