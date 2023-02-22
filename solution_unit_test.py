import unittest
from ali_solution import *


class MyTestCase(unittest.TestCase):

    @classmethod
    def setUp(cls):
        cls.puck_library = PuckLibrary()
        cls.puck_library.populate_parking_spots()
        cls.puck_library.populate_pucks()

    def test_one(self):
        """Test that the number of pucks is between 1 and 9 inclusive."""
        self.assertTrue(9 >= len(self.puck_library.get_current_pucks()) >= 1)

    def test_two(self):
        """Test that the pucks array was populated."""
        self.assertTrue(len(self.puck_library.get_current_pucks()) != 0)

    def test_three(self):
        """Test that only 9 parking spots were populated."""
        self.assertTrue(len(self.puck_library.get_valid_parking_spots()), 9)

    def test_four(self):
        """Test to see if a Puck at (0,0) gets appropriately aligned with the (180,60) parking spot."""
        puck = self.puck_library.get_current_pucks()[0]
        puck.set_x_coordinate(0)
        puck.set_y_coordinate(0)
        self.assertTrue((180, 60), self.puck_library.calculate_closest_parking_spot(puck))

    def test_five(self):
        """Test to see if a Puck at (420,180) gets appropriately aligned with the parking spot at (420,180)."""
        puck = self.puck_library.get_current_pucks()[0]
        puck.set_x_coordinate(420)
        puck.set_y_coordinate(180)
        self.assertTrue((420, 180), self.puck_library.calculate_closest_parking_spot(puck))

    def test_six(self):
        """Test that none of the Pucks were created at a position outside of the 480mmx480mm grid."""
        flag = False

        for puck in self.puck_library.get_current_pucks():
            if puck.get_x_coordinate() > 480 or puck.get_y_coordinate() > 480:
                flag = True

        self.assertFalse(flag, True)

    def test_seven(self):
        """Test that a puck is assigned to a parking spot appropriately."""
        puck = Puck()
        puck.set_x_coordinate(300)
        puck.set_y_coordinate(60)
        self.puck_library.calculate_closest_parking_spot(puck)
        self.assertEqual((300, 60), (puck.get_x_coordinate(), puck.get_y_coordinate()))

    def test_eight(self):
        """Test that when a puck is assigned to a parking spot and the closest is occupied,
        that the next closest parking spot is occupied now."""
        puck = Puck()
        puck.set_x_coordinate(419)
        puck.set_y_coordinate(179)
        self.puck_library.calculate_closest_parking_spot(puck)
        self.assertEqual((420, 180), (puck.get_x_coordinate(), puck.get_y_coordinate()))

    def test_nine(self):
        """Test that when there are gaps in the puck orientation and we deal with it, there are no longer gaps."""
        if self.puck_library.check_gaps():
            self.puck_library.fill_gaps()
            self.assertFalse(self.puck_library.check_gaps())

    def test_ten(self):
        """Test that when we perform our work, all pucks have been worked on."""
        if self.puck_library.check_gaps():
            self.puck_library.fill_gaps()

        self.puck_library.move_and_perform_work()
        test_length = len(self.puck_library.get_current_pucks())

        count = 0
        for puck in self.puck_library.get_current_pucks():
            if puck.get_work_complete_status():
                count += 1

        self.assertEqual(test_length, count)

    def test_eleven(self):
        """Test that when we perform our work and all pucks have been worked on, they are in their original spots."""

        puck_original_state = []
        for puck in self.puck_library.pucks:
            self.puck_library.calculate_closest_parking_spot(puck)
            puck_original_state.append((puck.get_x_coordinate(), puck.get_y_coordinate()))

        self.puck_library.check_gaps()

        self.puck_library.fill_gaps()

        self.puck_library.move_and_perform_work()

        puck_final_state = []
        for puck in self.puck_library.pucks:
            puck_final_state.append((puck.get_x_coordinate(), puck.get_y_coordinate()))

        self.assertCountEqual(puck_original_state, puck_final_state)


if __name__ == '__main__':
    unittest.main()
