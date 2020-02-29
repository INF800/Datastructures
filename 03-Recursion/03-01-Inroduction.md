#### Recursion

- What is Recursion
- Recursion Example
- Tracing Recursion
- Stack used in Recursion
- Time complexity
- Recurrance Relation

#### 01. What is Recursion
- A function calling itself
    ```
    type func (param)
    {
        if (<base-condition>)
        {
            ...
            ...

            func(param)

            ...
            ...
        }
    }
    ```
 - There must be a *base-condition* to terminate recursion. Otherwise, it will go into infinite calling

**Example**

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

**Tracing a Recursive function - Tracing tree of Recursive function**

- Reursion functions are traced in the form of *a tree*.
- Let us trace the above recursive function

Recursive call 1
```

                func(3)
                /     \
               /       \
              /         \
             3          func(2)
```
```
Output: 3
```

Recursive call 2
```

                func(3)
                /     \
               /       \
              /         \
             3          func(2)
                        /     \
                       /       \
                      /         \
                     2          func(1)
```
```
Output: 32
```

Recursive call 3
```

                func(3)
                /     \
               /       \
              /         \
             3          func(2)
                        /     \
                       /       \
                      /         \
                     2          func(1)
                                /     \
                               /       \
                              /         \
                             1          func(0)
                                          |
                                          |
                                         [X]
```
```
Output: 321
```

Recursive call 3 end
```

                func(3)
                /     \
               /       \
              /         \
             3          func(2)
                        /     \
                       /       \
                      /         \
                     2          func(1) <-----------+ 
                                /     \             |
                               /       \            |
                              /         \           |
                             1          func(0) ----+ memory-destroyed
                                          |
                                          |
                                         [X]
```
```
Output: 321
```

Recursive call 2 end
```

                func(3)
                /     \
               /       \
              /         \
             3          func(2) <-------------+
                        /     \               |
                       /       \              |
                      /         \ ------------+ memory-destroyed            
                     2          func(1) <-----------+
                                /     \             |
                               /       \            |
                              /         \           |
                             1          func(0) ----+ memory-destroyed
                                          |
                                          |
                                         [X]
```
```
Output: 321
```


Recursive call 2 end
```

                func(3) <-------------+
                /     \               |
               /       \              |
              /         \ ------------+ memory-destroyed
             3          func(2) <-------------+
                        /     \               |
                       /       \              |
                      /         \ ------------+ memory-destroyed      
                     2          func(1) <-----------+ 
                                /     \             |
                               /       \            |
                              /         \           |
                             1          func(0) ----+ memory-destroyed
                                          |
                                          |
                                         [X]
```
```
Output: 321
```

# NOW NOTE THIS INTERESTING DIFFERENCE

- Let us make some minor changes to to `func` above and call it `func2`
```
void func2 (int n)
{
    if (n>0)
    {
        func2(n-1);
        print("%d", n);
    }
}
```
```
void main()
{
    int x = 3;
    func2(x);
}
```

> Note: `print` statement is written after recursive call unlike in `func1`. So, output will be printed (or any other execution) only after recursive call ends!!

Recursive call 1
```

                func2(3)
                /     \
               /       \
              /         \
      <waiting>         func(2)
```
```
Output: <nothing>
```

Recursive call 2
```

                func2(3)
                /     \
               /       \
              /         \
      <waiting>         func2(2)
                        /     \
                       /       \
                      /         \
              <waiting>         func2(1)
```
```
Output: <nothing>
```

Recursive call 3
```

                func2(3)
                /     \
               /       \
              /         \
      <waiting>         func2(2)
                        /     \
                       /       \
                      /         \
              <waiting>         func2(1)
                                /     \
                               /       \
                              /         \
                      <waiting>         func2(0)
                                          |
                                          |
                                         [X]
```
```
Output: <nothing>
```

Recursive call 3 ends
```

                func2(3)
                /     \
               /       \
              /         \
      <waiting>         func2(2)
                        /     \
                       /       \
                      /         \
              <waiting>         func2(1) <--------------+
                                /     \                 |
                               /       \                |
                              /         \               |
                            1           func2(0) -------+
                                          |
                                          |
                                         [X]
```
```
Output: 1
```

Recursive call 2 ends
```

                func2(3)
                /     \
               /       \
              /         \
      <waiting>         func2(2) <--------------+
                        /     \                 |
                       /       \                |
                      /         \ --------------+
                     2          func2(1) <--------------+
                                /     \                 |
                               /       \                |
                              /         \               |
                            1           func2(0) -------+
                                          |
                                          |
                                         [X]
```
```
Output: 12
```

Recursive call 1 ends
```

                func2(3) <-------------+
                /     \                |
               /       \               |
              /         \ -------------+
             3          func2(2) <--------------+
                        /     \                 |
                       /       \                |
                      /         \ --------------+
                     2          func2(1) <--------------+
                                /     \                 |
                               /       \                |
                              /         \               |
                            1           func2(0) -------+
                                          |
                                          |
                                         [X]
```
```
Output: 123
```

**Note:** This time output is 
```
123
```
instead of
```
321
```
in `func1`

> Note how recursive function is waiting! You can write any code instead of simple print and make use of the logic in your algorithm
> Recursive functions are just like *rubber-band* first it ascends and then it descends.


# Generalizing Recursion

- We can generalize recursion code as

    ```
    void func (int n)
    {
        if (n>0)
        {
            1. .....      // code executed on CALL time ----> ASCENDING PHASE
            2. func(n-1)  // recursive call
            3. .....      // code executed on RETURN time ----> DESCENDING PHASE
        }
    }
    ```

- If there is any compution is there in the line of recursion call, they also will be executed during return time. For example
    ```
    int func (int n)
    {
        if (n>0)
        {
            1. .....      
            2. func(n-1) * 2 // `*2` executed on RETURN time
            3. .....      
        }
    }
    ```

**Difference Between Loop and Recursion**

| Phase | Recursion | Looop |
| --- | --- | --- |
| Ascending Phase | Available | Available |
| Descending Phase | Available | na |