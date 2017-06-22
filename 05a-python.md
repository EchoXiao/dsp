# Learn Python

Read Allen Downey's [Think Python](http://www.greenteapress.com/thinkpython/) for getting up to speed with Python 2.7 and computer science topics. It's completely available online, or you can buy a physical copy if you would like.

<a href="http://www.greenteapress.com/thinkpython/"><img src="img/think_python.png" style="width: 100px;" target="_blank"></a>

For quick and easy interactive practice with Python, many people enjoy [Codecademy's Python track](http://www.codecademy.com/en/tracks/python). There's also [Learn Python The Hard Way](http://learnpythonthehardway.org/book/) and [The Python Tutorial](https://docs.python.org/2/tutorial/).

---

### Q1. Lists &amp; Tuples

How are Python lists and tuples similar and different? Which will work as keys in dictionaries? Why?

>> Python lists are mutable, such that elements in the list can be replaced, deleted, where tuples are immutable and cannot be modified. Only immutable data types can be used as keys in dictionaries, this is because using immutable data types prevents any subsequent list modifications that could potentially affect the __hash__ method to map the associate key values pairs.

---

### Q2. Lists &amp; Sets

How are Python lists and sets similar and different? Give examples of using both. How does performance compare between lists and sets for finding an element. Why?

>> Python sets are unordered collection with no duplicate values, where Python lists can have duplicates. A hash lookup is used to locate an element within sets, which is why sets are unordered and is a lot more efficient than searching within list, because List elements are located through indices. Sets also allow to do operations such as `intersection`, `union`, `difference`, and `symmetric difference`. 

---

### Q3. Lambda Function

Describe Python's `lambda`. What is it, and what is it used for? Give at least one example, including an example of using a `lambda` in the `key` argument to `sorted`.

>> lambda operator or lambda function is a way to create small anonymous one-timer function. Theya re mainly used in combination with the functions `filter()`, `map()`, `sorted()`, and `reduce()`.

```python
sorted(['Apple', 'PEACH', 'strawberry', 'banana'], key = lambda word: word.upper())
['Apple', 'banana', 'PEACH', 'strawberry']
```

---

### Q4. List Comprehension, Map &amp; Filter

Explain list comprehensions. Give examples and show equivalents with `map` and `filter`. How do their capabilities compare? Also demonstrate set comprehensions and dictionary comprehensions.

>> List comprehensions are very natural and easy way or list manipulation. 

```python
names = ['Anne', 'Amy', 'Bob', 'David', 'Carrie', 'Barbara', 'Zach']
lengths = map(len, names)
print lengths
[4, 3, 3, 5, 6, 7, 4]
```
>> The above python map can be written in a more compact and natural format using list comprehension.

```python
names = ['Anne', 'Amy', 'Bob', 'David', 'Carrie', 'Barbara', 'Zach']
print ([len(name) for name in names])
[4, 3, 3, 5, 6, 7, 4]
```
>> Same concept can be applied to `filter()` using list comprehension.

```python
squares = [x**2 for x in range(15)]
filtered_squares = [s for s in squares if s > 5 and s < 100]
print(filtered_squares)
[9, 16, 25, 36, 49, 64, 81]
```
>> Such that, equivalent results were obtained with `map()` / `filter()` and list comprehensions. Set comprehension and dictionary comprehension is shown below:

```python
s = {x for x in range(15) if x%2 == 0}
print (s)
{0, 2, 4, 6, 8, 10, 12, 14}
```

```python
d = {n: n**3 for n in range(4)}
print (d)
{0: 0, 1: 1, 2: 8, 3: 27}
```
---

### Complete the following problems by editing the files below:

### Q5. Datetime
Use Python to compute days between start and stop date.   
a.  

```
date_start = '01-02-2013'    
date_stop = '07-28-2015'
```

>> 937

b.  
```
date_start = '12312013'  
date_stop = '05282015'  
```

>> 513

c.  
```
date_start = '15-Jan-1994'      
date_stop = '14-Jul-2015'  
```

>> 7850

Place code in this file: [q5_datetime.py](python/q5_datetime.py)

---

### Q6. Strings
Edit the 7 functions in [q6_strings.py](python/q6_strings.py)

---

### Q7. Lists
Edit the 5 functions in [q7_lists.py](python/q7_lists.py)

---

### Q8. Parsing
Write a script as indicated (using the football data) in [q8_parsing.py](python/q8_parsing.py)





