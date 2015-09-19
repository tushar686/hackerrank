import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Solution {
    private int numberOfTests;
    private String [] tests;
    
    public static void main(String[] args) {
        Solution solution = new Solution();
        solution.collectInput();        
        solution.calculateRequiredDeletionForAllTests();
    }

    private void calculateRequiredDeletionForAllTests() {
        for(int i=0; i<numberOfTests; i++) {
            System.out.println(howManyDeletionRequired(tests[i]));  
        }
    }
    
    private int howManyDeletionRequired(String testString) {
        int deletion = 0;
        char prevChar = ' ';
        for (int i = 0; i < testString.length(); i++) {
            char currentChar = testString.charAt(i);
            if(currentChar == prevChar) {
                deletion++;
            }
            prevChar = currentChar;
        }
        return deletion;
    }

    private void collectInput() {
        Scanner scanner = new Scanner(System.in);
        numberOfTests = Integer.parseInt(scanner.nextLine());
        tests = new String[numberOfTests];
        for(int i=0; i<numberOfTests; i++) {
            tests[i] = scanner.nextLine();
        }
    }
}