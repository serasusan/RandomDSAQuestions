// OOPS CONCEPTS
// What is OOP
// 4 PILLARS Of OOPS

import java.util.Scanner;

public class main{
    public static void main(String[] args) {
        for(int i =0;i<10;i++){
            System.out.println(i);
        }
        Car car1 = new Car(0);
        Car car2 = new Car(0, "blue");
        car1.setSpeed(10);
        Scanner sc = new Scanner(System.in);
        int speed 
    }
}

class Car{
    private int speed;
    private String color;

    public void setSpeed(int speed){
        this.speed = speed;
    }
    public void printSpeed(){
        System.out.println(this.speed);
    }
    // constructor
    public Car(int speed, String color){
        this.speed = speed;
        this.color = color;
    }
    public Car(int speed){
        this.speed = speed;
        this.color = "red";
    }
    
}