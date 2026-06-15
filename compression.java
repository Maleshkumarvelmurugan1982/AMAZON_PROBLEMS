mport java.util.*;
public class main{
    public static void main(String[] args){
        Scanner sc=new Scanner(System.in);
        String h;
        int count=1;
        System.out.println("Enter the String:");
        h=sc.next();
        char[]a=h.toCharArray();
        int b=a.length;
        for(int i=0;i<b-1;i++){
            if(a[i]==a[i+1]){
                count++;
               
            }else{
                System.out.print(a[i]);
                if(count>1){
                    System.out.print(count);
                }
                count=1;
            }
        }
        System.out.print(a[b - 1]);
        if(count > 1){
            System.out.print(count);
        }
    }
}
