# Author: Ali Alameedi

# Description: Refined implementation of puck-pathway grid exercise that utilizes classes, modularized methods,
#              and mathematical computations to perform work on a set of randomly generated pucks. Each puck is randomly
#              assigned to any position on the grid, then mathematical computations are made relative to each parking
#              spot to determine which parking spot it is close to. Thereafter, any gaps between pucks are handled. The
#              program then takes the head puck of the path, pops it, and moves it to the end of the queue after doing
#              work on it. The program successfully ends when all pucks have been worked on and they return to their
#              original position.

# Logic Flow:
# 1) A random number of pucks (1 - 9 inclusive range) are generated.
# 2) For each of the pucks generated, we attribute a random location anywhere on the entire 4x4 board.
# 3) Once each puck has its' random location, we assign it to the closest unoccupied parking spot.
# 4) Once all pucks have been assigned parking spots, we check for gaps.
# 5) If gaps are present, gaps are handled by moving all pucks forward in the queue as far as able.
# 6) If no gaps are present or have been dealt with, we pop the head puck (the one @ location 420,300), do work on it,
# and move the other pucks forward in location asynchronously. Meaning the work of the head puck and movement of pucks
# happen independent of one another (ie: at the same time).
# 7) Once the work is complete and remaining pucks are moved forward, the head puck is moved to the tail.
# 8) Once all pucks have been worked on & return to their original location, the program is successfully complete.


import math
import random


class Puck:
    """
    This class is an object representation of the Puck object from the problem statement. It contains the x-coordinate
    y-coordinate, and work_complete status flag for any instance of the object. Each data attribute has getter and
    setter methods to retrieve it from external to the class.

    x_coordinate - int
    y_coordinate - int
    work_complete - boolean
    """

    def __init__(self):
        self.x_coordinate = 0
        self.y_coordinate = 0
        self.work_complete = False

    def get_x_coordinate(self):
        return self.x_coordinate

    def set_x_coordinate(self, x_coordinate):
        self.x_coordinate = x_coordinate

    def get_y_coordinate(self):
        return self.y_coordinate

    def set_y_coordinate(self, y_coordinate):
        self.y_coordinate = y_coordinate

    def get_work_complete_status(self):
        return self.work_complete

    def set_work_complete_status(self):
        if not self.work_complete:
            self.work_complete = True

        return


class ParkingSpot:
    """
    This class is an object representation of the ParkingSpot object from the problem statement. It contains the
    x-coordinate, y-coordinate, and occupied status flag for any instance of the object. Each data attribute has
    getter and setter methods to retrieve it from external to the class.

    x_coordinate - int
    y_coordinate - int
    occupied - boolean
    """

    def __init__(self, x_coordinate, y_coordinate):
        self.x_coordinate = x_coordinate
        self.y_coordinate = y_coordinate
        self.occupied = False

    def get_x_coordinate(self):
        return self.x_coordinate

    def get_y_coordinate(self):
        return self.y_coordinate

    def get_occupied_status(self):
        return self.occupied

    def set_occupied_status(self):
        if not self.occupied:
            self.occupied = True

        elif self.occupied:
            self.occupied = False

        return


class PuckLibrary:
    """
    This class holds lists of parking spot and puck objects for data representation of the problem statement. The class
    populates both lists appropriately with their respective object (parking_spots: ParkingSpot, pucks: Puck) and
    provides methods for getting these attributes. The class is also a library that provides methods to calculate the
    Euclidean distance between points (to find the closest parking spot for a puck), do work on or move a puck, and
    check and fill gaps appropriately.

    parking_spots: List<ParkingSpot>
    pucks: List<Pucks>
    """

    def __init__(self):

        self.parking_spots = []  # start of array is tail of the path; end of array is head of the path.

        self.pucks = []

    def get_valid_parking_spots(self):
        return self.parking_spots

    def get_current_pucks(self):
        return self.pucks

    def populate_pucks(self):
        """
        This method randomly generates x & y coordinates for a random number of pucks and appends them to our
        internal list.

        Time Complexity: O(1), Space complexity: O(1)
        Explanation: Range is defined, # of pucks will never surpass 9 or grow with input size of program (as is).
        """
        for puck in range(random.randint(1, 9)):
            new_puck = Puck()
            new_puck.set_x_coordinate(random.randint(0, 480))
            new_puck.set_y_coordinate(random.randint(0, 480))
            self.pucks.append(new_puck)

        print("List of populated original pucks:", self.pucks)
        print("# of pucks:", len(self.pucks), "\n")
        return

    def populate_parking_spots(self):
        """
        This method generates our list of Parking Spots as objects and appends them to our internal Parking Spot list.

        Time Complexity: O(1), Space complexity: O(1)
        Explanation: # of parking spots remains 9. Space uptake will not grow with input size of program (as is).

        """
        for ps in [[180, 60], [300, 60], [420, 60], [420, 180], [300, 180], [180, 180],
                   [180, 300], [300, 300], [420, 300]]:
            ps_obj = ParkingSpot(ps[0], ps[1])
            self.parking_spots.append(ps_obj)

        print("List of parking spots:", self.parking_spots)
        print("# of parking spots:", len(self.parking_spots), "\n")
        return

    def do_work(self, puck_object):
        """
        This method takes in a puck instance and performs work on it.

        Time Complexity: O(1)
        Explanation: Work function checks and sets a boolean. Operation is constant time.
        """
        puck_object.set_work_complete_status()
        print("Work is being processed on this puck!")
        return

    def move_puck(self, puck_object, parking_spot):
        """
        This method takes in a puck instance and parking spot position, then moves the puck to that position and sets
        the occupied state of that parking spot to occupied.

        Time Complexity: O(1)
        Explanation: Move function uses set operations that are constant time.

        """
        puck_object.set_x_coordinate(parking_spot.get_x_coordinate())
        puck_object.set_y_coordinate(parking_spot.get_y_coordinate())
        parking_spot.set_occupied_status()
        return

    def calculate_closest_parking_spot(self, puck_object):
        """
        This method takes in a puck instance and calculates the Euclidean distance between the pucks' current position
        and all parking spots to determine the closest available parking spot to it (ie: not occupied and closest).

        Time Complexity: O(1), Space Complexity: O(1)
        Explanation: Move function uses set operations that are constant time.

        """

        # find parking spot that has minimum distance from current puck position
        min_dist = float("inf")
        min_parking_spot = float("inf")
        for parking_spot in self.parking_spots:
            distance = math.dist([parking_spot.get_x_coordinate(), parking_spot.get_y_coordinate()],
                                 [puck_object.get_x_coordinate(), puck_object.get_y_coordinate()])

            if distance < min_dist and not parking_spot.get_occupied_status():
                min_dist = distance
                min_parking_spot = parking_spot

        # this print statement will give us the original randomized location of the pucks and show us the nearest spot
        # assigned to it.

        print("Original Location:", (puck_object.get_x_coordinate(), puck_object.get_y_coordinate()), "Nearest Spot:",
              (min_parking_spot.get_x_coordinate(), min_parking_spot.get_y_coordinate()))

        # move puck to nearest spot
        self.move_puck(puck_object, min_parking_spot)

        # this print statement shows that the puck has now been assigned to the parking spot.
        print("New Location:", (puck_object.get_x_coordinate(), puck_object.get_y_coordinate()))
        return

    def check_gaps(self):
        """
        This method checks to see if our pucks have gaps between them. If so, we return True. If not, we return False.

        Time Complexity: Single for loops are generally O(N), however, this may actually be O(1).

        Explanation: We are looping through a list of parking spots. However, the number of parking spots will always
        be 9, so this may be O(1) on the understanding that time complexity is really about scalability and growth of
        our algorithm. Getter method is O(1).
        """

        # if we encounter a puck and then an empty parking spot, we know there's a gap.
        flag = False
        for val in self.parking_spots:
            if val.get_occupied_status():
                flag = True

            if flag and (not val.get_occupied_status()):
                return True

        return False

    def fill_gaps(self):
        """
        If there are gaps between our pucks, we fill those gaps by moving all pucks forward as far as possible.

        Time Complexity: O(N), Space Complexity: O(N)
        Explanation: At most, we loop through a array at some points in the method. There are no nested for loops. We
        also store statuses or the new puck orientations in an array based on the original array size we're looking at,
        so any additional storage would be based on the number of pucks or parking spots accordingly.
        """
        gap_fill_flag = self.check_gaps()

        if gap_fill_flag:

            # get occupied state of each parking spot - easier to read and look at for printing & debugging purposes
            occupied_state = []
            for ps in self.parking_spots:
                occupied_state.append(ps.get_occupied_status())

            print("Status of all occupied spots:", occupied_state, "\n")

            # how many spots are occupied
            occupied_frequency = occupied_state.count(True)
            print("Frequency of occupied spots:", occupied_frequency, "\n")

            # new array used to reorient all pucks to right-align to end of path and fill gaps
            adjusted_gap_array = [False for _ in range(len(self.parking_spots))]
            print("New potential adjustments array: ", adjusted_gap_array, "\n")

            # loop backwards in the array (head of the path) and fill until there are no pucks left
            for idx in range(len(adjusted_gap_array) - 1, -1, -1):
                if occupied_frequency >= 1:
                    adjusted_gap_array[idx] = True
                    occupied_frequency -= 1

            print("Removing gaps between pucks & end of path:", adjusted_gap_array, "\n")

            # update every parking spot to appropriate occupied status
            for idx in range(len(self.parking_spots)):
                if adjusted_gap_array[idx]:
                    if not self.parking_spots[idx].get_occupied_status():
                        self.parking_spots[idx].set_occupied_status()

                elif not adjusted_gap_array[idx]:
                    if self.parking_spots[idx].get_occupied_status():
                        self.parking_spots[idx].set_occupied_status()

            # verify all parking spots are appropriately marked as occupied or not
            print("New list of occupied states of parking spots:")
            for val in self.parking_spots:
                print(val.get_occupied_status())

            print()

            # set the coordinates of each puck to their appropriate parking spot
            tracker = 0
            for idx in range(len(self.parking_spots)):
                parking_spot = self.parking_spots[idx]
                if parking_spot.get_occupied_status():
                    self.pucks[tracker].set_x_coordinate(parking_spot.get_x_coordinate())
                    self.pucks[tracker].set_y_coordinate(parking_spot.get_y_coordinate())
                    tracker += 1

            # check the parking spots that are occupied & their coordinates to verify proper gap fill.
            for val in self.parking_spots:
                if val.get_occupied_status():
                    print("Occupied Parking Spot Coordinates:", (val.get_x_coordinate(), val.get_y_coordinate()))

            print()

            # check the pucks to ensure that their coordinates align with proper parking spots that are occupied
            for val in self.pucks:
                print("Pucks Coordinates:", (val.get_x_coordinate(), val.get_y_coordinate()))

            print()

        return

    def rotate(self, arr, n):
        """
        This method serves as the abstraction to moving the head puck to the tail of the path once processed. This will
        rotate the array by one index every iteration it is called (ie: the end of the array will move to the front
        and all other array members will move forward in the array by one).

        Time Complexity: O(N)
        Explanation: This function takes an array of 'n' length and loops through it. Length is subjective on our use.

        """

        # rotate array by one (end of array goes to start of array)
        x = arr[n - 1]

        for i in range(n - 1, 0, -1):
            arr[i] = arr[i - 1]

        arr[0] = x

        return

    def move_and_perform_work(self):
        """
        This method does work on the head puck, sets its' work status to complete, then rotates the array until all
        pucks have been worked on and they are back in their original positions.

        Time Complexity: O(N * N)
        Explanation: We have 'n # of pucks iterations and we rotate 'n' number of times to
        process all pucks. Each puck will result in us rotating the entire array, thus, I propose this is O(n^2).
        However, there is discussion to be had about the complexity being O(n) due to the fact that the number of
        iterations is always finite and constant. At most, it will be 9 pucks, and this will never scale,
        unless we change the number of pucks we have to work with.
        """
        iterations = len(self.pucks)

        # rotate through all pucks & do work on them, set their work status as True (complete).
        while iterations != 0:
            head_puck = self.pucks[-1]
            self.do_work(head_puck)
            head_puck.set_work_complete_status()
            iterations -= 1
            self.rotate(self.pucks, len(self.pucks))

        print()

        # display the order of pucks & their work complete status
        for val in self.pucks:
            print("Final Order of Pucks", (val.get_x_coordinate(), val.get_y_coordinate()), "||",
                  "Work Complete Status:", val.get_work_complete_status())

        return


if __name__ == '__main__':
    puck_library = PuckLibrary()
    puck_library.populate_pucks()
    puck_library.populate_parking_spots()
    for val in puck_library.pucks:
        puck_library.calculate_closest_parking_spot(val)

    print()
    print("Occupied status of parking spots after initial populating of pucks & assigning to closest parking"
          " spots:")

    for val in puck_library.parking_spots:
        print((val.get_x_coordinate(), val.get_y_coordinate()), "||", val.get_occupied_status())

    print()
    print("There are gaps:", puck_library.check_gaps(), "\n")

    puck_library.fill_gaps()

    puck_library.move_and_perform_work()
