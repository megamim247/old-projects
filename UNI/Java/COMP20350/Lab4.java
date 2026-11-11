import static org.junit.jupiter.api.Assertions.*;
import org.junit.jupiter.api.Test;
public class Lab4 {
    //test the some of the rules in Q6
    @Test
    void goldDilution0() {
        Metal gold = new Metal(5, 1.0, Metal.Type.GOLD);
        gold.mixWith(new Metal(100, 1.0, Metal.Type.TIN));
        assertEquals(1.0, gold.getPurity(), 0.0001);
        assertEquals(Metal.Type.TIN, gold.getType());
    }
    @Test
    void goldDilution1() {
        Metal tin = new Metal(50, 1.0, Metal.Type.TIN);
        tin.mixWith(new Metal(100, 1.0, Metal.Type.GOLD));
        assertEquals(Metal.Type.GOLD, tin.getType());
        assertEquals(1.0, tin.getPurity(), 0.0001);
    }
    @Test 
    void theEndGoal() {
        Metal tin = new Metal(100, 1.0, Metal.Type.TIN);
        tin.mixWith(new Metal(50, 1.0, Metal.Type.LEAD));
        assertEquals(Metal.Type.GOLD, tin.getType());
    }

    //test Constructor Constraints
    @Test
    void Purity() {
        assertThrows(IllegalArgumentException.class,
                () -> new Metal(10, 0.4, Metal.Type.GOLD));
    }
    @Test
    void Mass() {
        assertThrows(IllegalArgumentException.class,
                () -> new Metal(-10, 0.4, Metal.Type.GOLD));
    }
    //test toString
    @Test
    void to_String() {
        Metal m = new Metal(100, 1.0, Metal.Type.GOLD);
        assertEquals("Metal: Gold, Mass: 100.0 grams, Value: 4875.0", m.toString());
    }
}

