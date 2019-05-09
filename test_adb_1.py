#coding:utf-8
import os

p1=os.popen("adb devices").read()
print (p1,end="")

cmd="adb shell getprop "
prop1="ro.product.vendor.model"
args = ("ro.product.vendor.model","ro.product.model",
        "ro.product.vendor.device", "ro.product.device",
        "ro.product.vendor.manufacturer","ro.product.manufacturer",
        "ro.product.vendor.brand","ro.product.brand",
        "ro.vendor.build.fingerprint", "ro.build.fingerprint",
        "ro.product.vendor.name","ro.product.name","ro.build.product",
        "ro.build.version.incremental","ro.com.google.gmsversion","ro.com.google.clientidbase"
        )
count = 0
result={}
test_result=[]
while(count < len(args)):
    pi = os.popen(cmd+args[count]).read()
    print(args[count] + " = " + pi,end="")
    result[args[count]] = pi
    count = count+1

print("\033[1;31;0m=========================================================================================================\033[0m")

count2=0
while(count2<10):    
    if(result[args[count2]] == result[args[count2+1]]):
        print(args[count2],"==",args[count2+1],"==",result[args[count2]],end="")
        test_result.append("true");
    else:
        print("\033[1;31;0m",args[count2],"!=",args[count2+1],"!=",result[args[count2]],result[args[count2+1]],"\033[0m",end="")
        test_result.append("false");
    count2 = count2 + 2    
            
if(result[args[11]] == result[args[12]] == result[args[10]]):
    test_result.append("true");
    print(args[11],"==",args[12],"==",args[10],"==",result[args[0]],end="")
else:
    print("\033[1;31;0m",args[11],"!=",args[12],"!=",args[10],"\033[0m","\n",end="")
    test_result.append("false");
    print(result[args[11]].strip(),result[args[12]].strip(),result[args[10]].strip(),"\n")
    
if result["ro.build.version.incremental"].strip() in result["ro.build.fingerprint"].strip():###只有添加strip()去掉字符串中的空格才可准确比较
    print("ro.build.version.incremental match ro.build.fingerprint",end="")
    test_result.append("true");
else:
    print("ro.build.version.incremental is not match ro.build.fingerprint")
    test_result.append("false");

print("\n")
count_test_false_result = test_result.count("false")
if count_test_false_result>0:
    print("测试结果：\033[1;31;0mfailed，你有",count_test_false_result,"项失败")
else:
    print("\033[1;31;0m全部符合标准，测试成功")
    


