import java.util.Scanner;
import javax.swing.JOptionPane;
public class HelloWorldpp {
    public static void main(String[] args){
        Scanner in = new Scanner(System.in);
        System.out.print("Enter your name: ");
        String name = in.nextLine();
        System.out.println("hello " + name);
        in.close();
        name = JOptionPane.showInputDialog("enter your name:");
        JOptionPane.showMessageDialog(null,"hello "+name);
}
}
