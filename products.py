#读取档案
products = []
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

#让使用者输入
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

