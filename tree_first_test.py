""""
simple tree. First time trying to implement a tree data structure.
Will have nodes. Like doubly linked lists
"""
#no duplicate

class Tree:
    class TreeNode:
        def __init__(self, data:any, parent= None, level:int=0):
            self.data = data
            self.parent = parent
            self.childs = set()
            self.level = level

        def child_choice(self):
            choice = input("choose a child node: \n", self.childs)
            if choice in self.childs.data:
                pass
            pass




        def __repr__(self):
            return f"Tree:{str(self.data)}({f"childs={set([i.data for i in self.childs])}" if self.childs else None })"

            #return f"TreeNode(data={str(self.data)}, parent={self.parent}, level={self.level}, childs={set([i.data for i in self.childs])})"

    def __init__(self, root, have_duplicates :bool = False):
        self.root = self.TreeNode(root)
        self.curent_node = self.root


    def add_children(self, child):
        self.curent_node.childs.add(self.TreeNode(child, self.curent_node, self.curent_node.level+1))

    def next(self, next =None):
        if not self.curent_node.childs:
            raise Exception("No child nodes found")
        if next == None:
            self.curent_node = self.curent_node.child_choice()

    def remove(self, wipe_childrens = True):
        """
        remove the node from the tree
        :param wipe_childrens: remove the childrens from the tree. Or to make childrens of the removed node the new children of the ancestor.
        :return:
        """
        pass


def test():
    tree = Tree('mok')
    print(tree.root)
    tree.add_children('jjj')
    tree.add_children('fff')
    print(tree.root)
    print(tree.curent_node)
    tree.next()


if __name__ == '__main__':
    test()