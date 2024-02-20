from llist import LList, Node, append


def length(lst):
    """return the length of a finite linked list"""
    count = 0
    current = lst.head
    while current:
        count += 1
        current = current.next
    print("Length is", end=" ")
    return count

    # delete this line when you add your code


def llprint(lst):
    """print a finite linked list"""
    Message = ""
    current = lst.head
    if current is None:
        Message = "The list is empty"
    else:
        Message = "The Printed List is: "
        while current:
            Message = Message + str(current.val) + ", "
            current = current.next
    return Message


if __name__ == "__main__":

    # delete this line when you add your code below

    #

    llist = LList()
    append(llist, Node(17))
    append(llist, Node(100))
    print("List with 2 elements: 17 and 100")
    print(length(llist))
    print(llprint(llist))

    print("Empty List Example:")
    empty_list = LList()
    print(length(empty_list))
    print(llprint(empty_list))

    #
