#!/usr/bin/python
# -*- coding: UTF-8 -*-
def scanError():
    if error != False:
        if error == True:
            print "有错误发生。"
        else:
            print "程序未正常运行。"
settings_double = "double"
result = 0
addnum = 0
error = 0
print "请输入你要进行的计算"
print "[符号] +, -, *, / 四则运算"
print "[1] 质数与合数"
print "[2] 偶数与奇数"
print "[3] 范围整数输出"
print "[4] 范围指定类型数字输出"
print "[5] 设定"
print "[help] 查看用法"
print "[exit] 直接退出"
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
        print "[3] 范围整数输出"
        print "[4] 范围指定数字类型输出"
        print "[5] 设定"
        print "[exit] 直接退出"

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
        print "请选择要输出的数字类型"
        print "[1] 质数"
        print "[2] 合数"
        print "[3] X 的倍数"
        print "[4] 每隔 X 个数字获取一个数字"
        print "[5] 偶数"
        print "[6] 奇数"
        selection = raw_input("Enter:")
        if (selection == "1"):
            print "请输入范围最小值"
            range_m = int(input("Enter the minimum range>"))
            print "请输入范围最大值"
            range_x = int(input("Enter the maximum range>"))
            if range_m == 1:
                print "1 不能作为范围起点。"
                error = True
            elif range_x == 1:
                print "1 不能作为范围终点。"
                error = True
            if range_x < range_m:
                print "最大范围不可小于最小范围。"
            else:
                last_num = 0
                time = 0
                for num in range(range_m, range_x):
                    for i in range(2, num):
                        if num % i == 0:
                            break
                        else:
                            if num == last_num:
                                continue
                            print num
                            last_num = num
                            time += 1
                print "已列出 ", range_m, " ~ ", range_x, " 之间的所有质数。"
                print "共计 ", time, " 个。"
                scanError()
        
        elif (selection == "2"):
            print "请输入范围最小值"
            range_m = int(input("Enter the minimum range>"))
            print "请输入范围最大值"
            range_x = int(input("Enter the maximum range>"))
            if range_x < range_m:
                print "最大范围不可小于最小范围。"
            else:
                temp = 1
                last_num = 0
                time = 0
                for num in range(range_m, range_x):
                    for i in range(2, num):
                        if num % i == 0:
                            if num == last_num:
                                continue
                            if range_m <= 2:
                                if temp == 1:
                                    temp = 2
                                    print "2"
                            print num
                            last_num = num
                            time += 1
                        else:
                            break
                print "已列出 ", range_m, " ~ ", range_x, " 之间的所有合数。"
                print "共计 ", time, " 个。"
                scanError()
        elif (selection == "3"):
            print "是哪一个数字的倍数？"
            fromint =  int(input("Enter an int>"))
            print "这个数字的倍数到多少为止？"
            toint = int(input("Enter an int>"))
            if toint < fromint:
                print "终点不能比起点小"
            else:
                    if settings_double == "double":
                        double = 1
                        while True:
                            if fromint * double > toint:
                                break
                            fromint *= double
                            print "倍: ", double, "，值: ", fromint, " 。"
                            double += 1
                    else:
                        times = 1
                        while True:
                            if fromint * double_var > toint:
                                break
                            fromint *= double_var
                            print "倍: ", times, "，值:", fromint, " 。"
                            times += 1

        elif (selection == "4"):
            print "从哪个数开始？"
            fromint = int(input("Enter an int>"))
            print "每隔多少个数字获取一个数字？"
            x = int(input("Enter an int>"))
            print "从哪个数结束？"
            endint = int(input("Enter an int>"))
            if endint < fromint:
                print "终点不能小于起点。"
            elif fromint + x > endint:
                print "指定的数字太小了。"
            else:
                temp = 1
                while endint > fromint:
                    if temp == 1:
                        print fromint
                        temp = 0
                    else:
                        fromint = fromint + x + 1
                        print fromint
        elif (selection == "5"):
            print "从哪个数开始？"
            fromint = int(input("Enter an int>"))
            print "从哪个数结束？"
            endint = int(input("Enter an int>"))
            if endint < fromint:
                print "终点不能小于起点。"
            elif fromint + 2 > endint:
                print "指定的数字太小了。"
            else:
                while endint > fromint:
                    if fromint % 2 == 0:
                        print fromint
                        fromint += 1
                    else:
                        fromint += 1
        elif (selection == "6"):
            print "从哪个数开始？"
            fromint = int(input("Enter an int>"))
            print "从哪个数结束？"
            endint = int(input("Enter an int>"))
            if endint < fromint:
                print "终点不能小于起点。"
            elif fromint + 3 > endint:
                print "指定的数字太小了。"
            else:
                while endint > fromint:
                    if fromint % 2 != 0:
                        print fromint
                        fromint += 1
                    else:
                        fromint += 1


    if (choice == "5"):
        print "设定"
        print "[1] 自定义数字倍数"
        print "[2] Comming Soon..."
        scansee = raw_input("Enter:")
        if scansee == "1":
            print "设定数字倍数"
            print "输入 double 可设定倍增"
            print "输入 x2 可设定双倍"
            print "输入 x3 可设定三倍"
            print "输入 custom() 可自定义倍数"
            print "输入 preview() 可预览当前倍数"
            scanin = raw_input("Enter")
            if scanin == "double":
                settings_double = "double"
                print "已设置为倍增。"
            elif scanin == "x2":
                settings_double = "2"
                double_var = 2
                print "已设置为双倍。"
            elif scanin == "x3":
                settings_double = "3"
                double_var = 3
                print "已设置为三倍。"
            elif scanin == "custom()":
                double_var = int(input("Enter an int>"))
                print "已设置为 ", double_var, " 倍。" 
            elif scanin == "preview()":
                if settings_double == "double":
                    print "倍: 1，值: 8"
                    print "倍: 2, 值: 16"
                    print "倍: 3, 值: 42"
                    print "42 =  8 * 1 * 2 * 3"
                elif settings_double == "2":
                    print "倍: 1, 值: 16"
                    print "倍: 2, 值: 32"
                    print "倍: 3, 值: 64"
                    print "64 = 8 * 2 * 2 * 2"
                elif settings_double == "3":
                    print "倍: 1, 值 24"
                    print "倍: 2, 值 72"
                    print "倍: 3, 值 216"
                    print "216 = 8 * 3 * 3 * 3"
                else:
                    print "倍: 1, 值 ", 8 * double_var
                    print "倍: 2, 值 ", 8 * double_var * double_var
                    print "倍: 3, 值 ", 8 * double_var * double_var * double_var
                    print double_var * double_var * double_var, " = 8 * ", double_var, " * ", double_var, " * ", double_var



    if (choice == "exit"):
        print "操作被用户终止"
        exit()