import java.util.Scanner;

public class Test {
    public static void sayHello (String name) {
        System.out.println("Hello " + name);
    }
    public static void sayGoodbye(String name) {
        System.out.println("Goodbye " + name );
    }

    public static void main(String[] args) {

        System.out.println("Please enter your name here:\n");            // asks suer for their name
        Scanner in = new Scanner(System.in);
        String your_name = in.nextLine();




        sayHello(your_name);
        sayGoodbye(your_name);
    }
}
