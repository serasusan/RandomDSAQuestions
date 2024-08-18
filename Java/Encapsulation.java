class Human{
    private String name;
    private int age = 10;
    public String getName() {
        return name;
    }
    public void setName(String name) {
        this.name = name;
    }
    public int getAge() {
        return age;
    }
    public void setAge(int age) {
        this.age = age;
    }



}

public class Encapsulation{
    public static void main(String[] args) {
        Human h = new Human();
        h.setName("John");
        h.getAge();
    }
}