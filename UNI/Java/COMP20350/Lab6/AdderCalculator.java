package Lab6;

public class AdderCalculator implements Calculator {

    @Override
    public Calculatable calculate(Calculatable[] arr) {
        int sum = 0;
        for (int i = 0; i < arr.length; i++) {
            sum += arr[i].getValue();
        }
        return new SimpleCalculatable(sum);
    }
}