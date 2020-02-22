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

    - We pass **Address** of *actual-parametes* into *formal-parmeters*. Formal parametes must be declared as **POINTERS** (As they must be capable of accepting addresses.)

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


# 08. Arrays as Parameters

```
void display(int A[], int n)
{
    int i;
    for (i=0, i<n; i++)
        print("%d", A[i]);
}

int maiN()
{
    int arr[5] = {2, 4, 6, 8, 10};
    dispaly( arr, 5);
}
```

- In *declaration,* array should be given empty square brackets `A[ ]`
    - To distinguish it from a simple variable
    - Empty as the function cannot know the size of array beforehand. (Which will be decided in main function.)
    - Note that `A[ ]` is like **Pointer** to array. Not an array

- *Whether in C/C++ Array can only be passed by address!!!*

In above code, array `arr` is passed by address(always) and  variable `n` is passed by value 
```
    A                        n
    +------+                 +------+
    |  200 |                 |  5   |
    +------+                 +------+
       |
       |
       |
       V
    +------+------+------+------+------+
arr |  02  |  04  |  06  |  08  |  10  |
    +------+------+------+------+------+
     200
```

Note: We can use `*A` instead of `A[]` in `void display(int A[], int n)`. It means address variable `A` can point to **any data-type**. If we we write `A[]` we specifically mean address variable `A` points to an **array data-type**.

- If I make changes to array inside function, it will make changes to the original array (As always passed by address)

- **Functions returning an Array**

    ```
    // `int []` means return type of `integer-array`
    // We can even write -
    // `int * func( int n )`
    // But it won't specifically mean an array

    int [] func(int n)
    {
        int *p;                                 // declare a pointer variable 
        p = (int *) malloc( n * sizeof(int) )   // create array in heap and get it's address
        return p                                // return address of array in heap

        // once `RETURNED`, the memory allocated to this
        // function gets destroyed.
    }

    int main()
    {
        int *A;         // address variable created

        A = func(5)     // "address" of a data-type
                        // returned by `func(5)` is stored in `A`
    }
    ```

    Now we can access the array in heap using -
    ```
    *A[ 10 ] // or `A[10]`? No I guess.
    ```

# 10. Structures as Parameters

- Structures can be *called-by-value* or *called-by-address* or *called-by-reference* as per our requirements. Unlike arrays which are always *called-by-address*

- **Call by Value**
```
struct Rectangle
{
    int length;
    int breadth;
};

// calculates are by length*breadth

int area( struct Rectangle r1 )
{
    // if I make any changes to r1.length,
    // `r.length` in main() remains intact and same.

    return ( r1.length * r1.breadth )
}

int main()
{
    struc Rectangle r = {10, 5}
    printf("Area is %d", area(r) ) // sending the Recangle itself

}
```

- **Call by Reference** (C++ Only)

    - *Call* using same
        ```
        area(r)
        ```
    
    - But, in *declaration* use `&` -
        ```
        int area(struct Rectangle &r1 )
        ```
    - *Definition-body* remains same.

- **Call by Address**

    - Pass structure address `&` in *call* and use pointers `*` in *declaration* to catch the variable at address
    - In *definition-body* use `*`

    ```
    struct Rectangle
    {
        int length;
        int breadth;
    };

    void changeLength( struct Rectangle *p )
    {
        (*p).length = 0; // Note Precedence

        // or use
        p -> length = 0;
    }

    int main()
    {
        struct Rectangle r = {10, 5}
        changeLength(&r);
        print("changed length is %d", r.lenth)
    }
    ```

- **What if an `Array` is present insisde structure?**

    - We cannot pass an individual Array in *call-by-value*. Only *call-by-address* is supported. 
    - **But** we can pass an Array inside a struct by *call-by-value*
