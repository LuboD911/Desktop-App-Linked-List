def data_type_validation(data):
    if type(data) is not int or data < 0:
        raise ValueError("Please enter a number.")


class Node:

    def __init__(self, data):
        self.data = data
        self.next_node = None


class LinkedList:

    def __init__(self):
        self.head = None
        self.num_of_nodes = 0


    def insert(self, data):

        data_type_validation(data)

        self.num_of_nodes = self.num_of_nodes + 1
        new_node = Node(data)

        if not self.head:
            self.head = new_node
        else:
            actual_node = self.head

            while actual_node.next_node is not None:
                actual_node = actual_node.next_node

            actual_node.next_node = new_node


    def insert_left(self, data):

        data_type_validation(data)

        self.num_of_nodes = self.num_of_nodes + 1
        new_node = Node(data)

        if not self.head:
            self.head = new_node
        else:
            new_node.next_node = self.head
            self.head = new_node


    def size_of_list(self):
        return self.num_of_nodes

    def traverse(self):

        actual_node = self.head
        output = ''
        while actual_node is not None:
            # print(actual_node.data, end=" ")
            output += str(actual_node.data) + ' '
            actual_node = actual_node.next_node

        print(output)
        return output

    def remove(self, data):

        if self.head is None:
            return

        actual_node = self.head

        previous_node = None

        while actual_node is not None and actual_node.data != data:
            previous_node = actual_node
            actual_node = actual_node.next_node

        if actual_node is None:
            return

        self.num_of_nodes -= 1
        if previous_node is None:
            self.head = actual_node.next_node
        else:
            previous_node.next_node = actual_node.next_node

    def return_M(self, m):

        data_type_validation(m)

        if m > self.num_of_nodes-1 or m < 0:
            raise ValueError("Please enter a valid M-number. Тhe number cannot be negative or greater than the length of the list - 1 ")

        n = self.num_of_nodes - m

        if self.head is None:
            return

        actual_node = self.head

        i = 1
        while i < n:
            actual_node = actual_node.next_node
            i += 1

        return actual_node.data
