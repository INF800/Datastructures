#### Static Variables in Recursion (Same as Global variables)

Let us consider this function
```
int func (int n)
{
    if (n>0)
    {
        return func(n-1) + n; // gets executed during return time
    }
    return 0
}
```
```
int main()
{
    int a = 5;
    printf("%d", func(a))
}
```

- Both `static` and `global` variables get memory allocated at *code-section* of the memory 
- **Single copy** is maintained through out the exectution of program

-  Let us trace the tree

Recursive call 1
```

                func(5)
                /     \
               /       \
              /         \
           n = 5        func(4) + ___
```
```
Output: <nothing>
```

Recursive call 2
```

                func(5)
                /     \
               /       \
              /         \
            n = 5       func(4) + ___
                        /     \
                       /       \
                      /         \
                    n = 4       func(3) + ___
```
```
Output: <nothing>
```

Recursive call 3
```

                func(5)
                /     \
               /       \
              /         \
         n = 5          func(4) + ___
                        /     \
                       /       \
                      /         \
                 n = 4          func(3) + ___
                                /     \
                               /       \
                              /         \
                          n = 3         func(2) + ___
```
```
Output: <nothing>
```

Recursive call 4
```

                func(5)
                /     \
               /       \
              /         \
          n = 5         func(4) + ___
                        /     \
                       /       \
                      /         \
                  n = 4         func(3) + ___
                                /     \
                               /       \
                              /         \
                          n = 3         func(2) + ___
                                        /     \
                                       /       \
                                      /         \
                                  n = 2         func(1) + ___
```                                         
```
Output: <nothing>
```

Recursive call 5
```

                func(5)
                /     \
               /       \
              /         \
          n = 5         func(4) + ___
                        /     \
                       /       \
                      /         \
                  n = 4         func(3) + ___
                                /     \
                               /       \
                              /         \
                          n = 3         func(2) + ___
                                        /     \
                                       /       \
                                      /         \
                                  n = 2         func(1) + ___
                                                /     \
                                               /       \
                                              /         \
                                          n = 1         func(0) + ___
```                                      
```
Output: <nothing>
```

Recursive call 5 ends
```

                func(5)
                /     \
               /       \
              /         \
          n = 5         func(4) + ___
                        /     \
                       /       \
                      /         \
                  n = 4         func(3) + ___
                                /     \
                               /       \
                              /         \
                          n = 3         func(2) + ___
                                        /     \
                                       /       \
                                      /         \
                                  n = 2         func(1) + ___
                                                /     \
                                               /       \
                                              /         \
                                          n = 1         func(0) + 1    <---------+ 0 + 1 = 1
                                                           |                     |
                                                           |                     |
                                                           |                     |
                                                          [0] -------------------+
```                                      
```
Output: 1
```

Recursive call 4 ends
```

                func(5)
                /     \
               /       \
              /         \
          n = 5         func(4) + ___
                        /     \
                       /       \
                      /         \
                  n = 4         func(3) + ___
                                /     \
                               /       \
                              /         \
                          n = 3         func(2) + ___
                                        /     \
                                       /       \
                                      /         \
                                  n = 2         func(1) + 2    <----------+ 1 + 2 = 3 
                                                /     \                   |
                                               /       \                  |
                                              /         \ ----------------+
                                          n = 1         func(0) + 1    <---------+ 0 + 1 = 1
                                                           |                     |
                                                           |                     |
                                                           |                     |
                                                          [0] -------------------+
```                                      
```
Output: 3
```

Recursive call 3 ends
```

                func(5)
                /     \
               /       \
              /         \
          n = 5         func(4) + ___
                        /     \
                       /       \
                      /         \
                  n = 4         func(3) + ___
                                /     \
                               /       \
                              /         \ 
                          n = 3         func(2) + 3    <----------+ [3] + 3 = 6
                                        /     \                   |
                                       /       \                  |
                                      /         \ ----------------+
                                  n = 2         func(1) + 2    <----------+ [1] + 2 = 3 
                                                /     \                   |
                                               /       \                  |
                                              /         \ ----------------+
                                          n = 1         func(0) + 1    <---------+ [0] + 1 = 1
                                                           |                     |
                                                           |                     |
                                                           |                     |
                                                          [0] -------------------+
```                                      
```
Output: 6
```

Recursive call 2 ends
```

                func(5)
                /     \
               /       \
              /         \
          n = 5         func(4) + ___
                        /     \
                       /       \
                      /         \
                  n = 4         func(3) + 4    <----------+ [6] + 4 = 10
                                /     \                   |
                               /       \                  |
                              /         \ ----------------+
                          n = 3         func(2) + 3    <----------+ [3] + 3 = 6
                                        /     \                   |
                                       /       \                  |
                                      /         \ ----------------+
                                  n = 2         func(1) + 2    <----------+ [1] + 2 = 3 
                                                /     \                   |
                                               /       \                  |
                                              /         \ ----------------+
                                          n = 1         func(0) + 1    <---------+ [0] + 1 = 1
                                                           |                     |
                                                           |                     |
                                                           |                     |
                                                          [0] -------------------+
```                                      
```
Output: 10
```

Recursive call 1 ends
```

                func(5)
                /     \
               /       \
              /         \
          n = 5         func(4) + ___  <----------+ [10] + 5 = 15
                        /     \                   |
                       /       \                  |
                      /         \ ----------------+
                  n = 4         func(3) + 4    <----------+ [6] + 4 = 10
                                /     \                   |
                               /       \                  |
                              /         \ ----------------+
                          n = 3         func(2) + 3    <----------+ [3] + 3 = 6
                                        /     \                   |
                                       /       \                  |
                                      /         \ ----------------+
                                  n = 2         func(1) + 2    <----------+ [1] + 2 = 3 
                                                /     \                   |
                                               /       \                  |
                                              /         \ ----------------+
                                          n = 1         func(0) + 1    <---------+ [0] + 1 = 1
                                                           |                     |
                                                           |                     |
                                                           |                     |
                                                          [0] -------------------+
```                                      
```
Output: 15
```

Recursive to MAIN
```

                func(5)  <----------------+ [15]
                /     \                   |
               /       \                  |
              /         \ ----------------+
          n = 5         func(4) + 5    <----------+ [10] + 5 = 15
                        /     \                   |
                       /       \                  |
                      /         \ ----------------+
                  n = 4         func(3) + 4    <----------+ [6] + 4 = 10
                                /     \                   |
                               /       \                  |
                              /         \ ----------------+
                          n = 3         func(2) + 3    <----------+ [3] + 3 = 6
                                        /     \                   |
                                       /       \                  |
                                      /         \ ----------------+
                                  n = 2         func(1) + 2    <----------+ [1] + 2 = 3 
                                                /     \                   |
                                               /       \                  |
                                              /         \ ----------------+
                                          n = 1         func(0) + 1    <---------+ [0] + 1 = 1
                                                           |                     |
                                                           |                     |
                                                           |                     |
                                                          [0] -------------------+
```                                      
```
Output: 15
```

> Note how output is over-written

#### Now, let us add a static variable to the function

- Static variables and global variables are created inside *code-section* of main memory (Not *stack-section*!!)
- Single copy is maintained.

Let us consider this function *with static variable changes*
```
int func (int n)
{
    static int x = 0            // added
    if (n>0)
    {
        x ++;                   // added
        return func(n-1) + x;   // altered
    }
    return 0
}
```
```
int main()
{
    int a = 5;
    printf("%d", func(a))
}
```

Tracing the tree for above code

Function call from main 
```
// code section - single copy

  x
+---+
| 0 |
+---+
```
```
                func(5)

```
```
Output: <nothing>
```

Recursive call 1
```
// code section - single copy

  x
+---+
| 1 |
+---+
```
```

                func(5)
                /     \
               /       \
              /         \
           x = 1        func(4) + ___
```
```
Output: <nothing>
```

Recursive call 2
```
// code section - single copy

  x
+---+
| 2 |
+---+
```
```

                func(5)
                /     \
               /       \
              /         \
            x = 2       func(4) + ___
                        /     \
                       /       \
                      /         \
                    x = 2       func(3) + ___
```
```
Output: <nothing>
```

Recursive call 3
```
// code section - single copy

  x
+---+
| 3 |
+---+
```
```

                func(5)
                /     \
               /       \
              /         \
         x = 3          func(4) + ___
                        /     \
                       /       \
                      /         \
                 x = 3          func(3) + ___
                                /     \
                               /       \
                              /         \
                          x = 3         func(2) + ___
```
```
Output: <nothing>
```

Recursive call 4
```

                func(5)
                /     \
               /       \
              /         \
          x = 4         func(4) + ___
                        /     \
                       /       \
                      /         \
                  x = 4         func(3) + ___
                                /     \
                               /       \
                              /         \
                          x = 4         func(2) + ___
                                        /     \
                                       /       \
                                      /         \
                                  x = 4         func(1) + ___
```                                         
```
Output: <nothing>
```

Recursive call 5
```

                func(5)
                /     \
               /       \
              /         \
          x = 5         func(4) + ___
                        /     \
                       /       \
                      /         \
                  x = 5         func(3) + ___
                                /     \
                               /       \
                              /         \
                          x = 5         func(2) + ___
                                        /     \
                                       /       \
                                      /         \
                                  x = 5         func(1) + ___
                                                /     \
                                               /       \
                                              /         \
                                          x = 5         func(0) + ___
```                                      
```
Output: <nothing>
```

Recursive call 5 ends
```

                func(5)
                /     \
               /       \
              /         \
          x = 5         func(4) + ___
                        /     \
                       /       \
                      /         \
                  x = 5         func(3) + ___
                                /     \
                               /       \
                              /         \
                          x = 5         func(2) + ___
                                        /     \
                                       /       \
                                      /         \
                                  x = 5         func(1) + ___
                                                /     \
                                               /       \
                                              /         \
                                          x = 5         func(0) + 5    <---------+ [0] + 5 = 5
                                                           |                     |
                                                           |                     |
                                                           |                     |
                                                          [0] -------------------+
```                                      
```
Output: 5
```

Recursive call 4 ends
```

                func(5)
                /     \
               /       \
              /         \
          x = 5         func(4) + ___
                        /     \
                       /       \
                      /         \
                  x = 5         func(3) + ___
                                /     \
                               /       \
                              /         \
                          x = 5         func(2) + ___
                                        /     \
                                       /       \
                                      /         \
                                  x = 5         func(1) + 5    <----------+ [5] + 5 = 10 
                                                /     \                   |
                                               /       \                  |
                                              /         \ ----------------+
                                          x = 5         func(0) + 5    <---------+ [0] + 5 = 5
                                                           |                     |
                                                           |                     |
                                                           |                     |
                                                          [0] -------------------+
```                                      
```
Output: 10
```

Recursive call 3 ends
```

                func(5)
                /     \
               /       \
              /         \
          x = 5         func(4) + ___
                        /     \
                       /       \
                      /         \
                  x = 5         func(3) + ___
                                /     \
                               /       \
                              /         \ 
                          x = 5         func(2) + 5    <----------+ [10] + 5 = 15
                                        /     \                   |
                                       /       \                  |
                                      /         \ ----------------+
                                  x = 5         func(1) + 5    <----------+ [5] + 5 = 10
                                                /     \                   |
                                               /       \                  |
                                              /         \ ----------------+
                                          x = 5         func(0) + 5    <---------+ [0] + 5 = 5
                                                           |                     |
                                                           |                     |
                                                           |                     |
                                                          [0] -------------------+
```                                      
```
Output: 15
```

Recursive call 2 ends
```

                func(5)
                /     \
               /       \
              /         \
          x = 5         func(4) + ___
                        /     \
                       /       \
                      /         \
                  x = 5         func(3) + 5    <----------+ [15] + 5 = 20
                                /     \                   |
                               /       \                  |
                              /         \ ----------------+
                          x = 5         func(2) + 5    <----------+ [10] + 5 = 15
                                        /     \                   |
                                       /       \                  |
                                      /         \ ----------------+
                                  x = 5         func(1) + 5    <----------+ [5] + 5 = 10
                                                /     \                   |
                                               /       \                  |
                                              /         \ ----------------+
                                          x = 5         func(0) + 5    <---------+ [0] + 5 = 5
                                                           |                     |
                                                           |                     |
                                                           |                     |
                                                          [0] -------------------+
```                                      
```
Output: 20
```

Recursive call 1 ends
```

                func(5)
                /     \
               /       \
              /         \
          x = 5         func(4) + 5    <----------+ [20] + 5 = 25
                        /     \                   |
                       /       \                  |
                      /         \ ----------------+
                  x = 5         func(3) + 5    <----------+ [15] + 5 = 20
                                /     \                   |
                               /       \                  |
                              /         \ ----------------+
                          x = 5         func(2) + 5    <----------+ [10] + 5 = 15
                                        /     \                   |
                                       /       \                  |
                                      /         \ ----------------+
                                  x = 5         func(1) + 5    <----------+ [5] + 5 = 10 
                                                /     \                   |
                                               /       \                  |
                                              /         \ ----------------+
                                          x = 5         func(0) + 5    <---------+ [0] + 5 = 5
                                                           |                     |
                                                           |                     |
                                                           |                     |
                                                          [0] -------------------+
```                                      
```
Output: 25
```

Recursive to MAIN
```

                func(5)  <----------------+ [25] 
                /     \                   |
               /       \                  |
              /         \ ----------------+
          x = 5         func(4) + 5    <----------+ [20] + 5 = 25
                        /     \                   |
                       /       \                  |
                      /         \ ----------------+
                  x = 5         func(3) + 5    <----------+ [15] + 5 = 20
                                /     \                   |
                               /       \                  |
                              /         \ ----------------+
                          x = 5         func(2) + 5    <----------+ [10] + 5 = 15
                                        /     \                   |
                                       /       \                  |
                                      /         \ ----------------+
                                  x = 5         func(1) + 5    <----------+ [5] + 5 = 10 
                                                /     \                   |
                                               /       \                  |
                                              /         \ ----------------+
                                          x = 5         func(0) + 5    <---------+ [0] + 5 = 5
                                                           |                     |
                                                           |                     |
                                                           |                     |
                                                          [0] -------------------+
```                                                                         
```
Output: 25
```

- Note how single copy of `x` is maintained 

#### Global variable
- If we remove `static` and declare `x` as a global variable (as in below code), result of the function will be EXACTLY same
    ```
    int x = 0;  // Note
    int func (int n)
    {
        if (n>0)
        {
            x ++;                  
            return func(n-1) + x;  
        }
        return 0
    }
    ```