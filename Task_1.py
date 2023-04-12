# 1. Необходимо реализовать метод разворота связного списка
# (двухсвязного или односвязного на выбор).

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


def reverseList(head: Node) -> Node:
    # инициализируем три переменные:
    prev = None  # предыдущий элемент
    curr = head  # текущий элемент
    nxt = None   # следующий элемент (заранее неизвестный)

    while curr:
        nxt = curr.next  # сохраняем ссылку на следующий элемент
        curr.next = prev  # меняем ссылку текущего элемента на предыдущий
        prev = curr      # переопределяем предыдущий элемент на текущий
        curr = nxt       # переопределяем текущий элемент на следующий

    return prev


node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = None

reversed_head = reverseList(node1)

# вывод элементов развернутого списка
while reversed_head:
    print(reversed_head.val)
    reversed_head = reversed_head.next
