package Lab6;

public class SimpleCalculatable implements Calculatable {
    private int value;

    public SimpleCalculatable(int value) {
        this.value = value;
    }
    @Override
    public int getValue() {
        return value;
    }

    @Override
    public void negate() {
        value = -value;
    }
}