import math,os,random,re,sys

# for multiplier in (lambda x : i * x for i in range(5)):
#     print(multiplier(2))
#
# class Stack:
#     def __init__(self):
#         self.contains = []
#
#     def is_empty(self):
#         return self.contains == []
#
#     def pop(self):
#         return self.contains.pop()
#
#     def peek(self):
#         return self.contains[len(self.contains)-1]
#
#     def push(self, item):
#         self.contains.append(item)
#
#     def size(self):
#         return len(self.contains)
#
# def infix_to_postfix(infixexpr):
# #首先用一个dict来设定各个运算符的优先级
#     prec = {}
#     prec["*"] = 3
#     prec["/"] = 3
#     prec["+"] = 2
#     prec["-"] = 2
#     prec["("] = 1
#
# #step one 创建一个新的stack和一个空的list
#     opStack = Stack()
#     postfixList = []
#
# #运用split方法将输入的string 转化为list
#     tokenList = infixexpr.split()
#
#     for token in tokenList:
#         if token in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" or token in "0123456789":                                #检查是运算元还是运算符
#             postfixList.append(token)
#         elif token == '(':
#             opStack.push(token)
#         elif token == ')':
#             topToken = opStack.pop()
#             while topToken != '(':
#                 #这里不需要判断优先级，因为只会有一个运算符
#                 postfixList.append(topToken)
#                 topToken = opStack.pop()
#         else:
#             while (not opStack.is_empty()) and \
#                (prec[opStack.peek()] >= prec[token]):
#                   postfixList.append(opStack.pop())
#             opStack.push(token)
#
# #最后将stack清空
#     while not opStack.is_empty():
#         postfixList.append(opStack.pop())
#     return " ".join(postfixList)
#
# print(infix_to_postfix("A + B * C"))
#
# side1=float(input("the first side of triangle:"))
# side2=float(input("the second side of triangle:"))
# side3=float(input("the thrid side of triangle:"))
#
# if(side1+side2>side3)and(side2+side3>side1)and(side3+side1>side2):
#     print (side1,side2,side3,"is sides of triangle")
# else:
#
#     print (side1,side2,side3,"is not sides of triangle")'


# Complete the if_sum_n_distinct_fib function below.
def if_sum_n_distinct_fib(x, n):
    global max_i
    if x == 1 and n > 1:
        return False

    fib = [1, 1, 2]
    while len(fib) <= 40:
        fib.append(fib[-1] + fib[-2])
    for i in range(len(fib)):
        if fib[i] < x and fib[i+1] >= x:
            max_i = i
    if n == 1:
        if x == 1:
            return True
        elif (fib[a] == x for a in range(max_i)):
            return True
        return False




    if n == 3:
        for i,j,k in range(1,max_i):
            if i != j and j != k and fib[i] + fib[j] + fib[k] == x:
                return True
        return False

    return False

print(if_sum_n_distinct_fib(5,3))






#
# def get_count(n):
#     str_n = str(n)
#     return str_n
#
#
# print(get_count(19))

def solve(n):
    count = 1
    for num in range(n):
        i = 0
        haha = num
        while i < 1000:
            i += 1
            haha = square_summation(haha)
            if haha == 1:
                count += 1
                break
    return count


def square_summation(num):
    result = 0
    while num > 0:
        result += (num % 10) ** 2
        num = int(num / 10)
    return result

# print(solve(100))