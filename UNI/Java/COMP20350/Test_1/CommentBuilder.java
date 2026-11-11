package Test_1;
import java.util.Base64;
import java.util.Scanner;

public class CommentBuilder {
    public static void main(String[] args) {
        try(Scanner scanner = new Scanner(System.in)) {
            System.out.println("Enter your student ID: ");
            int studentID = Integer.parseInt(scanner.nextLine());
            System.out.println("Enter your name as it appears on your student ID: ");
            String name = scanner.nextLine();

            System.out.println("Put the following comment at top of the submission to CSMoodle:\n\n" + buildComment(studentID, name));

        } catch (NumberFormatException e) {
            System.err.println("You must enter a number for your Student ID");
        }
    }

    private static String buildComment(int studentNumber, String name) {
        String message = "Name: " + name + "\nID: " + studentNumber;
        return "//-- " + Base64.getEncoder().encodeToString(message.getBytes()) + "\n" + getGeneralClaim();
    }

    private static String getGeneralClaim() {
        return "//By including this comment, I acknowledge that this submission\n"
                + "//is my work, and my work alone. With no collaboration with (an)other student(s)\n"
                + "//I also acknowledge that I have not used any AI tools and have referenced\n"
                + "//by providing a web link (as a comment) any online sources I have consulted\n\n";
    }

}
