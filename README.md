# Introduction

This repository is to save the source code when resolve the challenges in hackerrank website.
Of course this readme file also records the error/issues I have ever meant.

Each source code folder is named according to the challenge domain name, and maybe also the
language version I selected. For example, python3 is for python domain based on python3.x.


# Python

https://www.hackerrank.com/domains/python

I choice python3 in this domain, just want to improve my understanding about the changes
from python version 2.x to 3.x. My local test version is python3.5. All files are run
like this "python3 filename" by default if there is no special notification.


## Say "Hello, World!" With Python

没有什么好说的， 直接复制题目说明中地例子即可， 如果你不屑于这么做， 注意字符串大小写和空格之类的。

## Reading Raw Input

Python3 之后去掉了raw_input(),  现在只有input 函数了， 返回值始终是string

    >>> i = input("int: ")
    int: 4
    >>> type(i)
        <class 'str'>

需要注意， 本题要求stdout只能有输入的内容， 所以input函数不能有prompt。
