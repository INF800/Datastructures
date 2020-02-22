#### 06. Functions

-  Parameter Passing
    - 1. Pass by Value (C / C++)
    - 2. Pass by Address (C / C++)
    - 3. Pass by Reference (Only C++)

- Function is a group of related instructions (like structure is a group of related data members)

**Monolithic Programming:** *Writing the whole code in single main function.*
    - Low Productivity (Only a single person can write the program)
    - Low Reusability 

**Modular Programming:** *Writing the whole code in cohesive modules using functions.*
    - High Productivity (A team singl can write the program)
    - High Reusability 

> C programs are Modular.

> C++ is even one step ahead - OOPs

Example,
```
int add(int a, int b)
{
    int c;
    c = a + b;
    return (c)
}

int main()
{
    int x, y, z;
    x = 10;
    y = 5;
    z = add(x, y);
    printf("the sum is %d", z);
}
```
- **Termnology**

    - `Prototype` (`Signature` of a function). It is `Declaration` of a function:
    ```
    int add(int a, int b)
    ```

    - `Definition` of a function:
    ```
    {
        int c;
        c = a + b;
        return (c)
    }
    ```
    
    - The variables we are passing to function during function call are called `actual parameters`
    ```
    z = add(x, y);
    ```
    `x` and `y` are actual parameters

    - The variables that are used in function *declaration* are called `formal parameters`
    ```
    int add(int a, int b)
    ```
    `a` and `b` are formal parameters.

    - When function is called, values of *actual parameters* is **copied** in *formal parameters*

    main function starts:
    ```
                ------[Main Memory------]
                +-----------------------+ -------
                |                       |    |
                |                       |  [Heap]
                |                       |    |
                +-----------------------+ -------
                |                       |    | 
                |                       |    |
                +-----------------------+    |
    stack frame |   <not-yet-created>   |  [Stack] 
    `add` func  |                       |    |
                |-----------------------|    |
    stack frame |    x[10]  y[10] c[ ]  |    |
    `main` func |                       |    |
                +-----------------------+ --------
                |    Machine codes of   |    |
                |    functions          |    |
                |                       |    |
                |    add .........      |    |
                |    .............      |    |
                |                       |    |
                |    main .........     |    |
                |    ..............     |  [Code]
                |    ..............     |    |
                |                       |    |
                +-----------------------+ --------
                ------[Main Memory------]
    ```
    Note: satck-frame of main() cannot access stack-frame of `add()` as they are local to it.
    
    `main()` calls `add()`. Values are copies and result copied
    ```
                    ------[Main Memory------]
                +-----------------------+ -------
                |                       |    |
                |                       |  [Heap]
                |                       |    |
                +-----------------------+ -------
                |                       |    | 
                |                       |    |
                +-----------------------+    |
                |   a[10]  b[10]  c[20] |  [Stack] 
                |                  |    |    |
                |------------------V----|    |
                |   x[10]  y[10] z[20]  |    |
                |                       |    |
                +-----------------------+ --------
                |    Machine codes of   |    |
                |    functions          |    |
                |                       |    |
        +-----------> add .........     |    |
        |       |     .............     |    |
        |       |                       |    |
        +----------- main .........     |    |
                |    ..............     |  [Code]
                |    ..............     |    |
                |                       |    |
                +-----------------------+ --------
                ------[Main Memory------]
    ```

    When main function continues after function call, stac-frame of add() is destroyed.
    ```
                    ------[Main Memory------]
                +-----------------------+ -------
                |                       |    |
                |                       |  [Heap]
                |                       |    |
                +-----------------------+ -------
                |                       |    | 
                |                       |    |
                +-----------------------+    |
                |       <destroyed>     |  [Stack] 
                |                       |    |
                |-----------------------|    |
                |   x[10]  y[10] z[20]  |    |
                |                       |    |
                +-----------------------+ --------
                |    Machine codes of   |    |
                |    functions          |    |
        Note arrow!                     |    |
        +-----------  add .........     |    |
        |       |     .............     |    |
        |       |                       |    |
        +----------> main .........     |    |
                |    ..............     |  [Code]
                |    ..............     |    |
                |                       |    |
                +-----------------------+ --------
                ------[Main Memory------]
    ```

# 07. Parameter Passing

- They are three types
    - Pass by Value
    - Pass by Address
    - Pass by Reference (Only C++)

    To better understand let us see from this *call-by-value* example:
    ```
    void swap(int x, int y)
    {
        int temp;
        temp = x;
        x = y;
        y = temp;
    }

    int main()
    {
        int a, b;
        a = 10;
        b = 20;
        swap(a, b)
        print("a = %d, b = %d", a, b)       
    }
    ```

- **Call by Value**

    We pass **Copies** of *actual-parametes* into *formal-parmeters*
    
    In main()
    ```
        int a, b;
        a = 10;
        b = 20;
    ```
    ```
                    +=============+=============+=============+
                    |                <heap>                   |
                    |                                         |
                    +=============+=============+=============+ ----
     swap()         |                                         |  |
     stack-frame    |                                         |  | 
                    |         <not-yet-allocated>             |  |
                    |                                         |  |
                    |                                         |  |
                    |-----------------------------------------| <stack>
    main()          |                                         |  |
    stack-frame     |     a           b                       |  |
                    |   +----+      +----+                    |  |
                    |   | 10 |      | 20 |                    |  |
                    |   +----+      +----+                    |  |  
                    |   200/201      202/203                  |  |
                    +=============+=============+=============+ ----
    ```
    
    In main:
    ```
    swap(a,b)
    ```
    In swap:
    ```
    void swap(int x, int y)
    ```
    ```
                    +=============+=============+=============+
                    |                <heap>                   |
                    |                                         |
                    +=============+=============+=============+ 
                    |                                         |
      swap          |     x           y                       |  
                    |   +----+      +----+                    | 
                    |   | 10 |      | 20 |                    |
                    |   +----+      +----+                    |  
                    |                                         |
                    |-----------------------------------------|
      main          |                                         |
                    |     a           b                       |  
                    |   +----+      +----+                    | 
                    |   | 10 |      | 20 |                    |
                    |   +----+      +----+                    |  
                    |    201/202    203/204                   |
                    +=============+=============+=============+
    ```

    In main:
    ```
    swap(a,b)
    ```
    In swap:
    ```
    temp = x;
    ```
    ```
                    +=============+=============+=============+
                    |                <heap>                   |
                    |                                         |
                    +=============+=============+=============+ 
                    |                                         |
      swap          |     x           y          temp         |  
                    |   +----+      +----+      +----+        | 
                    |   | 10 |      | 20 |      | 10 |        |
                    |   +----+      +----+      +----+        |  
                    |                                         |
                    |-----------------------------------------|
      main          |                                         |
                    |     a           b                       |  
                    |   +----+      +----+                    | 
                    |   | 10 |      | 20 |                    |
                    |   +----+      +----+                    |  
                    |    201/202    203/204                   |
                    +=============+=============+=============+
    ```

    In swap
    ```
        temp = x;
        x = y;
        y = temp;
        // end of swap
    ```
    ```
                    +=============+=============+=============+
                    |                <heap>                   |
                    |                                         |
                    +=============+=============+=============+ 
                    |                                         |
      swap          |     x           y          temp         |  
                    |   +----+      +----+      +----+        | 
                    |   | 20 |      | 10 |      | 10 |        |
                    |   +----+      +----+      +----+        |  
                    |                                         |
                    |-----------------------------------------|
      main          |                                         |
                    |     a           b                       |  
                    |   +----+      +----+                    | 
                    |   | 10 |      | 20 |                    |
                    |   +----+      +----+                    |  
                    |    201/202    203/204                   |
                    +=============+=============+=============+
    ```

    In main()
    ```
    print("a = %d, b = %d", a, b) 
    ```
    ```
                    +=============+=============+=============+
                    |                <heap>                   |
                    |                                         |
                    +=============+=============+=============+ 
                    |                                         |
      swap          |           <destroyed>                   |
                    |                                         |
                    |-----------------------------------------|
      main          |                                         |
                    |     a           b                       |  
                    |   +----+      +----+                    | 
                    |   | 10 |      | 20 |                    |
                    |   +----+      +----+                    |  
                    |    201/202    203/204                   |
                    +=============+=============+=============+
    ```
    Output in console
    ```
    a = 10, b = 20
    ```

    - When we *pass by value*,  `a` and `b` are not swapped at all. 
    - Any changes to *formal params* doesn't affect *actual params*

- **Call by Address**

    - We pass **Address** of *actual-parametes* into *formal-parmeters*. Formal parametes must be **POINTERS** (As they must be capable of accepting addresses.)

    - How to write
        - while *calling*,
            ```
            swap(&a, &b);
            ```
        - while accepting in *declaration*
            ```
            void swap(int *x, int *y);
            ```
        - In *definition*, put `*` before all `formal-params` as they are addresses. We are performin operations on *values-at-formal-params* i.e
        
            This code in *call-by-value*
            ```
            {
                int temp;
                temp = x;
                x = y;
                y = temp;
            }
            ```
        
            Turns into this in *call-by-addr*
            ```
            {
                int temp;
                temp = *x;
                *x = *y;
                *y = temp;
            }
            ```

        - Everything else is same as *Call By Value* code.
            ```
            void swap(int *x, int *y)
            {
                int temp;
                temp = *x;
                *x = *y;
                *y = temp;
            }

            int main()
            {
                int a, b;
                a = 10;
                b = 20;
                swap(&a, &b)
                print("a = %d, b = %d", a, b)       
            }
            ```

    - How it works?

        In main()
        ```
            int a, b;
            a = 10;
            b = 20;
        ```
        ```
                        +=============+=============+=============+
                        |                <heap>                   |
                        |                                         |
                        +=============+=============+=============+ ----
        swap()          |                                         |  |
        stack-frame     |                                         |  | 
                        |         <not-yet-allocated>             |  |
                        |                                         |  |
                        |                                         |  |
                        |-----------------------------------------| <stack>
        main()          |                                         |  |
        stack-frame     |     a           b                       |  |
                        |   +----+      +----+                    |  |
                        |   | 10 |      | 20 |                    |  |
                        |   +----+      +----+                    |  |  
                        |   200/201      202/203                  |  |
                        +=============+=============+=============+ ----
        ```

        In main:
        ```
        swap(&a, &b)
        ```
        In swap:
        ```
        void swap(int *x, int *y)
        ```
        ```
                        +=============+=============+=============+
                        |                <heap>                   |
                        |                                         |
                        +=============+=============+=============+ 
                        |                                         |
        swap            |     x           y                       |  
                        |   +----+      +----+                    | 
                        |   | 200|      | 202|                    |
                        |   +----+      +----+                    |  
                        |     |           |                       |
                        |-----|-----------|-----------------------|
        main            |     V           V                       |
                        |     a           b                       |  
                        |   +----+      +----+                    | 
                        |   | 10 |      | 20 |                    |
                        |   +----+      +----+                    |  
                        |    200/201    202/203                   |
                        +=============+=============+=============+
        ```
        **Note:** One function cannot access variables of another function **directly**. But like here, it can access them indirectly using addresses.

        In main:
        ```
        swap(&a, &b)
        ```
        In swap:
        ```
        temp = *x;
        ```
        ```
                        +=============+=============+=============+
                        |                <heap>                   |
                        |                                         |
                        +=============+=============+=============+ 
                        |                                         |
        swap            |     x           y          temp         |  
                        |   +----+      +----+      +----+        | 
                        |   | 200|      | 202|      |  10|        |
                        |   +----+      +----+      +----+        |  
                        |     |           |                       |
                        |-----|-----------|-----------------------|
        main            |     V           V                       |
                        |     a           b                       |  
                        |   +----+      +----+                    | 
                        |   | 10 |      | 20 |                    |
                        |   +----+      +----+                    |  
                        |    200/201    202/204                   |
                        +=============+=============+=============+
        ```

        In swap
        ```
        temp = *x;
        *x = *y;
        *y = temp;
        // end of swap
        ```
        **Note:** We are not performing operations on addresses. We are performing operations on *values-at* (`*`) addresses! 
        ```
                        +=============+=============+=============+
                        |                <heap>                   |
                        |                                         |
                        +=============+=============+=============+ 
                        |                                         |
        swap            |     x           y          temp         |  
                        |   +----+      +----+      +----+        | 
                        |   | 200|      | 202|      | 10 |        |
                        |   +----+      +----+      +----+        |  
                        |     |           |                       |
                        |-----|-----------|-----------------------|
        main            |     V           V                       |
                        |     a           b                       |  
                        |   +----+      +----+                    | 
                        |   | 20 |      | 10 |                    |
                        |   +----+      +----+                    |  
                        |    200/201    202/204                   |
                        +=============+=============+=============+
        ```
        
        In main()
        ```
        print("a = %d, b = %d", a, b) 
        ```
        Note: Only address variable are destroyed not the variables containing data!
        ```
                        +=============+=============+=============+
                        |                <heap>                   |
                        |                                         |
                        +=============+=============+=============+ 
                        |                                         |
        swap          |           <destroyed>                   |
                        |                                         |
                        |-----------------------------------------|
        main          |                                         |
                        |     a           b                       |  
                        |   +----+      +----+                    | 
                        |   | 20 |      | 10 |                    |
                        |   +----+      +----+                    |  
                        |    200/201    202/204                   |
                        +=============+=============+=============+
        ```
        Output in console
        ```
        a = 20, b = 10
        ```

        - Values swapped !!!
        - Actual values are modified! we will be using this kind. They are more useful.

- **Call by Reference** (ONLY C++)

    - We pass **Address** of *actual-parametes* into *formal-parmeters*. Formal parametes must be **POINTERS** (As they must be capable of accepting addresses.)

    - How to write
        - Don't make changes while *calling* actual parameters
            ```
            swap(a, b);
            ```
        - Don't make changes in *definition-body*
        - But in function definition write `&` before *formal-params*
            ```
            void swap(int &x, int &y)
            {
                ....
            }
            ```
        - Whole code
            ```
            void swap(int &x, int &y) // the only change
            {
                int temp;
                temp = x;
                x = y;
                y = temp;
            }

            int main()
            {
                int a, b;
                a = 10;
                b = 20;
                swap(a, b)
                print("a = %d, b = %d", a, b)       
            }
            ```


    - How it works?

        - Variables are created in *main()* function's stack frame. The same *main-stack-frame's* variables are refered to by *swap()* function

            ```
            a or x         b or y        
            +----+         +----+    
            | 20 |         | 10 |   
            +----+         +----+     
            200/201       202/204 
            ```
        - So, this modifies main function's *actual-params* as well! (Just like call-by-address)
        - We mentioned - One function cannot access varibles of another function directly. It can access them indirectly. But how come it can access the variables **directly** here?

        > If you notice, `swap()` is not a separate body of function. It became a part of `main()` function. 
        
        >It is possible as C++ will paste machine code of swap() inside main() when it sees `&` symbol in function declaration. It is more like *Monolithic* program.

        > Souce code is *procedural* or *Modular*. But MACHINE CODE is *Monolithic*!

        > C doesn't do this but C++ does it. Is it advisable to do it? Should it be entertained? **No!** Use it only for simple and small functions or if you are forced to. 

        > Use it carefully.

        > Looks easy to write source-code but will make compiling process complicted. That's why C++ has both call by address as well as call by reference