from ._global import EPSILON
import math


class Vector:
    def __init__(self, lst):
        # 为了每个对象不受传进来的引用变化导致的问题, 会做一次深拷贝
        # 如果变量是只想做类内的使用的话, 一般前面用单下划线的_
        self._values = list(lst)

    @classmethod
    def zero(cls, dim):
        """返回一个dim维的零向量"""
        return cls([0] * dim)

    def norm(self):
        """"返回向量的模"""
        return math.sqrt(sum(e**2 for e in self))

    def normalize(self):
        """返回向量的单位向量"""
        # 因为计算机计算浮点数时, 经常会有一些误差,
        # 根据这一点, 有时候比较大小的时候, 可以定义一个精度, 小于这个精度, 就认为是0了
        if self.norm() < EPSILON:
            raise ZeroDivisionError('norm is zero')
        return Vector(self._values) / self.norm()

    def __add__(self, another):
        """向量加法, 返回结果向量"""
        # 一般向量的运算, 都是返回一个全新的对象
        assert len(self) == len(another), 'error in adding.Length of vectors must be same.'
        return Vector([a + b] for a, b in zip(self, another))

    def __sub__(self, another):
        # 向量减法, 返回结果向量
        assert len(self) == len(another), 'error in sub.Length of vectors must be same.'
        return Vector([a - b] for a, b in zip(self, another))

    def dot(self, another):
        """"向量点乘, 返回结果标量"""
        assert len(self) == len(another), 'error in dot.Length of vectors must be same.'
        return sum(a * b for a, b in zip(self, another))

    def __mul__(self, k):
        # 返回向量乘法的结果向量 self * k
        return Vector([k * e for e in self])

    def __rmul__(self, k):
        # 返回数量乘法的结果向量 k * self
        return self * k

    def __truediv__(self, k):
        """返回数量除法, 就是乘法的一种应用"""
        return (1 / k) * self

    def __pos__(self):
        """返回向量取正的结果向量"""
        return 1 * self

    def __neg__(self):
        """返回向量取负的结果向量"""
        return -1 * self

    def __iter__(self):
        # 返回向量具体值的迭代器
        return self._values.__iter__()

    def __len__(self):
        # 返回向量的维度
        return len(self._values)

    def __getitem__(self, index):
        # 取向量的第index个元素
        return self._values[index]

    def __repr__(self):
        return f'Vector{self._values}'

    def __str__(self):
        return f'({",".join(str(e) for e in self._values)})'
