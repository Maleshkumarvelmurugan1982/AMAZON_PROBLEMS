import java.util.*;
public class main{
    public static void main(String[] args){
        Scanner sc=new Scanner(System.in);
        int n;
        System.out.println("Enter the no of elements:");
        n=sc.nextInt();
        int[] arr=new int[n];
        System.out.println("Enter the elements in an array:");
        for(int i=0;i<n;i++){
            arr[i]=sc.nextInt();
        }
        int k;
        System.out.println("Enter the number to search:");
        k=sc.nextInt();
        int low=0;
        int high=n-1;
        int res=-1;
        while (low<=high){
            int mid=(low+high)/2;
            if(arr[mid]==k){
                res=mid;
                break;
            }
            if(arr[low]<=arr[mid]){
                if(arr[low]<=k&&k<=arr[mid]){
                    high=mid-1;
                }else{
                    low=mid+1;
                }
            }
            else{
                if(arr[mid]<=k&&k<=arr[high]){
                    low=mid+1;
                }else{
                    high=mid-1;
                }
            }
           
        }
        if(res!=-1){
            System.out.println(k+" found at index "+res);
           
        }else{
            System.out.println("Element not found");
        }
    }
}
