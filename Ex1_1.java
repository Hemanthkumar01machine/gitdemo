import java.util.Scanner;		//Importing Scanner Classs from util package

public class Ex1_1 {
	public static void main(String[] args) {
		Scanner scan=new Scanner(System.in);		//Creating an object to the Scanner Class
		
		System.out.print("Enter A Number : ");
		int num=scan.nextInt();
		
		if (num%2!=0) {
			System.out.println("Weird");
		}
		else {
			if (num>=8 && num<=22) {
				System.out.println("Weird");
			}
			else {
				System.out.println("Not Weird");
			}
		}
	}

}
