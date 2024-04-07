public class Quadrierer {
    public static int quad (byte Zahl) {
        return Zahl * Zahl;
    }

    public static void main(String[] args) {
        byte Zahl = 11;
        System.out.println("Die zu quadrierende Zahl ist " + Zahl + "\n\n\n");
        System.out.println("Das Ergebnis ist:\n\n" + (byte) quad(Zahl));
    }
}
