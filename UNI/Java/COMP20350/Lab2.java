import java.util.Scanner;

public class Lab2 {
    int x,y,gap;
    static int[] NumOfTiles = {0,0,0,0,0};
    static void draw(int x, int y, int gap){
        for(int i=0;i<y;i++){
            if (i%(gap)==0){
                for(int i2=0;i2<x;i2++){
                    if(i2%(gap)==0){
                        System.out.print("+");
                        NumOfTiles[4]++;
                    }else{
                        System.out.print("-");
                        NumOfTiles[3]++;
                    }
                }
                System.out.println("");
            }else{
                for(int i2=0;i2<x;i2++){
                    if(i2%(gap)==0){
                        System.out.print("|");
                        NumOfTiles[2]++;
                    }else if((i2+i)%2==0){
                        System.out.print("o");
                        NumOfTiles[1]++;
                    }else{
                        System.out.print("x");
                        NumOfTiles[0]++;
                    }
                }
                System.out.println("");
            }
        }
    }
    public static void main(String[] args) {
        draw(16,16,5);
        System.out.print("No of x:\t"+NumOfTiles[0]+"\tCost\t"+NumOfTiles[0]*1+"\n"+
        "No of x:\t"+NumOfTiles[1]+"\tCost\t"+NumOfTiles[1]*2+"\n"+
        "No of x:\t"+NumOfTiles[2]+"\tCost\t"+NumOfTiles[2]*3+"\n"+
        "No of x:\t"+NumOfTiles[3]+"\tCost\t"+NumOfTiles[3]*4+"\n"+
        "No of x:\t"+NumOfTiles[4]+"\tCost\t"+NumOfTiles[4]*5+"\n"+
        "No of Tiles:\t"+(NumOfTiles[0]+NumOfTiles[1]+NumOfTiles[2]+NumOfTiles[3]+NumOfTiles[4])+"\tCost:\t"+((NumOfTiles[0]+NumOfTiles[1]*2+NumOfTiles[2]*3+NumOfTiles[3]*4+NumOfTiles[4]*5)+(NumOfTiles[0]+NumOfTiles[1]+NumOfTiles[2]+NumOfTiles[3]+NumOfTiles[4]))*1.23s
        );
    }
}
