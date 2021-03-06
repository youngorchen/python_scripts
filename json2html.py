# encoding: utf-8
#from django import forms
#import re
import json,re,os,time

__author__ = 'william'


#file_name = 'p_b93643.html'
#file_name = 'p_b93787.html'
#file_name = 'p_b102380.html'

def proc(path,file_name):
    with open(path+file_name + '.json', 'r', encoding='utf-8') as f:
        data = json.load(f)

    with open(path+'/out_' + file_name, 'w', encoding='utf-8') as f:
        f.writelines('<html><head><meta charset="utf-8">')
        f.writelines('<p><b>商品名称：' + data['title'] + '</b></p>')
        f.writelines('<p>类别：' + data['leibie'] + '</p>')
        f.writelines('<p>价格：' + data['price'] + '</p>')
        f.writelines('<p>图片：'  + '</p>')
        for i in range(1,11):
            #print(i)
            #print(data)
            if data['images'] != [] and data['images'][0]['img'+str(i)] != '':
                f.writelines('<img style="border:5px solid red;margin:20px;" width = "200px" src="' + data['images'][0]['img'+str(i)] + '" </img>')
        f.writelines('<p>说明：' + data['desc'] + '</p>')
        f.writelines('<p>   ' + data['detail1'] + '</p>')
        if data['detail2'] != []:
            for i in range(1, 11):
                if data['detail2'][0]['img'+str(i)] != '':
                    f.writelines('<img style="border:5px solid red;margin:20px;"  width = "200px" src="' + data['detail2'][0]['img'+str(i)] + '" </img>')

        f.writelines('</html>')


def proc1(path,file_name):
    with open(path+file_name + '.json', 'r', encoding='utf-8') as f:
        data = json.load(f)

    with open(path + '/all.txt', 'a+', encoding='utf-8') as f:
        #f.writelines('文件名,商品名称,类别,价格,图片,说明,细节文字,细节图片\n')
        f.write('out_' + file_name + ',')
        f.write(data['title'].replace(',','，') + ',')
        f.write(data['leibie'].replace(',','，') + ',')
        f.write(data['price'] + ',')

        for i in range(1,11):
            #print(i)
            #print(data)
            if data['images'] != [] and data['images'][0]['img'+str(i)] != '':
                f.write(data['images'][0]['img'+str(i)] + ';')
        f.write(',')
        f.write(data['desc'].replace('\n','').replace(',','，') + ',')
        f.write(data['detail1'].replace('\n','').replace(',','，') + ',')
        if data['detail2'] != []:
            for i in range(1, 11):
                if data['detail2'][0]['img'+str(i)] != '':
                    f.write(data['detail2'][0]['img'+str(i)] + ';')

        f.writelines('\n')

path = 'C:/Users/williamchen/PycharmProjects/untitled/product/'

with open(path + '/all.txt', 'w', encoding='utf-8') as f:
    f.writelines('文件名,商品名称,类别,价格,图片,说明,细节文字,细节图片\n')

for name in os.listdir(path):
    if os.path.isfile(path+name):
        #print(name)
        if re.match("p_b\d+.html$",name):
            n = "cd product & ruby ../builder.rb ../html_strip.rb " + name + "> null "
            print(n)
            os.system(n)
            time.sleep(1)
            #proc(path,name)
            proc1(path, name)
            #exit()