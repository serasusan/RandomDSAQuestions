class Car{
    static int wheels = 4;
    static void display(){
        System.out.println("Wheels: "+wheels);
    }
}

public class staticMethod{
    public static void main(String[] args) {
       Car.display();
    }

    
}
