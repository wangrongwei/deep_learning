# --coding:utf-8 --
import tensorflow as tf
import numpy as np

import matplotlib.pyplot as plt

# batch_matrix 代表[batch,channel,h,w] or [batch,h,w,channel]
# model: 0 代表 输入是上边第一种，1代表上边第二种
def batch_exchange(batch_matrix,batchs,channels,height,weight,model):
    if model==0:
        dist = np.zeros((batchs,height,weight,channels))
        for i in range(batchs):
            for (h,w) in range(height,weight):
                dist[i][h][w][0] = batch_matrix[i][0][h][w]
                dist[i][h][w][1] = batch_matrix[i][1][h][w]
                dist[i][h][w][2] = batch_matrix[i][2][h][w]

    else :
        dist = np.zeros((batchs,channels,height,weight))


# 读取单个的batch文件
def unpickle(file):
    import cPickle
    with open('./cifar-10-batches-py/'+file,'rb') as fo:
        dict = cPickle.load(fo)
    return dict


mydata = unpickle('data_batch_1')
X = mydata['data']
label = mydata['labels']
X = np.array(X)
np.set_printoptions(threshold='nan')

new = X.reshape(10000,3,32,32)


# 因为使用imshow将一个矩阵显示为RGB图片，需要
# 将三个32*32的矩阵合成一个32*32*3的三维矩阵

# 下面就是先将这三个矩阵（32*32）转化为1024*1的向量
# 然后使用hstack的功能将每个矩阵上相同位置的值合成
# 一个RGB像素点--->[r,g,b]
# 最后得到 1024*3的矩阵
red   = new[99][0].reshape(1024,1)
green = new[99][1].reshape(1024,1)
blue  = new[99][2].reshape(1024,1)

pic = np.hstack((red,green,blue))

# 打印最开始的32*32的矩阵，
# 因为为RGB图像，所以为有三个32*32的矩阵
print(new[0][0])
print(new[0][1])
print(new[0][2])

# 重新设置pic的形状
pic_rgb = pic.reshape(32,32,3)
# imshow显示的图片格式应该是
# (n,m) or (n,m,3) or (n,m,4)
# 显示最后得到的rgb图片
plt.imshow(pic_rgb)

plt.legend()
plt.show()


