class BSTree:
    """Class representing binary search tree"""

    def __init__(self, data=None, left=None, right=None, parent=None):
        """Method initializes instance of BSTree class
        
        Args:
            data (any, optional): Data in this node of tree. Defaults to None.
            left (BSTree, optional): Link to left subtree. Defaults to None.
            right (BSTree, optional): Link to right subtree. Defaults to None.
            parent (BSTree, optional): Link to parent subtree. Defaults to None.
        """
        self._parent = parent
        self._left = left
        self._right = right
        self.data = data

    def __iter__(self):
        """Method handles iterating through tree
        
        Returns:
            iterator: Iterator through this object
        """
        items = []

        def _iter_helper(node):
            """Function that helps iterate through this object
            
            Args:
                node (BSTree): Node to get child
            
            Returns:
                list: Empty list if has no childs
            """
            if node is None:
                return []
            else:
                items.append(node)
                _iter_helper(node.left)
                _iter_helper(node.right)

        _iter_helper(self)
        for item in items:
            yield item

    def set_left(self, value):
        """Method sets left child
        
        Args:
            value (any): Left child value to set
        """
        self._left = BSTree(value)

    def get_left(self):
        """Method gets left child
        
        Returns:
            any: Left child
        """
        return self._left

    left = property(get_left, set_left)

    def set_right(self, value):
        """Method sets right child
        
        Args:
            value (any): Right child
        """
        self._right = BSTree(value)

    def get_right(self):
        """Method gets right child
        
        Returns:
            any: Right child
        """
        return self._right

    right = property(get_right, set_right)

    def set_parent(self, value):
        """Method sets parent
        
        Args:
            value (any): Parent
        """
        self._parent = value

    def get_parent(self):
        """Method gets parent
        
        Returns:
            any: Parent
        """
        return self._parent

    parent = property(get_parent, set_parent)

    def get_leafs(self):
        """Method gets leafs
        
        Returns:
            list: Lis of leafs of this tree
        """
        elements = list(self.__iter__())
        leafs = list(
            filter(lambda x: x.left is None and x.right is None, elements))
        return leafs
