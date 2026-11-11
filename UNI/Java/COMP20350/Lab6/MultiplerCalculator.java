package Lab6;

public class MultiplerCalculator implements Calculator {
    @Override
    public Calculatable calculate(Calculatable[] arr) {
        int product = 1;
        for (int i = 0 ; i< arr.length;i++) {
            product *= arr[i].getValue();
        }
        return new SimpleCalculatable(product);
    }
}