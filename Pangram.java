import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Solution {

    public static void main(String [] args) {
        Scanner sc = new Scanner(System.in);
        
        String input = sc.nextLine();
        
        if(isPangram(input))
            System.out.println("pangram");
        else
            System.out.println("not pangram");    
    }
    
    private static boolean isPangram(String sentence) {
        int [] occurred = new int[26];
        int numberOfUniqueAlphabets = 0;
        
        for(int i=0; i<sentence.length(); i++) {
            char c = sentence.charAt(i);
            
            if(hasAlphabetOccurredFirstTime(c, occurred)) {
                numberOfUniqueAlphabets++;
            }
            
            if(numberOfUniqueAlphabets == 26) {
                return true;
            }
        }
        return false;
    }
    
    private static boolean hasAlphabetOccurredFirstTime(char c, int [] occurred) {
        int alphabetsPosition = getAlphabetsPosition(c);
            
        if(alphabetsPosition != -1) {
            if(occurred[alphabetsPosition] == 0) {
                occurred[alphabetsPosition] = 1;
                return true;
            }
        }
        return false;
    }
    
    private static int getAlphabetsPosition(int c) {
        int startOfUpperCase = 65;
        int startOfLowerCase = 97;
        
        if(c < startOfLowerCase)  {
            int upperCasePosition = c % startOfUpperCase;
            if(upperCasePosition < 26)
                return upperCasePosition;
        } else {
            int lowerCasePosition = c % startOfLowerCase;
            if(lowerCasePosition < 26)
                return lowerCasePosition;
        }
        
        return -1;
    }
 }