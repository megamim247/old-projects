import java.util.ArrayList;
public class Metal {
    double mass, purity, pricepergram;
    enum Type {
        GOLD, LEAD, TIN
    }
    Type type;
    final double GoldPrice = 48.75;
    final double LeadPrice = 0.01;
    final double TinPrice = 0.03;
    
    ArrayList<String> mixHistory = new ArrayList<String>();

    public Metal(double a, double b, Type c) {
        if(a<0){
            throw new IllegalArgumentException("mass cannot be negative");
        }
        if(b<0.5 || b>1){
            throw new IllegalArgumentException("purity must be between 0.5 and 1");
        }
        this.mass = a;
        this.purity = b;
        this.type = c;
        switch (c) {
            case GOLD:
                this.pricepergram=GoldPrice;
                this.mixHistory.add("GOLD "+this.mass+" "+this.purity);
                break;
            case TIN:
                this.pricepergram=TinPrice;
                this.mixHistory.add("LEAD "+this.mass+" "+this.purity);
                break;
            case LEAD:
                this.pricepergram=LeadPrice;
                this.mixHistory.add("TIN "+this.mass+" "+this.purity);
                break;
        }
    }

    public double getMass() {
        return this.mass;
    }

    public void setMass(double a) {
        if(a<0){
            throw new ArithmeticException("mass cannot be negative");
        }
        this.mass = a;
    }

    public double getPurity() {
        return this.purity;
    }

    public void setPurity(double a) {
        if(a<0.5){
            throw new ArithmeticException("purity cannot be less than 0.5");
        }
        this.purity = a;
    }
    public Type getType() {
        return this.type;
    }

    /*public String[] getMixHistory() {
        return mixHistory;
    }

    public void setMixHistory(String[] mixHistory) {
        this.mixHistory = mixHistory;
    }*/

    public double getValue(){
        return this.purity*this.mass*this.pricepergram;
    }

    public String toString(){
        switch(this.type){
            case GOLD:
                return "Metal: Gold, Mass: "+this.mass+" grams, Value: "+this.getValue();
            case LEAD:
                return "Metal: Lead, Mass: "+this.mass+" grams, Value: "+this.getValue();
            case TIN:
                return "Metal: Tin, Mass: "+this.mass+" grams, Value: "+this.getValue();
            default:
                return "";
        }
    }

    public void mixWith(Metal nuMetal){
        switch (this.getType()) {
            case GOLD:
                switch (nuMetal.getType()) {
                    case GOLD:
                        this.mass=nuMetal.getMass()+this.getMass();
                        this.purity=1;
                        break;
                    case LEAD:
                        this.purity=this.purity*(this.mass/(nuMetal.getMass()+this.mass));
                        if(this.purity<0.5){
                            this.purity=1;
                            this.type=Type.LEAD;
                        }
                        break;
                    case TIN:;
                        this.purity=this.purity*(this.mass/(nuMetal.getMass()+this.mass));
                        if(this.purity<0.5){
                            this.purity=1;
                            this.type=Type.TIN;f 
                        }
                }
            case LEAD:
                switch (nuMetal.getType()) {
                    case GOLD:
                        nuMetal.setPurity(nuMetal.getPurity()*(this.mass/(nuMetal.getMass()+this.mass)));
                        if(nuMetal.getPurity()>=0.5){
                            this.type=Type.GOLD;
                        }else{
                            this.purity=1;
                        }
                    case LEAD:
                        this.mass=nuMetal.getMass()+this.mass;
                        this.purity=1;
                        break;
                    case TIN:
                        this.mass=nuMetal.getMass()+this.mass;
                        this.type=Type.GOLD;
                        break;
                }
            case TIN:
                switch (nuMetal.getType()) {
                    case GOLD:
                        nuMetal.setPurity(nuMetal.getPurity()*(nuMetal.getMass()/(nuMetal.getMass()+this.mass)));
                        if(nuMetal.getPurity()>=0.5){
                            this.type=Type.GOLD;
                        }else{
                            this.purity=1;
                        }
                    case LEAD:
                        this.mass=nuMetal.getMass()+this.mass;
                        this.type=Type.GOLD;
                        break;
                    case TIN:
                        this.mass=nuMetal.getMass()+this.mass;
                        this.purity=1;
                        break;
                }
        }
        this.mixHistory.add("TIN "+this.mass+" "+this.purity);
    }
}
