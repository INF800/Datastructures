#### Time and Space Complexity

- How much time is machine taking for solving problems?
    - It depends on prodcedure of process under consideration (you can see it in code)
    - For example, let us take **list operations**
        - Process each element in a list once
            - code
                ```
                for(i=0; i<n; i++)
                {
                    //code
                }
                ```
            - **`O(n)`**
        - Process each element in list with each element in the list
            - code
                ```
                for(i=0; i<n; i++)
                {
                    for(j=0; j<n; j++)
                    {
                        //code
                    }
                }
                ```
            - **`O(n^2)`**
        - Process rest(right side) of the list while traversing a list
            - code
                ```
                for(i=0; i<n; i++)
                {
                    for(j=i+1; j<n; j++)
                    {
                        //code
                    }
                }
                ```
                - `1 + 2 + 3 + ... + (n-2) + (n-1)` = `n(n-1)/2` = `(n^2 - n)/2` = **`O(n)`**
        - Process half of half of half and so on ...
            - code
                ```
                for(i=n; i>1; i=i/2)
                {
                    //code
                }

                //or while loop

                while(i>1)
                {
                    //code
                    i = i/2;
                }
                ```
            - **`O(log n)`** (base 2)
    - **Linked List**
        - It is same as array. We will see more about it later

    - **Matrix Operations**
        - Process each element in a matrix once
            - code
                ```
                for(i=0; i<n; i++)
                {
                    for(j=0; j<n; j++)
                    {
                        //code
                    }
                }
                ```
            - **O(n^2)**
    - **Array of Linked List**
        ```
        ---     +---+       +---+---+     +---+---+     
         |      | x | ----> | 2 |   | --> | 6 |   | --> ... 
         |      +---+       +---+---+     +---+---+ 
         m      | x | ----> | 9 |   | --> | 5 |   | --> ...
         |      +---+       +---+---+     +---+---+ 
         |      | x | ----> | 1 |   | --> | 8 |   | --> ...
        ---     +---+       +---+---+     +---+---+ 

            | ------------- n ------------------------------|
        ```
        - Process all the elements
            - **`O(m + n)`** 

    - **Binary Tree**
        -  If you process from bottom to top yoiu notice that the number of nodes is becoming half of half of half and so on
            - **`O(log n)`**
        - If you want to analyze all nodes
            - **`O(log n)`**

#### 02. Space Complexity
    - Amount of space consumed in main memory during execution of program
    | Data type | Complexity |
    | --- | --- |
    | list | O(n) |
    | linked list | 2n = O(n) |
    | matrix | n^2 |
    | tree | O(n) |

#### 03. Time and Space Complexity from Code