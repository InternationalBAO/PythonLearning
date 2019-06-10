f = float(input('请输入华氏温度: '))
c = (f - 32) / 1.8
#1
print('%.1f华氏度 = %.1f摄氏度' % (f, c))
#2
print('{0}华氏度 = {1}摄氏度'.format(int(f),int(c)))