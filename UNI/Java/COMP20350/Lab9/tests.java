import static org.junit.jupiter.api.Assertions.*;

import org.junit.jupiter.api.Test;

class tests {

    private static final double DELTA = 1e-9;
    private static final Class<? extends Exception> REJECTED = IllegalArgumentException.class;

    private static House house(double floor0, double floor1) {
        House h = new House(2);
        h.addRoom(floor0, 0);
        h.addRoom(floor1, 1);
        return h;
    }

    private static Bungalow bungalow(double... areas) {
        Bungalow b = new Bungalow();
        for (double a : areas) {
            b.addRoom(a, 0);
        }
        return b;
    }

    private House threeRoomHouse() {
        House h = new House(2);
        h.addRoom(20, 0);
        h.addRoom(10, 0);
        h.addRoom(25, 1);
        return h;
    }

    @Test
    void houseWindows() {
        assertEquals(7, threeRoomHouse().getNumWindows()); 
    }

    @Test
    void houseFloorSpace() {
        House h = threeRoomHouse();
        assertEquals(30.0, h.getFloorSpace(0), DELTA);
        assertEquals(25.0, h.getFloorSpace(1), DELTA);
    }

    @Test
    void houseTotalFloorSpace() {
        assertEquals(55.0, threeRoomHouse().getTotalFloorSpace(), DELTA);
    }

    @Test
    void houseToString() {
        assertEquals("House: 7 Windows, 3 Rooms, Floor Space: 55.0, and 2 Floors",
                threeRoomHouse().toString());
    }

    @Test
    void topFloorRoomOfHouseWithMoreThanThreeFloorsGainsTwoWindows() {
        House h = new House(4);
        h.addRoom(10, 3);
        assertEquals(10, h.getNumWindows()); 
    }

    @Test
    void houseRejectsNegativeFloorCount() {
        assertThrows(REJECTED, () -> new House(-1));
    }

    @Test
    void houseRejectsNegativeArea() {
        assertThrows(REJECTED, () -> new House(2).addRoom(-5, 0));
    }

    @Test
    void houseRejectsNegativeFloorInAddRoom() {
        assertThrows(REJECTED, () -> new House(2).addRoom(5, -1));
    }

    @Test
    void houseRejectsNegativeFloorInGetFloorSpace() {
        assertThrows(REJECTED, () -> new House(2).getFloorSpace(-1));
    }

    // ---------- Part (c): Bungalow (two rooms) ----------

    @Test
    void bungalowWindows() {
        assertEquals(4, bungalow(25, 15).getNumWindows());
    }

    @Test
    void bungalowFloorSpace() {
        assertEquals(40.0, bungalow(25, 15).getFloorSpace(0), DELTA);
    }

    @Test
    void bungalowTotalFloorSpace() {
        assertEquals(40.0, bungalow(25, 15).getTotalFloorSpace(), DELTA);
    }

    @Test
    void bungalowToString() {
        assertEquals("Bungalow: 4 windows, 2 Rooms, Floor Space: 40.0, and 1 Floor",
                bungalow(25, 15).toString());
    }

    @Test
    void bungalowRejectsFloorsOtherThanZero() {
        assertThrows(REJECTED, () -> new Bungalow().addRoom(10, 1));
        assertThrows(REJECTED, () -> new Bungalow().getFloorSpace(1));
    }

    @Test
    void bungalowAllowsFloorSpaceOfSixty() {
        assertEquals(60.0, bungalow(40, 20).getTotalFloorSpace(), DELTA);
    }

    @Test
    void bungalowRejectsFloorSpaceOverSixty() {
        assertThrows(REJECTED, () -> bungalow(40, 20.5));
    }

    // ---------- Part (d): Estate (null list, policy 2, max 160) ----------

    @Test
    void estateAreaAfterAddingHouse() {
        Estate e = new Estate(null, 2, 160);
        e.addBuilding(house(20, 30));
        assertEquals(90.0, e.calculateArea(), DELTA); // 30 + 2 x 30
    }

    @Test
    void estateAreaAfterAddingBungalow() {
        Estate e = new Estate(null, 2, 160);
        e.addBuilding(house(20, 30));
        e.addBuilding(bungalow(15, 15));
        assertEquals(150.0, e.calculateArea(), DELTA); // 90 + (30 + (2/2) x 30)
    }

    @Test
    void estateWindows() {
        Estate e = new Estate(null, 2, 160);
        e.addBuilding(house(20, 30));
        e.addBuilding(bungalow(15, 15));
        assertEquals(10, e.getNumWindows()); // 6 + 4
    }

    @Test
    void addingBungalowAgainExceedsMaxArea() {
        Estate e = new Estate(null, 2, 160);
        e.addBuilding(house(20, 30));
        e.addBuilding(bungalow(15, 15));
        assertThrows(REJECTED, () -> e.addBuilding(bungalow(15, 15))); 
    }

    @Test
    void maxEstateAreaCountsTheGarden() {
        Estate e = new Estate(null, 2, 100);
        // largest floor is 40, but 40 + 2 x 40 = 120 > 100
        assertThrows(REJECTED, () -> e.addBuilding(house(40, 10)));
    }

    @Test
    void gardenSizePolicyMustBeBetweenHalfAndThree() {
        assertThrows(REJECTED, () -> new Estate(null, 0.4, 100));
        assertThrows(REJECTED, () -> new Estate(null, 3.1, 100));
    }

    @Test
    void maxEstateAreaMustBePositive() {
        assertThrows(REJECTED, () -> new Estate(null, 2, 0));
    }
}
