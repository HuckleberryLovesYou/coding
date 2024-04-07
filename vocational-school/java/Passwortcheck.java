import java.util.Scanner;

public class Passwortcheck {
    public static void main(String[] args) {
        boolean pw_cracked = false;

        while (!pw_cracked) {
            System.out.println("Enter Password:\n");
            Scanner passwort_scanner = new Scanner(System.in);
            int passwort_eingabe = passwort_scanner.nextInt();

            pw_cracked = passwortCheck(passwort_eingabe);

        }
        System.out.println("Du hast das Passwort erfolgreich eingebeben!!!!!!!!!!!!!!");
    }












































































    private static boolean passwortCheck(int pw_eingabe) {
        int password = 69;

        if (password == pw_eingabe) {
            return true;
        } else {return false;}
    }
}
