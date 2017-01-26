# CodeChallenge 

## 1) 
Write a subroutine, function, or method that takes an array of characters and returns
an array of the same characters in reversed order with every consonant lower cased 
and every vowel upper cased. Prove your implementation works.
every consonant lower cased and every vowel upper cased. Prove your implementation 
works.

>> arraymodifier.py 

To run arraymodifier, clone the CodeChallenge repo and run *this* command:  

>> $ python arraymodifier.py 

The subroutine that reverses the string array is reverser(). 
The subroutine that proves reverser is working is tester(). 
Running this file runs tester(), which calls reverser(). To control the inputs of this subroutine, changes must be made to _omega_string_, which is found at the top of the file. 


## 2) 
Write code that a caller can use to transform an arbitrarily nested data structure 
into either html or a Javascript literal. Choice of language is up to you, choose something that you're comfortable with 
(intercal is probably a bad idea, but feel free...). Make sure to handle at least a linear collection (array / list), 
associative collection (hash / map), and individual item (scalar / object).

>> datatransformer.py 

To run datatransformer, clone the CodeChallenge repo and run *this* command:  

>> $ python datatransformer.py 

When this file is run, the following examples are transformed into html and js, 
and both transformation results are written to std output: 

    a = ["random", 0, 1]
    b = [{1: "one"}, "random", 0]
    c = {'a': 0, 'c': 2, 'b': 1, 'd': 3}
    d = [{1: "one"}, "random", 0, {'a': {'aa':00, 'ab':01,}, 'c': 2, 'b': 1, 'd': 3}]

(These are examples I played around with in the process of coding this.) 
