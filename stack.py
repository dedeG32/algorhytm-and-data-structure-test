class Stack:
    """
    Caution: Limited size stacks cannot become unlimited again.
    """
    def __init__(self, size: int =0):
        """
        Stack class: Last in last out. Always returns the last element added to it. It can be size limited or not.
        :param is_bordered: int : Size limit of the stack. 0 is unlimited.

        """
        self.__size = size
        self.__items = []


    def push(self, item) -> None:
        if self.__size and len(self.__items) >= self.__size:
            raise IndexError('Stack is full')
        else:
            self.__items.append(item)

    def pop(self) -> any:
        """
        :return: remove and returns last element added to the list.
        """
        if len(self.__items) == 0 :
            raise IndexError("Empty Stack")
        else:
            return self.__items.pop()

    def top(self):
        """
        :return: last element added to the list without removing it.
        """
        if not self.is_empty():
            return self.__items[-1]
        else:
            raise IndexError("No element in the stack")

    def is_empty(self) -> bool:
        return len(self.__items) == 0

    def size(self) -> int:
        '''
        :return: defined size limit of the stack.
        '''
        return len(self.__items)

    def is_full(self):
        if self.__size:
            return len(self.__items) == self.__size
        else: return False

    def resize(self, size: int = 0) -> None:
        """
        resize the stack (can give size to an unlimited stack). if size left empty, the stack resize in sort to always be full.
        :param size: new size limit
        :return:
        """
        if size:
            assert size >= len(self.__items) , "Size can't be smaller than the number of element already in the stack"
            self.__size = size
        else:
            self.__size = len(self.__items)


    def __repr__(self):
        #return str(self.__items)
        content = f"stack size: ({len(self.__items)} out of {self.__size}) >>> "
        # for i in range(-1, -1 - len(self.__items), -1):
        #     content += f"#{self.__items[i]}\t"
        content += str(self.__items[::-1])
        return content

    def __len__(self):
        return len(self.__items)




def test():
    stack = Stack(5)

    print(stack)
    print("stack.is_empty() = ", stack.is_empty())
    print("stack.is_full() = ", stack.is_full())

    try:
        print(stack.pop())
    except Exception as e:
        print("Error: ", e)

    try:
        print(stack.top())
    except Exception as e:
        print("Error: ", e)


    for i in range(5):
        stack.push(i)

    print(stack)
    print("stack.is_empty() = ",stack.is_empty())
    print("stack.is_full() = ",stack.is_full())

    print("stack.pop() = ",stack.pop())
    print(stack)
    print("stack.is_empty() = ", stack.is_empty())
    print("stack.is_full() = ", stack.is_full())

    try:
        stack.push("hello")
        print(stack)
        stack.push("world")
        print(stack)
    except Exception as e:
        print("Error: ",e)

    print(stack)
    stack.resize(6)
    stack.push("world")
    print(stack)


    try:
        stack.push("war")
    except Exception as e:
        print("Error: ",e)
    print(stack)
    try:
        stack.resize(1)
    except Exception as e:
        print("Error: ",e)

    for i in range(3):
        print(stack.pop())

    stack.resize(3)

    print(stack)
    try:
        stack.push("eroor")
    except Exception as e:
        print("Error: ",e)
    print("stack.is_empty() = ", stack.is_empty())
    print("stack.is_full() = ", stack.is_full())


if __name__ == '__main__':
    test()