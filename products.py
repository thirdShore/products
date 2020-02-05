import os #operating system 作业系统 更多权限 相当于电脑的政府

products = []
if os.path.isfile('products.csv'):#os的path路径下检查档案在不在 bool值
	print('yeah!找到档案了！')
	#读取档案
	with open('products.csv','r') as f:
		for line in f:
			if '商品,价格' in line:
				continue #直接跳到下一次loop
	#		s = line.strip().split(',')
	#		name = s[0]
	#		price = s[1]
			name,price = line.strip().split(',')
			products.append([name,price])
	print(products)
else:
	print('找不到档案....')

#让使用者输入，继续输入购买新的商品
while True:
	name = input('请输入商品名称：')
	if name =='q':
		break
	price = input('请输入商品价格：')
#	p = [name,price]
	products.append([name,price])
print(products)

#印出所有购买记录
for p in products:
	print(p[0],'的价格是:',p[1])

#写入档案
with open('products.csv','w') as f:
	f.write('商品,价格\n')
	for p in products:
		f.write(p[0] + ',' + p[1] + '\n')

