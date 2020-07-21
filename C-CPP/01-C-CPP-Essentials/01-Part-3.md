##### This style of programming will be followed in entire data structures.

#### 11. structures and Functions

```
struct Rectangle
{
    int length;
    int breadth;
}
```
```
void initialize(struct Rectangle *p, int l, int b)
{
    (*p).length = l;
    (*p).breadth = b; 
}
```
```
int area(struct Rectangle r1)
{
    return r1.length * r1.breadth;
}
```
```
void changeLength( struct Rectangle *p, int l )
{
    (*p).length = l;
}
```
Main
```
int main()
{
    // create rectangle in stack frame of main()
    struct Rectangle r;
    
    // Initialize main's stack-frame data using a function
    // call-by-address
    initialize(&r, 10, 5);

    // get area 
    // call-by-value
    area(r);

    // Alter main's stack-frame data
    // call-by-address
    changeLength(&r, 90);
}
```

- Best style of programming in C Language
- This is how we can write *functions* on a *structure*
- This leads us to OOPs (Highest level of programming in C Language)
- Grouping of data and functions together - heart of OOPs (Just like what we did above)

#### 12. Converting a *C-Program* (above) to *C++ Class*

- In C++
- Data-members are `private`
- Member-functions are `public`

```
class Rectangle
{
    private:
        int length;
        int breadth;

    public:
        // Initialize is same as constructor
        Rectangle(int l, int b)
        {
            length = l;
            breadth = b
        }

        int area()
        {
            return length*breadth
        }

        void changeLength(int l)
        {
            length = l;
        }

}
```

Main
```
int main()
{
    Rectangle r(10,5); // Declare and initialize
    r.area(); 
    r.changeLength(20);
}
```

#### 12. Classes and construtors in C++

```
#include<iostream> // `.h` depends on compile
using namespace std; // if not `iostream.h` for `cin` and `cout`

class Rectangle
{
    private:
        int length;
        int breadth;

    public:

        // Types of functions
        // ------------------

        // Constructor and constructor overloading
        Rectangle() { length = 1; breadth = 1; }
        Rectangle(int l, int b);

        // Facilitators - Perform actions on data-members
        int area();
        int perimeter();

        // Accessor
        int getLength() { return length };
        
        // Mutator
        int setLength(int l) { length  = l; };

        // Destructor
        ~Rectangle()
}
```

Can write definition body for all types of fuctionsoutside the class using scope resolution operator `::`
```
Rectangle :: Rectangle(int l, int b)
{
    length = l;
    breadth = b;
}

int Rectangle :: area()
{
    return length*breadth;
}

int Rectangle :: perimeter()
{
    return 2*(length + breadth);
}

Rectangle :: ~Rectangle()
{
    // No need to do any thing
    // Yo can if you want to. 
} 
```

Main function()
```
Rectangle r(10, 5);

cout << r.area() ;
cout << r.perimeter() ;
r.setLength(20);
cout << getLength();
```

> If C language, we will use `struct` followed by `modules`
> If C++, we can use classes instead as it means the same yet better way to write code.

# Templates

- C++ supports generic functions - `Template Functions` and generic classes - `Template Classes`

Example,
```
class Arithametic
{
    private:
        int a;
        int b;
    
    public:
        Arithematic(int a, int b);
        int add();
        int sub();
};
```

Definitions using scope resolution operator:
```
Arithematic :: Arithematic (int a, int b)
{
    this.a = a; // or `this -> a = a`
    this.b = b; // or `this -> b = b`

    // Note: `this` is a pointer to current object
}
```
```
int Arithematic :: add()
{
    int c;
    c = a + b;
    return c;
}
```
```
int Arithematic :: sub()
{
    int c;
    c = b - a;
    return c;
}
```

- Now, what if `a` and `b` or of type *float* or *unsigned-int* or *long* or *double* ? Should we write the whole class again? No! Using generic classes i.e templates, we can avoid redundant code

    ```
    template <class T>
    ```

- Same above class made generic using templates
    ```
    
    template <class T>
    class Arithametic
    {
        private:
            T a;
            T b;
        
        public:
            Arithematic(T a, T b);
            T add();
            T sub();
    };

    // effect of template ends with end of class
    ```
    **Note:** Don't change all `int`s with `T`! change only the ones that will be generic.

    As the effect of template end with end of class, we have to tell again that "it is a template" in case of function bodies written with scope resolution operator

    > Synatx: `
    ```
    template<class T>
    return-type class-name<T> :: func-name(data-type param1, data-type param2 ...)
    ```
    **Note:** `data-type` may or may not be `T`


    ```
    template <class T>
    Arithametic<T> :: Arithametic (T a, T b)
    {
        this.a = a;
        this.b = b;
    }
    ``` 
    ```
    template <class T>
    int Arithematic<T> :: add()
    {
        T c;
        c = a + b;
        return c;
    }
    ```
    ```
    template <class T>
    T Arithematic<T> :: sub()
    {
        T c;
        c = b - a;
        return c;
    }
    ```

    Main: See how generic the class is
    ```
    int main()
    {
        Arithematic<int> arith1(10, 5);
        cout << add();

        Arithematic<float> arith(1.5, 5.5);
        cout << add();
    }
    ```
