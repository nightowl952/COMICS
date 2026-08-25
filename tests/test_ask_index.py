import json
import os
import unittest


ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


class AskIndexTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with open(os.path.join(ROOT, "ask-index.json"), encoding="utf-8") as handle:
            cls.data = json.load(handle)

    def test_expected_collection_shape(self):
        self.assertEqual(1, self.data["schema_version"])
        self.assertEqual(15, len(self.data["shelves"]))
        self.assertEqual(192, sum(len(shelf["volumes"]) for shelf in self.data["shelves"]))

    def test_volume_ids_routes_and_covers_are_valid(self):
        seen = set()
        for shelf in self.data["shelves"]:
            self.assertTrue(os.path.isfile(os.path.join(ROOT, shelf["tracker"])))
            ids = {volume["id"] for volume in shelf["volumes"]}
            for volume in shelf["volumes"]:
                key = shelf["id"], volume["id"]
                self.assertNotIn(key, seen)
                seen.add(key)
                self.assertTrue(os.path.isfile(os.path.join(ROOT, volume["cover"])), key)
                self.assertGreater(volume["issue_count"], 0, key)
                self.assertTrue(volume["chapters"], key)
                self.assertNotRegex(json.dumps(volume), r"</?(?:b|i|em|strong|br)\b")
            for mode in shelf["tone_modes"]:
                self.assertTrue(set(mode["volume_ids"]).issubset(ids), (shelf["id"], mode["label"]))

    def test_every_shelf_has_an_on_demand_tour(self):
        for shelf in self.data["shelves"]:
            path = os.path.join(ROOT, "ask-tours", shelf["id"] + ".json")
            self.assertTrue(os.path.isfile(path), shelf["id"])
            with open(path, encoding="utf-8") as handle:
                tour = json.load(handle)
            self.assertTrue(tour.get("overview"), shelf["id"])
            self.assertEqual(
                {volume["id"] for volume in shelf["volumes"]},
                set((tour.get("volumes") or {}).keys()),
                shelf["id"],
            )


if __name__ == "__main__":
    unittest.main()
