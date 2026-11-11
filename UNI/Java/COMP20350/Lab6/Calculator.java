package Lab6;

public interface Calculator {
    Calculatable calculate(Calculatable[] values);

    // Q6: class (static) method returning the interface type.
    // (Bad practice in real code. A Factory class is the proper approach.)
    static Calculator create(String type) {
        switch (type.toLowerCase()) {
            case "add":
                return new AdderCalculator();
            case "multiply":
                return new MultiplerCalculator();
            default:
                throw new IllegalArgumentException("Unknown calculator type: " + type);
        }
    }
}