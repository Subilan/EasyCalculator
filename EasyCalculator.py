#!/usr/bin/python
# -*- coding: UTF-8 -*-
result = 0
addnum = 0
print "请输入你要进行的计算"
print "[符号] +, -, *, / 四则运算"
print "[1] 质数与合数"
print "[2] 偶数与奇数"
print "[3] 范围数字输出"
print "[4] 直接退出"
print "[help] 查看用法"
while True:
    choice = raw_input("Enter: ")

    if (choice == "+"):
        while True:
            print "请依次输入加数, 输入 0 结束输入"
            addnum = int(input("Enter an int>"))
            if addnum == 0:
                print "结果为: ", result
                break
            else:
                result += addnum

    if (choice == "-"):
        temp = 1
        print "请输入被减数"
        dim = int(input("Enter an int>"))
        while True:
            print "请依次输入减数，输入 0 结束输入"
            dimnum = int(input("Enter an int>"))
            if dimnum == 0:
                print "结果为: ", result
                break
            elif temp == 1:
                result = dim - dimnum
                temp += 1
            else:
                result = result - dimnum

    if (choice == "*"):
        temp = 1
        while True:

            print "请依次输入因数，输入 0 结束输入"
            mulnum = int(input("Enter an int>"))
            if mulnum == 0:
                print "结果为: ", result
                break
            elif temp == 1:
                result = mulnum
                temp == 0
            else:
                result = result * mulnum

    if (choice == "/"):
        temp = 1
        print "请输入被除数，带小数点"
        dis = float(input("Enter a float>"))
        while True:
            print "请依次输入除数，带小数点，输入 0.0 结束输入"
            disnum = float(input("Enter a float>"))
            if disnum == 0.0:
                if result == 0:
                    print "错误的值: 缺少必要操作数。"
                    temp = 1
                else:
                    print "结果为: ", result
                    break
            elif temp == 1:
                result = dis / disnum
                temp == 0
            else:
                result = result / disnum

    if (choice == "help"):
        print "请输入你要进行的计算"
        print "[符号] +, -, *, / 四则运算"
        print "[1] 质数与合数"
        print "[2] 偶数与奇数"
        print "[3] 范围数字输出"
        print "[4] 直接退出"

    if (choice == "1"):
        print "输入一个整数来判断是否为质数或合数"
        judgementNumber = int(input("Enter an int>"))
        i = 2
        if judgementNumber >= 2:
            while i < judgementNumber:
                if judgementNumber % i == 0:
                    print judgementNumber, " 是合数。"
                    print "相当于 ", i, " * ", judgementNumber//i
                    break
                else:
                    i += 1
            else:
                print judgementNumber, " 是质数。"
        elif judgementNumber == 1:
            print "1 既不是质数也不是合数"
        else:
            print judgementNumber, " 不是质数。"
    
    if (choice == "2"):
        print "输入一个自然数来判断是否为偶数或奇数"
        judgementNumber = int(input("Enter an natural number>"))
        if judgementNumber >= 0:
            if judgementNumber == 0:
                print "0 是偶数"
            elif judgementNumber % 2 == 0:
                print judgementNumber, " 是偶数。"
                print "是 2 的 ", judgementNumber//2, " 倍。"
            else:
                print judgementNumber, " 是奇数。"
        else:
            print "请输入自然数。"

    if (choice == "3"):
        print "输入一个范围最小值"
        range_m = int(input("Enter the minimum range>"))
        print "输入一个范围最大值"
        range_x = int(input("Enter the maximum range>"))
        if range_x < range_m:
            print "最大范围不可小于最小范围。"
        elif range_m == range_x:
            print "范围内数字有 1 个"
            print range_m
        else:
            temp = range_m
            count = 0
            while temp <= range_x:
                print temp
                temp += 1
                count += 1
            else:
                print "范围内数字一共有 ", count, " 个。"

    if (choice == "4"):
        print "操作被用户终止"
        exit()
    
    if (choice == "exit"):
        print "操作被用户终止"
        exit()