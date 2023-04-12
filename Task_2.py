# 2. Реализовать сортировку пузырьком для двухсвязного списка


class Node:
    def __init__(self, data):
        self.prev = None
        self.data = data
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    # Добавление элемента в конец списка
    def add_node(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

    # Получение длины списка
    def get_length(self):
        current = self.head
        count = 0

        while current is not None:
            count += 1
            current = current.next

        return count

    # Сортировка пузырьком двусвязного списка
    def bubble_sort(self):
        length = self.get_length()

        # 1-й цикл for проходится по всему списку начиная с головы
        for i in range(length - 1):
            current = self.head

            # 2-й цикл for нужен для сравнения элементов в списка
            for j in range(length - i - 1):

                # Если предыдущий элемент больше следующего, то меняем их местами
                if current is not None and current.data > current.next.data:
                    temp = current.data
                    current.data = current.next.data
                    current.next.data = temp

                current = current.next

    # Отображение элементов списка
    def display(self):
        current = self.head
        while (current):
            print(current.data)
            current = current.next


doubly_linked_list = DoublyLinkedList()
doubly_linked_list.add_node(3)
doubly_linked_list.add_node(4)
doubly_linked_list.add_node(2)
doubly_linked_list.add_node(1)
doubly_linked_list.display()
doubly_linked_list.bubble_sort()
doubly_linked_list.display()
