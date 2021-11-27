import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;

public class ReadFile {  
public static void main(String[] args) {  
    try {
        File myObj = new File("example.txt");
        Scanner myReader = new Scanner(myObj);  
        while (myReader.hasNextLine()) {
            String data = myReader.nextLine();
            String[] raw = data.replace("~", "0").split(" ", 5);

            int badge = Integer.parseInt(raw[0]);
            int x = Integer.parseInt(raw[2]);
            int y = Integer.parseInt(raw[3]);

        }
        myReader.close();
    } catch (FileNotFoundException e) {
        System.out.println("An error occurred.");
        e.printStackTrace();
    } 
}  
}