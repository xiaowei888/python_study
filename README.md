# python_study
test_adb_1.py
在GMS白名单申请时需要对系统属性做相关检测，规则如下：
For 9
ro.product.vendor.model = ro.product.model 
ro.product.vendor.device= ro.product.device
ro.vendor.build.fingerprint= ro.build.fingerprint
ro.product.vendor.name= ro.product.name=ro.build.product
ro.product.vendor.manufacturer=ro.product.manufacturer
ro.product.vendor.brand=ro.product.brand
ro.build.version.incremental >> need to match to fingerprint
ro.com.google.gmsversion不可过期