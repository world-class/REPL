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
- [Topic 2b User Defined Types: Enumerations and Classes](#topic-2b-user-defined-types-enumerations-and-classes)
  - [Enumerations](#enumerations)
    - [Points to Remember](#points-to-remember-6)
    - [Key Reading](#key-reading-5)
    - [Supplementary Reading](#supplementary-reading-3)
    - [Core Guidelines](#core-guidelines-3)
    - [CPP Reference](#cpp-reference-4)
  - [Classes](#classes)
- [Topic 2c File Organization](#topic-2c-file-organization)

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
- A named variable can only be used if it is in **scope**. There are four levels of scope:
  - **Local Scope** - a name declared in a function, lambda or local block `{}`, includes function parameters.
  - **Class Scope** - a name is called a **member name** if it is declared in a class, outside any function or lambda.
  - **Namespace Scope** - a name is called a **namespace member name** if declared in a namespace outside a function/lambda.
  - **Global Scope** - a name declared outside any construct.
- variables can be made *immutable* by declaring them as `const` (meaning "I promise not to change this"), or `constexpr` (meaning "to be evaluated at compile time"), the difference is when the value is calculated either run-time or compile time respectively.
- in variable declarations `*` signifies a **pointer** and `&` signifies a **reference**. Both are ways to denote an object in memory without evaluating or copying it. The syntax to access the values is different (see *Tour*, p. 11)



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

## Topic 2b User Defined Types: Enumerations and Classes
### Enumerations
#### Points to Remember
- **Enumerations**, or `enums` are a simple user-defined type. They specify a set of values (or **enumerators**) as *symbolic constants* and allow us to group together *sets of integral constants*.
- Enumerations are very useful. Use them when we need a set of related named integer constants. EG, for alternatives (up,down; yes, no; on, off, N, S, E, W; bid, offer) or distinct values (red, green blue, yellow, crimson)
- There are two types of enumeration. Original `enums` are known as **plain** or **unscoped**. Their enumerators can "pollute" the scope in which the enum is defined as they implicitly export their enumerators to their scope. They also allow implicit conversion to int.
- Generally avoided now in favour of C++ **scoped enumerations** or `enum classes`, use as follows:

  ```C++
  enum class Month {
    jan =1, feb, mar, apr, may, jun, jul, aug, sep, oct, nov, dec
  };

  Month m = Month::feb; //good
  int n = m; //error, no implicit conversion from Month to int
  m = 7; //error, can't assign an int to a Month
  ```
- The `class` denotes that the enumerators are in the scope of the enumeration, so to refer to `jan` you say `Month::jan`. No implicit conversion to ints.
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

### Classes
## Topic 2c File Organization