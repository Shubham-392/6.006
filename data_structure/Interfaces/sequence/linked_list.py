class Node:
    """
    A constant-sized container with two properties
    i.e.,

    `self.item` & `self.next `
    """

    def __init__(self, stored_item):
        self.item = stored_item
        self.next = None

    def later_node(self, index):
        """
        Return the node that is `index` steps ahead of this node.

        index = 0 -> return self

        index = 1 -> return next node
        and so on.

        Raises AssertionError if the list ends before reaching index.
        """

        if index == 0:
            return self
        assert (
            self.next
        )  # checks if self.next is not 'None' if yes raises AssertionError
        return self.next.later_node(index - 1)

    def __str__(self):
        return str(self.item)


class LinkedListSequence:
    """
    A linked list is a different type of data structure entirely.

    Instead of allocating a contiguous chunk
    of memory in which to store items,
    a linked list stores each item in a `node`,

    node -- a constant-sized container with two properties:
    `node.item` -- storing the item

    `node.next` -- storing the memory address of the node containing the next item in the sequence.
    """

    def __init__(self):
        self.head = None
        self.size = 0

    def __len__(self):
        return self.size

    def __iter__(self):
        node = self.head
        while node:
            yield node.item
            node = node.next

    def build(self, iterable):
        for item in reversed(iterable):
            self.insert_first(item)

    def get_at(self, index):  # O(index:i)
        node = self.head.later_node(index)
        return node.item

    def set_at(self, index, new_item: Node):
        node = self.head.later_node(index)
        node.item = new_item

    def insert_first(self, item: Node):
        new_node = Node(item)
        new_node.next = self.head
        self.head = new_node
        self.size += 1

    def delete_first(self) -> Node:
        head_item = self.head.item
        self.head = self.head.next
        self.size -= 1
        return head_item

    def insert_at(self, index: int, item: Node):
        if index == 0:
            self.insert_first(item)
            return
        new_node = Node(item)
        node = self.head.later_node(index - 1)
        new_node.next = node.next
        node.next = new_node
        self.size += 1

    def delete_at(self, index: int):
        if index == 0:
            self.delete_first()
            return

        node = self.head.later_node(index=index - 1)
        deleted_item = node.next.item
        node.next = node.next.next
        self.size -= 1
        return deleted_item

    def insert_last(self, item: Node):
        self.insert_at(len(self), item=item)

    def delete_last(self):
        return self.delete_at(len(self) - 1)

    def __str__(self):
        if not self.head:
            return "Empty list"
        unpretty_linkedList = []
        for i in range(len(self)):
            node = self.get_at(i)
            unpretty_linkedList.append(str(node))
        pretty_linkedList = " -> ".join(unpretty_linkedList)
        return pretty_linkedList


linked_list = LinkedListSequence()

X = [3, 6, 9, 12, 15, 18, 21, 24, 27]
linked_list.build(X)
print(linked_list)
fourth_item = linked_list.get_at(4)
print(fourth_item)
linked_list.insert_at(4, 13)
print(linked_list)
