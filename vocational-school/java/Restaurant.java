import java.util.Scanner;

public class Restaurant {
    public static void main(String[ ] args){



        boolean gefunden = false;
        boolean gefunden_1 = false;
        boolean gefunden_2 = false;
        boolean gefunden_3 = false;
        boolean gefunden_4 = false;



        System.out.println("Ist Pizza vorhanden?");            // frägt User, ob der Schalter 1 aktiv ist
        Scanner pizza_scanner = new Scanner(System.in);
        boolean pizza = pizza_scanner.nextBoolean();


        while (!gefunden )
            if (pizza) {
                System.out.println("Der Kunde bekommt eine Pizza");
                gefunden_1 = true;
                gefunden = true;
                System. exit(0);
            }


        System.out.println("Sind Pommes vorhanden?");            // frägt User, ob der Schalter 1 aktiv ist
        Scanner pommes_scanner = new Scanner(System.in);
        boolean pommes = pommes_scanner.nextBoolean();

        while (!gefunden)
            if (pommes) {
                System.out.println("Der Kunde bekommt Pommes");
                gefunden_2 = true;
                gefunden = true;
                System. exit(0);
            }


        System.out.println("Ist Döner vorhanden?");            // frägt User, ob der Schalter 1 aktiv ist
        Scanner Doener_scanner = new Scanner(System.in);
        boolean Doener = Doener_scanner.nextBoolean();

        while (!gefunden)
            if (Doener) {
                System.out.println("Der Kunde bekommt einen Döner");
                gefunden_3= true;
                gefunden = true;
                System. exit(0);
            }

        System.out.println("Ist Salat vorhanden?");            // frägt User, ob der Schalter 1 aktiv ist
        Scanner Salat_scanner = new Scanner(System.in);
        boolean Salat = Salat_scanner.nextBoolean();

        while (!gefunden)
            if (Salat) {
                System.out.println("Der Kunde bekommt einen Salat");
                gefunden_4 = true;
                gefunden = true;
                System. exit(0);
            } else System.out.println("Der Kunde bekommt Wasser");









    }
}
