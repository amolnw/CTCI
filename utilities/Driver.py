from utilities.LinkedList import LinkedList


def test_linkedList():
    ll = LinkedList()
    ll.add_element(1)
    ll.add_element(3)
    ll.add_element(5)
    print(ll)
    ll.remove_element(3)
    print(ll)


def main():
    test_linkedList()


if __name__ == "__main__":
    main()

