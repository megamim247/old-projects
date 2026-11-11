import java.util.Scanner;
public class Lab3{
    public static void main(String[] args){
        Scanner in = new Scanner(System.in);
        System.out.print("Enter starting money: ");
        String inString = in.nextLine();
        CashRegister POS1 = new CashRegister( Double.parseDouble(inString));
        System.out.println("money: "+POS1.GetMoney());
        System.out.print("Set money: ");
        inString = in.nextLine();
        POS1.SetMoney( Double.parseDouble(inString));
        System.out.println("money: "+POS1.GetMoney());
        System.out.print("Add money: ");
        inString = in.nextLine();
        POS1.add( Double.parseDouble(inString));
        System.out.println("money: "+POS1.GetMoney());
        System.out.print("new Point Of Sales Base cash: ");
        inString = in.nextLine();
        CashRegister POS2 = new CashRegister( Double.parseDouble(inString));
        System.out.println("are the cash amounts equal? "+POS1. equals(POS2));
    }
}