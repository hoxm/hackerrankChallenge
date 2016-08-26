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


## [Capitalize](https://www.hackerrank.com/challenges/capitalize)

[示例](https://github.com/hoxm/hackerrankChallenge/blob/master/python3/capitalize.py)

"1 w r 3g" 这种case 不能用string.title()
'Long string with     multi white spaces' 这种case也不能以word为单位调用string.capitalize()
所以最后只能用笨办法， 暂时不知道有没有更优雅的方式



## [Capitalize](https://www.hackerrank.com/challenges/the-minion-game)

[示例](https://github.com/hoxm/hackerrankChallenge/blob/master/python3/the_minion_game.py)

最开始的时候被题目误导，首先等到所有子字符串，然后去掉重复: list(set(l))
然后再开始统计重复，一次判断累加分数到哪边。
当规模达到上限1000000时， 内存直接爆掉。生成字串时候直接判断，去掉没有必要的内存消耗，
甚至发现子串也没有必要生成，但是时间还是太长。只能仔细思考规律，才得出示例版本。


## [The captain's Room](https://www.hackerrank.com/challenges/the-captains-room)

[示例](https://github.com/hoxm/hackerrankChallenge/blob/master/python3/the_captains_room.py)

第一次提交代码没有通过， 因为超时， 所以还等想一下不是那么直截了当的方法实现。


## [Find Angle MBC](https://www.hackerrank.com/challenges/find-angle)

[示例](https://github.com/hoxm/hackerrankChallenge/blob/master/python3/find_angle.py)

这是一个特列， 要求不能用python3, 注意‘a/b’ 要转为float才能得到float结果。
用到数学知识： atan，以及MBC是个等边三角形， BC中点是N的话， MNB也是直角三角形。
所以tan MBC == tan ACB == AB/BC  atan 即可得到角度。

