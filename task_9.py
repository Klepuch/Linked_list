class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def partition(head, x):
    less_dummy = ListNode()
    greater_dummy = ListNode()
    less = less_dummy
    greater = greater_dummy

    while head is not None:
        if head.val < x:
            less.next = head
            less = less.next
        else:
            greater.next = head
            greater = greater.next
        head = head.next

    greater.next = None              # кінець другого списку
    less.next = greater_dummy.next   # з'єднуємо дві частини

    return less_dummy.next


# ---------- Допоміжні функції ----------

def build_list(values):
    dummy = ListNode()
    tail = dummy
    for v in values:
        tail.next = ListNode(v)
        tail = tail.next
    return dummy.next


def to_list(head):
    result = []
    while head is not None:
        result.append(head.val)
        head = head.next
    return result


def check(values, x, expected):
    result = to_list(partition(build_list(values), x))
    print(f"Вхід: head = {values}, x = {x}")
    print(f"Вихід:     {result}")
    print(f"Очікувано: {expected}")
    print("OK" if result == expected else "ПОМИЛКА")
    print()


if __name__ == "__main__":
    check([1, 4, 3, 2, 5, 2], 3, [1, 2, 2, 4, 3, 5])
    check([2, 1], 2, [1, 2])
    check([], 0, [])
