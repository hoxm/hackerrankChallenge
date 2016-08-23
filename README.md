# Introduction

This repository is to save the source code when resolve the challenges in hackerrank website.
Of course this readme file also records the error/issues I have ever meant.

Each source code folder is named according to the challenge domain name, and maybe also the
language version I selected. For example, python3 is for python domain based on python3.x.


# [30 Days of code](https://www.hackerrank.com/domains/tutorials/30-days-of-code)

## [Loops](https://www.hackerrank.com/challenges/30-loops)

Python 2 中range() 被删除了， xrange() 被重命名为python3 中的 range()


## [Arrays](https://www.hackerrank.com/challenges/30-arrays)

python 还是很优雅的

Print the elements of array in reverse order as a single line of space-separated numbers.
print(' '.join(['%d' % i for i in a[-1::-1]]))


## [Dictionaries and Maps](https://www.hackerrank.com/challenges/30-dictionaries-and-maps)

字典get()方法第二个参数应该是位置参数，不是键值参数， 虽然有些文档提到get(key, default=<default>)


# [Python](https://www.hackerrank.com/domains/python)

I choice python3 in this domain, just want to improve my understanding about the changes
from python version 2.x to 3.x. My local test version is python3.5. All files are run
like this "python3 filename" by default if there is no special notification.


## [Say "Hello, World!" With Python](https://www.hackerrank.com/challenges/py-hello-world)

[示例](https://github.com/hoxm/hackerrankChallenge/blob/master/python3/helloworld.py)

没有什么好说的， 直接复制题目说明中地例子即可， 如果你不屑于这么做， 注意字符串大小写和空格之类的。

## [Reading Raw Input](https://www.hackerrank.com/challenges/python-raw-input)

[示例](https://github.com/hoxm/hackerrankChallenge/blob/master/python3/reading_raw_input.py)

Python3 之后去掉了raw_input(),  现在只有input 函数了， 返回值始终是string

    >>> i = input("int: ")
    int: 4
    >>> type(i)
        <class 'str'>

需要注意， 本题要求stdout只能有输入的内容， 所以input函数不能有prompt。


## [Python If-Else](https://www.hackerrank.com/challenges/py-if-else)

[示例](https://github.com/hoxm/hackerrankChallenge/blob/master/python3/py_if_else.py)

这个没有什么好说地， if-elif-else 没有什么改变。


## [Arithmetic Operators](https://www.hackerrank.com/challenges/python-arithmetic-operators)

[示例](https://github.com/hoxm/hackerrankChallenge/blob/master/python3/arithmetic_operators.py)

最简单的办法是三行print， 示例中把运算法则做成参数列表， 可以灵活添加。更加高级黑魔法有待研究。


## [Nested Lists](https://www.hackerrank.com/challenges/nested-list)

[示例](https://github.com/hoxm/hackerrankChallenge/blob/master/python3/nested_lists.py)

使用列表的排序和序列化操作，可以思考还有没有更优化的做法。


## [Find s string](https://www.hackerrank.com/challenges/find-a-string)


[示例](https://github.com/hoxm/hackerrankChallenge/blob/master/python3/find_a_string.py)

注意cdcdc 这种算是match两遍， 所以简单地findall不好用。


## [Alphabet Rangoli](https://www.hackerrank.com/challenges/alphabet-rangoli)


[示例](https://github.com/hoxm/hackerrankChallenge/blob/master/python3/alphabet_rangoli.py)

