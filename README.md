package Lab;

import java.util.Random;

 /**
  *  This code will create a random list, then it will bubble sort and count the comparisons
    then it will quick sort and count the comparisons and then finally display the lists with their comparisons 
  @author varun chandan
  */


public class Sorting {
// Declaring the values
             static int countquick=0;

           static int l,h;

            static int arraysize=100;

          

            
// the command to print the array
            public static void printArr(int ar[])

           {
 // The for loop initializes the array and prints it out
                      for(int i=0;i<ar.length;i++)

                      {

                                 System.out.print(ar[i] + " ");

                      }

                       

                      

                     System.out.println();

                   

            }

    /* This the main body of the code where we carry out operations to give the output */      

            

             public static void main(String[] args)

             {
               int [] items = new int[arraysize];
              Random r = new Random();

             int[] bubbleaverage = new int[100]; // to calculate the bubble sorting average of 0-99 numbers

             int[] quickaverage = new int[100]; // to calculate the quick sorting average of 0-99 numbers

 

           int i = 0;

           int o = 0;

          

            
// to print the unsorted list
            for (o=1;o<11;o++)

           {
            	System.out.println(" ");

                System.out.println(" The unsorted List :-");

          
// to save the unsorted list in an array for bubble sorting
            for(i=0;i<arraysize;i++)

          {        

             items[i]=r.nextInt(arraysize);

             System.out.print(items[i]+" ");          

          }
                    // to calculate the number of comparisons for bubble and quick sort
             System.out.println();

             bubbleaverage[o-1]=BubbleSort(items); // we subtract 1 that it does not exceed the out of bound for arrays

             System.out.println(" the Bubblesort list with comparisons:-"+bubbleaverage[o-1]);

                     
             Quicksort(items, 0,arraysize-1 );
            
             quickaverage[o-1]= countquick;
             System.out.println("list sorted by quick sort with comparisons:- "+quickaverage[o-1]);
            
             countquick=0;
                
             for( int x=0;x<arraysize;x++) 
             {
                System.out.print(items[x]+" ");
                         }
            
                }

            
  
             }
 
  // Starting the bubble sort by swapping the larger numbers with smaller numbers to the left in a repeated manner
             
            public static int BubbleSort(int ar[])

          {

            int bubblecount = 0 ;

            for(int i=0;i<arraysize;i++)

              {

             for(int j=0;j<arraysize-1-i;j++)

             {

             if (ar[j]>ar[j+1])

              {
// swapping ar[j] with ar[j+1] if the condition on the top is true
             int x = ar[j];

             ar[j] = ar[j+1];

             ar[j+1]=x;

            bubblecount++;

             }

                 }

                    }
                
            printArr(ar); // displaying the output

           System.out.println();

           return bubblecount;

                                 }

 

 

 

    /* The last element in the function is called pivot
     * when the number is smaller it keeps on swapping with big number on the left */

   static int partition(int items[], int low, int high)

    {

        int pivot = items[high]; 

        int i = (low-1); // index of smaller element

        for (int j=low; j<high; j++)

        {

            // If current element is smaller than or

            // equal to pivot

            if (items[j] <= pivot)

            {

                i++;

  

                // swapping items[i] and items[j]

                int temp = items[i];

                items[i] = items[j];

                items[j] = temp;

                countquick++;

               

            }

        }

  

        // swap items[i+1] and items[high]

        int temp = items[i+1];

        items[i+1] = items[high];

        items[high] = temp;

  countquick++;

        return i+1;

    }

        

   static void Quicksort(int ar[], int low, int high)

    {

        if (low < high)

        {

           

            int pi = partition(ar, low, high);

  

            // Recursively sort elements before

            // partition and after partition

            Quicksort(ar, low, pi-1);

            Quicksort(ar, pi+1, high);
            
         

        }

   

       }

}

// https://www.geeksforgeeks.org
