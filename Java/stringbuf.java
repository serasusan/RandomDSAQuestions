

public class stringbuf{
    public static void main(String[] args) {
        StringBuffer sb = new StringBuffer("Hello");
        System.out.println("After adding \"Hello\" : "+sb.capacity());
        sb.append(" World");
        sb.append(" World");
        sb.append(" World");
        System.out.println(sb);
        System.out.println("After adding \" World\""+sb.capacity());

        sb.insert(5, " Java");
        System.out.println(sb);
        
        sb.replace(5, 10, "Python");
        
        System.out.println(sb);
        sb.delete(5, 11);
        System.out.println(sb);
        sb.reverse();
        System.out.println(sb);
    }
}