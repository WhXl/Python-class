'''
numpy.argmax(a, axis=None, out=None)
返回沿轴axis最大值的索引
argmax返回的是最大数的索引.argmax有一个参数axis,默认是0,表示第几维的最大值.看二维的情况
'''
#一维
import numpy as np
a = np.array([3, 1, 2, 4, 6, 1])
print(np.argmax(a))
'''
为了描述方便,a就表示这个二维数组.np.argmax(a, axis=0)的含义是a[0][j],a[1][j],a[2][j](j=0,1,2,3)
中最大值的索引.从a[0][j]开始,最大值索引最初为(0,0,0,0),拿a[0][j]和a[1][j]作比较,9大于1,6大于5,8大于2,
所以最大值索引由(0,0,0,0)更新为(1,1,0,1),再和a[1][j]作比较,7大于6,9大于5所以更新为(1,2,2,1).再分析下面的输出
'''
import numpy as np
a = np.array([[1, 5, 5, 2],
              [9, 6, 2, 8],
              [3, 7, 9, 1]])
print(np.argmax(a, axis=0))

'''
np.argmax(a, axis=1)的含义是a[i][0],a[i][1],a[i][2],a[i][3](i=0,1,2)中最大值的索引.
从a[i][0]开始,a[i][0]对应的索引为(0,0,0),先假定它就是最大值索引(思路和上节简单例子完全一致)
拿a[i][0]和a[i][1]作比较,5大于1,7大于3所以最大值索引由(0,0,0)更新为(1,0,1),再和a[i][2]作
比较,9大于7,更新为(1,0,2),再和a[i][3]作比较,不用更新,最终值为(1,0,2)
'''
import numpy as np
a = np.array([[1, 5, 5, 2],
              [9, 6, 2, 10],
              [3, 7, 9, 1]])
print(np.argmax(a, axis=1))

'''
np.argmax(a, axis=0)的含义是a[0][j][k],a[1][j][k] (j=0,1,2,k=0,1,2,3)中最大值的索引.
从a[0][j][k]开始,a[0][j][k]对应的索引为((0,0,0,0),(0,0,0,0),(0,0,0,0)),拿a[0][j][k]
和a[1][j][k]对应项作比较6大于-6,3大于-3,9大于-9,所以更新这几个位置的索引,
将((0,0,0,0),(0,0,0,0),(0,0,0,0))更新为((0,0,0,0),(0,1,0,0),(1,0,1,0)). 再看axis=1的情况.
'''
import numpy as np

a = np.array([
    [
        [1, 5, 5, 2],
        [9, -6, 2, 8],
        [-3, 7, -9, 1]
    ],

    [
        [-1, 5, -5, 2],
        [9, 6, 2, 8],
        [3, 7, 9, 1]
    ]
])
print(np.argmax(a, axis=1))
'''
np.argmax(a, axis=1)的含义是a[i][0][k],a[i][1][k] (i=0,1,k=0,1,2,3)中最大值的索引.
从a[i][0][k]开始,a[i][0][k]对应的索引为((0,0,0,0),(0,0,0,0)),拿a[i][0][k]和a[i][1][k]
对应项作比较,9大于1,8大于2,9大于-1,6大于5,2大于-5,8大于2,所以更新这几个位置的索引,
将((0,0,0,0),(0,0,0,0))更新为((1,0,0,1),(1,1,1,1)),现在最大值对应的数组为((9,5,5,8),(9,6,2,8)).
再拿((9,5,5,8),(9,6,2,8))和a[i][2][k]对应项从比较,7大于5,7大于6,9大于2.更新这几个位置的索引.
将((1,0,0,1),(1,1,1,1))更新为((1,2,0,1),(1,2,2,1)).axis=2的情况也是类似的.

'''
i = 12 % 1
print(i)
list = np.zeros((52,52,85))
print(len(list[]))
