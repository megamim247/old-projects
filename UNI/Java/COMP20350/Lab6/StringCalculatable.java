package Lab6;

public class StringCalculatable implements Calculatable {
    private static final String[] WORDS = {
        "zero", "one", "two", "three", "four",
        "five", "six", "seven", "eight", "nine"
    };

    private int value;

    public StringCalculatable(String s) {
        if (s == null || s.trim().isEmpty()) {
            throw new IllegalArgumentException("Input must not be null or empty");
        }
        s = s.trim();
        
        String[] parts = s.split("\\s+");
        StringBuilder digits = new StringBuilder();
        for (int i=0;i<parts.length;i++) {
            digits.append(wordToDigit(parts[i]));
        }
        value = Integer.parseInt(digits.toString());
        
    }

    private static int wordToDigit(String word) {
        for (int i = 0; i < WORDS.length; i++) {
            if (WORDS[i].equalsIgnoreCase(word)) {
                return i;
            }
        }
        throw new IllegalArgumentException("Not a valid digit word: " + word);
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