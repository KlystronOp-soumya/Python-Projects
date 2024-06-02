>>> from collections import Counter
>>> c= Counter(cats=4 , dog = 2)
>>> c
Counter({'cats': 4, 'dog': 2})
>>> c.elements()
<itertools.chain object at 0x01828118>
>>> sorted(c)
>>> from collections import Counter
>>> li1 = [(1,2) , (3,4) , (5,6)]
>>> c = Counter(li1)
>>> c
Counter({(1, 2): 1, (3, 4): 1, (5, 6): 1})
>>> li1 = [(1,2) , (3,4) , (5,6) , (5,6)]
>>> c = Counter(li1)
>>> c
Counter({(5, 6): 2, (1, 2): 1, (3, 4): 1})
>>> c.elements()
<itertools.chain object at 0x016B8178>
>>> c.items()
dict_items([((1, 2), 1), ((3, 4), 1), ((5, 6), 2)])
>>> li2=[1,2,3,4,1,2,3,4,5,5,5,5,5,]
>>> c1=Counter(li2)
>>> c1.items()
dict_items([(1, 2), (2, 2), (3, 2), (4, 2), (5, 5)])
>>> c1
Counter({5: 5, 1: 2, 2: 2, 3: 2, 4: 2})
>>> s = "aabbbcjjd"
>>> c2 = Counter(s)
>>> c2
Counter({'b': 3, 'a': 2, 'j': 2, 'c': 1, 'd': 1})
>>> c.most_common(3) 
[((5, 6), 2), ((1, 2), 1), ((3, 4), 1)]
>>> c2.most_common(3) 
[('b', 3), ('a', 2), ('j', 2)]
>>> c2.most_common(1) 
[('b', 3)]
>>> c2.total()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'Counter' object has no attribute 'total'
>>> list(c2)
['a', 'b', 'c', 'j', 'd']
>>> set(c2)
{'d', 'b', 'a', 'j', 'c'}
>>> dict(c)
{(1, 2): 1, (3, 4): 1, (5, 6): 2}
>>> dict(c2) 
{'a': 2, 'b': 3, 'c': 1, 'j': 2, 'd': 1}
>>> c3 = Counter(a=3 , b=2)
>>> c3
Counter({'a': 3, 'b': 2})
>>> c.elements()
<itertools.chain object at 0x016B8268>
>>> sorted(c3.elements())
['a', 'a', 'a', 'b', 'b']
>>> d3 =Counter(a = 1 , b= 3)  
>>> sorted(d3.elements())
['a', 'b', 'b', 'b']
>>> c3+d3
Counter({'b': 5, 'a': 4})
>>> c3-d3 
Counter({'a': 2})
>>> c3|d3 
Counter({'a': 3, 'b': 3})
>>> c3&d3 
Counter({'b': 2, 'a': 1})
>>> c3==d3
False
>>> c3<=d3
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: '<=' not supported between instances of 'Counter' and 'Counter'
>>> c3 <= d3 
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: '<=' not supported between instances of 'Counter' and 'Counter'
>>> d4 =Counter(a = 0 , b= 3 , c = 2) 
>>> +d4
Counter({'b': 3, 'c': 2})
>>> -d4
Counter()
