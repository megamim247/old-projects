public class CashRegister {
    double money;
    public CashRegister(double a){
        if(a<0){
            throw new ArithmeticException("Money cannot be negative");
        }
        money = a;
    }
    public double GetMoney(){
        return money;
    }
    public void  SetMoney(double a){
        if(a<0){
             throw new ArithmeticException("Money cannot be negative");
        }
        money = a;
    }
    public String toString(){
        return Double.toString(money);
    }
    public void add(double a){
        if(a<0){
             throw new ArithmeticException("Money cannot be negative");
        }
        money += a;
    }
    public void remove(double a){
        if(money - a<0){
             throw new ArithmeticException("Money cannot be negative");
        }
        money -= a;
    }
    public boolean equals(Object o){
        if 
        return money == o.GetMoney();
    }
}