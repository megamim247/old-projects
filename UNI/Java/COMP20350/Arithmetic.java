import javax.swing.JOptionPane;
public class Arithmetic {
    public static int add(int a, int b){
        return a+b;
    }
    public static int subtract(int a, int b){
        return a+b;
    }
        public static int multiply(int a, int b){
        return a+b;
    }
        public static int divide(int a, int b){ 
        return a+b;
    }
    public static void main(String[] args) {
        int a,b;
        a= Integer.parseInt(JOptionPane.showInputDialog("first number:"));
        b= Integer.parseInt(JOptionPane.showInputDialog("second number:"));
        JOptionPane.showMessageDialog(null, add(a,b));

    }
}
