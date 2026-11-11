package Lab8;

import java.io.*;
import java.util.ArrayList;
import java.util.Scanner;

public class Abalone {

    // Integer constants representing the allowed sexes
    public static final int MALE = 0;
    public static final int FEMALE = 1;
    public static final int INFANT = 2;

    private int sex;
    private double length;
    private double diameter;
    private double weight;
    private int age;

    public Abalone(int sex, double length, double diameter, double weight, int age) {
        setSex(sex);
        setLength(length);
        setDiameter(diameter);
        setWeight(weight);
        setAge(age);
    }

    // ---- Getters ----

    public int getSex() {
        return sex;
    }

    public double getLength() {
        return length;
    }

    public double getDiameter() {
        return diameter;
    }

    public double getWeight() {
        return weight;
    }

    public int getAge() {
        return age;
    }

    // ---- Setters (validate their input) ----

    public void setSex(int sex) {
        if (sex != MALE && sex != FEMALE && sex != INFANT) {
            throw new IllegalArgumentException(
                "Sex must be Abalone.MALE, Abalone.FEMALE or Abalone.INFANT, but was " + sex);
        }
        this.sex = sex;
    }

    public void setLength(double length) {
        if (!(length > 0)) { // also rejects NaN
            throw new IllegalArgumentException("Length must be positive, but was " + length);
        }
        this.length = length;
    }

    public void setDiameter(double diameter) {
        if (!(diameter > 0)) {
            throw new IllegalArgumentException("Diameter must be positive, but was " + diameter);
        }
        this.diameter = diameter;
    }

    public void setWeight(double weight) {
        if (!(weight > 0)) {
            throw new IllegalArgumentException("Weight must be positive, but was " + weight);
        }
        this.weight = weight;
    }

    public void setAge(int age) {
        this.age = age;
    }

    
    public String toString() {
        String sexLetter;
        switch (sex) {
            case MALE:
                sexLetter = "M";
                break;
            case FEMALE:
                sexLetter = "F";
                break;
            default:
                sexLetter = "I";
                break;
        }
        return "Abalone (" + sexLetter + "), length=" + length + ", diameter=" + diameter + ", weight=" + weight + ", age=" + age;
    }

    public boolean equals(Abalone o) {
        if(o.getSex()==sex && length == o.getLength() && diameter == o.getDiameter() && weight == o.getWeight() && age == o.getAge()){
            return true;
        } else{
            return false;
        }
    }
    
    public static ArrayList<Abalone> read(File file) throws FileNotFoundException {
        ArrayList<Abalone> abalones = new ArrayList<>();
 
        try (Scanner in = new Scanner(file)) {
            while (in.hasNextLine()) {
                String line = in.nextLine().trim();
                if (line.isEmpty()) {
                    continue; // ignore blank lines
                }
 
                String[] tokens = line.split(",");
                int sex=-1;
                switch (tokens[0].trim()) {
                    case "M":
                        sex = 0;
                        break;
                    
                    case "F":
                        sex = 1;
                        break;

                    case "I":
                        sex = 1;
                        break;
                    default:
                        throw new IllegalArgumentException("Sex must be M/F/I");
                }
                
                double length = Double.parseDouble(tokens[1].trim());
                double diameter = Double.parseDouble(tokens[2].trim());
                double weight = Double.parseDouble(tokens[3].trim());
                int age = Integer.parseInt(tokens[4].trim());
 
                abalones.add(new Abalone(sex, length, diameter, weight, age));
            }
        }
 
        return abalones;
    }
    public static void main(String[] args) {
        try {
            ArrayList<Abalone> list = Abalone.read(new File("C:/Gits/Programming/UNI/Java/COMP20350/Lab8/abalone-short.csv"));
 
            System.out.println("Read " + list.size() + " abalones");
            for (Abalone a : list) {
                System.out.println(a);
            }
        } catch (FileNotFoundException e) {
            System.out.println("File not found: " + e.getMessage());
        }
    }


}