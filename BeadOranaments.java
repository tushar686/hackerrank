import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Solution {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int tests = Integer.parseInt(scanner.nextLine());
		List<int []> beadsList = new ArrayList<int []>();

		while(tests > 0) { 
			int size = Integer.parseInt(scanner.nextLine());
			int [] beadArr = new int[size];
            String beads = scanner.nextLine();
            int i = 0;
            for(String bead:beads.split(" ")) {
				beadArr[i++] = Integer.parseInt(bead);
            }
			beadsList.add(beadArr);
            tests--;
        }
		
		for(int [] beadArr: beadsList) {
			BigInteger total = totalNumberOfConfigurations(beadArr);
			System.out.println(total.divideAndRemainder( BigInteger.valueOf(1000000007) )[1] );
		}
    }
    
    static BigInteger numberOfOrnaments(int beadCount) {
        if (beadCount <= 2) {
            return BigInteger.ONE;
        }
        return BigInteger.valueOf(beadCount).pow(beadCount-2);
    }
    
    static BigInteger totalNumberOfConfigurations(int[] beadCounts) {
		if(beadCounts.length == 1) {
			return numberOfOrnaments(beadCounts[0]);
		}
		
        BigInteger result = BigInteger.ONE;
        int sum = 0;
        for (int n : beadCounts) {
            result = result.multiply(numberOfOrnaments(n));
            result = result.multiply(BigInteger.valueOf(n));
            sum += n;
        }
        BigInteger x = BigInteger.valueOf(sum).pow(beadCounts.length - 2);
        result = result.multiply(x);
        return result;
    }
}