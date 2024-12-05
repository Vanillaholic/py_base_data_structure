class SequentialList:
    def __init__(self):
        # ��ʼ��˳���
        self.capacity = 10
        self.size = 0
        self.elements = [0] * self.capacity

    def __del__(self):
        # ����˳���
        del self.elements

    def ssize(self):
        # ��ȡ˳���Ԫ�ظ���
        return self.size

    def is_empty(self):
        # �ж�˳����Ƿ�Ϊ��
        return self.size == 0

    def insert(self, index, element):
        # ��ָ������������Ԫ��
        if index < 0 or index > self.size:
            raise ValueError("Invalid index")
        if self.size == self.capacity:
            self.resize()
        for i in range(self.size, index, -1):
            self.elements[i] = self.elements[i - 1]
        self.elements[index] = element
        self.size += 1

    def remove(self, index):
        # ɾ��ָ����������Ԫ��
        if index < 0 or index >= self.size:
            raise ValueError("Invalid index")
        self.elements[index] = 0
        for i in range(index + 1, self.size):
            self.elements[i - 1] = self.elements[i]
        self.size -= 1

    def get(self, index):
        # ��ȡָ����������Ԫ��
        if index < 0 or index >= self.size:
            raise ValueError("Invalid index")
        return self.elements[index]

    def set(self, index, element):
        # �޸�ָ����������Ԫ��
        if index < 0 or index >= self.size:
            raise ValueError("Invalid index")
        self.elements[index] = element

    def find(self, element):
        # ����Ԫ����˳����е�����
        for i in range(self.size):
            if self.elements[i] == element:
                return i
        return -1

    def resize(self):
        # ����˳�������
        new_capacity = self.capacity * 2
        new_elements = [0] * new_capacity
        for i in range(self.size):
            new_elements[i] = self.elements[i]
        self.capacity = new_capacity
        self.elements = new_elements

    def __iter__(self):
        # ����˳����е�Ԫ��
        for i in range(self.size):
            yield self.elements[i]

    def __str__(self):
        # ��ӡ˳���
        return "Sequential List: " + str(self.elements[:self.size])


# ���Դ���
if __name__ == "__main__":
    my_list = SequentialList()

    # ���Ԫ��
    my_list.insert(0, 1)
    my_list.insert(1, 2)
    my_list.insert(2, 3)
    my_list.insert(3, 4)
    my_list.insert(4, 5)

    # ��ӡ˳���
    print(my_list)

    # ��ȡԪ�ظ���
    print("Size:", my_list.ssize())

    # �ж�˳����Ƿ�Ϊ��
    print("Empty:", my_list.is_empty())

    # ��ָ������������Ԫ��
    my_list.insert(3, 6)
    print(my_list)

    # ɾ��ָ����������Ԫ��
    my_list.remove(3)
    print(my_list)

    # ��ȡָ����������Ԫ��
    print("Get element at index 2:", my_list.get(2))

    # �޸�ָ����������Ԫ��
    my_list.set(2, 10)
    print(my_list)

    # ����Ԫ����˳����е�����
    print("Index of element 3:", my_list.find(3))

    # ����˳����е�Ԫ��
    for element in my_list:
        print(element)