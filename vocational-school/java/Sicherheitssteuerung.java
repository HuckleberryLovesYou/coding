import java.util.*;

public class Sicherheitssteuerung {
    public static void main(String[] args){
        
        System.out.println("Ist Schalter 1 aktiv?");            // asks the user if lever 1 is active
        Scanner lever1IsOn_scanner = new Scanner(System.in);    // answer has to be "true"
        boolean lever1IsOn = lever1IsOn_scanner.nextBoolean();

            System.out.println("Ist Schalter 2 aktiv?");            //  asks the user if lever 2 is active
        Scanner lever2IsOn_scanner = new Scanner(System.in);        // answer has to be "true"
        boolean lever2IsOn = lever2IsOn_scanner.nextBoolean();

        
        boolean LeversAreOn = false;
        if ( (lever1IsOn) && (lever2IsOn) ) {     // checks if both levers are on
            LeversAreOn = true;
            System.out.println("alle Schalter sind an");

        }

        System.out.println("Ist die Türe geschlossen?");            // asks the user if the gate to the machine is closed
        Scanner GitterGeschlossen_scanner = new Scanner(System.in);
        boolean GitterGeschlossen = GitterGeschlossen_scanner.nextBoolean();

        System.out.println("Wie weit bist du in CM von der Maschine entfernt?");            // asks the user how far he is away from the machine in cm
        Scanner DistanceToPress_scanner = new Scanner(System.in);
        int DistanceToPress = DistanceToPress_scanner.nextInt();

        if ( (LeversAreOn) && (GitterGeschlossen) && (DistanceToPress >= 100)) {             // checks if all requirements are meet to start the machine
            press.start //"turns on machine"
            System.out.println("Maschine startet");


        }
    }
}
