package datacleaning;

import java.util.ArrayList;
import java.util.Map;
import org.jblas.DoubleMatrix;
import org.json.JSONObject;


public class DataCleaning {
    public static void main(String[] args) 
    {
        clean obj = new clean();
        String path = "CandidateProfileData/";
       
        String data = obj.readFile("Candidate1.txt");
        JSONObject can = new JSONObject(data);
        
  
        
    }
}
