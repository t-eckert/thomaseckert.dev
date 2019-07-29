# Calculating n! in O(1) Time

It feels like a mathematical cheat code - bypassing the laws of math that demand rigor and work to be successful - but it's not. It plays by all the same rules as any other part of math.  

Factorials are used to calculate the number of combinations of things.  

``` math
1! = 1 = 1
2! = 2*1 = 2
3! = 3*2*1 = 6
4! = 4*3*2*1 = 24
5! = 5*4*3*2*1 = 120
```

They get big and hard to calculate very quickly. The number of calculations required to solve `n!` is equal to `n`.  

Factorials are so important that we have developed ways to calculate them more quickly. One way is to write down the calculations as we go. If we can keep a table of what `31573!` is, we don't have to multiply 31573 numbers together.  

However, this approach becomes untennable. You could quickly fill a book or the memory of a computer with a factorial table.

``` math
n! ≅ sqrt[(2n + 1/3) pi] * n^n * e^(-n)
```

How close is this approximation to the real answer?  

As n gets larger, the difference between the approximation and the actual number gets smaller.  
