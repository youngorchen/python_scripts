# encoding: utf-8
#from django import forms
#import re

__author__ = 'william'

"""Module documentation goes here
"""

# http://nzago.kiwifield.com/Home/Detail/98164
#
# curl -A "mozilla/5.0 (iphone; cpu iphone os 5_1_1 like mac os x) applewebkit/534.46 (khtml, like gecko) mobile/9b206 micromessenger/5.0" -I -m 10 -o /dev/null -s -w %{http_code} http://nzago.kiwifield.com/Home/Detail/98164
#
# curl -A "mozilla/5.0 (iphone; cpu iphone os 5_1_1 like mac os x) applewebkit/534.46 (khtml, like gecko) mobile/9b206 micromessenger/5.0"  -H "Accept: */*" -H "Accept-Encoding: gzip, deflate, br" -H "Accept-Language: zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2" -H "Cache-Control: no-cache" -H "Connection: keep-alive" -H "Content-Type: application/x-www-form-urlencoded; charset=UTF-8" -H "Cookie: ASP.NET_SessionId=lfsu3hxylvvsnkj5rr5dudqz; Enring_MC_Token__g=00f2B35/8tY=; Enring_MC_Token__c=tTDKdDokUj8xuo0Fdrv+W+kpGhjyGEJe; Enring_MC_Token__p=4icFRBWm4K34Kbk1zz48ZZdpuio3908L; __asc=d92294b1162607d563a2042ec6c; __auc=d92294b1162607d563a2042ec6c; _ga=GA1.2.374224087.1522037250; _gid=GA1.2.488787050.1522037250; Enring_MC_Token__lq=H7hUguwHPIQo4I6wVfA/200t22La1RMm" -H "DNT: 1" -H "Host: mp.kiwifield.com" -H "Pragma: no-cache" -H "Referer: https://mp.kiwifield.com/Dashboard/ContentManager?token=8774bda68afded6cc1b89bc29c21d8cf" -H "X-Requested-With: XMLHttpRequest" https://mp.kiwifield.com/Dashboard/ContentAJAX
#
# curl -A "mozilla/5.0 (iphone; cpu iphone os 5_1_1 like mac os x) applewebkit/534.46 (khtml, like gecko) mobile/9b206 micromessenger/5.0"  -H "Host: mp.kiwifield.com" -H "User-Agent: Mozilla/5.0 (Windows NT 10.0; WOW64; rv:59.0) Gecko/20100101 Firefox/59.0" -H "Accept: */*" -H "Accept-Language: zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2" -H "Accept-Encoding: gzip, deflate, br" -H "Referer: https://mp.kiwifield.com/Dashboard/ContentManager?token=8774bda68afded6cc1b89bc29c21d8cf" -H "Content-Type: application/x-www-form-urlencoded; charset=UTF-8" -H "X-Requested-With: XMLHttpRequest" -H "Cookie: ASP.NET_SessionId=lfsu3hxylvvsnkj5rr5dudqz; Enring_MC_Token__g=00f2B35/8tY=; Enring_MC_Token__c=tTDKdDokUj8xuo0Fdrv+W+kpGhjyGEJe; Enring_MC_Token__p=4icFRBWm4K34Kbk1zz48ZZdpuio3908L; __asc=d92294b1162607d563a2042ec6c; __auc=d92294b1162607d563a2042ec6c; _ga=GA1.2.374224087.1522037250; _gid=GA1.2.488787050.1522037250; Enring_MC_Token__lq=H7hUguwHPIQo4I6wVfA/200t22La1RMm" -H "DNT: 1" -H "Connection: keep-alive" -H "Pragma: no-cache" -H "Cache-Control: no-cache" -X POST -d "token=8774bda68afded6cc1b89bc29c21d8cf&categoryid=4660&toplevel=0&comment=10000&search&sku&pageindex=13" https://mp.kiwifield.com/Dashboard/ContentAJAX
#
# 0 -- >max = 44
#
# src=".*? data-original=
# src
#

str0 = "curl -A \"mozilla/5.0 (iphone; cpu iphone os 5_1_1 like mac os x) applewebkit/534.46 (khtml, like gecko) mobile/9b206 micromessenger/5.0\"  -H \"Host: mp.kiwifield.com\" -H \"User-Agent: Mozilla/5.0 (Windows NT 10.0; WOW64; rv:59.0) Gecko/20100101 Firefox/59.0\" -H \"Accept: */*\" -H \"Accept-Language: zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2\" -H \"Accept-Encoding: gzip, deflate, br\" -H \"Referer: https://mp.kiwifield.com/Dashboard/ContentManager?token=8774bda68afded6cc1b89bc29c21d8cf\" -H \"Content-Type: application/x-www-form-urlencoded; charset=UTF-8\" -H \"X-Requested-With: XMLHttpRequest\" -H \"Cookie: ASP.NET_SessionId=lfsu3hxylvvsnkj5rr5dudqz; Enring_MC_Token__g=00f2B35/8tY=; Enring_MC_Token__c=tTDKdDokUj8xuo0Fdrv+W+kpGhjyGEJe; Enring_MC_Token__p=4icFRBWm4K34Kbk1zz48ZZdpuio3908L; __asc=d92294b1162607d563a2042ec6c; __auc=d92294b1162607d563a2042ec6c; _ga=GA1.2.374224087.1522037250; _gid=GA1.2.488787050.1522037250; Enring_MC_Token__lq=H7hUguwHPIQo4I6wVfA/200t22La1RMm\" -H \"DNT: 1\" -H \"Connection: keep-alive\" -H \"Pragma: no-cache\" -H \"Cache-Control: no-cache\" -X POST -d \"token=8774bda68afded6cc1b89bc29c21d8cf&categoryid=4660&toplevel=0&comment=10000&search&sku&pageindex=PNPN\" --retry 10 --retry-delay 100  --retry-max-time 100 https://mp.kiwifield.com/Dashboard/ContentAJAX > aPNPN.html"
for i in range(44):
    str1 = str0.replace("PNPN",str(i))
    print(str1)

