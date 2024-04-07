import java.util.Scanner;

public class Restaurant {
    public static void main(String[ ] args){



        System.out.println("Ist Pizza vorhanden?");            // asks user if pizza is available
        Scanner pizza_scanner = new Scanner(System.in);
        boolean pizza = pizza_scanner.nextBoolean();

        System.out.println("Sind Pommes vorhanden?");            // asks user if french fries is available
        Scanner pommes_scanner = new Scanner(System.in);
        boolean pommes = pommes_scanner.nextBoolean();

        System.out.println("Ist Döner vorhanden?");            // asks user if Döner is available
        Scanner Doener_scanner = new Scanner(System.in);
        boolean Doener = Doener_scanner.nextBoolean();

        System.out.println("Ist Salat vorhanden?");            // asks user if salad is available
        Scanner Salat_scanner = new Scanner(System.in);
        boolean Salat = Salat_scanner.nextBoolean();



        if (pizza) {
            System.out.println("Der Kunde bekommt eine Pizza");
            System.exit(0);
        } else if (pommes) {
            System.out.println("Der Kunde bekommt Pommes");
            System.exit(0);
        } else if (Doener) {
            System.out.println("Der Kunde bekommt einen Döner");
            System.exit(0);
        } else if (Salat) {
            System.out.println("Der Kunde bekommt einen Salat");
            System.exit(0);
        } else System.out.println("Der Kunde bekommt Wasser");
    }
}
