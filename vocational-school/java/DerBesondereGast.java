public class DerBesondereGast {
    public static void main(String[] args) {




        // Lagerbestand
        boolean pizza = false;
        boolean pommes = false;
        boolean doener = false;
        boolean salat = true;
        boolean wasser = true;

        if (pizza) {
            System.out.println("Der Kunde bekommt eine Pizza");
        } else if (pommes) {
            System.out.println("Der Kunde bekommt Pommes");
        } else if (doener) {
            System.out.println("Der Kunde bekommt einen Döner");
        } else if (salat) {
            System.out.println("Der Kunde bekommt einen Salat");
        } else if (wasser) {
            System.out.println("Der Kunde bekommt ein Wasser");
        }

    }

}