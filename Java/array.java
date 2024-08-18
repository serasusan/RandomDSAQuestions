
public class array{
    public static void main(String args[]){
        int[] arr = new int[5];
        arr[0] = 10;
        arr[1] = 20;
        arr[2] = 30;
        arr[3] = 40;
        arr[4] = 50;
        for(int i=0;i<arr.length;i++){
            System.out.println(arr[i]);
        }

        int nums[][] = new int[2][2];

        for(int i=0;i<nums[0].length;i++){
            for(int j=0;j<nums.length;j++){
                nums[i][j] = (int)(Math.random()*100);
            }
        }

        System.out.println("\n2D Matrix display using normal for loops\n");
        for(int i=0;i<nums[0].length;i++){
            for(int j=0;j<nums.length;j++){
                System.out.print(nums[i][j]+" ");
            }
            System.out.println();
        }
        // Advanced for loop
        System.out.println("2D Matrix display using advanced for loop");
        for(int n[] : nums){
            for(int m : n){
                System.out.print(m + " ");
            }
            System.out.println();
        }
        
        //jagged array
        int arr2[][] = new int[3][];
        arr2[0] = new int[3];
        arr2[1] = new int[2];
        arr2[2] = new int[1];

        for(int i=0;i<arr2.length;i++){
            for(int j=0;j<arr2[i].length;j++){
                arr2[i][j] = (int)(Math.random()*100);
            }
        }
        
        for(int n[] : arr2){
            for(int m : n){
                System.out.print(m + " ");
            }
            System.out.println();
        }
    }
}
