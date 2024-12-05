class SequentialList:
    def __init__(self):
        # 初始化顺序表
        self.capacity = 10
        self.size = 0
        self.elements = [0] * self.capacity

    def __del__(self):
        # 销毁顺序表
        del self.elements

    def ssize(self):
        # 获取顺序表元素个数
        return self.size

    def is_empty(self):
        # 判断顺序表是否为空
        return self.size == 0

    def insert(self, index, element):
        # 在指定索引处插入元素
        if index < 0 or index > self.size:
            raise ValueError("Invalid index")
        if self.size == self.capacity:
            self.resize()
        for i in range(self.size, index, -1):
            self.elements[i] = self.elements[i - 1]
        self.elements[index] = element
        self.size += 1

    def remove(self, index):
        # 删除指定索引处的元素
        if index < 0 or index >= self.size:
            raise ValueError("Invalid index")
        self.elements[index] = 0
        for i in range(index + 1, self.size):
            self.elements[i - 1] = self.elements[i]
        self.size -= 1

    def get(self, index):
        # 获取指定索引处的元素
        if index < 0 or index >= self.size:
            raise ValueError("Invalid index")
        return self.elements[index]

    def set(self, index, element):
        # 修改指定索引处的元素
        if index < 0 or index >= self.size:
            raise ValueError("Invalid index")
        self.elements[index] = element

    def find(self, element):
        # 查找元素在顺序表中的索引
        for i in range(self.size):
            if self.elements[i] == element:
                return i
        return -1

    def resize(self):
        # 调整顺序表容量
        new_capacity = self.capacity * 2
        new_elements = [0] * new_capacity
        for i in range(self.size):
            new_elements[i] = self.elements[i]
        self.capacity = new_capacity
        self.elements = new_elements

    def __iter__(self):
        # 迭代顺序表中的元素
        for i in range(self.size):
            yield self.elements[i]

    def __str__(self):
        # 打印顺序表
        return "Sequential List: " + str(self.elements[:self.size])


# 测试代码
if __name__ == "__main__":
    my_list = SequentialList()

    # 添加元素
    my_list.insert(0, 1)
    my_list.insert(1, 2)
    my_list.insert(2, 3)
    my_list.insert(3, 4)
    my_list.insert(4, 5)

    # 打印顺序表
    print(my_list)

    # 获取元素个数
    print("Size:", my_list.ssize())

    # 判断顺序表是否为空
    print("Empty:", my_list.is_empty())

    # 在指定索引处插入元素
    my_list.insert(3, 6)
    print(my_list)

    # 删除指定索引处的元素
    my_list.remove(3)
    print(my_list)

    # 获取指定索引处的元素
    print("Get element at index 2:", my_list.get(2))

    # 修改指定索引处的元素
    my_list.set(2, 10)
    print(my_list)

    # 查找元素在顺序表中的索引
    print("Index of element 3:", my_list.find(3))

    # 迭代顺序表中的元素
    for element in my_list:
        print(element)