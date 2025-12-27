from typing import Self


class BinaryNode:
    """
    a linked node container, similar to a linked list node, having a constant number of fields:

    • a pointer to an item stored at the node,

    • a pointer to a parent node (possibly None),

    • a pointer to a left child node (possibly None), and

    • a pointer to a right child node (possibly None).

    By default the traversal Order is: `In-Order`
    """
    def __init__(self,value):
        self.item = value
        self.parent = None
        self.left = None
        self.right = None
    # iterating over the tree for inoder traversal
    def subtree_iter(self):
        if self.left:
            yield from self.left.subtree_iter()
        yield self
        if self.right:
            yield from self.right.subtree_iter()

    # Operations for Tree-Navigation to getting the items as per traversal order
    # --- startAndLastMethods: to get first and last node in traversal order------------
    def subtree_first(self):
        """
        – If <X> has left child, recursively return the first node in the left subtree

        – Otherwise, <X> is the first node, so return it

        Running time is O(h) where h is the height of the tree
        """
        if self.left:
            return self.left.subtree_first()
        else:
            return self

    def subtree_last(self):
        """
        return: the last node in the traversal order
            – If <X> has right child, recursively return the last node in the right subtree

            – Otherwise, <X> is the last node, so return it

        Running time is O(h) where h is the height of the tree
        """
        if self.right:
            return self.right.subtree_last()
        else:
            return self

    #----- END startandLastMethods--------------------------------------------------------
    #
    #
    # --- Successor$PredecessorMethods:----------------------------------------------------
    # to get the next and previous node in the traversal order for a specific node

    def successor(self):
        """
        In a tree to find successor:

            -- if `<X>` has right child, return first of right subtree

            -- Otherwise, return lowest ancestor of <X> for which <X> is in its left subtree

        Running time is O(h) where h is the height of the tree
        """
        # case1: if has right child
        if self.right:
            return self.right.subtree_first()

        # case2: otherwise, lowest ancestor for which node is in lowest ancestor's left subtree
        curr = self
        while (curr.parent) and (curr is curr.parent.right):
            curr = curr.parent
        # finally return
        return curr.parent

    def predecessor(self):
        """
        In a tree to find predecessor:

            -- if `<X>` has left child, return last of left subtree

            -- Otherwise, return lowest ancestor of <X> for which <X> is in its right subtree

        Running time is O(h) where h is the height of the tree
        """
        # case1: if has left child
        if self.left:
            return self.left.subtree_last()

        # case2: otherwise, lowest ancestor for which node is in lowest ancestor's right subtree
        curr = self
        while (curr.parent) and (curr is curr.parent.left):
            curr = curr.parent
        # finally return
        return curr.parent

    # --- END Successor$PredecessorMethods----------------------------------------------------

    #--- DYNAMIC_OPERATIONS $$$$-----------------------------------------------------------
    # If we want to add or remove items in a binary tree,
    # we must take care to preserve the traversal order of the other items in the tree
    #

    def subtree_insert_before(self, newNode:Self):
        """
        To insert a node <newNode> before a given node <A> in the traversal order,
        either node <A> has a left child or not.

            -- If <A> does not have a left child, than we can simply add
               <newNode> as the left child of <A>.
            -- Otherwise, if <A> has a left child, we can add <B> as the right child of
               the last node in <A>’s left subtree (which cannot have a right child).

        Running time is O(h) where h is the height of the tree.
        """
        if self.left:
            A = self.left.subtree_last()
            A.right, newNode.parent = newNode, A
        else:
            self.left, newNode.parent = newNode, self


    def subtree_insert_after(self, newNode:Self):
        """
        To insert a node <newNode> after a given node <A> in the traversal order,
        either node <A> has a right child or not.

            -- If <A> does not have a right child, than we can simply add
               <newNode> as the right child of <A>.
            -- Otherwise, if <A> has a right child, we can add <newNode> as the left child of
               the first node in <A>’s right subtree (which cannot have a left child).

        Running time is O(h) where h is the height of the tree.
        """
        if self.right:
            A = self.right.subtree_first()
            (A.left, newNode.parent) = (newNode, A)
        else:
            (self.right, newNode.parent) = (newNode, self)

    def subtree_delete(self):
        """
        Delete the item in node <X> from <X>’s subtree

            -- If <X> is a leaf, detach from parent and return
            -- Otherwise, <X> has a child
                ∗ If <X> has a left child, swap items with the predecessor of <X> and recurse

                ∗ Otherwise <X> has a right child, swap items with the successor of <X> and recurse
        -- Running time is O(h) where h is the height of the tree
        """
        if self.left or self.right:
            if self.left :
                B = self.predecessor()
            else:
                B = self.successor()
            self.item, B.item = B.item, self.item
            return B.delete()

        if self.parent:
            if self.parent.left is self:
                self.parent.left = None
            else:
                self.parent.right = None

        return self
