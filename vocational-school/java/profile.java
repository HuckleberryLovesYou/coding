import java.time.*;

public class profile {
    public static void main(String[] args) {

        LocalDate dob = LocalDate.of(2007, 04, 01);
        LocalDate curDate = LocalDate.now();
        Period period = Period.between(dob, curDate);

        String prename = "Martina";
        String surname = "Musterfrau";
        char gender = 'w';
        int age = period.getYears();
        float body_height = 1.63F;
        int postal_code = 89456;
        String phone_number = "01234567";
        int weight = 80;
        double bmi = weight / (body_height * body_height);
        boolean isadult = false;
        if (age >= 18) isadult = true;

        System.out.printf("%-24s%s%n","Vorname:",prename);
        System.out.printf("%-24s%s%n","Nachname:",surname);
        System.out.printf("%-24s%s%n","Geschlecht:",gender);
        System.out.printf("%-24s%s%n","Alter:",age);
        System.out.printf("%-24s%s%n","Körpergröße:",body_height);
        System.out.printf("%-24s%s%n","Postleitzahl",postal_code);
        System.out.printf("%-24s%s%n","Telefonnummer:",phone_number);
        System.out.printf("%-24s%s%n","Ist volljährig:",isadult);
        System.out.printf("%-24s%s%n","Dein BMI:",Math.round( bmi * 100 ) / 100. );
        System.out.printf("%-24s%s%n","Du bist:",period.getYears());

    }
}
