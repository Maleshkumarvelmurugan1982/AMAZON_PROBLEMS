import java.util.*;
public class main{
	public static void main(String[] args){
		Scanner sc=new Scanner(System.in);
		int n;
		System.out.println("Enter the No of pumps:");
		n=sc.nextInt();
		int [] pet=new int[n];
		int [] dis=new int[n];
		System.out.println("Enter the petrols:");
		for(int i=0;i<n;i++){
			pet[i]=sc.nextInt();
		}
		System.out.println("Enter the Distances:");
		for(int i=0;i<n;i++){
			dis[i]=sc.nextInt();
		}
		int s;
		System.out.println("Enter the starting pump:");
		s=sc.nextInt();
		int fuel=pet[s]-dis[s];
		if(fuel<0){
			System.out.println("Cannot complete the run");
			return;
		}
		int current=(s+1)%n;
		while(current!=s){
			fuel+=pet[current];
			fuel-=dis[current];
			if(fuel<0){
				System.out.println("Cannot complete the run");
				return;
			}
			current=(current+1)%n;
		}
		System.out.println("Can complete the circle");
		System.out.println("Fuel is:"+ fuel);
	}
}

