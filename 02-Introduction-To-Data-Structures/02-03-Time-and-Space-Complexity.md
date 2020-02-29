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

            |--------------------- n ------------------------|
        ```
        - Process all the elements
            - **`O(m + n)`** 

    - **Binary Tree**
        -  If you process from bottom to top yoiu notice that the number of nodes is becoming half of half of half and so on
            - **`O(log n)`**
        - If you want to analyze all nodes
            - **`O(log n)`**

#### 02. Space Complexity

Amount of space consumed in main memory during execution of program

| Data type | Complexity |
| --- | --- |
| list | O(n) |
| linked list | 2n = O(n) |
| matrix | n^2 |
| array of linked list | O(m+n) |
| tree | O(n) |

#### 03. Time and Space Complexity from Code

- A *simple satemen*t may have *arithematic operations*, *conditionals* or *assignment operations.* 
- We assume every *simple statement* in a a program takes *one unit* of time

**Finding Time Function and Time Complexity**

- Let us see function 1 - swapping two variables
    ```
    void swap(int x, int y)
    {
        int t;
        t = x; // 1 unit of time
        x = y; // 1 unit of time
        y = t; // 1 unit of time
    }
    ```
    - Time Function = 1 + 1 + 1 = 3 
        ```
        f(n) = 3 
        ```
    - Time Complexity: It is the `n` to the power of it's degree in the time function.
        - Here, `f(n) = 3 * n^0`
            ```
            n^0 = 1 //constant
            ```
            i.e
            ```
            O(1)
            ```

- Function 2 - Sum of all elements in an array
    ```
    int sum(int A[], int n)
    {
        int s, i;
        s = 0;                  // 1 unit of time

        for (i=0; i<n; i++)     // i = 0 : 1 unit of time
                                // i < n : (n + 1) units of time (True `n` times false `1` time)
                                // i++   : n units of time
                                // -------------------------------------------------------------
                                // Total : (n + 1) or 2(n+1) units of time

        {                   
            s = s + A[i];       // n units of time
        }
        return s;               // 1 unit of time
    }
    ```
    > Note: For `for (i=0; i<n; i++) ` many literatures say `n+1` units of timw instead of actual `2(n+1)` units of time.

    - Time function
        ```
        f(n) = 1 + (n+1) + n + 1
             = 2n + 3
        ```
    - Time Complexity: It is the `n` to the power of it's degree in the time function.
        ```
        n^1 = n
        ```
        i.e
        ```
        O(n)
        ```
    > Note: You can even find time complexity simply by knowing the process. Here the function finds sum of all elements. So, it has to process all the elements of the array atleast once i.e time complexity `O(n)`

- Function 3 - Add two matrices
    ```
    void Add(int n)
    {
        int i, j;
        for (i=0; i<n; i++)                     // (n+1) units of time
        {
            for (j=0; j<n; j++)                 // n * (n+1)
            {
                C[i][j] = A[i][j] + B[i][j];    // n * n
            }
        }
    }
    ```
    - Time function
        ```
        f(n) = (n+1) + n(n+1) + (n*n)
             = 2n^2 + 2n + 1
        ```
    - Time complexity - higest degree
        ```
        n^2
        ```
        i.e
        ```
        O(n^2)
        ```
    > Note you can call `O()` *Order-of* or *Big-Oh*

- Code snippet
    ```
    func1()             
    {
        func2(); // n
    }

    func2()
    {
        for (i=0; i<n; i++) //Total order: n
        {
            //code
        }
    }
    ```
    - Order of func1: `O(n)`
    > *for-loop* or *while-loop* both work in the same way with their own complexity 

- Similarly we can write *space functions* and derive *space complexity*

