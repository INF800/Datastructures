## Sum of Natural Numbers

- **Step 1 :** Alaways write a recursive func and then convert it into code

    - sum(n) = `1 + 2 + 3 + 4 + ... + (n-1)` + n
    - sum(n) = `sum(n-1)` + n

- **Step 2 :** Write it along with base condition (usually a constant)

    ```
             +-----> 0          if n=0 
             |
    sum(n) --+
             |
             +-----> sum(n-1)   if n>0
    ```

    ```
    // Note: As this is a tail recursion,
    // we can convert it into while-loop

    // complexity
    //  - time  : 
    //  - space : 
    int sumOf(int n)
    {
        if (n==0)
        {
            return 0;
        }
        else
            return sumOf(n-1) + n;

    }

    ```
- **Step 3 :** Check if the process can be made more efficient
    - Yes, it can be done using
        
        - **For Loop** (Note all loops are same)
            ```
            int effSumOf(int n)
            {
                int i, s=0;             // 1 unit of time

                for (i=0; i<n; i++)     // genrally, n+1 units of timw
                {
                    s = s + 1           // n units of time (main one)
                }

                return s                // 1 unit of time
            }
            ```
            ```
            Time Complexity: O(n)
            Space Complexity: 3 int-size
            ```
        - **While Loop** (Note, all tail recursions can be intutively written as a while loop)
            ```
            int efficientSumOf(int n)
            {
                if (n==0)                   
                {
                    return 0;
                }

                while (n>0)
                {
                    return efficientSumOf(n-1) + 1;
                }
            }
            ```
            ```
            Time comlexity: O(n) (Only Ascending, but same time complexity as recursion)
            ```
        - **Formula**
            ```
            int sumOf(int n)
            {
                return n * ( n + 1) / 2;
            }
            ```
            ```
            Number of operations: 3  i.e *, + and /
            Time complexity: O(1)
            ```
