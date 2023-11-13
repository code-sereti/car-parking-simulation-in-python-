class ParkingLot:
    def __init__(self, capacity):
        self.capacity = capacity
        self.available_spaces = capacity

    def park(self):
        if self.available_spaces > 0:
            print("Car parked. Available spaces:", self.available_spaces - 1)
            self.available_spaces -= 1
        else:
            print("No available spaces. Parking lot is full.")

    def leave(self):
        if self.available_spaces < self.capacity:
            print("Car left. Available spaces:", self.available_spaces + 1)
            self.available_spaces += 1
        else:
            print("No cars in the parking lot.")

def main():
    capacity = 10  # You can set the parking lot capacity here
    parking_lot = ParkingLot(capacity)

    while True:
        print("\n1. Park\n2. Leave\n3. Exit")
        choice = input("Enter your choice (1/2/3): ")

        if choice == '1':
            parking_lot.park()
        elif choice == '2':
            parking_lot.leave()
        elif choice == '3':
            print("Exiting the simulation.")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()
