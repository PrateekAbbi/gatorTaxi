from rbt import RedBlackTree
from minHeap import MinHeap

import sys
import re

rbt = RedBlackTree()
mH = MinHeap()

inputFileName = sys.argv[-1]+".txt"
outputFileName = input("Write Outputs into: ")+".txt"

input = open(inputFileName, "r")
output = open(outputFileName, "w")

for operation in input:
    rideDetails = re.findall('\((.*?)\)', operation)

    if "Insert" in operation:
        rideNumber, rideCost, tripDuration = [int(rideDetail) if rideDetail.isdigit(
        ) else rideDetail for rideDetail in rideDetails[0].split(',')]
        newRide = rbt.Insert(rideNumber, rideCost, tripDuration)

        if newRide == "Duplicate RideNumber":
            output.write(newRide+"\n")
            break
        else:
            mH.Insert(rideNumber, rideCost, tripDuration, newRide[0])

    elif "GetNextRide" in operation:
        nextRide = mH.GetNextRide()
        if nextRide:
            rbt.CancelRide(nextRide[0])
            output.write(str((nextRide[0], nextRide[1], nextRide[2]))+"\n")
        else:
            output.write("No active ride requests\n")

    elif "UpdateTrip" in operation:
        rideNumber, new_tripDuration = [int(rideDetail) if rideDetail.isdigit(
        ) else rideDetail for rideDetail in rideDetails[0].split(',')]
        updatedRide = rbt.search(rideNumber)
        mH.UpdateTrip(updatedRide, new_tripDuration)
        rbt.UpdateTrip(updatedRide, new_tripDuration)

    elif "CancelRide" in operation:
        rideNumber = int(rideDetails[0])
        ride = rbt.search(rideNumber)
        if ride != rbt.NIL:
            mH.CancelRide(ride)
            rbt.CancelRide(rideNumber)

    elif "Print" in operation:
        rideNumbers = [int(rideDetail) if rideDetail.isdigit(
        ) else rideDetail for rideDetail in rideDetails[0].split(',')]

        if len(rideNumbers) == 1:
            ride = rbt.search(rideNumbers[0])
            if (ride == rbt.NIL):
                output.write("(0, 0, 0)\n")
            else:
                output.write(
                    str((ride.rideDetails[0], ride.rideDetails[1], ride.rideDetails[2])) + "\n")
        else:
            rides = rbt.Print(rideNumbers[0], rideNumbers[1])
            if len(rides) == 0:
                output.write("(0, 0, 0)\n")
            else:
                output.write(",".join(str(ride) for ride in rides)+"\n")


input.close()
output.close()


# output1 = open("output.txt", "r")

# for line in output1:
#     print(line)

# output1.close()
