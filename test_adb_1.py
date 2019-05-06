#coding:utf-8
import os

p1=os.popen("adb devices").read()
print (p1)

cmd="adb shell getprop "
prop1="ro.product.vendor.model"
args = ("ro.product.vendor.model","ro.product.model",
        "ro.product.vendor.device", "ro.product.device",
        "ro.product.vendor.manufacturer","ro.product.manufacturer",
        "ro.product.vendor.brand","ro.product.brand",
        "ro.vendor.build.fingerprint", "ro.build.fingerprint",
        "ro.product.vendor.name","ro.product.name","ro.build.product",
        "ro.build.version.incremental","ro.com.google.gmsversion",
        )
count = 0
result={}
while(count < len(args)):
    pi = os.popen(cmd+args[count]).read()
    print(args[count] + " = " + pi)
    result[args[count]] = pi
    count = count+1

count2=0
while(count2<10):    
    if(result[args[count2]] == result[args[count2+1]]):
        print(args[count2],"==",args[count2+1],"==",result[args[count2]])
    else:
        print(args[count2],"!=",args[count2+1],"!=",result[args[count2]],result[args[count2+1]])
    count2 = count2 + 2    
            
if(result[args[11]] == result[args[12]] == result[args[10]]):
    print(args[11],"==",args[12],"==",args[10],"==",result[args[0]])
else:
    print(args[11],"!=",args[12],"!=",args[10])
    print(result[args[11]],result[args[12]],result[args[10]])
    
if result["ro.build.version.incremental"].strip() in result["ro.build.fingerprint"].strip():
    print("ro.build.version.incremental match ro.build.fingerprint")
else:
    print("ro.build.version.incremental is not match ro.build.fingerprint")
    


