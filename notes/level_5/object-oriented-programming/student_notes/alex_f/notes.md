<!-- omit in toc -->
# OOP++
- [Intro](#intro)
- [Topic 0: Background Concepts and C++ Terminology](#topic-0-background-concepts-and-c-terminology)
  - [Points to Remember](#points-to-remember)
  - [Key Reading](#key-reading)
- [Topic 1: Functions and User Input](#topic-1-functions-and-user-input)
  - [Function Basics](#function-basics)
    - [Points to Remember](#points-to-remember-1)
    - [Scope and Lifetime](#scope-and-lifetime)
    - [Key Reading](#key-reading-1)
    - [Supplementary Readings](#supplementary-readings)
    - [Core Guidelines](#core-guidelines)
    - [CPP Reference](#cpp-reference)
  - [User Input Handling](#user-input-handling)
    - [Points to Remember](#points-to-remember-2)
    - [Basic Error Handling](#basic-error-handling)
    - [Key Reading](#key-reading-2)
    - [Supplementary Reading](#supplementary-reading)
    - [Core Guidelines](#core-guidelines-1)
    - [CPP Reference](#cpp-reference-1)
- [Topic 2a Fundamental and Built-in Data Types](#topic-2a-fundamental-and-built-in-data-types)
  - [Points to Remember](#points-to-remember-3)
  - [Booleans](#booleans)
  - [Number Types](#number-types)
    - [Points to Remember](#points-to-remember-4)
    - [Key Reading](#key-reading-3)
    - [Supplementary Reading](#supplementary-reading-1)
    - [CPP Reference](#cpp-reference-2)
  - [Strings](#strings)
    - [Points to Remember](#points-to-remember-5)
    - [Key Reading](#key-reading-4)
    - [Supplementary Reading](#supplementary-reading-2)
    - [Core Guidelines](#core-guidelines-2)
    - [CPP Reference](#cpp-reference-3)
  - [Vectors](#vectors)
    - [Points to Remember](#points-to-remember-6)
    - [Key Reading](#key-reading-5)
    - [Supplementary Reading](#supplementary-reading-3)
    - [Core Guidelines](#core-guidelines-3)
    - [CPP Reference](#cpp-reference-4)
- [Topic 2b User Defined Types: Enumerations and Classes](#topic-2b-user-defined-types-enumerations-and-classes)
  - [Enumerations](#enumerations)
    - [Points to Remember](#points-to-remember-7)
    - [Key Reading](#key-reading-6)
    - [Supplementary Reading](#supplementary-reading-4)
    - [Core Guidelines](#core-guidelines-4)
    - [CPP Reference](#cpp-reference-5)
  - [Classes: Basic Syntax and Constructors](#classes-basic-syntax-and-constructors)
    - [Points to Remember](#points-to-remember-8)
    - [Member Functions](#member-functions)
    - [Key Reading](#key-reading-7)
    - [Supplementary Reading](#supplementary-reading-5)
    - [Core Guidelines](#core-guidelines-5)
    - [CPP Reference](#cpp-reference-6)
- [Topic 2c File Organization](#topic-2c-file-organization)
  - [Class Structure and Header Files](#class-structure-and-header-files)
    - [Points to Remember](#points-to-remember-9)
    - [Key Reading](#key-reading-8)
    - [Supplementary Reading](#supplementary-reading-6)
    - [Core Guidelines](#core-guidelines-6)
    - [CPP Reference](#cpp-reference-7)

## Intro

Some notes for the UoL OOP course with additional readings, especially from the following textbooks:

- [*Programming*:](http://www.stroustrup.com/Programming/) Stroustrup, *Programming: Principles and Practice Using C++* (Second Edition)
- [*C++*:](https://www.amazon.com/The-Programming-Language-4th-Edition/dp/0321563840/) Stroustrup, *The C++ Programming Language* (Fourth Edition)
- [*Tour*:](https://www.amazon.com/Tour-2nd-Depth-Bjarne-Stroustrup/dp/0134997832) Stroustrup, *A Tour of C++* (Second Edition)
- [*Primer*:](https://www.amazon.com/Primer-5th-Stanley-B-Lippman/dp/0321714113) Lippman, Lajoie, and Moo, *C++ Primer* (Fifth Edition)

And references to the following resources:

- [C++ Core Guidelines](http://isocpp.github.io/CppCoreGuidelines/CppCoreGuidelines.html)
- [C++ Reference](https://en.cppreference.com/w/)

## Topic 0: Background Concepts and C++ Terminology

### Points to Remember
- An **object** is a region of memory with a **type** that defines its possible values and a set of operations that can be applied to it.
- A **variable** is a named object.
- A **value** is a set of bits interpreted according to type.
- C++ features **built-in types**, among the most important are **bool**, **char** (C-style character), **int**, **double**, **unsigned** (non-negative int).
- The standard library defines other important types, eg **string** and **vector** (like a JS array).
- To use a type from a **namespace** you need to `#include` it at the start of your file, and either refer to it using namespace notation `std::cout` or bring the namespace into scope `using namespace std;` (can lead to name clashes so avoid where possible) or the particular type `using std::cout;` then just `cout` will work.
- C++ also allows **User Defined Types**, also known as **Classes**, which are *first class citizens*.
- Before an object can be used it must be **initialized** which allocates the memory correctly depending on type.
- A named variable can only be used if it is in **scope**.
- Scope is a region of program text. A name is declared in a scope, and is valid (or "in scope") from the point of declaration to the end of that scope. There are four levels of scope:
  - **Local Scope** - a name declared in a function, lambda or local block `{}`, includes function parameters.
  - **Class Scope** - a name is called a **member name** if it is declared in a class, outside any function or lambda.
  - **Namespace Scope** - a name is called a **namespace member name** if declared in a namespace outside a function/lambda.
  - **Global Scope** - a name declared outside any construct.
- Variables can be made *immutable* by declaring them as `const` (meaning "I promise not to change this"), or `constexpr` (meaning "to be evaluated at compile time"), the difference is when the value is calculated either run-time or compile time respectively.
- In variable declarations `*` signifies a **pointer** and `&` signifies a **reference**. Both are ways to denote an object in memory without evaluating or copying it. The syntax to access the values is different (see *Tour*, p. 11)



### Key Reading

- *Tour*: Chapter One, *The Basics* (pp 1 - 19)

## Topic 1: Functions and User Input

### Function Basics

#### Points to Remember

- Functions must be declared before use (no hoisting). A **function declaration** is a definition without the function body.
- Though you can omit parameter names in the declaration, just need types, good practice to include meaningful names.
- Declaration is a promise to the compiler that the function is defined somewhere, definition is keeping that promise.
- Missing declaration will get a compiler error of the name not being in scope. Missing definition will get a linker error.
- Functions pass objects by value by default, even complex structures, use references or pointers to pass by location and avoid copying.
- Arguments might be silently converted on being passed to the function (eg float truncated to int), depends on compiler.
- No guarantee on the order in which parameters are initialized when the function is called.
- Functions must be called with the correct number of arguments (NB functions can be **overloaded**, so multiple functions of the same name defined with different parameter lists)
- Functions cannot return functions or C-arrays, but can return pointers to them.
- However never return references to local objects, behaviour is undefined, see *Primer*, p. 225 - ask "what pre-existing object is the reference referring to" and if the answer is none don't return a reference!

#### Scope and Lifetime

- In C++ names have *scope* and objects have *lifetimes*
- The **scope** of a name is the *part of a program's text* in which that name is visible.
- The **lifetime** of an object is *the time during the program's execution* that the object exists.
- C++ is block scoped, parameters and variables defined in a block are **local variables** they will hide declarations of the same name made in outer scope.
- Can create global objects defined outside any function, will not be destroyed until the program ends.
- Objects that correspond to ordinary local variables are destroyed when control passes through the end of the block where they are defined. They are known as **automatic objects**.
- NB you cannot nest functions within other functions so **no closure**.
- If you need a local variable to persist across multiple function calls you need to declare it as a **local static object**, using the `static` keyword.

#### Key Reading

- *Primer*: Chapter 6, sections 6.1 - 6.3, *Function Basics*, *Argument Passing*, and *Return Types and the `return` Statement* (pp 201 - 230)
- *Programming*: Chapter 8, *Technicalities: Functions* (pp 255 - 297)

#### Supplementary Readings
- *Tour*: Section 1.3, *Functions* (pp 4 - 5)
- *Programming*:  Section 4.5, *Functions* (pp 113 - 117)
- *C++*: Chapter 12, *Functions*, especially sections 12.1 - 12.1.5 (pp 305 - 310)

#### Core Guidelines

- [F Functions - General](http://isocpp.github.io/CppCoreGuidelines/CppCoreGuidelines#f-functions)
- [F.1 Package meaningful operations as functions](http://isocpp.github.io/CppCoreGuidelines/CppCoreGuidelines#Rf-package)
- [F.2 A Function should perform a single logical operation](http://isocpp.github.io/CppCoreGuidelines/CppCoreGuidelines#Rf-logical)
- [F.3 Keep Functions short and simple](http://isocpp.github.io/CppCoreGuidelines/CppCoreGuidelines#Rf-single)

#### CPP Reference
- [Intro to Functions](https://en.cppreference.com/w/cpp/language/functions)
- [Function Declarations and Definitions](https://en.cppreference.com/w/cpp/language/function)

### User Input Handling

#### Points to Remember

- The standard library defines 4 IO objects. `cin` and `cout` are standard input and output. `cerr` is the **standard error** stream, and `clog` is the **standard log** for execution info.
- Usually the system associates the streams with the window the program is executed. So data are read in and written out to the same window as program execution by default.
- `<<` takes two operands, left operand is an output stream, right operand is a value. It returns its left-hand operand, allowing chaining.
- Streams are buffered. *Flushing* the output stream prints it to the window immediately. You can flush with `std::endl`
- NB if you don't flush a statement while debugging it might be left in the buffer when the program crashes.
- `>>` behaves like `<<` but takes an object as its right operand to store the input.
- `>>` is type sensitive, it reads according to the type of variable you are reading into.
- Trailing whitespace terminates the reading of strings, but is otherwise ignored by `>>`. Leading whitespace is ignored for reading strings.
- Input of the wrong type will cause the `>>` operation to fail.

#### Basic Error Handling

- Error handling is managed by reference to **stream states**. There are four stream states:
  - `good()` - The operations succeeded.
  - `eof()` - We hit end of input ("end of file")
  - `fail()` - Something unexpected happened - eg we looked for an int and got a character.
  - `bad()` - Something really bad happened, like disc corruption.
- NB difference between `fail()` and `bad()` is not precisely defined, but if state is `bad()` usually have to bail.
- if input stream has reached `fail()` state we can use the `clear()` method to flush the buffer and restore the state to `good()`
- General logic for error handling from *Programming*, p. 355:

```c++
int i = 0;

cin >> i;

if(!cin)
{
    // only executes if input operation failed - ie no int or something worse
    if(cin.bad()) error("cin is bad") //stream is corrupted so we have to bail
    if(cin.eof())
    {
        //no more input, often this is desired outcome
    }
    if(cin.fail())
    {
        //stream has encountered unexpected type
        cin.clear() //make ready for more input
        //somehow recover, get more input?
    }
}
```

#### Key Reading
- *Programming*: Chapter 10, *Input and Output Streams* (p. 345ff), especially:
  - Sections 10.1 and 10.2, *Input and Output* and *The I/O Stream model* (pp 346 - 349)
  - Sections 10.6 and 10.7, *I/O error handling* and *Reading a single value* (pp 354 - 363)
- *Primer*: Sections 1.2, *A First Look at Input and Output* (pp 5 - 9) and 8.1, *The IO Classes* (pp 309 - 316)

#### Supplementary Reading
- *Tour*: Chapter 10, *Input and Output* especially sections 10.1-10.4 (pp 123 - 127)
- *Programming*:
  - Section 3.1, *Input* (pp 60 - 62)
  - Section 3.3, *Input and Type* (pp 64 - 65)
  - Section 5.6.3, *Bad Input* (pp 150 - 152)
- *C++*: Chapter 38, especially:
  - Section 38.1 *Introduction* (pp 1073 - 1075)
  - Section 38.3 *Error Handling* (pp 1080 - 1081)
  - Section 38.4.1.1 *Formatted Input* (pp 1082-1083)
  - I/O advice (p. 1107)


#### Core Guidelines
- [I/O Stream](http://isocpp.github.io/CppCoreGuidelines/CppCoreGuidelines#SS-io)
- [Avoid Character level input](http://isocpp.github.io/CppCoreGuidelines/CppCoreGuidelines#slio1-use-character-level-input-only-when-you-have-to)
- [Prefer I/O streams](http://isocpp.github.io/CppCoreGuidelines/CppCoreGuidelines#slio1-use-character-level-input-only-when-you-have-to)
- [Avoid endl](http://isocpp.github.io/CppCoreGuidelines/CppCoreGuidelines#Rio-endl)

#### CPP Reference
- [I/O Library](https://en.cppreference.com/w/cpp/io)
- [std::flush](https://en.cppreference.com/w/cpp/io/manip/flush)
- [std::endl](https://en.cppreference.com/w/cpp/io/manip/endl)

## Topic 2a Fundamental and Built-in Data Types

### Points to Remember
- Types are fundamental to C++. All objects in memory have a fixed type. Think of an object as a box in memory that can only hold a certain type.
- All fundamental types have a fixed size in memory, based on hardware and the compiler used, that determines the range of values that can be represented.
- The smallest chunk of addressable memory is a **byte** (8 bits), the basic unit of storage in a machine is referred to as a **word**, in most machines a word is either 32 or 64 bits (4 or 8 bytes).
- Use `sizeof($var or type)` to see the byte size of the type on specific hardware.
- For the guaranteed value ranges of fundamental types see [cpp reference](https://en.cppreference.com/w/cpp/language/types) or *Primer*, p. 32. The main ones are:
  - `char` - 8 bits.
  - `int` - 16 bits.
  - `long` - 32 bits.
  - `long long` - 64 bits.
  - `float` - 6 significant digits
  - `double` - 10 significant digits
- A program is **type-safe** when objects are only used according to the rules for their type.
- There are ways of doing operations that are not type-safe, eg using a variable before it has been initialized.
- Initialize all variables when you declare them to avoid problems (eg `double x = 0.0;` not `double x;`) *Primer*, p. 45.
- A **safe conversion** involves no information loss. The following are safe:
  - bool to char
  - bool to int
  - bool to double
  - char to int
  - char to double
  - int to double
- An **unsafe conversion** risks information loss, but is still accepted by the compiler. These are unsafe:
  - double to int
  - double to char
  - double to bool
  - int to char
  - int to bool
  - char to bool

### Booleans

- By definition, `true` has the value `1`, `false` has the value `0` when converted to integers.
- Integers can be implicitly converted to `bool` values - nonzero integers convert to `true`, `0` converts to `false`.
- A pointer can also be implicitly converted, a `non-null` pointer converts to `true` a `nullptr` converts to `false`. (so if `p` is a pointer then `if(p)` works).

### Number Types

#### Points to Remember
- C++ compilers use [Two's Complement](https://en.wikipedia.org/wiki/Two%27s_complement) representation of numbers.
- Floats and doubles use [IEEE 754](https://en.wikipedia.org/wiki/IEEE_754) formats, 32 bit for floats, 64 bit for doubles.
- Integer types are default decimal. `0b` prefix indicates binary, `0x` prefix indicates hex, `0` prefix means octal, eg `0334`.
- For a full table of prefixes and suffixes on number types see *C++*, p. 147.
- Numbers might be silently cast on initialization or assignment. eg `float f = 3.2` may cast a double to a float with unpredictable results and `int i = 4.3` will truncate to `4`. You can explicitly say `float f = 3.2f` to get round the first problems, compiler should warn about the second.
- Initialization syntax `int i {4.3}` will throw a narrowing error on compilation (c++ 11).
- Memory restrictions mean that when we do maths with floating-point numbers **rounding errors** are inevitable. The only question is whether they are significant enough to affect the result. Always check computation results for plausibility.
- When working with integers, it's common to have problems with **overflow** where a number becomes negative when it exceeds the maximum value that is possible to store. Compiler will not catch these errors when computed at run time.
- Can also have issues casting an integer to float - because they can take the same space and float needs exponent and mantissa. So can have issues with float not representing the largest ints correctly.
- Avoid unsigned ints if possible, using them is error-prone (*Programming*, p 965). Avoid mixing signed and unsigned ints (*Primer*, p. 37)
- Avoid using floats, use doubles instead as floats lack required precision, also avoid `long double` as it is very costly (*Primer*, p. 34)
#### Key Reading

- *Primer*: Sections 2.1 and 2.2.1 - 2.2.2, *Primitive Built-in Types* and *Variables* (pp 32 - 46)
- *C++*: Section 6.2, *Types* (pp 138 - 151)

#### Supplementary Reading

- *Tour*: Section 1.4, *Types, Variables, and Arithmetic* (pp 5 - 8)
- *Programming*:
  - Sections 3.8 and 3.9, *Types and objects* and *Type Safety* (pp 77 - 88)
  - Section 24.2, *Size, precision and overflow* (pp 890 - 895)
  - Section 25.5.3, *Signed and unsigned integers* (pp 961 - 965)

#### CPP Reference
- [Fundamental Types](https://en.cppreference.com/w/cpp/language/types)


### Strings
#### Points to Remember
- A `string` is a variable length sequence of characters that knows its own length.
- Use as follows:
  ```C++
  #include <string>
  using std::string;
  string name = "Matthew King"; //name is a copy of the string literal
  string defString; //default initialization to empty string
  string s4c(4, 'c'); // s4c is "cccc"
  ```
- You can concatenate a string, a string literal, a C-style string, or a character to a `string`.
- `+=` appends to the end of a string.
- Some useful string methods:
  ```C++
  #include <string>
  using std::string;

  string name = "Matthew King";
  string surname = name.substr(8, 4); // s = "King" arg 1 is index, arg 2 is length
  name.replace(0,7, "brian"); //name becomes "brian King" arg 1 is index, arg 2 is length, arg 3 is replacement value
  name[0] = toupper(name[0]); //name becomes "Brian King"
  bool empty = name.empty(); //returns false as not an empty string
  string::size_type nameLength = name.size(); //returns length of name string, NB does not return an int!
  auto nameLength2 = name.size(); // does the same thing, but easier to type, relies on auto typing.
  bool stringMatch = (name == surname); // returns false - NB comparison is case-sensitive
  ```
- Watch out for `.size()` it returns an unsigned bespoke type so be careful of mixing it with signed numbers (*Primer*, p. 88)
- Comparison operators follow lexicographic ordering: `<, >, <=, >=`.
- For processing strings - searching, selecting etc, see *Primer*, section 3.2.3 (p. 90ff)
- `string` is usually implemented using **short-string optimization** where short strings (c. 14 chars) are kept in the `string` object itself, while longer strings are placed on the free store and referred to.
- Memory allocation for strings can be relatively costly.
- A `string_view` type allows manipulation of character sequences regardless of how they are stored (eg `std::string` or C-arrays)
- `getline()` can be used to get an entire line of input, including whitespace but *not including newline*. Use as follows:
  ```C++
  string line;
  while (getline(cin, line))
      cout << line << '\n'; //NB have to add '\n' back in
  ```
- You cannot `switch` on strings, annoyingly.
#### Key Reading
- *Primer*: Section 3.2, *Library `string` Type* (pp 84 - 96)
- *C++*: Chapter 36, *Strings* (pp 1033 - 1049), especially:
  - Section 36.4, *Advice* (p. 1049)
  - Section 36.2.1 *Classification Functions* (p. 1034)
  - Section 36.3.7 *The `find` Family* (p. 1046) on search methods

#### Supplementary Reading
- *Tour*: Section 9.2, *Strings* (pp 111 - 114)
- *Programming* Section 23.2 and 23.3, *Strings* and *I/O Streams* (pp 850 - 855), especially:
  - Selected string operations (p. 851)

#### Core Guidelines
- [std::string](http://isocpp.github.io/CppCoreGuidelines/CppCoreGuidelines#SS-string)
- [Use std::string to own character sequences](http://isocpp.github.io/CppCoreGuidelines/CppCoreGuidelines#Rstr-string)
- [Use char* to refer to a single character](http://isocpp.github.io/CppCoreGuidelines/CppCoreGuidelines#Rstr-char*)
- [Use 's' suffix for string literals meant to be std::string](http://isocpp.github.io/CppCoreGuidelines/CppCoreGuidelines#Rstr-s)

#### CPP Reference
- [String Library](https://en.cppreference.com/w/cpp/string)
- [basic strings](https://en.cppreference.com/w/cpp/string/basic_string)

### Vectors

#### Points to Remember
- A `vector` is a collection, or **container** of objects, all with the same type, that knows its own length. Objects in the vector can be accessed through their index.
- NB `vector` is a template, not a type. Templates allow you to generate different types from them depending on information you pass with `<>` after the template name.
- In vector's case you specify the type of the objects the vector will hold. EG `vector<int>`, `vector<string>`, `vector<My_class>`. These are three different types.
- Vectors can hold vectors, declared as follows: `vector<vector<int>>` (or old style `vector<vector<int> >` with a space).
- Most common is to initialize empty vector and populate at runtime, other common ways to initialize:

```C++

#include <vector>
using std::vector;

vector<T> v1;   //vector that holds objects of type T. Default initialization is empty (most common).

vector<T> v2(v1); //vector v2 has a copy of every element in v1, could also say v2 = v1.

vector<T> v3(n, val); // vector has n elements of value val

vector<T> v4(n); // vector has n elements with default values for their type (only if that type supports default initialization)

vector<T> v5{a, b, c}; // vector contains a,b,c

```

- For fiddly aspects of initialization, including **list initialization** and **element counts** see *Primer*, p. 99.
- Key to vectors in C++ is that they *grow efficiently*. Unless all the elements have the same value it is better to initialize an empty vector and then grow it, rather than create a vector of a specific size. (*Primer*, p. 101). Unlike C/Java.
- `push_back()` method takes a value and adds it to the end of the vector. The most common way to add elements. Some examples:

```C++
vector<int> v2;
for (int i =0; i != 100, ++i)
    v2.push_back(i);

//end of loop v2 has 100 elements, 0 - 99

string word;
vector<string> text;
while(cin >> word) {
  text.push_back(word)
}
//text has all the words from the input stream as elements.
```

- use a range `for` loop to process all elements of a vector:

```C++

vector<int> v{1,2,3,4,5,6,7,8};

for(auto &i : v)      //for all elements in v, NB i is a reference allowing us to change values, auto deduces type.
  i *= i;             //square the value
for(auto i : v)       //for each element (not a reference)
  cout << i << " ";   //outputs the square of the original elements.
cout << '\n';
```

- Useful vector methods:

```C++

v.empty()       //boolean return
v.size()        //returns number of elements. NB returns vector<T>::size_type, not int
v[n]            //returns a reference to the element at n in v. NB cannot add elements to vector using [], only access and replace.
v.push_back(t)  //adds an element with value t at the end of the vector
v.pop_back()    //removes last element from vector - careful with references and iterators
v1 = v2         //replaces elements of v1 with a copy of elements in v2
v1 == v2        //vectors are equal if they are the same size and each element in v1 is equal to corresponding element in v2
<, >, <=, >=    //comparisons use dictionary ordering, see *Primer*, p. 102.

```

- Range checking is a common problem. Accessing elements out of range does not throw compiler error, and causes undefined values to be returned. For Stroustrup's custom solution see *Tour*, pp 141-142.
- Consider vectors the default container, use them unless you have a reason not to (Stroustrup).

#### Key Reading
- *Primer*: Section 3.3, *Library `vector` Type* (pp 96 - 105)
- *Programming*: Section 4.6, `vector` (pp 117 - 125)

#### Supplementary Reading
- *Tour*: Section 11.2, `vector` (pp 138 - 142)
- *C++*: Section 31.4.1, `vector` (pp 902 - 906)
- *Programming*: Chapters 17, 18, and 19 implement a `vector` Template and deep dive into how it works. They cover a lot of ground inc. constructors, destructors, the free store, templates etc. Useful reference for specific issues.

#### Core Guidelines
- [Containers](https://isocpp.github.io/CppCoreGuidelines/CppCoreGuidelines#SS-con)
- [Prefer STL `vector` by default](https://isocpp.github.io/CppCoreGuidelines/CppCoreGuidelines#Rsl-vectorr)
- [Avoid Bounds Errors](https://isocpp.github.io/CppCoreGuidelines/CppCoreGuidelines#Rsl-bounds)

#### CPP Reference
- [vectors](https://en.cppreference.com/w/cpp/container/vector)


## Topic 2b User Defined Types: Enumerations and Classes
### Enumerations
#### Points to Remember
- **Enumerations**, or `enums` are a simple user-defined type. They specify a set of values (or **enumerators**) as *symbolic constants* and allow us to group together *sets of integral constants*.
- Enumerations are very useful. Use them when we need a set of related named integer constants. EG, for alternatives (up,down; yes, no; on, off, N, S, E, W; bid, offer) or distinct values (red, green blue, yellow, crimson)
- There are two types of enumeration. Original `enums` are known as **plain** or **unscoped**. Their enumerators can "pollute" the scope in which the enum is defined as they implicitly export their enumerators to their scope. They also allow implicit conversion to int.
- Generally avoided now in favour of C++ **scoped enumerations** or `enum classes`, use as follows:

  ```C++
  #include <iostream>
  #include <type_traits>
  #include <map>
  #include <string>

  enum class Month {
    jan =1, feb, mar, apr, may, jun, jul, aug, sep, oct, nov, dec
  };

  //use a map to create labels for the enumerators to print them
  std::map<Month, std::string> months = {
    {Month::jan, "January"},
    {Month::feb, "February"},
    ...
  };

  Month m = Month::feb; //good
  int n = m; //error, no implicit conversion from Month to int
  m = 7; //error, can't assign an int to a Month
  std::cout << m; //error, no implicit conversion, << not defined for `Month`
  std::cout << static_cast<std::underlying_type<Month>::type>(m); //ok, outputs '2'
  std::cout << months[m]; //ok, outputs "February"
  ```
- The `class` denotes that the enumerators are in the scope of the enumeration, so to refer to `jan` you say `Month::jan`. No implicit conversion to ints.
- This makes it fiddly to, for example, `cout` an enum class. You have to explicitly cast it to the underlying type. See eg this [Stack Overflow post](https://stackoverflow.com/questions/11421432/how-can-i-output-the-value-of-an-enum-class-in-c11).
- Or you can create a map of labels if you want to print a string (see code example above).
- The compiler will pick the value for each enumerator you don't specify, default starting at `0`, then incrementing by 1. Better to let the compiler pick values for you, though you can explicitly define each value.
- You can also specify the underlying type of the enum, if you don't want an int, but this is generally avoided.

#### Key Reading
- *Programming*: Section 9.5, *Enumerations* (pp 318 - 321)
- *Primer*: Section 19.3, *Enumerations* (pp 832 - 835)

#### Supplementary Reading
- *C++*: Section 8.4, *Enumerations* (pp 218 - 224)

#### Core Guidelines
- [Enumerations](https://isocpp.github.io/CppCoreGuidelines/CppCoreGuidelines#S-enum)
- [Use enumerations to represent sets of related named constants](https://isocpp.github.io/CppCoreGuidelines/CppCoreGuidelines#Renum-set)
- [Prefer enum classes over "plain" enums](https://isocpp.github.io/CppCoreGuidelines/CppCoreGuidelines#Renum-class)
- [Define operations on enumerations for safe use](https://isocpp.github.io/CppCoreGuidelines/CppCoreGuidelines#Renum-oper)
- [Avoid ALL_CAPS](https://isocpp.github.io/CppCoreGuidelines/CppCoreGuidelines#Renum-caps)
- [Avoid unnamed enums](https://isocpp.github.io/CppCoreGuidelines/CppCoreGuidelines#Renum-unnamed)
- [Specify the underlying type of the enum only if necessary](https://isocpp.github.io/CppCoreGuidelines/CppCoreGuidelines#Renum-underlying)
- [Specify the enumerator values only if necessary](https://isocpp.github.io/CppCoreGuidelines/CppCoreGuidelines#Renum-value)

#### CPP Reference
- [Enum declaration](https://en.cppreference.com/w/cpp/language/enum)

### Classes: Basic Syntax and Constructors
#### Points to Remember

- A class is a **user-defined type** consisting of a set of **members**. The most common kinds of members are **data members** and **member functions**.
- Members are accessed by using `.` for objects and `->` for pointers.
- A class is a namespace containing its members.
- The **public** members define a class's **interface**, while its **private** members detail its **implementation**.
- A **struct** is a class where all members are by default public. By default members of a `class` are private.
- The construct `class X {...};` is a **class definition**, often referred to as a **class declaration**.
- `struct S {...};` is simply shorthand for `class S{public:...};`.
- It is not a requirement to declare data first in a class definition before they are used in member functions. Often useful to show the functions first.
- A **constructor** is a function that specifies how objects of a class are initialized. They are recognized by having the same name as the class itself.
- When a class has a constructor, all objects of that class will by initialized by a constructor call. If that constructor requires arguments, those must be supplied.
- By having multiple constructors with different arguments, we can create a variety of ways of initializing class objects, ie constructors can be *overloaded* like regular functions.
- Here is an example `Date` class with private members and public constructors showing the syntax, including for default values in constructors:

```C++
  class Date {
    int d,m,y; //these are private data members, can also specify `private:` to be explicit

    public:

    Date(int dd =0,int mm =0,int yy =0); //constructor for day,month,year, with defaults used in constructor below
    Date(int dd,int mm); //constructor for day, month, assume current year, no defaults
    Date(int); //constructor for day, assume current month and year
    Date(); //default constructor, initialize to today
    Date(const char*); //date from a string
  }; //don't forget semi-colon!

  Date::Date(int dd, int mm, int yy)
  {
    d = dd ? dd : today.d; //assume today has been created with public members
    m = mm ? mm : today.m;
    y = yy ? yy : today.y;

    //check date validity
  }

  Date::Date(int dd, int mm)
  :y{today.y}, m{mm}, d{dd} //initializer list syntax
  {
    //check date validity
  }

  Date date1 {30,4,2020}; // uses first constructor, NB Stroustrup prefers {} when initializing
  Date date2(30,4); //same effect, uses second constructor, but Stroustrup doesn't like () here.
```
#### Member Functions
- We define and declare member functions similarly to ordinary functions. Member functions *must* be declared within the class. They *may* be defined inside the class itself or outside the class body using the namespace: `Class::memberFunction(){};`.
- See section on header files for usual way of declaring and defining member functions.
- Almost always, when a member function is called, it is called on behalf of an object (an instance of the class).
- When a member function is called an extra, implicit parameter is initialized, called `this`. `this` is a const pointer to the address of the object on which the function was evoked.
- Inside a member function we can then refer directly to members of the object without any access operator or namespace. It will be interpreted as an implicit reference to `this`.
- So an ordinary member function declaration specifies three distinct things:
  - The function can access the private parts of the class declaration.
  - The function is in the scope of the class.
  - The function must be invoked on an object (has a `this` pointer).
- You can declare a member function `static` to give it the first two properties only. And you can declare a nonmember function a `friend` to give it the first property. (This is covered later).
- The compiler processes classes in two steps. First member declarations are compiled, and then member function bodies are processed. So member functions can use other members in the class regardless of where those members are declared.
#### Key Reading
- *Programming*, Chapter 9, *Technicalities: Classes, etc* (pp 303 - 342) Ch. 9 evolves a date class, growing in complexity.
- *C++*, Sections 16.1 - 16.2.5 (pp 449 - 457), and p. 571.

#### Supplementary Reading
- *Tour*, Sections 4.1 and 4.2 (pp 47 - 51)
- *Primer*:
  -  Section 7.1.2, on member functions (pp 256 - 260)
  -  Section 7.1.3, on class helper functions (pp 260 - 262)
  -  Section 7.1.4, *Constructors* (pp 262 - 266)
  -  NB *Primer* chapter on classes relies a lot on a case study built up over previous chapters so a bit hard to follow if you're not working through the book.

#### Core Guidelines
- [Classes](https://isocpp.github.io/CppCoreGuidelines/CppCoreGuidelines#S-class)
- [Organize related data into structures (`struct` or `class`)](https://isocpp.github.io/CppCoreGuidelines/CppCoreGuidelines#Rc-org)
- [Use `class` not `struct` if there are invariants](https://isocpp.github.io/CppCoreGuidelines/CppCoreGuidelines#Rc-struct)
- [Use `class` not `struct` if there are any private members](https://isocpp.github.io/CppCoreGuidelines/CppCoreGuidelines#Rc-class)
- [Represent the distinction between *interface* and *implementation* in the class](https://isocpp.github.io/CppCoreGuidelines/CppCoreGuidelines#Rc-interface)

#### CPP Reference
- [Classes](https://en.cppreference.com/w/cpp/language/classes)
- [Default Constructor](https://en.cppreference.com/w/cpp/language/default_constructor)
## Topic 2c File Organization

### Class Structure and Header Files

#### Points to Remember
- C++ allows for **separate compilation** where user code only sees the declarations of the classes and functions it uses (their *interfaces*).
- The full definitions are then in separate source code files and can be compiled separately, minimizing compile times.
- Typically a class is written in two files:
  -  a **header file** `Class.h` containing the class definition and declarations of its member variables and functions.
  -  an **implementation file** `Class.cpp`, with the full definitions of the class's member functions.
- For what can and can't be included in header files, see *C++*, p. 424.
- A `.cpp` file that is compiled by itself is called a **translation unit**, a program might contain thousands of units.
- The **One-Definition Rule** states that classes can only be defined once in a translation unit. For the full rule see *C++*, p. 425.
- The source code fragments are pulled together during **pre-processing**, a stage in building the program that executes before compilation, using the `#include` mechanism.

```C++
  #include "Class.h" //use quotes for class headers in current directory
  #include <iostream> //use <> for standard include directory, eg standard library.
  #include < string > //error, whitespace is significant
  #include " Class.h " //error whitespace is significant here too.
```
- `#include` is equivalent to pasting the text from the header file, bringing all the names into scope.
- Because each header represents a class as a self-contained unit, there can be a lot of redundancy in `#include` statements. We can also quickly get errors as class definitions are `#include`d more than once in the same translation unit, which breaks the *One-Definition Rule*.
- To get around this we use **header guards**, also called **include guards**. These ensure header files are only included once in a translation unit. There are two common ways:

```C++
#pragma once
//rest of the header here
```
- `#pragma once` is non-standard, but supported by most modern compilers. See [CPP Reference](https://en.cppreference.com/w/cpp/preprocessor/impl). Alternatively:

```C++
#ifndef LIBRARY_FILENAME_H //preprocessor checks if variable is not defined, if so continues to execute
#define LIBRARY_FILENAME_H //define the variable so it is in scope if encountered again. Use ALL_CAPS, and a long name to avoid clashes.
// contents of the header
#endif /* LIBRARY_FILENAME_H */ //end the conditional and resume execution
```
#### Key Reading
- *C++*:
  - Section 15.2.2 - 15.2.4, *Header Files*, *The One-Definition Rule*, and *Standard-Library Headers* (pp 424 - 428)
  - Section 15.3, *Using Header Files* (pp 431 - 441)

#### Supplementary Reading
- *Tour*, Section 3.2, *Separate Compilation* (pp 30 - 32)
- *Primer*, Section 2.6.3, *Writing our Own Header Files* (pp 76 - 77)
- *Programming*, Section 8.3, *Header Files* (pp 264 - 266)

#### Core Guidelines
- [Source Files](https://isocpp.github.io/CppCoreGuidelines/CppCoreGuidelines#S-source)
- [Use header files for all declarations used in multiple files](https://isocpp.github.io/CppCoreGuidelines/CppCoreGuidelines#Rs-declaration-header)
- [Header files should be self-contained](https://isocpp.github.io/CppCoreGuidelines/CppCoreGuidelines#Rs-contained)
- [Use `#include` guards on all header files](https://isocpp.github.io/CppCoreGuidelines/CppCoreGuidelines#Rs-guards)
- [Put `#include` at the top of files](https://isocpp.github.io/CppCoreGuidelines/CppCoreGuidelines#Rs-include-order)
- [Avoid cyclic dependencies if possible](https://isocpp.github.io/CppCoreGuidelines/CppCoreGuidelines#Rs-cycles)

#### CPP Reference
- [Source file inclusion](https://en.cppreference.com/w/cpp/preprocessor/include)
- [#pragma once](https://en.cppreference.com/w/cpp/preprocessor/impl)
- [preprocessor conditional inclusion - `ifdef` etc](https://en.cppreference.com/w/cpp/preprocessor/conditional)