class factorial{
    int fact(int n){
        int result;
        if (n==1) return 1;
        result = fact(n-1) * n;
        return result;
    }
}

public class createObject{
    public static void main(String args[]){
        int a = 3;
        factorial f = new factorial();        
        System.out.println("Factorial of " + a + " is " + f.fact(a));
    }
}
