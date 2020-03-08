## Types of Recursion

4. INDIRECT RECURSION
5. NESTED RECURSION

#### 04. Indirect Recursion

- There may be more than one function, calling one another in a circular fashion

          +--------> func1 ->>----+
          |                       |
          |                       |
          |                       V
        func3 <-------------<<- func2
                        
- Example skeleton,
    ```
    void A(int n)
    {
        if (...)
        {
            ...
            ...
            B(n-1);
        }
    }
    ``` 
    ```
    void B(int n)
    {
        if (...)
        {
            ...
            ...
            A(n-1);
        }
    }
    ```
    ```
    A(10)
    ```

- Let us trace this example,
    ```
    void funcA (int n)
    {
        if (n>0)
        {
            printf("%d", n);
            funcB(n-1);
        }
    }

    void funcB (int n)
    {
        if (n>1)
        {
            printf("%d", n);
            funcA(n/2);
        }
    }

    int main()
    {
        funcA(20);
    }
    ```

**Tracing Tree**
```
            funcA(20)
           /     \
          /       \
        20        funcB(19)
                 /     \
                /       \
              19         funcA(9)
                        /     \
                       /       \
                      9        funcB(8)
                              /     \
                             /       \
                            8        funcA(4)
                                    /     \
                                   /       \
                                  4         funcB(3)
                                            /     \
                                           /       \
                                          3        funcA(1)
                                                  /     \
                                                 /       \
                                                1        funcB(0)
                                                          |
                                                          |
                                                         [x]
```
```
            funcA(20)
           /     \
          /       \
        20        funcB(19)
```
```
output: 20
```
```
            funcA(20)
           /     \
          /       \
        20        funcB(19)
                 /     \
                /       \
              19         funcA(9)
```
```
output: 2019
```
```
            funcA(20)
           /     \
          /       \
        20        funcB(19)
                 /     \
                /       \
              19         funcA(9)
                        /     \
                       /       \
                      9        funcB(8)
```
```
output: 20199
```
```
            funcA(20)
           /     \
          /       \
        20        funcB(19)
                 /     \
                /       \
              19         funcA(9)
                        /     \
                       /       \
                      9        funcB(8)
                              /     \
                             /       \
                            8        funcA(4)
```
```
output: 201998
```
```
            funcA(20)
           /     \
          /       \
        20        funcB(19)
                 /     \
                /       \
              19         funcA(9)
                        /     \
                       /       \
                      9        funcB(8)
                              /     \
                             /       \
                            8        funcA(4)
                                    /     \
                                   /       \
                                  4         funcB(3)
```
```
output: 201998
```
```
            funcA(20)
           /     \
          /       \
        20        funcB(19)
                 /     \
                /       \
              19         funcA(9)
                        /     \
                       /       \
                      9        funcB(8)
                              /     \
                             /       \
                            8        funcA(4)
                                    /     \
                                   /       \
                                  4         funcB(3)
                                            /     \
                                           /       \
                                          3        funcA(1)
```
```
output: 20199843
```
```
            funcA(20)
           /     \
          /       \
        20        funcB(19)
                 /     \
                /       \
              19         funcA(9)
                        /     \
                       /       \
                      9        funcB(8)
                              /     \
                             /       \
                            8        funcA(4)
                                    /     \
                                   /       \
                                  4         funcB(3)
                                            /     \
                                           /       \
                                          3        funcA(1)
                                                  /     \
                                                 /       \
                                                1        funcB(0)
```
```
output: 201998431
```
```
            funcA(20)
           /     \
          /       \
        20        funcB(19)
                 /     \
                /       \
              19         funcA(9)
                        /     \
                       /       \
                      9        funcB(8)
                              /     \
                             /       \
                            8        funcA(4)
                                    /     \
                                   /       \
                                  4         funcB(3)
                                            /     \
                                           /       \
                                          3        funcA(1)
                                                  /     \
                                                 /       \
                                                1        funcB(0)
                                                          |
                                                          |
                                                         [x]
```
```
output: 201998431
```
```
            funcA(20)
           /     \
          /       \
        20        funcB(19)
                 /     \
                /       \
              19         funcA(9)
                        /     \
                       /       \
                      9        funcB(8)
                              /     \
                             /       \
                            8        funcA(4)
                                    /     \
                                   /       \
                                  4         funcB(3)
                                            /     \
                                           /       \
                                          3        funcA(1) <---------+
                                                  /     \             |
                                                 /       \            |
                                                1        funcB(0) ----+
                                                          |
                                                          |
                                                         [x]
```
```
output: 201998431
```
```
            funcA(20)
           /     \
          /       \
        20        funcB(19)
                 /     \
                /       \
              19         funcA(9)
                        /     \
                       /       \
                      9        funcB(8)
                              /     \
                             /       \
                            8        funcA(4)
                                    /     \
                                   /       \
                                  4         funcB(3) <---------+
                                            /     \            |
                                           /       \ ----------+
                                          3        funcA(1) <---------+
                                                  /     \             |
                                                 /       \            |
                                                1        funcB(0) ----+
                                                          |
                                                          |
                                                         [x]
```
```
output: 201998431
```
```
            funcA(20)
           /     \
          /       \
        20        funcB(19)
                 /     \
                /       \
              19         funcA(9)
                        /     \
                       /       \
                      9        funcB(8)
                              /     \
                             /       \
                            8        funcA(4) <--------+
                                    /     \            |
                                   /       \ ----------+
                                  4         funcB(3) <---------+
                                            /     \            |
                                           /       \ ----------+
                                          3        funcA(1) <---------+
                                                  /     \             |
                                                 /       \            |
                                                1        funcB(0) ----+
                                                          |
                                                          |
                                                         [x]
```
```
output: 201998431
```
```
            funcA(20)
           /     \
          /       \
        20        funcB(19)
                 /     \
                /       \
              19         funcA(9)
                        /     \
                       /       \
                      9        funcB(8) <--------+
                              /     \            |
                             /       \ ----------+
                            8        funcA(4) <--------+
                                    /     \            |
                                   /       \ ----------+
                                  4         funcB(3) <---------+
                                            /     \            |
                                           /       \ ----------+
                                          3        funcA(1) <---------+
                                                  /     \             |
                                                 /       \            |
                                                1        funcB(0) ----+
                                                          |
                                                          |
                                                         [x]
```
```
output: 201998431
```
```
            funcA(20)
           /     \
          /       \
        20        funcB(19)
                 /     \
                /       \
              19         funcA(9) <--------+
                        /     \            |
                       /       \ ----------+
                      9        funcB(8) <--------+
                              /     \            |
                             /       \ ----------+
                            8        funcA(4) <--------+
                                    /     \            |
                                   /       \ ----------+
                                  4         funcB(3) <---------+
                                            /     \            |
                                           /       \ ----------+
                                          3        funcA(1) <---------+
                                                  /     \             |
                                                 /       \            |
                                                1        funcB(0) ----+
                                                          |
                                                          |
                                                         [x]
```
```
output: 201998431
```
```
            funcA(20)
           /     \
          /       \
        20        funcB(19) <-------+
                 /     \            |
                /       \ ----------+
              19         funcA(9) <--------+
                        /     \            |
                       /       \ ----------+
                      9        funcB(8) <--------+
                              /     \            |
                             /       \ ----------+
                            8        funcA(4) <--------+
                                    /     \            |
                                   /       \ ----------+
                                  4         funcB(3) <---------+
                                            /     \            |
                                           /       \ ----------+
                                          3        funcA(1) <---------+
                                                  /     \             |
                                                 /       \            |
                                                1        funcB(0) ----+
                                                          |
                                                          |
                                                         [x]
```
```
output: 201998431
```
```
            funcA(20) <-------+
           /     \            |
          /       \ ----------+
        20        funcB(19) <-------+
                 /     \            |
                /       \ ----------+
              19         funcA(9) <--------+
                        /     \            |
                       /       \ ----------+
                      9        funcB(8) <--------+
                              /     \            |
                             /       \ ----------+
                            8        funcA(4) <--------+
                                    /     \            |
                                   /       \ ----------+
                                  4         funcB(3) <---------+
                                            /     \            |
                                           /       \ ----------+
                                          3        funcA(1) <---------+
                                                  /     \             |
                                                 /       \            |
                                                1        funcB(0) ----+
                                                          |
                                                          |
                                                         [x]
```
```
output: 201998431
```


#### 05. Nested Recursion

- Recursive function will pass *recursive call* as a parameter!
- usually, their tracing tree expands like anything
```
void func (int n)
{
    if (...)
    {
        ...
        ...
        func( func(n-1) );
    }
}
```
Unless result of `func(n-1)` is not obtained in `func( func(n-1) )`, call cannot be made

- let us trace this nested recursive function
```
int func(int n)
{
    if (n>100)
    {
        return (n-10);
    }
    else
    {
        return func( func(n+11) );
    }
}
```
```
func(95)
```