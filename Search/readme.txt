目录

一、基本概念
二、无序表查找
三、有序表查找

3.1 二分查找(Binary Search)
3.2 插值查找
3.3 斐波那契查找

四、线性索引查找

4.1 稠密索引
4.2 分块索引
4.3 倒排索引

五、二叉排序树
六、 平衡二叉树
七、多路查找树（B树）

7.1 2-3树
7.2 2-3-4树
7.3 B树
7.4 B+树

八、散列表（哈希表）

8.1 散列函数的构造方法
8.2 处理散列冲突
8.3 散列表查找实现
8.4 散列表查找性能分析

参考书目《大话数据结构》

一、基本概念
查找（Searching）就是根据给定的某个值，在查找表中确定一个其关键字等于给定值的数据元素（或记录）。

查找表（Search Table）：由同一类型的数据元素（或记录）构成的集合
关键字（Key）：数据元素中某个数据项的值，又称为键值。
主键（Primary Key）：可唯一地标识某个数据元素或记录的关键字。

查找表按照操作方式可分为：

静态查找表（Static Search Table）：只做查找操作的查找表。它的主要操作是：
查询某个“特定的”数据元素是否在表中
检索某个“特定的”数据元素和各种属性
动态查找表（Dynamic Search Table）：在查找中同时进行插入或删除等操作：
查找时插入数据
查找时删除数据
二、无序表查找
也就是数据不排序的线性查找，遍历数据元素。
算法分析：最好情况是在第一个位置就找到了，此为O(1)；最坏情况在最后一个位置才找到，此为O(n)；所以平均查找次数为(n+1)/2。最终时间复杂度为O(n)

# 最基础的遍历无序列表的查找算法
# 时间复杂度O(n)

def sequential_search(lis, key):
    length = len(lis)
    for i in range(length):
        if lis[i] == key:
            return i
    else:
        return False


if __name__ == '__main__':
    LIST = [1, 5, 8, 123, 22, 54, 7, 99, 300, 222]
    result = sequential_search(LIST, 123)
    print(result)
三、有序表查找
查找表中的数据必须按某个主键进行某种排序！

1. 二分查找(Binary Search)
算法核心：在查找表中不断取中间元素与查找值进行比较，以二分之一的倍率进行表范围的缩小。

# 针对有序查找表的二分查找算法
# 时间复杂度O(log(n))

def binary_search(lis, key):
    low = 0
    high = len(lis) - 1
    time = 0
    while low < high:
        time += 1
        mid = int((low + high) / 2)
        if key < lis[mid]:
            high = mid - 1
        elif key > lis[mid]:
            low = mid + 1
        else:
            # 打印折半的次数
            print("times: %s" % time)
            return mid
    print("times: %s" % time)
    return False

if __name__ == '__main__':
    LIST = [1, 5, 7, 8, 22, 54, 99, 123, 200, 222, 444]
    result = binary_search(LIST, 99)
    print(result)
2. 插值查找
二分查找法虽然已经很不错了，但还有可以优化的地方。
有的时候，对半过滤还不够狠，要是每次都排除十分之九的数据岂不是更好？选择这个值就是关键问题，插值的意义就是：以更快的速度进行缩减。

插值的核心就是使用公式：
value = (key - list[low])/(list[high] - list[low])

用这个value来代替二分查找中的1/2。
上面的代码可以直接使用，只需要改一句。

# 插值查找算法
# 时间复杂度O(log(n))

def binary_search(lis, key):
    low = 0
    high = len(lis) - 1
    time = 0
    while low < high:
        time += 1
        # 计算mid值是插值算法的核心代码
        mid = low + int((high - low) * (key - lis[low])/(lis[high] - lis[low]))
        print("mid=%s, low=%s, high=%s" % (mid, low, high))
        if key < lis[mid]:
            high = mid - 1
        elif key > lis[mid]:
            low = mid + 1
        else:
            # 打印查找的次数
            print("times: %s" % time)
            return mid
    print("times: %s" % time)
    return False

if __name__ == '__main__':
    LIST = [1, 5, 7, 8, 22, 54, 99, 123, 200, 222, 444]
    result = binary_search(LIST, 444)
    print(result)
插值算法的总体时间复杂度仍然属于O(log(n))级别的。其优点是，对于表内数据量较大，且关键字分布比较均匀的查找表，使用插值算法的平均性能比二分查找要好得多。反之，对于分布极端不均匀的数据，则不适合使用插值算法。

3. 斐波那契查找
由插值算法带来的启发，发明了斐波那契算法。其核心也是如何优化那个缩减速率，使得查找次数尽量降低。
使用这种算法，前提是已经有一个包含斐波那契数据的列表
F = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144,...]

# 斐波那契查找算法
# 时间复杂度O(log(n))

def fibonacci_search(lis, key):
    # 需要一个现成的斐波那契列表。其最大元素的值必须超过查找表中元素个数的数值。
    F = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144,
         233, 377, 610, 987, 1597, 2584, 4181, 6765,
         10946, 17711, 28657, 46368]
    low = 0
    high = len(lis) - 1
    
    # 为了使得查找表满足斐波那契特性，在表的最后添加几个同样的值
    # 这个值是原查找表的最后那个元素的值
    # 添加的个数由F[k]-1-high决定
    k = 0
    while high > F[k]-1:
        k += 1
    print(k)
    i = high
    while F[k]-1 > i:
        lis.append(lis[high])
        i += 1
    print(lis)
    
    # 算法主逻辑。time用于展示循环的次数。
    time = 0
    while low <= high:
        time += 1
        # 为了防止F列表下标溢出，设置if和else
        if k < 2:
            mid = low
        else:
            mid = low + F[k-1]-1
        
        print("low=%s, mid=%s, high=%s" % (low, mid, high))
        if key < lis[mid]:
            high = mid - 1
            k -= 1
        elif key > lis[mid]:
            low = mid + 1
            k -= 2
        else:
            if mid <= high:
                # 打印查找的次数
                print("times: %s" % time)
                return mid
            else:
                print("times: %s" % time)
                return high
    print("times: %s" % time)
    return False

if __name__ == '__main__':
    LIST = [1, 5, 7, 8, 22, 54, 99, 123, 200, 222, 444]
    result = fibonacci_search(LIST, 444)
    print(result)
算法分析：斐波那契查找的整体时间复杂度也为O(log(n))。但就平均性能，要优于二分查找。但是在最坏情况下，比如这里如果key为1，则始终处于左侧半区查找，此时其效率要低于二分查找。

总结：二分查找的mid运算是加法与除法，插值查找则是复杂的四则运算，而斐波那契查找只是最简单的加减运算。在海量数据的查找中，这种细微的差别可能会影响最终的查找效率。因此，三种有序表的查找方法本质上是分割点的选择不同，各有优劣，应根据实际情况进行选择。

四、线性索引查找
对于海量的无序数据，为了提高查找速度，一般会为其构造索引表。
索引就是把一个关键字与它相对应的记录进行关联的过程。
一个索引由若干个索引项构成，每个索引项至少包含关键字和其对应的记录在存储器中的位置等信息。
索引按照结构可以分为：线性索引、树形索引和多级索引。
线性索引：将索引项的集合通过线性结构来组织，也叫索引表。
线性索引可分为：稠密索引、分块索引和倒排索引

稠密索引
稠密索引指的是在线性索引中，为数据集合中的每个记录都建立一个索引项。
image_1b2cl8r0dk1v1u0ssf0rmk8o29.png-157.4kB

这其实就相当于给无序的集合，建立了一张有序的线性表。其索引项一定是按照关键码进行有序的排列。
这也相当于把查找过程中需要的排序工作给提前做了。

分块索引
给大量的无序数据集合进行分块处理，使得块内无序，块与块之间有序。
这其实是有序查找和无序查找的一种中间状态或者说妥协状态。因为数据量过大，建立完整的稠密索引耗时耗力，占用资源过多；但如果不做任何排序或者索引，那么遍历的查找也无法接受，只能折中，做一定程度的排序或索引。
image_1b2clkecf3mt1j7a8hn3v5vbrm.png-136.6kB

分块索引的效率比遍历查找的O(n)要高一些，但与二分查找的O(logn)还是要差不少。

倒排索引
不是由记录来确定属性值，而是由属性值来确定记录的位置，这种被称为倒排索引。其中记录号表存储具有相同次关键字的所有记录的地址或引用（可以是指向记录的指针或该记录的主关键字）。

倒排索引是最基础的搜索引擎索引技术。

五、二叉排序树
二叉排序树又称为二叉查找树。它或者是一颗空树，或者是具有下列性质的二叉树：

若它的左子树不为空，则左子树上所有节点的值均小于它的根结构的值；
若它的右子树不为空，则右子树上所有节点的值均大于它的根结构的值；
它的左、右子树也分别为二叉排序树。
image_1b2cm8v3mi50141m1vi31v658dh13.png-61.7kB
构造一颗二叉排序树的目的，往往不是为了排序，而是为了提高查找和插入删除关键字的速度。

二叉排序树的操作：

查找：对比节点的值和关键字，相等则表明找到了；小了则往节点的左子树去找，大了则往右子树去找，这么递归下去，最后返回布尔值或找到的节点。
插入：从根节点开始逐个与关键字进行对比，小了去左边，大了去右边，碰到子树为空的情况就将新的节点链接。
删除：如果要删除的节点是叶子，直接删；如果只有左子树或只有右子树，则删除节点后，将子树链接到父节点即可；如果同时有左右子树，则可以将二叉排序树进行中序遍历，取将要被删除的节点的前驱或者后继节点替代这个被删除的节点的位置。
#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Liu Jiang
# Python 3.5


class BSTNode:
    """
    定义一个二叉树节点类。
    以讨论算法为主，忽略了一些诸如对数据类型进行判断的问题。
    """
    def __init__(self, data, left=None, right=None):
        """
        初始化
        :param data: 节点储存的数据
        :param left: 节点左子树
        :param right: 节点右子树
        """
        self.data = data
        self.left = left
        self.right = right


class BinarySortTree:
    """
    基于BSTNode类的二叉排序树。维护一个根节点的指针。
    """
    def __init__(self):
        self._root = None

    def is_empty(self):
        return self._root is None

    def search(self, key):
        """
        关键码检索
        :param key: 关键码
        :return: 查询节点或None
        """
        bt = self._root
        while bt:
            entry = bt.data
            if key < entry:
                bt = bt.left
            elif key > entry:
                bt = bt.right
            else:
                return entry
        return None

    def insert(self, key):
        """
        插入操作
        :param key:关键码 
        :return: 布尔值
        """
        bt = self._root
        if not bt:
            self._root = BSTNode(key)
            return
        while True:
            entry = bt.data
            if key < entry:
                if bt.left is None:
                    bt.left = BSTNode(key)
                    return
                bt = bt.left
            elif key > entry:
                if bt.right is None:
                    bt.right = BSTNode(key)
                    return
                bt = bt.right
            else:
                bt.data = key
                return

    def delete(self, key):
        """
        二叉排序树最复杂的方法
        :param key: 关键码
        :return: 布尔值
        """
        p, q = None, self._root     # 维持p为q的父节点，用于后面的链接操作
        if not q:
            print("空树！")
            return
        while q and q.data != key:
            p = q
            if key < q.data:
                q = q.left
            else:
                q = q.right
            if not q:               # 当树中没有关键码key时，结束退出。
                return
        # 上面已将找到了要删除的节点，用q引用。而p则是q的父节点或者None（q为根节点时）。
        if not q.left:
            if p is None:
                self._root = q.right
            elif q is p.left:
                p.left = q.right
            else:
                p.right = q.right
            return
        # 查找节点q的左子树的最右节点，将q的右子树链接为该节点的右子树
        # 该方法可能会增大树的深度，效率并不算高。可以设计其它的方法。
        r = q.left
        while r.right:
            r = r.right
        r.right = q.right
        if p is None:
            self._root = q.left
        elif p.left is q:
            p.left = q.left
        else:
            p.right = q.left

    def __iter__(self):
        """
        实现二叉树的中序遍历算法,
        展示我们创建的二叉排序树.
        直接使用python内置的列表作为一个栈。
        :return: data
        """
        stack = []
        node = self._root
        while node or stack:
            while node:
                stack.append(node)
                node = node.left
            node = stack.pop()
            yield node.data
            node = node.right


if __name__ == '__main__':
    lis = [62, 58, 88, 48, 73, 99, 35, 51, 93, 29, 37, 49, 56, 36, 50]
    bs_tree = BinarySortTree()
    for i in range(len(lis)):
        bs_tree.insert(lis[i])
    # bs_tree.insert(100)
    bs_tree.delete(58)
    for i in bs_tree:
        print(i, end=" ")
    # print("\n", bs_tree.search(4))
二叉排序树总结：

二叉排序树以链式进行存储，保持了链接结构在插入和删除操作上的优点。
在极端情况下，查询次数为1，但最大操作次数不会超过树的深度。也就是说，二叉排序树的查找性能取决于二叉排序树的形状，也就引申出了后面的平衡二叉树。
给定一个元素集合，可以构造不同的二叉排序树，当它同时是一个完全二叉树的时候，查找的时间复杂度为O(log(n))，近似于二分查找。
当出现最极端的斜树时，其时间复杂度为O(n)，等同于顺序查找，效果最差。
image_1b2kcsdqk12m1fd1vsjdmf1fbt9.png-50.5kB

六、 平衡二叉树
平衡二叉树（AVL树，发明者的姓名缩写）：一种高度平衡的排序二叉树，其每一个节点的左子树和右子树的高度差最多等于1。

平衡二叉树首先必须是一棵二叉排序树！

平衡因子（Balance Factor）：将二叉树上节点的左子树深度减去右子树深度的值。

对于平衡二叉树所有包括分支节点和叶节点的平衡因子只可能是-1,0和1，只要有一个节点的因子不在这三个值之内，该二叉树就是不平衡的。

image_1b3f3d2tq1lmvelp17moce414qa9.png-239.9kB

最小不平衡子树：距离插入结点最近的，且平衡因子的绝对值大于1的节点为根的子树。

平衡二叉树的构建思想：每当插入一个新结点时，先检查是否破坏了树的平衡性，若有，找出最小不平衡子树。在保持二叉排序树特性的前提下，调整最小不平衡子树中各结点之间的连接关系，进行相应的旋转，成为新的平衡子树。

下面是由[1,2,3,4,5,6,7,10,9]构建平衡二叉树

image_1b3f49a2mkiu6taohbri51rc51g.png-87.9kB
image_1b3f4a556pnriva182n7ikihv1t.png-91.1kB
image_1b3f4d2j1r2ko961fmj14gd90i2a.png-91.8kB
image_1b3f4dl7u1hrc4jf1cf21shb1h6s2n.png-119.2kB
image_1b3f4f8u2vvgl424p9drs1ge734.png-164.6kB
image_1b3f4gg6g11ts12m8ksa17i41tb53h.png-81.2kB
image_1b3f4hsdjckb1vodaoi1qmpg2u3u.png-187.5kB

七、多路查找树（B树）
多路查找树（muitl-way search tree）：其每一个节点的孩子可以多于两个，且每一个结点处可以存储多个元素。
对于多路查找树，每个节点可以存储多少个元素，以及它的孩子数的多少是关键，常用的有这4种形式：2-3树、2-3-4树、B树和B+树。

2-3树
2-3树：每个结点都具有2个孩子，或者3个孩子，或者没有孩子。

一个2结点包含一个元素和两个孩子（或者没有孩子，不能只有一个孩子）。与二叉排序树类似，其左子树包含的元素都小于该元素，右子树包含的元素都大于该元素。
一个3结点包含两个元素和三个孩子（或者没有孩子，不能只有一个或两个孩子）。

2-3树中所有的叶子都必须在同一层次上。

image_1b3f9opsn55815u31cme12fp1qjh4b.png-96.7kB

其插入操作如下：
image_1b3f9smmb1f4nf7o1trm76q1n1f4o.png-55kB
image_1b3f9t1gtmb6o8n6aekqp1fob55.png-51.5kB
image_1b3f9tdsj1n4p1q427fb5cd1jkh5i.png-56.7kB
image_1b3f9to5t55u19ocp9m1grgd125v.png-61.2kB
其删除操作如下：

image_1b3f9vqfa1rnqcnr1r1fl8v62k6c.png-45.4kB
image_1b3fa085flva1j9n18jm1t9r7t86p.png-40.2kB
image_1b3fa0ijm10oe88d1fuq16s7jo876.png-47.3kB
image_1b3fa0q0j81u3jv1b4o12k6qo67j.png-63kB
image_1b3fa10unfc7199spfk1te364480.png-44.2kB
image_1b3fa1b341qng11darqm1b92au38d.png-33kB
image_1b3fa1nrt18u511d5q5k9dr10sc8q.png-47.5kB
image_1b3fa1v031vl15141t201smr1o4r97.png-50.2kB

2-3-4树
其实就是2-3树的扩展，包括了4结点的使用。一个4结点包含小中大三个元素和四个孩子（或没有孩子）。

其插入操作:
image_1b3fa4fei1p319u4r9h15im1nr49k.png-83kB
其删除操作：
image_1b3fa538hcnj20j1fd01en81ohta1.png-87.6kB

B树
B树是一种平衡的多路查找树。节点最大的孩子数目称为B树的阶（order）。2-3树是3阶B树，2-3-4是4阶B树。
B树的数据结构主要用在内存和外部存储器的数据交互中。
image_1b3fajra41dobmdl1jbn1gk9461ar.png-159.6kB
image_1b3fahcg450l11lo19eor1i1gv2ae.png-30.7kB
image_1b3fal5pn1m8119551bh0nuf1oqgb8.png-176.4kB

B+树
为了解决B树的所有元素遍历等基本问题，在原有的结构基础上，加入新的元素组织方式后，形成了B+树。

B+树是应文件系统所需而出现的一种B树的变形树，严格意义上将，它已经不是最基本的树了。

B+树中，出现在分支节点中的元素会被当做他们在该分支节点位置的中序后继者（叶子节点）中再次列出。另外，每一个叶子节点都会保存一个指向后一叶子节点的指针。
image_1b3fav2fa7661pl21usc1g331vq8bl.png-29.7kB

所有的叶子节点包含全部的关键字的信息，及相关指针，叶子节点本身依关键字的大小自小到大顺序链接

B+树的结构特别适合带有范围的查找。比如查找年龄在20~30岁之间的人。

八、散列表（哈希表）
散列表：所有的元素之间没有任何关系。元素的存储位置，是利用元素的关键字通过某个函数直接计算出来的。这个一一对应的关系函数称为散列函数或Hash函数。
采用散列技术将记录存储在一块连续的存储空间中，称为散列表或哈希表（Hash Table）。关键字对应的存储位置，称为散列地址。

散列表是一种面向查找的存储结构。它最适合求解的问题是查找与给定值相等的记录。但是对于某个关键字能对应很多记录的情况就不适用，比如查找所有的“男”性。也不适合范围查找，比如查找年龄20~30之间的人。排序、最大、最小等也不合适。

因此，散列表通常用于关键字不重复的数据结构。比如python的字典数据类型。

设计出一个简单、均匀、存储利用率高的散列函数是散列技术中最关键的问题。
但是，一般散列函数都面临着冲突的问题。
冲突：两个不同的关键字，通过散列函数计算后结果却相同的现象。collision。

8.1 散列函数的构造方法
好的散列函数：计算简单、散列地址分布均匀

直接定址法
例如取关键字的某个线性函数为散列函数：
f(key) = a*key + b (a,b为常数）
数字分析法
抽取关键字里的数字，根据数字的特点进行地址分配
平方取中法
将关键字的数字求平方，再截取部分
折叠法
将关键字的数字分割后分别计算，再合并计算，一种玩弄数字的手段。
除留余数法
最为常见的方法之一。
对于表长为m的数据集合，散列公式为：
f(key) = key mod p (p<=m)
mod：取模（求余数）
该方法最关键的是p的选择，而且数据量较大的时候，冲突是必然的。一般会选择接近m的质数。
随机数法
选择一个随机数，取关键字的随机函数值为它的散列地址。
f(key) = random(key)
总结，实际情况下根据不同的数据特性采用不同的散列方法，考虑下面一些主要问题：

计算散列地址所需的时间
关键字的长度
散列表的大小
关键字的分布情况
记录查找的频率
8.2 处理散列冲突
开放定址法
就是一旦发生冲突，就去寻找下一个空的散列地址，只要散列表足够大，空的散列地址总能找到，并将记录存入。

公式是：
image_1b3gi1p0u6qpdqukj3c961kp99.png-29.8kB
这种简单的冲突解决办法被称为线性探测，无非就是自家的坑被占了，就逐个拜访后面的坑，有空的就进，也不管这个坑是不是后面有人预定了的。
线性探测带来的最大问题就是冲突的堆积，你把别人预定的坑占了，别人也就要像你一样去找坑。

改进的办法有二次方探测法和随机数探测法。

再散列函数法
发生冲突时就换一个散列函数计算，总会有一个可以把冲突解决掉，它能够使得关键字不产生聚集，但相应地增加了计算的时间。

链接地址法
碰到冲突时，不更换地址，而是将所有关键字为同义词的记录存储在一个链表里，在散列表中只存储同义词子表的头指针，如下图：
image_1b3gig3eu1uh3rujcvuli1qspm.png-59.3kB

这样的好处是，不怕冲突多；缺点是降低了散列结构的随机存储性能。本质是用单链表结构辅助散列结构的不足。

公共溢出区法
其实就是为所有的冲突，额外开辟一块存储空间。如果相对基本表而言，冲突的数据很少的时候，使用这种方法比较合适。
image_1b3gim8dp1m4hd0015su1jvm15mg13.png-56.8kB
8.3 散列表查找实现
下面是一段简单的实现代码：

#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Liu Jiang
# Python 3.5
# 忽略了对数据类型，元素溢出等问题的判断。


class HashTable:
    def __init__(self, size):
        self.elem = [None for i in range(size)]  # 使用list数据结构作为哈希表元素保存方法
        self.count = size  # 最大表长

    def hash(self, key):
        return key % self.count  # 散列函数采用除留余数法

    def insert_hash(self, key):
        """插入关键字到哈希表内"""
        address = self.hash(key)  # 求散列地址
        while self.elem[address]:  # 当前位置已经有数据了，发生冲突。
            address = (address+1) % self.count  # 线性探测下一地址是否可用
        self.elem[address] = key  # 没有冲突则直接保存。

    def search_hash(self, key):
        """查找关键字，返回布尔值"""
        star = address = self.hash(key)
        while self.elem[address] != key:
            address = (address + 1) % self.count
            if not self.elem[address] or address == star:  # 说明没找到或者循环到了开始的位置
                return False
        return True


if __name__ == '__main__':
    list_a = [12, 67, 56, 16, 25, 37, 22, 29, 15, 47, 48, 34]
    hash_table = HashTable(12)
    for i in list_a:
        hash_table.insert_hash(i)

    for i in hash_table.elem:
        if i:
            print((i, hash_table.elem.index(i)), end=" ")
    print("\n")

    print(hash_table.search_hash(15))
    print(hash_table.search_hash(33))
8.4 散列表查找性能分析
如果没发生冲突，则其查找时间复杂度为O(1)，属于最极端的好了。
但是，现实中冲突可不可避免的，下面三个方面对查找性能影响较大：

散列函数是否均匀
处理冲突的办法
散列表的装填因子（表内数据装满的程度）
