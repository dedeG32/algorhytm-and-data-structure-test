from single_linked_list import Single_linked_list
class Stack_linked(Single_linked_list):
    def __init__(self):
        super().__init__()

    def top(self):
        """
        :return: last element added to the list without removing it.
        """
        if not self.is_empty():
            return self.__items[0]
        else:
            raise IndexError("No element in the stack")





def test():
    stack = Stack_linked()
    stack.add_node("MO")
    stack.add_node('Mohamed')
    stack.add_node(1)
    stack.add_node(2)
    stack.add_node(3)
    stack.add_node("vovador")

    for node in range(len(stack)-1):
        print(stack.curent_node())
        print(stack.next())


test()