import os #operating system 作业系统 更多权限 相当于电脑的政府
#读取档案
def read_file(filename):
	products = []
	with open(filename,'r') as f:
			for line in f:
				if '商品,价格' in line:
					continue #直接跳到下一次loop
		#		s = line.strip().split(',')
		#		name = s[0]
		#		price = s[1]
				name,price = line.strip().split(',')
				products.append([name,price])
			print(products)
	return products

#def read_file(filename):
	
	
	

#让使用者输入，继续输入购买新的商品
def user_input(products): #products清单原本在函数外边，需放函数内，作为参数
	while True:
		name = input('请输入商品名称：')
		if name =='q':
			break
		price = input('请输入商品价格：')
	#	p = [name,price]
		products.append([name,price])
	print(products)
	return(products)

#印出所有购买记录
def print_products(products): #将外部products传入函数
	for p in products:
		print(p[0],'的价格是:',p[1])

#写入档案
def write_file(filename, products): #传入文档名和products清单
	with open(filename,'w') as f:
		f.write('商品,价格\n')
		for p in products:
			f.write(p[0] + ',' + p[1] + '\n')

def main(): #4个功能放入一个main功能
	filename = 'products.csv'
	if os.path.isfile(filename):#os的path路径下检查档案在不在 bool值 档案名做参数，用传参的方式传入档案
		print('yeah!找到档案了！')
		products = read_file(filename) #读取数据结果存回products
		
	else:
		print('找不到档案....')

	products =  user_input(products) #把增加的商品存入products
	print_products(products) #依次打印出商品及价格
	write_file('products.csv', products)

main()
