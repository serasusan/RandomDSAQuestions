4 Numeral systems in C++
- decimal (base 10), binary (base 2), hexadecimal (base 16), and octal (base 8).


- Decimal - base 10
- 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, …
- By default, numbers in C++ programs are assumed to be decimal

```cpp 
int x { 12 }; // 12 is assumed to be a decimal number
```

- Binary - base 2 
- 0 and 1
- 0, 1, 10, 11, 100, 101, 110, 111, ...

- Octal - base 8
-  0, 1, 2, 3, 4, 5, 6, and 7
- 0, 1, 2, 3, 4, 5, 6, 7, 10, 11, 12, …
- To use an octal literal, **prefix your literal with a 0 (zero)**:

```cpp
#include <iostream>

int main()
{
    int x{ 012 }; // 0 before the number means this is octal
    std::cout << x << '\n';
    return 0;
}

output : 10
- Why 10 instead of 12? Because numbers are output in decimal by default, and 12 octal = 10 decimal.
```


#### Hexadecimal
- Hexadecimal - base 16. 
- 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, A, B, C, D, E, F, 10, 11, 12, …
- To use a hexadecimal literal, **prefix your literal with 0x**
```cpp
#include <iostream>

int main()
{
    int x{ 0xF }; // 0x before the number means this is hexadecimal
    std::cout << x << '\n';
    return 0;
}

output : 15
```

#### Binary
- Prior to C++14, there is no support for binary literals. However, hexadecimal literals provide us with a useful workaround 
eg. bin = 0x0008; // assign binary 0000 0000 0000 1000 to the variable
- In C++14 onward, we can use binary literals by using the 0b prefix
- bin = 0b11110000; // assign binary 0000 0000 1111 0000 to the variable


There are digit separators - quotation mark (‘) 
eg. int bin { 0b1011'0010 };

#### Outputting values.
- By default, C++ outputs values in decimal 
- But we can change the output format via use of std::dec, std::oct, and std::hex I/O manipulators
- once applied, the I/O manipulator remains set for future output until it is changed again.


```cpp
#include <iostream>

int main()
{
    int x { 12 };
    std::cout << x << '\n'; // decimal (by default)
    std::cout << std::hex << x << '\n'; // hexadecimal
    std::cout << x << '\n'; // now hexadecimal
    std::cout << std::oct << x << '\n'; // octal
    std::cout << std::dec << x << '\n'; // return to decimal
    std::cout << x << '\n'; // decimal

    return 0;
}

Output:
12
c
c
14
12
12
```

- Outputting values in binary is a little harder, as std::cout doesn’t come with this capability built-in. Fortunately, the C++ standard library includes a type called **std::bitset** that will do this for us (in the <bitset> header).
- To use std::bitset, we can define a std::bitset variable and tell std::bitset how many bits we want to store.

```cpp
#include <bitset> // for std::bitset
#include <iostream>

int main()
{
	// std::bitset<8> means we want to store 8 bits
	std::bitset<8> bin1{ 0b1100'0101 }; // binary literal for binary 1100 0101
	std::bitset<8> bin2{ 0xC5 }; // hexadecimal literal for binary 1100 0101

	std::cout << bin1 << '\n' << bin2 << '\n';
	std::cout << std::bitset<4>{ 0b1010 } << '\n'; // create a temporary std::bitset and print it

	return 0;
}
```

- To print binary in a formatted way, we can use *std::format*
eg. std::println("{:b} {:#b}", 0b1010, 0b1010);  
output - 1010 0b1010

{:b} formats the argument as binary digits:
{:#b} formats the argument as 0b-prefixed binary digits
