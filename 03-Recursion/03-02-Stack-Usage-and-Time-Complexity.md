#### How Recursion Uses Stack

Let us take ascending recursion as an example
```
 void func1 (int n)
 {
    if (n>0)
    {
        print("%d", n);
        func1(n-1);
    }
 }
```
```
 void main()
 {
     int x = 3;
     func1(x);
 }
```

- We already know the model of memory. Memory is divided into 3 sections *heap*, *stack* and *code* sections. 

- Right after compilation, machine code is stored in *code* section of memory

- *stack* and *heap* sections are shown below
    ```
                    step1                                   step 2                         step3                           step 4 and 5

                    +=============+=============+           +=============+=============+  +=============+=============+   +=============+=============+         
                    |           <heap>          |           |           <heap>          |  |           <heap>          |   |           <heap>          |
                    |                           |           |                           |  |                           |   |                           |
                    +=============+=============+  ---      +=============+=============+  +=============+=============+   +=============+=============+ 
    func1           |    <not-yet-created>      |   |       |    <not-yet-created>      |  |    <not-yet-created>      |   | [0]                       |
                    |                           |   |       |                           |  |                           |   |  n                        |
                    +---------------------------+   |       +---------------------------+  +---------------------------+   +---------------------------+ 
    func1           |    <not-yet-created>      |   |       |    <not-yet-created>      |  |    <not-yet-created>      |   | [1]                       |
                    |                           |   |       |                           |  |                           |   |  n                        |
                    +---------------------------+   |       +---------------------------+  +---------------------------+   +---------------------------+  
    func1           |    <not-yet-created>      |   |       |    <not-yet-created>      |  | [2]                       |   | [2]                       |
                    |                           |   |       |                           |  |  n                        |   |  n                        |
                    +---------------------------+   |       +---------------------------+  +---------------------------+   +---------------------------+
    func1           |    <not-yet-created>      |  stack    | [3]                       |  | [3]                       |   | [3]                       |
                    |                           |   |       |  n                        |  |  n                        |   |  n                        |
                    +---------------------------+   |       +---------------------------+  +---------------------------+   +---------------------------+
    main            | [3]                       |   |       | [3]                       |  | [3]                       |   | [3]                       |
                    |  x                        |   |       |  x                        |  |  x                        |   |  x                        |
                    +=============+=============+  ---      +=============+=============+  +=============+=============+   +=============+=============+

                    main function called                    recursive call 1               recursive call 2                recursive call 3
    ```

    ```
    step 6                         step 7                         step 8                           step 9                   step 10

    +=============+=============+ +=============+=============+ +=============+=============+ +=============+=============+ +=============+=============+ 
    |        <destroyed>        | |        <destroyed>        | |        <destroyed>        | |        <destroyed>        | |        <destroyed>        | 
    |                           | |                           | |                           | |                           | |                           |
    +---------------------------+ +---------------------------+ +---------------------------+ +---------------------------+ +---------------------------+ 
    | [1]                       | |        <destroyed>        | |        <destroyed>        | |        <destroyed>        | |        <destroyed>        | 
    |  n                        | |                           | |                           | |                           | |                           | 
    +---------------------------+ +---------------------------+ +---------------------------+ +---------------------------+ +---------------------------+ 
    | [2]                       | | [2]                       | |        <destroyed>        | |        <destroyed>        | |        <destroyed>        | 
    |  n                        | |  n                        | |                           | |                           | |                           | 
    +---------------------------+ +---------------------------+ +---------------------------+ +---------------------------+ +---------------------------+ 
    | [3]                       | | [3]                       | | [3]                       | |        <destroyed>        | |        <destroyed>        | 
    |  n                        | |  n                        | |  n                        | |                           | |                           | 
    +---------------------------+ +---------------------------+ +---------------------------+ +---------------------------+ +---------------------------+ 
    | [3]                       | | [3]                       | | [3]                       | | [3]                       | |        <destroyed>        | 
    |  x                        | |  x                        | |  x                        | |  x                        | |                           | 
    +---------------------------+ +---------------------------+ +---------------------------+ +---------------------------+ +---------------------------+ 

    recursive call 3 end          recursive call 2 end          recursive call 1 end          main function call end

    ```

    - **NOTE**
    - 4 activation records/stack frames are created one recursive function
    - Memory consumed = 4 x (size of variable in recursive function). Here, `4 x 1int = 4x2 = 8bytes`
    - Total `n+1` calls will be made for above recursive function
    - Time complexity. Deg = 1 (`n+1`)
        ```
        O(n)
        ```
    - Space complexity
        ```
        O(n) (Ignoring main)
        ```
    - Recursive functions are memory consuming!

> For descending recursive call, the procedure for creating activation frames and destroying them will be exactly same. But...,

> Only difference is - ascending recursive function uses the variable created while ascending(creation time itself). Wheras, descending recursive function uses the variable created during descending (just before destroying it.)


#### Time Complexity of Recursive Functions

- We don't mention actual time. We simple use *one-unit-of-time* 
- Let us see for above function

    ```
    void func1 (int n)
    {
        if (n>0)
        {
            print("%d", n);     // n-times * 1 unit of time.
                                // Here, 3*1
            func1(n-1);
        }
    }
    ```
    ```
    void main()
    {
        int x = 3;
        func1(x);
    }
    ```

    - Time Complexity = `O(n)` (from code)

- **Finding time complexity using recurance relation**
    ```
    void func1 (int n)          // T(n) units of time (Let time taken by this func)

    {
        if (n>0)                // 1 unit of time
        {
            print("%d", n);     // 1 unit of time
            func1(n-1);         // T(n-1) units of time
        }
    }
    ```
    - Total time = `T(n)` = `1 + 1 + T(n-1)` 
        ```
        T(n) = T(n-1) + 2
        ```
        ```
                +-->   1        , n < 0 (To check if false)
                |
        T(n) =  |
                |
                +--> T(n-1) + 2 , n>0
        ```
        (Time complexity od recursive function can be represented like recurance relation above)
    
    - This recurance relation can be solved using *induction method* (sucessive substitution method)

        - First, write any constant in your recursive relatoin as `1`
            ```
                    +-->   1        , n < 0
                    |
            T(n) =  |
                    |
                    +--> T(n-1) + 1 , n>0
            ```
        > Note: `2` changed into `1`

        - Now, perform continous successive substitution
            ```
            T(n) = T(n-1) + 1    -------------- 1st
            T(n) = T(n-2) + 2    -------------- 2nd
            T(n) = T(n-3) + 3    -------------- 3rd
            .
            .
            .
            T(n) = T(n-k) + k    --------------- k'th 
            ```
        - Let us assume we reached our base condition on k'th thime.
            - i.e during k'th recursive call, 
                ```
                Assume, T(n-k) = T(0)
                ``` 
                ```
                => n-k = 0
                => n = k
                ```
            - substitute in k'th call
                ```
                T(n) = T(n-n) + k
                     = T(0) + k
                     = 1 + k
                     = 1 + n    (cz, n=k)
                ```
    - Hence, Time complexity - `n` with it's highest deg. `1`
        ```
        O(n)
        ```
> Note: Same result as in tracing tree!
> Note: We are not using notations like *big-oh*, *omega* and *theta*