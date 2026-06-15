import java.util.*;
public class main{
    public static void main(String[] args){
        Scanner sc=new Scanner(System.in);
        int n,m;
        System.out.println("Enter the number of rows and columns:");
        n=sc.nextInt();
        m=sc.nextInt();
        int[][] arr=new int[n][m];
        System.out.println("Enter the elements of the array:");
        for(int i=0;i<n;i++){
            for(int j=0;j<m;j++){
                arr[i][j]=sc.nextInt();
            }
        }
        Arrays.sort(arr, (a, b) -> Integer.compare(a[0], b[0]));
        System.out.println(Arrays.deepToString(arr));
        int t;
        System.out.println("Enter the target:");
        t=sc.nextInt();
        boolean f=false;
        for(int i=0;i<n;i++){
            for(int j=0;j<m;j++){
                if(t==arr[i][j]){
                    System.out.println(t+" found");
                    f=true;
                    break;
                }
            }
            if(f){
                break;
            }
        }
        if(!f){
            System.out.println("0");
        }
    }
}

