/******************************************************************************

                            Online Java Compiler.
                Code, Compile, Run and Debug java program online.
Write your code in this editor and press "Run" button to execute it.

*******************************************************************************/

import java.util.Scanner;

public class Main
{
	public static void main(String[] args) {
		    for( int i = 0 ; i < 10 ; i++ ) {

                if( i % 2 == 0) { 
                  continue;    
                }

                 System.out.println("The number is " + i );

                if( i == 7 ) {
                  break;        
            }

        }
	}
}
