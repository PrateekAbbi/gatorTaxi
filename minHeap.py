class MinHeap:

    def __init__(self) -> None:
        self.size = 0
        self.Heap = []
        self.indexMap = {}

    # to get the index of the triplet inside the heap array @ line 5
    def getIndex(self, rideNumber):
        # i is the index of the triplet of the Heap array @ line 5 and j is the triplet itself.
        for i, j in enumerate(self.Heap):
            if rideNumber == j[0]:
                return i
        return -1  # -1 indicates that triplet is not found

    # For insertion into the Heap
    def Insert(self, rideNumber, rideCost, tripDuration, redBlackNode):
        self.Heap.append([rideNumber, rideCost, tripDuration, redBlackNode])
        numberOfRides = len(self.Heap) - 1
        self.indexMap[redBlackNode] = numberOfRides
        self.upHeap(numberOfRides)
        return

    # To update ride details
    def UpdateTrip(self, updatedNode, new_tripDuration):
        index = self.indexMap[updatedNode]

        if new_tripDuration <= self.Heap[index][2]:
            self.Heap[index][2] = new_tripDuration
            self.upHeap(index)
            updatedRideIndex = self.indexMap[updatedNode]
            self.downHeap(updatedRideIndex)

        elif self.Heap[index][2] < new_tripDuration <= 2*self.Heap[index][2]:
            self.Heap[index][1] = self.Heap[index][1] + 10
            self.Heap[index][2] = new_tripDuration
            self.upHeap(index)
            updatedRide = self.indexMap[updatedNode]
            self.downHeap(updatedRide)

        elif new_tripDuration > 2*self.Heap[index][2]:
            self.CancelRide(updatedNode)

    # To cancel the trip
    def CancelRide(self, ride):
        index = self.indexMap[ride]

        if index != -1:
            if index == len(self.Heap) - 1:
                del self.indexMap[self.Heap[index][3]]
                self.Heap.pop()
            else:
                self.indexMap[self.Heap[-1][3]
                              ] = self.indexMap[self.Heap[index][3]]
                del self.indexMap[self.Heap[index][3]]
                self.Heap[index] = self.Heap.pop()
                self.downHeap(index)

    # To retrieve the next ride
    def GetNextRide(self):
        if len(self.Heap) == 1:
            del self.indexMap[self.Heap[-1][3]]
            ans = self.Heap.pop()
        elif len(self.Heap) == 0:
            return
        else:
            ans = self.Heap[0]
            del self.indexMap[self.Heap[0][3]]
            self.indexMap[self.Heap[-1][3]] = 0
            self.Heap[0] = self.Heap.pop()
            self.downHeap(0)
        return ans

    def upHeap(self, index):
        if index > 0 and (self.Heap[index][1] < self.Heap[(index-1)//2][1] or (self.Heap[index][1] == self.Heap[(index-1)//2][1] and self.Heap[index][2] < self.Heap[(index-1)//2][2])):
            self.indexMap[self.Heap[index][3]
                          ] = (index-1)//2
            self.indexMap[self.Heap[(index-1)//2][3]] = index
            self.Heap[index], self.Heap[(
                index-1)//2] = self.Heap[(index-1)//2], self.Heap[index]
            self.upHeap((index-1)//2)
        return

    def downHeap(self, index):
        l = 2*index+1
        r = 2*index+2
        largest = index
        if l < len(self.Heap) and ((self.Heap[l][1] < self.Heap[largest][1]) or (self.Heap[l][1] == self.Heap[largest][1] and self.Heap[l][2] < self.Heap[largest][2])):
            largest = l
        if r < len(self.Heap) and ((self.Heap[r][1] < self.Heap[largest][1]) or (self.Heap[r][1] == self.Heap[largest][1] and self.Heap[r][2] < self.Heap[largest][2])):
            largest = r
        if largest != index:
            self.indexMap[self.Heap[index][3]
                          ] = largest
            self.indexMap[self.Heap[largest][3]] = index
            self.Heap[index], self.Heap[largest] = self.Heap[largest], self.Heap[index]
            self.downHeap(largest)
        return
