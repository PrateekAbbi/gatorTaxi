# GatorTaxi

This project was developed at the University of Florida under Professor Sartaj Sahni. The goal of this project is to efficiently manage ride bookings using Red-Black Tree (RBT) and Min-Heap data structures. The project handles ride operations such as printing ride details, inserting new rides, getting the next ride, canceling rides, and updating trip durations.

## Features

- **Efficient Ride Management:** Utilizes Red-Black Tree and Min-Heap for optimized ride booking operations.
- **Ride Operations:**
  1. `Print(rideNumber)`: Prints the triplet `(rideNumber, rideCost, tripDuration)`.
  2. `Print(rideNumber1, rideNumber2)`: Prints all triplets `(rx, rideCost, tripDuration)` where `rideNumber1 <= rx <= rideNumber2`.
  3. `Insert(rideNumber, rideCost, tripDuration)`: Inserts a new triplet, ensuring the `rideNumber` is unique.
  4. `GetNextRide()`: Outputs and deletes the ride with the lowest `rideCost` (ties broken by `tripDuration`).
  5. `CancelRide(rideNumber)`: Deletes the specified triplet from the data structures.
  6. `UpdateTrip(rideNumber, new_tripDuration)`: Updates the trip duration and manages penalties based on specified conditions.

## Data Structures

- **Min-Heap:** Stores `(rideNumber, rideCost, tripDuration)` triplets ordered by `rideCost`. Ties in `rideCost` are broken by `tripDuration`.
- **Red-Black Tree (RBT):** Stores `(rideNumber, rideCost, tripDuration)` triplets ordered by `rideNumber`.

## How It Works

- **Insertion:** New rides are inserted into both the Min-Heap and RBT.
- **Deletion:** Deleting a ride removes it from both the Min-Heap and RBT.
- **Printing:** Rides can be printed based on their `rideNumber` or within a range of ride numbers.
- **Updating Trips:** Handles trip updates with penalties for extended trip durations and automatic ride decline for excessively extended durations.

## Running the Project

### Prerequisites

- Python 3.x

### Usage

1. Clone the repository:
    ```bash
    git clone https://github.com/PrateekAbbi/gatorTaxi.git
    cd gatorTaxi
    ```

2. Prepare your input file with test cases.

3. Run the project with the input file:
    ```bash
    python <input_file_name.txt>
    ```
   Replace `<input_file_name.txt>` with the actual file name containing the test cases.

## Example

An example input file (`example_input.txt`):
