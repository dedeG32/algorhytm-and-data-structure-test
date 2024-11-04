class Single_linked_list():
    class Node():
        def __init__(self, data, next_node=None):
            self.data = data
            self.next = next_node

        def __str__(self):
            return str(self.data)

        def __repr__(self):
            return str(self.data)

    def __init__(self):
        self.__head = None
        self.__tail = None
        self.__lenght = 0
        self.__node = None
        self.__idx = 0
        #self.size

    def chage_node(self, value = any) -> None:
        self.__node.data = value
    def add_node(self, new_data: any) -> None:
        """
        Adds a new node to end of the linked list
        :param new_data: the value that the node holds. Can be any.
        :return:
        """
        if self.__head is None:
            self.__head = self.Node(new_data)
            self.__node = self.__head
            self.__tail = self.__head
            self.__lenght += 1
            return
        self.__tail.next = self.Node(new_data)
        self.__tail = self.__tail.next
        self.__lenght += 1

    def next(self, skip_number= 1) -> any:
        """
        Move to the next node and return it value
        :param skip_number: Number of node to skip (min = 1, max = len(linked_list) - 1 - linked_list.index())
        :return: current node data
        """
        #
        assert skip_number >= 1, "Invalid skip number (must be greater than 1)"

        if self.__idx + skip_number  >= self.__lenght:
            raise IndexError("Out of range")

        for _ in range(skip_number):
            self.__node= self.__node.next
            self.__idx += 1

        return self.__node.data
    def curent_node(self) :
        return self.__node.data

    def __len__(self) -> int:
        return self.__lenght

    # def __repr__(self):
    #     list = []
    #     curent_node = self.curent_node
    #     self.curent_node = self.head
    #     curent_index = self.index
    #     self.index = 0
    #     list.append(str(self.curent_node))
    #     for _ in range(self.lenght -1):
    #         self.next()
    #         if self.curent_node is curent_node:
    #             list.append(f"<<{self.curent_node}>>")
    #         else:
    #             list.append(str(self.curent_node))

    def __iter__(self) -> any:
        pass

    def __next__(self) -> any:
        pass

    def index(self):
        return self.__idx

    def __repr__(self) -> str:
        """
        :return: Returns a string representation of the singly linked list
        """
        content = ''
        curent_node = self.__node
        self.__node = self.__head
        curent_index = self.__idx
        self.__idx = 0
        content += str(self.__node)
        for _ in range(self.__lenght - 1):
            content += " >> "
            self.next()
            if self.__node is curent_node:
                content += "*" + str(self.__node) + "*"
            else:
                content += str(self.__node)

        self.__node = curent_node
        self.__idx = curent_index
        return content




linked = Single_linked_list()
linked.add_node('Mohamed')
linked.add_node(1)
linked.add_node(2)
linked.add_node(3)
linked.add_node("vovador")

for node in range(len(linked)-1):
    print(linked.curent_node())
    print(linked.next())


print(linked)
