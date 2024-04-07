
import java.util.*;


public class sekintime {
    public static void main(String[] args) {
        int sekEingabe;
        int tage,stunden,minuten, sekunden;
        int tageRest, stundenRest, minutenRest;

        Scanner input = new Scanner(System.in);
        System.out.println("Eingabe der Sekunden");
        sekEingabe = input.nextInt();

        tage = sekEingabe / 86400;
        tageRest = sekEingabe % 86400;

        stunden = tageRest / 24;
        stundenRest = tageRest % 24;

        minuten = stundenRest / 60;
        minutenRest = stundenRest % 60;

        sekunden = minutenRest;


        System.out.println("Anzahl der Sekunden " + sekEingabe);
        System.out.println(tage + " Tage");
        System.out.println(stunden + " Stunden");
        System.out.println(minuten + " Minuten");
        System.out.println(sekunden + " Sekunden");



    }
}
