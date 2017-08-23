import unittest

import sc2reader

import techlabreactor


class TestUtil(unittest.TestCase):

    def test_structure_types(self):
        replay = sc2reader.load_replay("test_replays/random_tvp.SC2Replay")

        for player in replay.players:
            units = [
                event.unit
                for event
                in replay.events
                if (
                    event.name in ["UnitDoneEvent", "UnitBornEvent"] and
                    event.unit.owner == player and
                    techlabreactor.is_unit_produced(event.unit))]
            unit_types = set(techlabreactor.get_unit_type(unit) for unit in units)
            structure_types = list(set(techlabreactor.get_structure_type(unit_type) for unit_type in unit_types))

            self.assertNotIn("Unknown", structure_types)
