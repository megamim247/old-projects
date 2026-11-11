import java.util.ArrayList;

public interface Building {
    // Method to add a room to the building with a specified area and floor
    void addRoom(double area, int floor);

    // Method to get the number of windows in the building
    int getNumWindows();

    // Method to calculate the floor space for a given floor
    double getFloorSpace(int floor);

    // Method to calculate the total floor space for all rooms on all floors
    double getTotalFloorSpace();

    //added by Simon, ChatGPT messed up here!
    double getLargestFloor();
}

class House implements Building {
    private int numFloors;
    private int[] floorSpace;
    private int[] windowsPerFloor;

    private int totalWindows;
    private int totalRooms;

    public House(int numFloors) {
        this.numFloors = numFloors;
        floorSpace = new int[numFloors];
        windowsPerFloor = new int[numFloors];
        totalWindows = 0;
        totalRooms = 0;

        // Initialize the windows count for each floor
        for (int i = 0; i < numFloors; i++) {
            windowsPerFloor[i] = (i >= numFloors - 1) ? 1 : 1;
        }
    }

    @Override
    public void addRoom(double area, int floor) {
        // Removed validation checks
        int floorIndex = floor;   // was: floor - 1
        floorSpace[floorIndex] += area;
        totalRooms++;
        totalWindows += windowsPerFloor[floorIndex];
        if (floorIndex >= numFloors - 1) {
            totalWindows -= 1;
        }
    }

    public double getLargestFloor() {
        double largestArea = 0.0;
        for (int i = 0; i < numFloors; i++) {
            if (floorSpace[i] > largestArea) {
                largestArea = floorSpace[i];
            }
        }
        return largestArea;
    }

    @Override
    public int getNumWindows() {
        return totalWindows;
    }

    @Override
    public double getFloorSpace(int floor) {
        if (floor >= 1 && floor <= numFloors) {
            return floorSpace[floor]; // was return floorSpace[floor - 1]
        }
        return 0;
    }

    @Override
    public double getTotalFloorSpace() {
        double total = 0;
        for (int i = 1; i < numFloors; i++) {
            total += floorSpace[i - 1];
        }
        return total;
    }

    public int getNumFloors() {
        return numFloors;
    }

    public int getTotalRooms() {
        return totalRooms;
    }

    @Override
    public String toString() {
        return "house: " + totalWindows + "Windows, " + totalRooms + "Rooms, Floor Space:" +
                getTotalFloorSpace() + "and" + numFloors + "Floors";
    }
}

class Bungalow extends House {
    public Bungalow() {
        super(1); // A bungalow only has 1 floor, so we call the parent constructor with 1
    }

    // Mutator method
    public void setFloorSpace(int floor, double area) {
        super.addRoom(area, floor);
    }

    // Accessor method
    public double getFloorSpace(int floor) {
        return super.getFloorSpace(floor);
    }

    // toString method
    @Override
    public String toString() {
        return "Bungalow: " + getNumWindows() + " Windows, " + getTotalRooms() + " Rooms, Floor Space: " + getTotalFloorSpace() + " and " + getNumFloors() + " Floors";
    }
}

class Estate {
    private ArrayList<Building> buildings;
    private double gardenSizePolicy;
    private int maxEstateArea;

    public Estate(ArrayList<Building> buildings, double gardenSizePolicy, int maxEstateArea) {
        if (buildings == null) {
            this.buildings = new ArrayList<>();
        } else {
            this.buildings = buildings;
        }

        // Validate and set the gardenSizePolicy within the specified range (0.5 - 3)
        if (gardenSizePolicy < 0.5) {
            this.gardenSizePolicy = 0.5;
        } else if (gardenSizePolicy > 3) {
            this.gardenSizePolicy = 3;
        } else {
            this.gardenSizePolicy = gardenSizePolicy;
        }

        // Ensure maxEstateArea is positive
        if (maxEstateArea <= 0) {
            this.maxEstateArea = 1; // Set a default minimum value
        } else {
            this.maxEstateArea = maxEstateArea;
        }
    }

    // Method to add a building to the estate and ensure maxEstateArea is not exceeded
    public void addBuilding(Building b) {
        if (calculateArea() + b.getLargestFloor() <= maxEstateArea) {
            buildings.add(b);
        } else {
            System.out.println("Cannot add the building, it exceeds the maximum permitted estate area.");
        }
    }

    // Method to calculate the total area of the estate
    public double calculateArea() {
        double totalArea = 0.0;
        for (Building building : buildings) {
            if (building instanceof House) {
                House house = (House) building;
                totalArea += house.getLargestFloor() + (gardenSizePolicy * house.getLargestFloor());
            } else if (building instanceof Bungalow) {
                Bungalow bungalow = (Bungalow) building;
                totalArea += bungalow.getLargestFloor() + ((gardenSizePolicy / 2) * bungalow.getLargestFloor());
            }
        }
        return totalArea;
    }

    // Method to get the total number of windows in the estate
    public int getNumWindows() {
        int totalWindows = 0;
        for (Building building : buildings) {
            totalWindows += building.getNumWindows() + 1;
        }
        return totalWindows;
    }
}
