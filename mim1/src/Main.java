//import
import java.util.Date;
import java.util.Scanner;

//Main is the class(the actual program that is to be run )
public class Main {
    //public means it can be used anywhere and static means(insert) void means it will not output anything main(String[] args) refers to the
    public static void main(String[] args) {
        //variables:

        //primitive types
        byte a= 0;
        float b=1.33f;//identifier
        char c='a';//char uses'' but string uses""
        //const:
        final int j=1;
        //refrence types (addresses referencing to objects)
        Date d =new Date();//allocate memory(new) Date() is the blueprint original for new instances
        //d.getTime();//operate on the reference value
            /*/differences between primitive and reference
            primitive values are independent as they are stored in diffrent memory locations
            reference types store addresses to an object (Date)
            therefore to store new objects the object has to be redifiend with new Data()
            d=address of Date object
            */

        //string
        String e="hi"+"!!";
        /*/
            String is reference type that can be defined easily and can be operated to make a new object as strings are immutable

            parameter is (args,args)
            args are the values inputted in the parameter
            special charecters: ; , " ' \ \n \t \\"(for ackslash at end of string)

            strings are in the base package for java (java.lang)
             */
        //arrays
        int[] f = new int[5];
        f[0] = 1;
        /*/
        arrays are reffrence types
        f stores the address of array so f will print the addres of the array
        util.Arrays is very helpful for arrays
        new way to define array:*/
        int[] g ={2,3,4,5};
        //multidiomensional array
        int[][] h =new int[1][1];
        //easy method
        int[][] i ={{3,4},  {2,3,4,5}};
        //operators
        /*
        +
        -
        *
        divide:
        int n = a/b
        double n=a/b
        double n=(double)9/(double)10
        ()

        augmented/compound
        +=
        -=
        /=
        *=
        the values being operated are operands

        bodmas is applied

        */

        //Mathclass(jvava.lang.Math)
        //casting
        /*
        implicit: automatic(short +) byte->short->int->long->float->double
        explicit: (float)5.1f+(float)6.2f
        Math.round has to be used for flt too int
        parse: integer.parseintreger
         */
        //taking input
        /*
        util.scanner
        scanner (var)=new Scanner(system.in); a new scanner object is created from the system.in object(any other object like a document can also be used)
        then a variable is defined by:
        byte (var)=scanner.nextByte();
         */
        //logical operators
        /*
        ==
        !=
        <=
        >=
        >
        <
        other:
        &&
        ||
        () parentheses should be used to wrap all bool expressions
        !
        for strings;
        str.equals("str")
         */
        //if statments:
        /*
        if(bool){

        }
         */
        //ternary opperator
        /*
        (bool) ? "true":"false"
         */
        //for loop
        /*
        for (int n/i/j/k = 0 ;(n<5);n++)
         */
        //while loop
        /*
        while(bool)
         */
        //always  make sccaner objects outside of the loop code block
        //do while
        /*
        do{

        }while(bool);
         */
    }
}