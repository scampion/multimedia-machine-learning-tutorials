import java.io.File;
import java.io.IOException;
import java.util.ArrayList;
import java.util.List;
import java.util.Scanner; 

public class SpamClassifier {
    public static final int NB_MAILS = 4601;
    public static final int NB_ATTRS = 58 ;

    public static void main( String [] args )
    {
	try {
	    float[][] matrix = loadData("spambase.data", NB_MAILS, NB_ATTRS);

	    int nb_of_spams = 0;
	    for(int i=0; i < NB_MAILS; i++){
		if (matrix[i][57] == 1) {
		    nb_of_spams += 1;
		}		  
	    }
	    System.out.println(nb_of_spams + " spams loaded");

	    Stats spams_stats = new Stats();
	    spams_stats.learn(matrix, 50, 1);
	    
	}
	catch(Exception e){
	    e.printStackTrace();
	}
    }

    public static float[][] loadData(String filename, int total, int nbargs ) throws Exception {
	float matrix[][] = new float[total][nbargs];
	File ifile = new File(filename);
	Scanner scanner = new Scanner(ifile);
	int count = 0 ;
	while (scanner.hasNextLine()) {
	    String line = scanner.nextLine();
	    String[] data = line.split(" ");
	    for(int i = 0; i < data.length ; i++)
		matrix[count][i] = Float.parseFloat(data[i]);
	    count++; 
	}
	// DEBUG print the first mail stat
	/*
	System.out.println("First mail stats");
	for (int i = 0 ; i < 58; i++)
	    System.out.print(matrix[0][i] + " ");
	System.out.println("");
	*/
	return matrix;
    }

}

class Stats {
    int NB_ATTRS = 58 ;
    float[] avg = new float[NB_ATTRS];
    float[] std = new float[NB_ATTRS];
    
    public void learn(float[][] matrix, int size, int flag){
	int count = 0 ;
	for(int i = 0; (i < matrix.length && count < size); i++){
	    if (matrix[i][57] == flag) {
		for( int j = 0; j < 57; j++){
		    this.avg[j] += matrix[i][j]; 
		}
	    }
	}
	for( int j = 0; j < 57; j++){
	    this.avg[j] = this.avg[j] / size ;
	}    
    }
}
