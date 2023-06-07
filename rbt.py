class Node:
    def __init__(self, rideDetails):
        self.rideDetails = rideDetails
        self.color = 'Red'
        self.parent = None
        self.left = None
        self.right = None


class RedBlackTree:
    def __init__(self):
        self.NIL = Node(0)
        self.NIL.color = 'Black'
        self.root = self.NIL

    def rotateLeft(self, node):
        y = node.right
        node.right = y.left

        if y.left != self.NIL:
            y.left.parent = node
        y.parent = node.parent

        if node.parent == self.NIL:  # node is root node
            self.root = y
        elif node == node.parent.left:  # node is left child node
            node.parent.left = y
        else:  # node is right child node
            node.parent.right = y
        y.left = node
        node.parent = y

    def rotateRight(self, node):
        y = node.left
        node.left = y.right

        if y.right != self.NIL:
            y.right.parent = node
        y.parent = node.parent

        if node.parent == self.NIL:  # node is root node
            self.root = y
        elif node == node.parent.right:  # node is right child node
            node.parent.right = y
        else:  # node is left child node
            node.parent.left = y
        y.right = node
        node.parent = y

    # For insertion into the red-black tree.
    def Insert(self, rideNumber, rideCost, tripDuration):
        rideDetails = [rideNumber, rideCost, tripDuration]

        ride = self.search(rideNumber)
        if ride != self.NIL:
            return "Duplicate RideNumber"

        newRide = Node(rideDetails)
        # newRide.parent = None
        newRide.left = self.NIL
        newRide.right = self.NIL
        # newRide.color = "Red"

        y = self.NIL
        temp = self.root
        while temp != self.NIL:
            y = temp
            if rideNumber < temp.rideDetails[0]:
                temp = temp.left
            else:
                temp = temp.right

        newRide.parent = y

        if y == self.NIL:
            self.root = newRide
        elif rideNumber < y.rideDetails[0]:
            y.left = newRide
        else:
            y.right = newRide

        self.fixInsert(newRide)
        return [newRide, newRide.rideDetails]

    # to maintain the properties of red-black tree
    def fixInsert(self, newRide):
        while newRide.parent.color == "Red":
            # Case 1: if parent of newly inserted node is right child of its parent
            if newRide.parent == newRide.parent.parent.right:
                # left child of newly inserted node's grandparent is uncle of newly inserted node.
                uncle = newRide.parent.parent.left
                if uncle.color == "Red":
                    uncle.color = "Black"
                    newRide.parent.color = "Black"
                    newRide.parent.parent.color = "Red"
                    newRide = newRide.parent.parent
                else:
                    if newRide == newRide.parent.left:
                        newRide = newRide.parent
                        self.rotateRight(newRide)
                    newRide.parent.color = "Black"
                    newRide.parent.parent.color = "Red"
                    self.rotateLeft(newRide.parent.parent)
            else:
                # right child of newly inserted node's grandparent is uncle of newly inserted node.
                uncle = newRide.parent.parent.right
                if uncle.color == "Red":
                    uncle.color = "Black"
                    newRide.parent.color = "Black"
                    newRide.parent.parent.color = "Red"
                    newRide = newRide.parent.parent
                else:
                    if newRide == newRide.parent.right:
                        newRide = newRide.parent
                        self.rotateLeft(newRide)
                    newRide.parent.color = "Black"
                    newRide.parent.parent.color = "Red"
                    self.rotateRight(newRide.parent.parent)

        self.root.color = "Black"

    # to delete the node from the tree
    def CancelRide(self, rideNumber):
        ride = self.search(rideNumber)

        if ride == self.NIL:
            return

        y = ride
        rideOriginalColor = y.color

        if ride.left == self.NIL:
            x = ride.right
            self.swap(ride, ride.right)
        elif ride.right == self.NIL:
            x = ride.left
            self.swap(ride, ride.left)
        else:
            y = self.minimum(ride.right)
            rideOriginalColor = y.color
            x = y.right

            if y.parent == ride:
                x.parent = y
            else:
                self.swap(y, y.right)
                y.right = ride.right
                y.right.parent = y

            self.swap(ride, y)
            y.left = ride.left
            y.left.parent = y
            y.color = ride.color

        if rideOriginalColor == "Black":
            self.fixCancellation(x)

    # to maintain the properties of red-black tree
    def fixCancellation(self, ride):
        while ride != self.root and ride.color == "Black":
            if ride == ride.parent.left:
                v = ride.parent.right

                if v.color == "Red":
                    v.color = "Black"
                    ride.parent.color = "Red"
                    self.rotateLeft(ride.parent)
                    v = ride.parent.right

                if v.left.color == "Black" and v.right.color == "Black":
                    v.color = "Red"
                    ride = ride.parent

                else:
                    if v.right.color == "Black":
                        v.left.color = "Black"
                        v.color = "Red"
                        self.rotateRight(v)
                        v = ride.parent.right

                    v.color = ride.parent.color
                    ride.parent.color = "Black"
                    v.right.color = "Black"
                    self.rotateLeft(ride.parent)
                    ride = self.root

            else:
                v = ride.parent.left

                if v.color == "Red":
                    v.color = "Black"
                    ride.parent.color = "Red"
                    self.rotateRight(ride.parent)
                    v = ride.parent.left

                if v.right.color == "Black" and v.left.color == "Black":
                    v.color = "Red"
                    ride = ride.parent
                else:
                    if v.left.color == "Black":
                        v.right.color = "Black"
                        v.color = "Red"
                        self.rotateLeft(v)
                        v = ride.parent.left

                    v.color = ride.parent.color
                    ride.parent.color = "Black"
                    v.left.color = "Black"
                    self.rotateRight(ride.parent)
                    ride = self.root

        ride.color = "Black"

    def swap(self, u, v):
        if u.parent == self.NIL:
            self.root = v
        elif u == u.parent.left:
            u.parent.left = v
        else:
            u.parent.right = v
        v.parent = u.parent

    # to update the details of the trip
    def UpdateTrip(self, updatedNode, new_tripDuration):
        if new_tripDuration <= updatedNode.rideDetails[2]:
            updatedNode.rideDetails[2] = new_tripDuration
        elif updatedNode.rideDetails[2] <= new_tripDuration <= 2*updatedNode.rideDetails[2]:
            updatedNode.rideDetails[1] = updatedNode.rideDetails[1] + 10
            updatedNode.rideDetails[2] = new_tripDuration
        elif new_tripDuration > 2*updatedNode.rideDetails[2]:
            self.CancelRide(updatedNode.rideDetails[0])

    # to search the trip through ride number.
    def search(self, rideNumber):
        node = self.root
        print(node, node.rideDetails)
        while node != self.NIL and rideNumber != node.rideDetails[0]:
            if rideNumber < node.rideDetails[0]:
                node = node.left
            else:
                node = node.right
        return node

    def Print(self, rideNumber1, rideNumber2):
        rides = []
        self.printRides(rides, self.root, rideNumber1, rideNumber2)
        return rides

    def printRides(self, rides, ride, rideNumber1, rideNumber2):
        if ride != self.NIL:
            if ride.rideDetails[0] < rideNumber1:
                self.printRides(rides, ride.right, rideNumber1, rideNumber2)
            elif ride.rideDetails[0] > rideNumber2:
                self.printRides(rides, ride.left, rideNumber1, rideNumber2)
            else:
                self.printRides(rides, ride.left, rideNumber1, rideNumber2)
                if ride.rideDetails[0] >= rideNumber1 and ride.rideDetails[0] <= rideNumber2:
                    rides.append(ride.rideDetails)
                self.printRides(rides, ride.right, rideNumber1, rideNumber2)

    def minimum(self, x):
        while x.left != self.NIL:
            x = x.left
        return x
