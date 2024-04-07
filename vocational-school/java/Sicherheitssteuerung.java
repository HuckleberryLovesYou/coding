import java.util.*;

public class Sicherheitssteuerung {
    public static void main(String[] args){

//        byte a,b,c;
//
//        a = 12;
//        b = 12;
//        c = (byte) (a + b);



        System.out.println("Ist Schalter 1 aktiv?");            // frägt User, ob der Schalter 1 aktiv ist
        Scanner lever1IsOn_scanner = new Scanner(System.in);
        boolean lever1IsOn = lever1IsOn_scanner.nextBoolean();

        System.out.println("Ist Schalter 2 aktiv?");            // frägt User, ob der Schalter 2 aktiv ist
        Scanner lever2IsOn_scanner = new Scanner(System.in);
        boolean lever2IsOn = lever2IsOn_scanner.nextBoolean();

        boolean LeversAreOn = false;

        if ( (lever1IsOn) && (lever2IsOn) ) {     // gibt true aus, wenn beide Schalter an sind
            LeversAreOn = true;
            System.out.println("alle Schalter sind an");

        }

        System.out.println("Ist das Gitter geschlossen?");            // frägt User, ob das Gitter geschlossen ist
        Scanner GitterGeschlossen_scanner = new Scanner(System.in);
        boolean GitterGeschlossen = GitterGeschlossen_scanner.nextBoolean();

        System.out.println("Wie weit bist du in CM von der Maschine entfernt?");            // frägt User, wie viel CM er von der Maschine entfernt ist
        Scanner DistanceToPress_scanner = new Scanner(System.in);
        int DistanceToPress = DistanceToPress_scanner.nextInt();

        if ( (LeversAreOn) && (GitterGeschlossen) && (DistanceToPress >= 100)) {             // Überprüfen der Vorraussezungen zum Start der Maschine
            boolean startPress = true;
            System.out.println("Maschine startet");


        }
    }
}
