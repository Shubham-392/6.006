class Node:
    """
    A constant-sized container with two properties
    i.e.,

    `self.item` & `self.next`
    """

    def __init__(self, stored_item):
        self.item = stored_item
        self.next = None
        self.prev = None

    def later_node(self, index):
        """
        Return the node that is `index` steps ahead of this node.

        index = 0 -> return self

        index = 1 -> return next node
        and so on.

        Raises AssertionError if the list ends before reaching index.
        """

        node = self
        for _ in range(index):
            assert node.next, f"List ended before reaching index {index}"
            node = node.next
        return node

    def __str__(self):
        return str(self.item)


class DoubleLinkedListSequence:
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
        self.tail = None
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

    def insert_first(self, item):
        new_node = Node(item)
        new_node.next = self.head
        if self.head is not None:
            self.head.prev = new_node
        self.head = new_node
        if self.tail is None:
            self.tail = new_node
        self.size += 1

    def delete_first(self):
        if self.head is None:
            raise IndexError("Cannot operate delete at empty sequence.")
        head_item = self.head.item
        if self.head.next is not None:
            self.head.next.prev = None
        else:
            self.tail = None
        self.size -= 1
        self.head = self.head.next
        return head_item

    def insert_at(self, index: int, item):
        if index == 0:
            self.insert_first(item)
            return
        new_node = Node(item)
        node = self.head.later_node(index - 1)
        new_node.next = node.next
        new_node.prev = node
        if node.next is not None:
            node.next.prev = new_node
        else:
            self.tail = new_node
        node.next = new_node
        self.size += 1

    def delete_at(self, index: int):
        if index == 0:
            return self.delete_first()

        node = self.head.later_node(index - 1)
        deleted_item = node.next.item

        if node.next.next is not None:  # Deleting from middle
            node.next.next.prev = node
            node.next = node.next.next
        else:  # Deleting the last element
            node.next = None
            self.tail = node

        self.size -= 1
        return deleted_item

    def insert_last(self, item):
        new_node = Node(item)
        if self.tail is None:  # Empty list
            self.head = new_node
            self.tail = new_node
        else:                  # Non-empty list
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
        self.size += 1

    def delete_last(self):
        tail = self.tail
        if tail is None:
            raise IndexError(
                'Cannot operate delete at empty sequence.'
            )
        tail_item = tail.item
        prev_node = tail.prev
        if prev_node is not  None:
            tail.prev = None
            prev_node.next = None
            self.tail = prev_node
        else:
            self.head = None
            self.tail = None
        self.size -= 1
        return tail_item


    def __str__(self):
        if not self.head:
            return "Empty list"
        unpretty_linkedList = []
        for i in range(len(self)):
            node = self.get_at(i)
            unpretty_linkedList.append(str(node))
        pretty_linkedList = " <-> ".join(unpretty_linkedList)
        return pretty_linkedList

linked_list = DoubleLinkedListSequence()

X = [3, 6, 9, 12, 15, 18, 21, 24, 27]
linked_list.build(X)
print(linked_list)
print(linked_list.head)
print(linked_list.tail)
linked_list.set_at(4,34)
print(linked_list)
print(linked_list.head)
print(linked_list.tail)
