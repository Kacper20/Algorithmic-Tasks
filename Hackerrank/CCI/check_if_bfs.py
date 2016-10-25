def check_binary_search_tree_(root):
    def is_bst(root, prev):
        if root is not None:
            if not is_bst(root.left, prev):
                return False
            if prev is not None and prev.data >= root.data:
                return False
            prev = root
            return is_bst(root.right, prev)
        return True
    return is_bst(root, None)
