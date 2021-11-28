package snipets;
import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;
import java.util.ArrayList;

public class ReadInstruction {  
public static void main(String[] args) {  
    try {
        File myObj = new File("example.txt");
        Scanner myReader = new Scanner(myObj);  

        while (myReader.hasNextLine()) {
            String data = myReader.nextLine();
            String[] raw = data.replace("~", "0").split(" ", 5);

            double badge = Integer.parseInt(raw[0]); // This is for timing. Theres currently no support for adaptive badges so its your choice to touch badges.
            double x = Integer.parseInt(raw[2]);
            double y = Integer.parseInt(raw[3]);
            
            // Add stopwatch here (Theres one in WPILib)

            // Run Code

            // Add wait / subtract wait if behind
            
            System.out.println(x+" "+y);


        }
        myReader.close();
    } catch (FileNotFoundException e) {
        System.out.println("An error occurred.");
        e.printStackTrace();
    } 
}  
}