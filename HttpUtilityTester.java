
import java.io.IOException;
import java.util.HashMap;
import java.util.Map;
import java.util.Scanner;

public class HttpUtilityTester {

    /**
     * This program uses the HttpUtility class to send a GET request
     * And send a POST request with data.
     */
    public static void main(String[] args)
    {
	/* test sending GET request
        String requestURL = "http://192.168.43.84:8080/hello.php";
        try {
            HttpUtility.sendGetRequest(requestURL);
            String[] response = HttpUtility.readMultipleLinesRespone();
            for (String line : response) {
                System.out.println(line);
            }
        } catch (IOException ex) {
            ex.printStackTrace();
        }
        HttpUtility.disconnect();
	*/

        // Sending POST request
        Map<String, String> params = new HashMap<String, String>();
        String requestURL = "http://192.168.43.84:8080/testpost.php";	//IP OF THE SERVER WITH ADDRESS OF THE PHP PAGE
	Scanner sc = new Scanner(System.in);
	String ID = sc.next();			//INPUT IS DATA FROM NFC TAG i.e. STUDENT ID
	params.put("ID", ID);			//Sending the ID as "ID"
        try {
            HttpUtility.sendPostRequest(requestURL, params);
            String[] response = HttpUtility.readMultipleLinesRespone();
            for (String line : response) {
                System.out.println(line);
            }
        } catch (IOException ex) {
            ex.printStackTrace();
        }
        HttpUtility.disconnect();
    }
}
