# What are constants
## a constant is a value that may not be changed during the program’s execution.

### In C++, there are 2 types
- Named constants - constant values that are associated with an identifier. These are also sometimes called symbolic constants.
- Literal constants - constant values that are not associated with an identifier.


## Named constants
### 3 types - 3 ways to define it
- constant variables
- Object-like macros with substitution text
- Enumerated constants


## Constant variables
`const` double gravity { 9.8 }
 
### why {} - to prevent narrowing
const double gravity { 9.8 }; **brace initialization** or **uniform initialization**
It simply initializes the variable gravity with the value 9.8. It’s almost the same as: ``const double gravity = 9.8;`` but with some extra safety features.

Copy initialization	int x = 5;	Older style, works fine but allows some unwanted conversions
Direct initialization	int x(5);	Slightly safer
Brace (Uniform) initialization	int x{5};	Modern and safest — prevents narrowing conversions

🔍 Example 1: Safe initialization
int x { 5 };  // ✅ OK
double y { 5.5 }; // ✅ OK

⚠️ Example 2: Prevents narrowing conversions
int x { 5.5 };  // ❌ Error! 

Using {} prevents accidentally losing data (called narrowing).
- 5.5 is a double, and converting it to int would lose the decimal part.
- C++ disallows that when using {}.

But with =, it would allow it silently:
int x = 5.5;  // ✅ Allowed, but x becomes 5 (decimal part lost!)
So {} gives type safety — it forces you to be precise.

- Place const before the type (because it is more conventional to do so).
- Const variables must be initialized when you define them, and then that value can not be changed via assignment
- Note that const variables can be initialized from other variables (including non-const ones)
- Function parameters can be made constants via the const keyword: but Don’t use const for value parameters. why? Making a function parameter constant enlists the compiler’s help to ensure that the parameter’s value is not changed inside the function. However, in modern C++ we don’t make value parameters const because we generally don’t care if the function changes the value of the parameter (since it’s just a copy that will be destroyed at the end of the function anyway). The const keyword also adds a small amount of unnecessary clutter to the function prototype.
- A function’s return value may also be made const: but Don’t use const when returning by value.
- Whenever we can make a variable constant, do it. Exception cases include by-value function parameters and by-value return types, which should generally not be made constant.
- Prefer constant variables over object-like macros with substitution text.