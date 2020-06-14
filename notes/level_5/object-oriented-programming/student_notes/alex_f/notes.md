<!-- omit in toc -->

# OOP++

- [Intro](#intro)
- [Topic 0: Background Concepts and C++ Terminology](#topic-0-background-concepts-and-c-terminology)
- [Topic 1: Functions and User Input](#topic-1-functions-and-user-input)
  - [Function Basics](#function-basics)
    - [Points to Remember](#points-to-remember)
    - [Scope and Lifetime](#scope-and-lifetime)
  - [User Input Handling](#user-input-handling)
    - [Points to Remember](#points-to-remember-1)
    - [Basic Error Handling](#basic-error-handling)
- [Topic 2a Fundamental and Built-in Data Types](#topic-2a-fundamental-and-built-in-data-types)
  - [Points to Remember](#points-to-remember-2)
  - [Booleans](#booleans)
  - [Number Types](#number-types)
  - [Strings](#strings)
  - [Vectors](#vectors)
- [Topic 2b User Defined Types: Enumerations and Classes](#topic-2b-user-defined-types-enumerations-and-classes)
  - [Enumerations](#enumerations)
  - [Classes: Basic Syntax and Constructors](#classes-basic-syntax-and-constructors)
    - [Points to Remember](#points-to-remember-3)
    - [Member Functions](#member-functions)
- [Topic 2c Source File Organization](#topic-2c-source-file-organization)
  - [Class Structure and Header Files](#class-structure-and-header-files)
- [Topic 3: File Handling, Input Streams, and Exceptions](#topic-3-file-handling-input-streams-and-exceptions)
  - [File Handling](#file-handling)
    - [File Modes](#file-modes)
  - [Input Streams and Tokenizing](#input-streams-and-tokenizing)
  - [Exception Handling](#exception-handling)
    - [Points to Remember](#points-to-remember-4)
    - [Throwing an Exception](#throwing-an-exception)
    - [Catching an Exception](#catching-an-exception)
    - [Exception Classes](#exception-classes)
- [Topic 4: Associative Containers and Sorting](#topic-4-associative-containers-and-sorting)
  - [Associative Containers: Maps and Sets](#associative-containers-maps-and-sets)
  - [Sorting](#sorting)
- [Topic 5: Member Functions and Operator Overloading](#topic-5-member-functions-and-operator-overloading)
  - [Member Functions Continued: `static`, `const` and `friend` functions](#member-functions-continued-static-const-and-friend-functions)
    - [`static` functions](#static-functions)
    - [`const` member functions](#const-member-functions)
    - [`friend` functions](#friend-functions)
  - [Operator Overloading](#operator-overloading)

## Intro

Some notes for the UoL OOP course with additional readings, especially from the following textbooks:

- [_Programming_:](http://www.stroustrup.com/Programming/) Stroustrup, _Programming: Principles and Practice Using C++_ (Second Edition)
- [_C++_:](https://www.amazon.com/The-Programming-Language-4th-Edition/dp/0321563840/) Stroustrup, _The C++ Programming Language_ (Fourth Edition)
- [_Tour_:](https://www.amazon.com/Tour-2nd-Depth-Bjarne-Stroustrup/dp/0134997832) Stroustrup, _A Tour of C++_ (Second Edition)
- [_Primer_:](https://www.amazon.com/Primer-5th-Stanley-B-Lippman/dp/0321714113) Lippman, Lajoie, and Moo, _C++ Primer_ (Fifth Edition)

And references to the following resources:

- [C++ Core Guidelines](http://isocpp.github.io/CppCoreGuidelines/CppCoreGuidelines.html)
- [C++ Reference](https://en.cppreference.com/w/)

## Topic 0: Background Concepts and C++ Terminology

<!-- omit in toc -->

### Points to Remember

- An **object** is a region of memory with a **type** that defines its possible values and a set of operations that can be applied to it.
- A **variable** is a named object.
- A **value** is a sequence of bits interpreted according to type.
- C++ features **built-in types**, among the most important are **bool**, **char** (C-style character), **int**, **double**, **unsigned** (non-negative int).
- The standard library defines other important types, eg **string** and **vector** (like a JS array).
- To use a type from a **namespace** you need to `#include` it at the start of your file, and either refer to it using namespace notation `std::cout` or bring the namespace into scope `using namespace std;` (can lead to name clashes so avoid where possible) or the particular type `using std::cout;` then just `cout` will work.
- C++ also allows **User Defined Types**, also known as **Classes**, which are _first class citizens_.
- Before an object can be used it must be **initialized** which allocates the memory correctly depending on type.
- A named variable can only be used if it is in **scope**.
- Scope is a region of program text. A name is declared in a scope, and is valid (or "in scope") from the point of declaration to the end of that scope. There are four levels of scope:
  - **Local Scope** - a name declared in a function, lambda or local block `{}`, includes function parameters.
  - **Class Scope** - a name is called a **member name** if it is declared in a class, outside any function or lambda.
  - **Namespace Scope** - a name is called a **namespace member name** if declared in a namespace outside a function/lambda.
  - **Global Scope** - a name declared outside any construct.
- Variables can be made _immutable_ by declaring them as `const` (meaning "I promise not to change this"), or `constexpr` (meaning "to be evaluated at compile time"), the difference is when the value is calculated either run-time or compile time respectively.
- In variable declarations `*` signifies a **pointer** and `&` signifies a **reference**. Both are ways to denote an object in memory without evaluating or copying it. The syntax to access the values is different (see _Tour_, p. 11)

<!-- omit in toc -->

### Key Reading

- _Tour_: Chapter One, _The Basics_ (pp 1 - 19)

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
- However never return references to local objects, behaviour is undefined, see _Primer_, p. 225 - ask "what pre-existing object is the reference referring to" and if the answer is none don't return a reference!

#### Scope and Lifetime

- In C++ names have _scope_ and objects have _lifetimes_
- The **scope** of a name is the _part of a program's text_ in which that name is visible.
- The **lifetime** of an object is _the time during the program's execution_ that the object exists.
- C++ is block scoped, parameters and variables defined in a block are **local variables** they will hide declarations of the same name made in outer scope.
- Can create global objects defined outside any function, will not be destroyed until the program ends.
- Objects that correspond to ordinary local variables are destroyed when control passes through the end of the block where they are defined. They are known as **automatic objects**.
- NB you cannot nest functions within other functions so **no closure**.
- If you need a local variable to persist across multiple function calls you need to declare it as a **local static object**, using the `static` keyword.
<!-- omit in toc -->

#### Key Reading

- _Primer_: Chapter 6, sections 6.1 - 6.3, _Function Basics_, _Argument Passing_, and _Return Types and the `return` Statement_ (pp 201 - 230)
- _Programming_: Chapter 8, _Technicalities: Functions_ (pp 255 - 297)
<!-- omit in toc -->

#### Supplementary Readings

- _Tour_: Section 1.3, _Functions_ (pp 4 - 5)
- _Programming_: Section 4.5, _Functions_ (pp 113 - 117)
- _C++_: Chapter 12, _Functions_, especially sections 12.1 - 12.1.5 (pp 305 - 310)
<!-- omit in toc -->

#### Core Guidelines

- [F Functions - General](http://isocpp.github.io/CppCoreGuidelines/CppCoreGuidelines#f-functions)
- [F.1 Package meaningful operations as functions](http://isocpp.github.io/CppCoreGuidelines/CppCoreGuidelines#Rf-package)
- [F.2 A Function should perform a single logical operation](http://isocpp.github.io/CppCoreGuidelines/CppCoreGuidelines#Rf-logical)
- [F.3 Keep Functions short and simple](http://isocpp.github.io/CppCoreGuidelines/CppCoreGuidelines#Rf-single)
<!-- omit in toc -->

#### CPP Reference

- [Intro to Functions](https://en.cppreference.com/w/cpp/language/functions)
- [Function Declarations and Definitions](https://en.cppreference.com/w/cpp/language/function)

### User Input Handling

#### Points to Remember

- The standard library `<iostream>` defines 4 I/O objects. `cin` and `cout` are standard input and output. `cerr` is the **standard error** stream, and `clog` is the **standard log** for execution info.
- Usually the system associates the streams with the window the program is executed. So data are read in and written out to the same window as program execution by default.
- `<<` takes two operands, left operand is an output stream, right operand is a value. It returns its left-hand operand, allowing chaining.
- Streams are buffered. _Flushing_ the output stream prints it to the window immediately. You can flush with `std::endl` or `std::flush`
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
- General logic for error handling from _Programming_, p. 355:

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

<!-- omit in toc -->

#### Key Reading

- _Programming_: Chapter 10, _Input and Output Streams_ (p. 345ff), especially:
  - Sections 10.1 and 10.2, _Input and Output_ and _The I/O Stream model_ (pp 346 - 349)
  - Sections 10.6 and 10.7, _I/O error handling_ and _Reading a single value_ (pp 354 - 363)
- _Primer_: Sections 1.2, _A First Look at Input and Output_ (pp 5 - 9) and 8.1, _The IO Classes_ (pp 309 - 316)
<!-- omit in toc -->

#### Supplementary Reading

- _Tour_: Chapter 10, _Input and Output_ especially sections 10.1-10.4 (pp 123 - 127)
- _Programming_:
  - Section 3.1, _Input_ (pp 60 - 62)
  - Section 3.3, _Input and Type_ (pp 64 - 65)
  - Section 5.6.3, _Bad Input_ (pp 150 - 152)
- _C++_: Chapter 38, especially:
  - Section 38.1 _Introduction_ (pp 1073 - 1075)
  - Section 38.3 _Error Handling_ (pp 1080 - 1081)
  - Section 38.4.1.1 _Formatted Input_ (pp 1082-1083)
  - I/O advice (p. 1107)

<!-- omit in toc -->

#### Core Guidelines

- [I/O Stream](http://isocpp.github.io/CppCoreGuidelines/CppCoreGuidelines#SS-io)
- [Avoid Character level input](http://isocpp.github.io/CppCoreGuidelines/CppCoreGuidelines#slio1-use-character-level-input-only-when-you-have-to)
- [Prefer I/O streams](http://isocpp.github.io/CppCoreGuidelines/CppCoreGuidelines#slio1-use-character-level-input-only-when-you-have-to)
- [Avoid endl](http://isocpp.github.io/CppCoreGuidelines/CppCoreGuidelines#Rio-endl)
<!-- omit in toc -->

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
- For the guaranteed value ranges of fundamental types see [cpp reference](https://en.cppreference.com/w/cpp/language/types) or _Primer_, p. 32. The main ones are:
  - `char` - 8 bits.
  - `int` - 16 bits.
  - `long` - 32 bits.
  - `long long` - 64 bits.
  - `float` - 6 significant digits
  - `double` - 10 significant digits
- A program is **type-safe** when objects are only used according to the rules for their type.
- There are ways of doing operations that are not type-safe, eg using a variable before it has been initialized.
- Initialize all variables when you declare them to avoid problems (eg `double x = 0.0;` not `double x;`) _Primer_, p. 45.
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

<!-- omit in toc -->

#### Points to Remember

- C++ compilers use [Two's Complement](https://en.wikipedia.org/wiki/Two%27s_complement) representation of numbers.
- Floats and doubles use [IEEE 754](https://en.wikipedia.org/wiki/IEEE_754) formats, 32 bit for floats, 64 bit for doubles.
- Integer types are default decimal. `0b` prefix indicates binary, `0x` prefix indicates hex, `0` prefix means octal, eg `0334`.
- For a full table of prefixes and suffixes on number types see _C++_, p. 147.
- Numbers might be silently cast on initialization or assignment. eg `float f = 3.2` may cast a double to a float with unpredictable results and `int i = 4.3` will truncate to `4`. You can explicitly say `float f = 3.2f` to get round the first problems, compiler should warn about the second.
- Initialization syntax `int i {4.3}` will throw a narrowing error on compilation (c++ 11).
- Memory restrictions mean that when we do maths with floating-point numbers **rounding errors** are inevitable. The only question is whether they are significant enough to affect the result. Always check computation results for plausibility.
- When working with integers, it's common to have problems with **overflow** where a number becomes negative when it exceeds the maximum value that is possible to store. Compiler will not catch these errors when computed at run time.
- Can also have issues casting an integer to float - because they can take the same space and float needs exponent and mantissa. So can have issues with float not representing the largest ints correctly.
- Avoid unsigned ints if possible, using them is error-prone (_Programming_, p 965). Avoid mixing signed and unsigned ints (_Primer_, p. 37)
- Avoid using floats, use doubles instead as floats lack required precision, also avoid `long double` as it is very costly (_Primer_, p. 34)
<!-- omit in toc -->

#### Key Reading

- _Primer_: Sections 2.1 and 2.2.1 - 2.2.2, _Primitive Built-in Types_ and _Variables_ (pp 32 - 46)
- _C++_: Section 6.2, _Types_ (pp 138 - 151)
<!-- omit in toc -->

#### Supplementary Reading

- _Tour_: Section 1.4, _Types, Variables, and Arithmetic_ (pp 5 - 8)
- _Programming_:
  - Sections 3.8 and 3.9, _Types and objects_ and _Type Safety_ (pp 77 - 88)
  - Section 24.2, _Size, precision and overflow_ (pp 890 - 895)
  - Section 25.5.3, _Signed and unsigned integers_ (pp 961 - 965)
  <!-- omit in toc -->

#### CPP Reference

- [Fundamental Types](https://en.cppreference.com/w/cpp/language/types)

### Strings

<!-- omit in toc -->

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

- Watch out for `.size()` it returns an unsigned bespoke type so be careful of mixing it with signed numbers (_Primer_, p. 88)
- Comparison operators follow lexicographic ordering: `<, >, <=, >=`.
- For processing strings - searching, selecting etc, see _Primer_, section 3.2.3 (p. 90ff)
- `string` is usually implemented using **short-string optimization** where short strings (c. 14 chars) are kept in the `string` object itself, while longer strings are placed on the free store and referred to.
- Memory allocation for strings can be relatively costly.
- A `string_view` type allows manipulation of character sequences regardless of how they are stored (eg `std::string` or C-arrays)
- `getline()` can be used to get an entire line of input, including whitespace but _not including newline_. Use as follows:
  ```C++
  string line;
  while (getline(cin, line))
      cout << line << '\n'; //NB have to add '\n' back in
  ```
- You cannot `switch` on strings, annoyingly.
<!-- omit in toc -->

#### Key Reading

- _Primer_: Section 3.2, _Library `string` Type_ (pp 84 - 96)
- _C++_: Chapter 36, _Strings_ (pp 1033 - 1049), especially:
  - Section 36.4, _Advice_ (p. 1049)
  - Section 36.2.1 _Classification Functions_ (p. 1034)
  - Section 36.3.7 _The `find` Family_ (p. 1046) on search methods
  <!-- omit in toc -->

#### Supplementary Reading

- _Tour_: Section 9.2, _Strings_ (pp 111 - 114)
- _Programming_ Section 23.2 and 23.3, _Strings_ and _I/O Streams_ (pp 850 - 855), especially:
  - Selected string operations (p. 851)
  <!-- omit in toc -->

#### Core Guidelines

- [std::string](http://isocpp.github.io/CppCoreGuidelines/CppCoreGuidelines#SS-string)
- [Use std::string to own character sequences](http://isocpp.github.io/CppCoreGuidelines/CppCoreGuidelines#Rstr-string)
- [Use char\* to refer to a single character](http://isocpp.github.io/CppCoreGuidelines/CppCoreGuidelines#Rstr-char*)
- [Use 's' suffix for string literals meant to be std::string](http://isocpp.github.io/CppCoreGuidelines/CppCoreGuidelines#Rstr-s)
<!-- omit in toc -->

#### CPP Reference

- [String Library](https://en.cppreference.com/w/cpp/string)
- [basic strings](https://en.cppreference.com/w/cpp/string/basic_string)

### Vectors

<!-- omit in toc -->

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

- For fiddly aspects of initialization, including **list initialization** and **element counts** see _Primer_, p. 99.
- Key to vectors in C++ is that they _grow efficiently_. Unless all the elements have the same value it is better to initialize an empty vector and then grow it, rather than create a vector of a specific size. (_Primer_, p. 101). Unlike C/Java.
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

- Range checking is a common problem. Accessing elements out of range does not throw compiler error, and causes undefined values to be returned. For Stroustrup's custom solution see _Tour_, pp 141-142.
- Consider vectors the default container, use them unless you have a reason not to (Stroustrup).
<!-- omit in toc -->

#### Key Reading

- _Primer_: Section 3.3, _Library `vector` Type_ (pp 96 - 105)
- _Programming_: Section 4.6, `vector` (pp 117 - 125)
<!-- omit in toc -->

#### Supplementary Reading

- _Tour_: Section 11.2, `vector` (pp 138 - 142)
- _C++_: Section 31.4.1, `vector` (pp 902 - 906)
- _Programming_: Chapters 17, 18, and 19 implement a `vector` Template and deep dive into how it works. They cover a lot of ground inc. constructors, destructors, the free store, templates etc. Useful reference for specific issues.
<!-- omit in toc -->

#### Core Guidelines

- [Containers](https://isocpp.github.io/CppCoreGuidelines/CppCoreGuidelines#SS-con)
- [Prefer STL `vector` by default](https://isocpp.github.io/CppCoreGuidelines/CppCoreGuidelines#Rsl-vectorr)
- [Avoid Bounds Errors](https://isocpp.github.io/CppCoreGuidelines/CppCoreGuidelines#Rsl-bounds)
<!-- omit in toc -->

#### CPP Reference

- [vectors](https://en.cppreference.com/w/cpp/container/vector)

## Topic 2b User Defined Types: Enumerations and Classes

### Enumerations

<!-- omit in toc -->

#### Points to Remember

- **Enumerations**, or `enums` are a simple user-defined type. They specify a set of values (or **enumerators**) as _symbolic constants_ and allow us to group together _sets of integral constants_.
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
<!-- omit in toc -->

#### Key Reading

- _Programming_: Section 9.5, _Enumerations_ (pp 318 - 321)
- _Primer_: Section 19.3, _Enumerations_ (pp 832 - 835)
<!-- omit in toc -->

#### Supplementary Reading

- _C++_: Section 8.4, _Enumerations_ (pp 218 - 224)
<!-- omit in toc -->

#### Core Guidelines

- [Enumerations](https://isocpp.github.io/CppCoreGuidelines/CppCoreGuidelines#S-enum)
- [Use enumerations to represent sets of related named constants](https://isocpp.github.io/CppCoreGuidelines/CppCoreGuidelines#Renum-set)
- [Prefer enum classes over "plain" enums](https://isocpp.github.io/CppCoreGuidelines/CppCoreGuidelines#Renum-class)
- [Define operations on enumerations for safe use](https://isocpp.github.io/CppCoreGuidelines/CppCoreGuidelines#Renum-oper)
- [Avoid ALL_CAPS](https://isocpp.github.io/CppCoreGuidelines/CppCoreGuidelines#Renum-caps)
- [Avoid unnamed enums](https://isocpp.github.io/CppCoreGuidelines/CppCoreGuidelines#Renum-unnamed)
- [Specify the underlying type of the enum only if necessary](https://isocpp.github.io/CppCoreGuidelines/CppCoreGuidelines#Renum-underlying)
- [Specify the enumerator values only if necessary](https://isocpp.github.io/CppCoreGuidelines/CppCoreGuidelines#Renum-value)
<!-- omit in toc -->

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
- By having multiple constructors with different arguments, we can create a variety of ways of initializing class objects, ie constructors can be _overloaded_ like regular functions.
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

- We define and declare member functions similarly to ordinary functions. Member functions _must_ be declared within the class. They _may_ be defined inside the class itself or outside the class body using the namespace: `Class::memberFunction(){};`.
- See section on [header files](#points-to-remember-9) for the usual way of declaring and defining member functions.
- Almost always, when a member function is called, it is called on behalf of an object (an instance of the class).
- When a member function is called an extra, implicit parameter is initialized, called `this`. `this` is a const pointer to the address of the object on which the function was evoked.
- Inside a member function we can then refer directly to members of the object without any access operator or namespace. It will be interpreted as an implicit reference to `this`.
- So an ordinary member function declaration specifies three distinct things:
  - The function can access the private parts of the class declaration.
  - The function is in the scope of the class.
  - The function must be invoked on an object (has a `this` pointer).
- You can declare a member function `static` to give it the first two properties only. And you can declare a nonmember function a `friend` to give it the first property. (This is covered later).
- The compiler processes classes in two steps. First member declarations are compiled, and then member function bodies are processed. So member functions can use other members in the class regardless of where those members are declared.
<!-- omit in toc -->

#### Key Reading

- _Programming_, Chapter 9, _Technicalities: Classes, etc_ (pp 303 - 342) Ch. 9 evolves a date class, growing in complexity.
- _C++_, Sections 16.1 - 16.2.5 (pp 449 - 457), and p. 571.
<!-- omit in toc -->

#### Supplementary Reading

- _Tour_, Sections 4.1 and 4.2 (pp 47 - 51)
- _Primer_:
  - Section 7.1.2, on member functions (pp 256 - 260)
  - Section 7.1.3, on class helper functions (pp 260 - 262)
  - Section 7.1.4, _Constructors_ (pp 262 - 266)
  - NB _Primer_ chapter on classes relies a lot on a case study built up over previous chapters so a bit hard to follow if you're not working through the book.
  <!-- omit in toc -->

#### Core Guidelines

- [Classes](https://isocpp.github.io/CppCoreGuidelines/CppCoreGuidelines#S-class)
- [Organize related data into structures (`struct` or `class`)](https://isocpp.github.io/CppCoreGuidelines/CppCoreGuidelines#Rc-org)
- [Use `class` not `struct` if there are invariants](https://isocpp.github.io/CppCoreGuidelines/CppCoreGuidelines#Rc-struct)
- [Use `class` not `struct` if there are any private members](https://isocpp.github.io/CppCoreGuidelines/CppCoreGuidelines#Rc-class)
- [Represent the distinction between _interface_ and _implementation_ in the class](https://isocpp.github.io/CppCoreGuidelines/CppCoreGuidelines#Rc-interface)
<!-- omit in toc -->

#### CPP Reference

- [Classes](https://en.cppreference.com/w/cpp/language/classes)
- [Default Constructor](https://en.cppreference.com/w/cpp/language/default_constructor)

## Topic 2c Source File Organization

### Class Structure and Header Files

<!-- omit in toc -->

#### Points to Remember

- C++ allows for **separate compilation** where user code only sees the declarations of the classes and functions it uses (their _interfaces_).
- The full definitions are then in separate source code files and can be compiled separately, minimizing compile times.
- Typically a class is written in two files:
  - a **header file** `Class.h` containing the class definition and declarations of its member variables and functions.
  - an **implementation file** `Class.cpp`, with the full definitions of the class's member functions.
- For what can and can't be included in header files, see _C++_, p. 424.
- A `.cpp` file that is compiled by itself is called a **translation unit**, a program might contain thousands of units.
- The **One-Definition Rule** states that classes can only be defined once in a translation unit. For the full rule see _C++_, p. 425.
- The source code fragments are pulled together during **pre-processing**, a stage in building the program that executes before compilation, using the `#include` mechanism.

```C++
  #include "Class.h" //use quotes for class headers in current directory
  #include <iostream> //use <> for standard include directory, eg standard library.
  #include < string > //error, whitespace is significant
  #include " Class.h " //error whitespace is significant here too.
```

- `#include` is equivalent to pasting the text from the header file, bringing all the names into scope.
- Because each header represents a class as a self-contained unit, there can be a lot of redundancy in `#include` statements. We can also quickly get errors as class definitions are `#include`d more than once in the same translation unit, which breaks the _One-Definition Rule_.
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

<!-- omit in toc -->

#### Key Reading

- _C++_:
  - Section 15.2.2 - 15.2.4, _Header Files_, _The One-Definition Rule_, and _Standard-Library Headers_ (pp 424 - 428)
  - Section 15.3, _Using Header Files_ (pp 431 - 441)
  <!-- omit in toc -->

#### Supplementary Reading

- _Tour_, Section 3.2, _Separate Compilation_ (pp 30 - 32)
- _Primer_, Section 2.6.3, _Writing our Own Header Files_ (pp 76 - 77)
- _Programming_, Section 8.3, _Header Files_ (pp 264 - 266)
<!-- omit in toc -->

#### Core Guidelines

- [Source Files](https://isocpp.github.io/CppCoreGuidelines/CppCoreGuidelines#S-source)
- [Use header files for all declarations used in multiple files](https://isocpp.github.io/CppCoreGuidelines/CppCoreGuidelines#Rs-declaration-header)
- [Header files should be self-contained](https://isocpp.github.io/CppCoreGuidelines/CppCoreGuidelines#Rs-contained)
- [Use `#include` guards on all header files](https://isocpp.github.io/CppCoreGuidelines/CppCoreGuidelines#Rs-guards)
- [Put `#include` at the top of files](https://isocpp.github.io/CppCoreGuidelines/CppCoreGuidelines#Rs-include-order)
- [Avoid cyclic dependencies if possible](https://isocpp.github.io/CppCoreGuidelines/CppCoreGuidelines#Rs-cycles)
<!-- omit in toc -->

#### CPP Reference

- [Source file inclusion](https://en.cppreference.com/w/cpp/preprocessor/include)
- [#pragma once](https://en.cppreference.com/w/cpp/preprocessor/impl)
- [preprocessor conditional inclusion - `ifdef` etc](https://en.cppreference.com/w/cpp/preprocessor/conditional)

## Topic 3: File Handling, Input Streams, and Exceptions

### File Handling

<!-- omit in toc -->

#### Points to Remember

- In C++, a **file** is an abstraction on what the OS provides. It is a sequence of bytes numbered from 0 upwards.
- In C++, the assumption is that these "bytes on disk" are characters in the usual character set. So by default a **file stream** interprets a sequence of bytes as a sequence of characters and converts them to objects in memory (or vice versa).
- The `<fstream>` header defines three types to use for file IO. `ifstream` to read from a file, `ofstream` to write to a file, and `fstream` to read and write to the same file.
- These types inherit the same operations as the standard streams `cin` and `cout`, eg `<<` and `>>`. They have the same stream states.
- They also have custom methods for managing files, used as follows:

```C++
#include <fstream>
#include <string>
//using a "example.csv" file in the same directory as an example
std::string file = "example.csv"

std::ifstream inputFS; //creates an input file stream
inputFS.open(file) //opens the file and binds it to inputFS

std::ifstream inputFS2{file}; // equivalent to above, using constructor to open file

inputFS.close(); //closes the file
inputFS.is_open(); //returns true if file has been opened successfully and not closed.
```

- Once a file has been bound to a stream it must be closed before that stream can be bound to another file.
- If the call to `open` fails, the stream `failbit` will be set, which you can use to check whether it is safe to proceed:

```C++

std::ifstream inputFS{"example.csv"}

if(inputFS) {...} //only execute if file has opened

if(inputFS.is_open()) {...} //alternative, does the same thing

if(!inputFS) {error()...} //Stroustrup's preference, throw the error, then main logic is not wrapped in `if`.
```

- When a filestream object goes out of scope it is destroyed and `close` is called automatically.
- When an output file is closed its buffer is flushed.
- Opening a file implicitly using the stream constructor, and allowing the scope of the stream to close it is the ideal. (Stroustrup, _Programming_, p. 351)

#### File Modes

- Each stream has an associated **file mode** that represents how the file may be used.
- The full list of file modes is:
  - `in` - Open for input (not available on `ofstream` objects)
  - `out` - Open for output (not available on `ifstream` objects)
  - `app` - "append". Seek to the end of the file before every write
  - `ate` - "at end". Seek to the end of the file immediately after open
  - `trunc` - Truncate the file to 0 length
  - `binary` - Do IO operations in binary mode, when the default 'char' based IO is not appropriate.
- We can supply the file mode after the filename string when we call `open`, the mode is set again every time the file is opened.
- NB if we open a file for output it is opened in `trunc` mode by default, so the contents are discarded:

```C++
#include <fstream>

std::ofstream output{"example.csv"} //contents of "example.csv" are discarded

std::ofstream output{"example.csv", std::ofstream::app} //preserves the file contents, appends to end of file

std::fstream output{"example.csv"} //preserves file content, file available for input and output

```

<!-- omit in toc -->

#### Key Reading

- _Primer_: Section 8.2, _File Input and Output_ (pp 316 - 320)
- _Programming_:
  - Sections 10.3 - 10.5, _Files_, _Opening a file_, _Reading and writing a file_ (pp 349 - 354)
  - Section 11.3, _File opening and positioning_ (pp 388 - 394)
  <!-- omit in toc -->

#### Supplementary Reading

- _Tour_: Section 10.7, _File Streams_ (p. 130)
- _CPP_: Section 38.2.1, _File Streams_ (pp 1076 - 1078)
<!-- omit in toc -->

#### CPP Reference

- [`<fstream>` Header](https://en.cppreference.com/w/cpp/header/fstream)
- [Stream states](https://en.cppreference.com/w/cpp/io/ios_base/iostate)
- [`ifstream` - File input stream](https://en.cppreference.com/w/cpp/io/basic_ifstream)
- [`ofstream` - File output stream](https://en.cppreference.com/w/cpp/io/basic_ofstream)
- [`fstream` - File I/O stream](https://en.cppreference.com/w/cpp/io/basic_fstream)
- [`open` a file for input](https://en.cppreference.com/w/cpp/io/basic_ifstream/open)

### Input Streams and Tokenizing

<!-- omit in toc -->

#### Points to Remember

- Remember the fundamental purpose of an IO stream is to translate between a sequence of bytes (usually) interpreted as standard [ASCII characters](https://en.cppreference.com/w/cpp/language/ascii) ('a', '3', '\n' etc) and objects in memory of any type.
- The standard stream libraries provide two main tool-kits to do this:
  - **Formatted operations** are recommended, they come with a lot of support for error handling and formatting built-in types.
  - **Unformatted operations** provide lower-level control of how characters are interpreted, and should be used only if necessary, a lot of room for error.
- **Formatted input** is provided by two main operators:
  - `inputStream >> x` reads from the stream according to the type of `x`. The `>>` operator can be _overloaded_ to handle user-defined types.
  - `getline(inputStream, s)` reads a line from `inputStream` into a string `s`. It terminates on the `\n` character, discards it from the stream, and does not store it in `s`.
- NB almost all formatted IO operations and methods return a reference to the stream so can be chained together.
- For unformatted input operations and their challenges see eg _C++_, p. 1083.
- `>>` will keep reading characters until it encounters a character that doesn't fit the type it is reading into. For example:

```C++

#include <iostream>
#include <string>

using std::string;
using std::cin;

//hypothetical input of "12345a 23.415"

int x;
string s, s2;
double d;
cin >> x; // x will be 12345
// input stream will now be "a 23.415"
cin >> s; // s will be "a", formatted string input is terminated on whitespace by default
// input stream will now be " 23.415"
cin >> d; // d will be "23.415", leading whitespace is ignored

//alternatively read a whole line of input, input is "12345a 23.415" terminated by '\n'

std::getline(cin, s2); //s2 is "12345a 23.415"
```

- On when to use `>>` and when to use `getline()` see _Programming_, pp 395 - 396.
- Strings themselves can be used as input streams using the `<sstream>` library.
- The unformatted version of `getline()` can be called with a delimiter as a third argument.
- These could be combined to grab a line from a CSV file as a string, and then use that line as a input stream for parsing with the `,` separator (bit fiddly though and no error handling, better ways of doing this, you'd have to use character level manipulation to handle the `,` in places). Shown as an example of mixing formatted and unformatted input methods:

```C++
#include <iostream>
#include <string>
#include <sstream>
#include <vector>

using std::string;

    string s = "Bob,Jones,32,5"; //line from csv, result of calling getline() on the csv file stream

    std::istringstream stringStream{s}; //stringStream is now an input stream consisting of s.

    string firstName,
        secondName;
    int age, children;

    getline(stringStream, firstName, ',');  //terminates on ',' and discards
    getline(stringStream, secondName, ','); //NB preserves any leading whitespace
    stringStream >> age;                    //gets last value, ignores trailing ',' but would put back on stream
    stringStream.ignore(1, ',');            //ignores single character
    stringStream >> children;

    //better way, just tokenise to strings and then validate the tokens:

    string s2 = "Fred,Flintstone,32,2";

    std::istringstream ss2{s2};
    std::vector<string> tokens;

    for(string token; getline(ss2,token,','); ) {
        tokens.push_back(token);
    } //tokens now has a set of fields in the csv line handle validation elsewhere
```

- NB a lot of formatting methods are more useful for output processing than input, this is covered later.

<!-- omit in toc -->

#### Key Reading

- _Programming_:
  - Chapter 6 is an extended deep dive on approaching handling input by building a command line calculator, implementing a custom `Token` class for tokenization. A very different approach to the UoL module, worth following through.
  - Chapters 10 and 11 are also deep dives into I/O. Sections particularly relevant are:
    - Section 10.6, _I/O error handling_ (pp 354 - 358)
    - Section 10.7, _Reading a single value_ (pp 358 - 363)
    - Sections 10.9, 10.10, and 10.11, _User-defined input operators_, _A standard input loop_, and _Reading a structured file_ (pp 365 - 376)
    - Section 11.1, _Regularity and Irregularity_ (p. 380)
    - Sections 11.4 - 11.7, _String Streams_, _Line-oriented input_, _Character classificaitons_, _Using nonstandard separators_
- _Primer_: Section 17.5.1 and 17.4.2, _Formatted and unformatted Input/Output operations_ (pp 753 - 763) (includes stuff on formatting output not relevant here)
<!-- omit in toc -->

#### Supplementary Reading

- _C++_:
  - Section 38.4.1, _Input Operations_ (pp 1081 - 1084)
  - Section 38.6, _Buffering_ (pp 1100 - 1105)
- _Primer_: Section 8.3, _String Streams_ (pp 321 - 323)
- _Programming_:
  - Section B.7.3, _Input Operations_ (p. 1172)
  - Section B.8.1, _Character Classification_ (p. 1175)
  <!-- omit in toc -->

#### Core Guidelines

- [Use character level input only when necessary](https://isocpp.github.io/CppCoreGuidelines/CppCoreGuidelines#Rio-low)
- [Always handle ill-formed input](https://isocpp.github.io/CppCoreGuidelines/CppCoreGuidelines#Rio-validate)
<!-- omit in toc -->

#### CPP Reference

- [`>>` Operator](https://en.cppreference.com/w/cpp/io/basic_istream/operator_gtgt)
- [getline() Template](https://en.cppreference.com/w/cpp/string/basic_string/getline)
- [ASCII Chart](https://en.cppreference.com/w/cpp/language/ascii)

### Exception Handling

#### Points to Remember

- An **exception** is a run-time anomaly, such as losing a database connection or receiving bad input, that is outside the normal functioning of a program. Managing exceptions is one of the hardest parts of program design.
- **Exception handling** allows separately developed parts of a program to communicate about and handle problems that occur at run time, separating problem detection from detection resolution.
- This is valuable, because the detecting part might not be best placed to decide how to resolve the situation.
- There are three main building blocks in C++ for exception handling:
  - **`throw` expressions** which the detecting part uses to signal that it encountered a problem. A `throw` **raises** an exception.
  - **`try` blocks** which the handling part uses to deal with an exception. Also referred to as **exception handlers**. They consist of the `try` keyword followed by one or more `catch` clauses.
  - A set of **exception classes** that hare used to pass information about what happened from a `throw` to an associated `catch`.
- Error handling in general is a huge topic. On when to use exceptions and when to use other tools, see _Tour_, p. 39.
- It is also strongly linked to safe resource management, see the discussion of _RAII (Resource Acquisition Is Initialization)_ in _Tour_, p. 72.

#### Throwing an Exception

- When a function detects a problem it _throws_ or _raises_ an exception using the [`throw` keyword](https://en.cppreference.com/w/cpp/language/throw), followed by an expression. The type of the expression determines what kind of exception is thrown. For example:

```C++
if(varA != varB)
  throw runtime_error("Your variables don't match!");
else
  //all is fine, normal logic
```

- When a `throw` is executed, any statements following the `throw` are not executed, instead control is transferred to a matching `catch` block (if any). The catch might be local to the same function or a direct or indirect caller. So think of `throw` as like a `return` statement.
- After an exception has been thrown, the current function is suspended and the search for a matching catch clause by **unwinding** the execution stack, looking up the chain of nested function calls until a `catch` clause for the exception is found.
- If a matching `catch` is found, that `catch` is entered and the program executes the code inside. It then continues execution immediately after the last `catch` clause associated with that try block.
- If no matching `catch` is found the program calls the library `terminate` function, and excecution is stopped. Precise behaviour of `terminate` is system-dependent.
- Because normal execution is halted immediately an exception is thrown:
  - Functions along the chain may be prematurely exited
  - Objects are automatically destroyed during stack unwinding
  - Where objects have a destructor, those are executed automatically
  - If thrown during a constructor, the object will be destroyed
  - If thrown during the creation of a container (eg vector), the container will be destroyed.
  - This is why we use constructors to allocate resources rather than doing it manually, to ensure proper destruction.
- Programs that properly clean up during exception handling and avoid resource leaks etc are called **exception safe**.
- Sometimes a single `catch` might not completely handle an exception, it can **re-throw** the exception by using the `throw` keyword with no following expression: `throw;`it can modify the exception object (by reference) before the re-throw.

#### Catching an Exception

- The general form of a [try/catch block](https://en.cppreference.com/w/cpp/language/try_catch) is:

```C++
try {
  //program logic
  //NB varibles declared here are inaccessible within catch blocks
} catch (exception-declaration) {
  //handler-statements
} catch (exception-declaration) {
  //handler-statements
} //program continues...
```

- The **exception declaration** in a catch clause looks like a function parameter list with exactly one parameter, the type of the declaration determines what kinds of exceptions the handler can catch.
- Ordinarily a catch takes an exception type by reference.
- The catch that is found, going up the execution stack and through the list of catch blocks at each level, is the first one that matches the exception at all.
- So generally write specialized catch blocks first, before more general ones.
- You can catch all exceptions as follows: `catch (...) {//handle anything}`. Any `catch` statements following this in a block will never be matched. Often used to do some tidying and then rethrow.

#### Exception Classes

- The C++ library defines several classes it uses to report problems that can be used in our programs. Several key ones are defined in the `<stdexcept>` header.
- These include `runtime_error`, `range_error`, `invalid_argument`, see _Primer_, p. 197 for full list.
- Library exception classes have only a few operations, you can create, copy and assign objects of any of the types.
- Most of the exception types _must_ be initialized from a string containing more info. IE `runtime_error()` would error, no default initializer, but `runtime_error("my error message")` is OK.
- The exception types define a single operation named `what`, that takes no arguments and returns a C-string with info on the exception thrown. Often the intializer string if applicable. eg:

```C++
catch (runtime_error& e) {
  cout << e.what() << '\n';
}
```

- It is possible to define your own exception types, freestanding or inheriting from the standard library types. For discussion and examples see _Primer_, pp 782 - 784.
<!-- omit in toc -->

#### Key Reading

- _Primer_:
  - Section 5.6, _Try Blocks and Exception Handling_ (pp 193 - 198)
  - Section 18.1, _Exception Handling_ (pp 772 - 785)
- _Programming_:
  - Section 5.5, _Run-time errors_ (pp 140 - 146)
  - Section 5.6, _Exceptions_ (pp 146 - 154)
  <!-- omit in toc -->

#### Supplementary Reading

- _Tour_:
  - Section 3.5, _Error Handling_ (pp 35 - 40)
- _C++_: Chapter 13, _Exception Handling_ (pp 343 - 387).
  - Very deep dive, see especially: - Section 13.5, _Throwing and Catching Exceptions_, pp 363 - 374 - _Advice_, p. 387 - _Traditional Error Handling_, pp 345 - 346 - _Exception Guarantees_, pp 353 - 354
  <!-- omit in toc -->

#### Core Guidelines

- [Error Handling](https://isocpp.github.io/CppCoreGuidelines/CppCoreGuidelines#S-errors)
- [Throw an exception to indicate a function cannot complete its task](https://isocpp.github.io/CppCoreGuidelines/CppCoreGuidelines#Re-throw)
- [Design error handling around _invariants_](https://isocpp.github.io/CppCoreGuidelines/CppCoreGuidelines#Re-design-invariants)
- [Use RAII to avoid resource leaks](https://isocpp.github.io/CppCoreGuidelines/CppCoreGuidelines#Re-raii)
- [Properly order your catch clauses](https://isocpp.github.io/CppCoreGuidelines/CppCoreGuidelines#Re_catch)
<!-- omit in toc -->

#### CPP Reference

- [Exceptions overview](https://en.cppreference.com/w/cpp/language/exceptions)
- [Exception types](https://en.cppreference.com/w/cpp/error/exception)
- [`throw` expression](https://en.cppreference.com/w/cpp/language/throw)
- [`try` block](https://en.cppreference.com/w/cpp/language/try_catch)

## Topic 4: Associative Containers and Sorting

### Associative Containers: Maps and Sets

<!-- omit in toc -->

#### Points to Remember

- A **map** in C++ is a means of efficiently storing and retrieving _(key, value)_ pairs. Along with a **set** it is one of the two main **associative containers** in C++.
- There are two kinds of maps:
  - `<map>` (`std::map<T1,T2>`) is implemented as a balanced binary search tree and requires an _ordering function_ (default is `<`). Cost of a lookup is `O(log(n))` where `n` is the number of elements in the map.
  - `<unordered_map>` (`std::unordered_map<T1,T2>`) is a hash table, and provides hashing functions for STL and built-in types. Lookup will be faster with a good hashing function than an ordered map `O(1)`.
- Use unordered where you need fast lookup on a large set, or if elements have no natural order, ordered where you need to iterate in order over the set.
- For constraints on what types can be used as keys see _Primer_, p. 424.
- When we fetch an element from a map we get an object of type `pair` with two data elements `first` (the key) and `second` (the value), see example below.
- Their use is pretty similar, `map` shown here:

```C++
#include <map>
#include <string>
#include <iostream>

using std::map;
using std::string;

map<string,int> phone_directory {
  {"Matthew King", 123456},
  {"Sara Santos", 3455212},
  {"Marco Gilles", 987653}
};

string name = "Matthew King";

std::cout << phone_directory[name]; // prints 123456

string unknown = "Brian Blessed";

int number = phone_directory[unknown]; // key is not found, so entered on the map with default value, 0 for integers

std::cout << number //default value (0)

map<string, int> word_count;
string word;

while(cin >> word) {
  ++word_count[word]; //Note this creates an entry with 0 and increments to 1 if not previously seen.
}

for (const auto &w : word_count) {
  std::cout << w.first << " occurs " << w.second << " times." <<std::endl;
  }
```

- NB there are also `multimap<T1,T2>` and `unordered_multimap<T1,T2>` types where a key can occur multiple times. For example a dictionary with multiple definitions of a single word.
- There is also a `set<T>` type which is a `map` where there is no value, just a key. It also has a corresponding `multiset<T>` type. An `unordered_set<T>` and `unordered_multiset<T>` are hash-table versions of sets.
- Use cases for sets include a list of ignore words in text processing:

```C++
#include <set>
#include <string>

std::set<std::string> exclude = {"the", "but", "and", "a", "an", "or", "A", "An"}
```

<!-- omit in toc -->

#### Key Reading

- _Primer_: Chapter 11, _Associative Containers_ (pp 419 - 447)
- _Programming_: Section 21.6, _Associative containers_ (pp 776 - 789)
<!-- omit in toc -->

#### Supplementary Reading

- _Tour_, Sections 11.4 and 11.5, _`map`_ and _`unordered_map`_ (pp 144 - 146)
- _C++_, Section 31.4.3, _Associative Containers_ (pp 909 - 920)
<!-- omit in toc -->

#### CPP Reference

- [Associative Containers](https://en.cppreference.com/w/cpp/named_req/AssociativeContainer)
- [`std::map`](https://en.cppreference.com/w/cpp/container/map)
- [`std::set`](https://en.cppreference.com/w/cpp/container/set)

### Sorting

<!-- omit in toc -->

#### Points to Remember

- The `std::sort()` algorithm in the `<algorithm>` header, known as **plain sort** comes in two flavours:

```C++
sort(b,e) //Sort [b:e)
sort(b,e,f) //Sort [b:e) using f(*p,*q) as the sort criterion

//example of use:

#include <algorithm>
#include <vector>

std::vector<int> myVector{9,8,7,6,5,4,3,2,1};

std::sort(myVector.begin(),myVector.end()) //sorts vector in ascending order

//dummy custom comparator function
bool greaterThan(int a, int b) {
  return a > b;
}

std::sort(myVector.begin(),myVector.end(),greaterThan) //sorts in descending order
```

- The default comparator is the `<` operator.
- The first two arguments are iterators marking the beginning and end of the range to be sorted. The iterators must meet the random access requirement.
- Equivalence of values `a` and `b` is not done through `==` rather `!(a<b)&&!(b<a)`.
- Basic sort efficiency on average is `N*log(N)`.
- `stable_sort()` maintains the order of equal elements, its efficiency is `N*log(N)*log(N)` but improves with sufficient system memory.
- For other members of the `sort` family, see _C++_, p. 943.
<!-- omit in toc -->

#### Key Reading

- _Programming_, Section 21.8, _Sorting and Searching_ (pp 794 - 796)
- _C++_, Section 32.6, _Sorting and Searching_ (pp 942 - 945)
<!-- omit in toc -->

#### CPP Reference

- [`sort()`](https://en.cppreference.com/w/cpp/algorithm/sort)
- [`stable_sort()`](https://en.cppreference.com/w/cpp/algorithm/stable_sort)
- [`partial_sort()`](https://en.cppreference.com/w/cpp/algorithm/partial_sort)

## Topic 5: Member Functions and Operator Overloading

### Member Functions Continued: `static`, `const` and `friend` functions

#### `static` functions

- Classes sometimes need members that are associated with the class, rather than with individual objects of the class type. For example, a bank account might need a data member representing the current prime interest rate. We would not want every object to store that rate.
- A member is associated with the class, rather than particular objects, by adding the keyword `static` to its declaration.
- `static` members can be public or private, data members can be `const`, reference, array, class type etc.
- The `static` members exist outside any object. Objects do not contain the data associated with `static members`, nor do `static` member functions have a `this` pointer.
- `static` member functions cannot therefore be `const`, or refer to `this`, explicitly or implicitly (by calling a non-static member function).
- We declare a static member function in the class definition, the definition of the function can be outside the class definition, you do not need to repeat the `static` keyword. For example:

```C++
class Account {
public:
  void calculate() { amount += amount * interestRate;} //member functions can use static members directly
  static double rate() {return interestRate;}
  static void rate(double);
private:
  std::string owner;
  double amount;
  static double interestRate;
  static double initRate();
};

void Account::rate(double newRate) {
    interestRate = newRate;
}

double r;
r = Account::rate(); //We can access a static member using the scope operator

//we can access static members through an object of the class type too.
Account ac1;
Account *ac2 = &ac1;

r = ac1.rate(); //through an account object or reference
r = ac2->rate(); //through a pointer
```

#### `const` member functions

- `const` member functions may not change the state of the object on which they are called.
- We should make member functions const by default ([core guidelines](https://isocpp.github.io/CppCoreGuidelines/CppCoreGuidelines#Rconst-fct)).
- The effect of a `const` declaration is to change the implicit `this` pointer to a const version of the object (See _Primer_, p. 258).
- The `const` keyword goes in the class declaration after the parameter list. It must also be listed in the function definition. The const becomes part of the function type.
- A const member function can be invoked for both const and non-const objects, whereas a non-const member function can only be invoked for a non-const object.
- An example of use:

```C++
class Date {
  int d,m,y;
  public:
    int day() const {return d;} //const member, day() cannot modify the object state
    int month() const {return m;} //as above
    int year() const;

    void add_year(int n); //not const, modifies state of object
};

int Date::year() //error, const missing in member function type
{
  return y;
}

int Date::year() const //ok
{
    return y;
}
```

#### `friend` functions

- A function that is not a member of a class can be granted access to all members through a `friend` declaration within the class definition.
- A class makes a function its friend by including a declaration for that function preceded by the keyword `friend`.
- Friend declarations may appear only within the class definition, they can appear anywhere inside, but best to group them at the start or end of the definition.
- A friend declaration only specifies access, it is not a general declaration and the function should still be declared as normal, though many compilers allow you to skip this.
- Examples of use cases would be when a function needs to access two classes:

```C++
Vector operator*(const Matrix&, const Vector&);

class Vector {
  friend Vector operator*(const Matrix&, const Vector&);
  //...
}

class Matrix {
  friend Vector operator*(const Matrix&, const Vector&);
  //...
}
```

<!-- omit in toc -->

#### Key Reading

_On `static` members_:

- _Primer_, section 7.6, _`static` Class Members_, pp 300 - 304.

_On `const` members_:

- _C++_, section 16.2.9.1 _Constant Member Functions_, p. 461.
  _On Friends_:
- _Primer_, sections 7.2.1, _Friends_, pp 269 - 271, and 7.3.4, _Friendship Revisited_, pp 279 - 282.

<!-- omit in toc -->

#### Supplementary Reading

_On static members_:

- _C++_, section 16.2.12, _`static` Members_, pp 467 - 468.

_On `const` members_:

- _Primer_, p. 258

_On Friends_:

- _Programming_, section A.12.1.3 _Friends_, p. 1111.

<!-- omit in toc -->

#### Core Guidelines

- [Make member functions `const` by default](https://isocpp.github.io/CppCoreGuidelines/CppCoreGuidelines#Rconst-fct)
<!-- omit in toc -->

#### CPP Reference

- [static members](https://en.cppreference.com/w/cpp/language/static)
- [const member functions](https://en.cppreference.com/w/cpp/language/member_functions#const-_and_volatile-qualified_member_functions)
- [friend declarations](https://en.cppreference.com/w/cpp/language/friend)

### Operator Overloading

<!-- omit in toc -->

#### Points to Remember

- You can define almost all C++ operators for class or enumeration operands. This is often referred to as _operator overloading_.
- You can only define existing operators, not make up new ones, e.g. you cannot invent a `$=` operator.
- You can only use the conventional number of operands, e.g. you cannot have a unary `<=` operator.
- Four symbols serve as both unary and binary operators `+ - * &`. The number of parameters in the overloading function determines which operator is being overloaded.
- Overloaded operators must have at least one user defined type as an operand, eg you can't overload `+` operating on two `int` objects.
- Try to define operators with their conventional meaning, e.g. `+` means addition.
- An example in use:

```C++
enum class Month {
  Jan =1,Feb,Mar,Apr...
}

Month operator++(Month& m) {
  m = (m==Month::Dec) ? Month::Jan : Month(int(m)+1);
  return m;
}

Month m = Feb;

m++; //m is now Mar
operator++(m); //equivalent, m is now Apr
```

- The following operators cannot be overloaded: `?: . .* :: sizeof typeid alignas noexcept`
- Operand evaluation guarantees are not preserved for overloaded operators. For example in `&&` or `||` operations.
- So ordinarily don't overload these operators: `&& || , &` - their behaviour may surprise users.
- If a class has `==`, it should probably have `!=` as well. Likewise if it has `<` it should probably have other relations.
- Where an operator overload is a class member function, the first (left-hand) operand is bound to the implicit `this` pointer. So member operator functions have one less explicit parameter than the number of operands.
- Some tips on when to define overloads as member or non-member functions:
  - Assignment (`=`), subscript (`[]`), call (`()`), and member access arrow (`->`) must be defined as member functions.
  - Compound assignment operators (eg `+=`) should be defined as member functions.
  - Operators that change the state of their object or are closely tied to their given type (eg increment, decrement, dereference) usually should be member functions
  - Symmetric operators - those that might convert either operand (eg arithmetic, equality, relational, bitwise) should usually be non-member functions.
  - IO operators should be non-member functions.
  - Any time the left-hand operand might not be an object of the class, the overload should be a non-member function.
- An example of overloading the ostream operator `<<` from _Primer_, p. 557:

```C++
ostream &operator<<(ostream &os, const Sales_data &item) {
  os << item.isbn << " " << item.units_sold << " "
     << item.revenue << " " << item.avg_price();
  return os;
}
```

- Generally output operators should print the contents of the object with minimal formatting, they should not print a newline.
- Input operators must deal with the possibility that input might fail, output operators generally don't bother. In particular, input operators need to make sure they leave the object in a valid state.
- Sometimes the input operator might need to do additional validation (like checking a value is in a range), if that validation fails the operator can set the `failbit` of the stream to indicate failure.
- For outlines of other common operators and their use see _Primer_, pp 561 - 572.
<!-- omit in toc -->

#### Key Reading

- _Primer_, Chapter 14, _Overloaded Operations and Conversions_, p. 552ff
- _C++_, Chapter 18, _Operator Overloading_, p. 527ff
<!-- omit in toc -->

#### Supplementary Reading

- _Programming_, section 9.6, _Operator Overloading_, pp 321 -323.
<!-- omit in toc -->

#### Core Guidelines

- [Overloading Operators](https://isocpp.github.io/CppCoreGuidelines/CppCoreGuidelines#SS-overload)
- [Mimic Conventional Usage](https://isocpp.github.io/CppCoreGuidelines/CppCoreGuidelines#Ro-conventional)
- [Use non-member functions for symmetric operators](https://isocpp.github.io/CppCoreGuidelines/CppCoreGuidelines#Ro-symmetric)
- [Avoid implicit conversion operators](https://isocpp.github.io/CppCoreGuidelines/CppCoreGuidelines#Ro-conversion)
- [Define overloaded operators in the namespace of their operands](https://isocpp.github.io/CppCoreGuidelines/CppCoreGuidelines#Ro-namespace)
<!-- omit in toc -->

#### CPP Reference

- [Operator Overloading](https://en.cppreference.com/w/cpp/language/operators)
