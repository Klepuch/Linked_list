class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def merge_two_lists(list1, list2):
    dummy = ListNode()
    tail = dummy

    while list1 is not None and list2 is not None:
        if list1.val <= list2.val:
            tail.next = list1
            list1 = list1.next
        else:
            tail.next = list2
            list2 = list2.next
        tail = tail.next

    # Приєднуємо залишок того списку, який ще не закінчився
    tail.next = list1 if list1 is not None else list2

    return dummy.next


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


def check(values1, values2, expected):
    result = to_list(merge_two_lists(build_list(values1), build_list(values2)))
    print(f"Вхід: list1 = {values1}, list2 = {values2}")
    print(f"Вихід:     {result}")
    print(f"Очікувано: {expected}")
    print("OK" if result == expected else "ПОМИЛКА")
    print()


if __name__ == "__main__":
    check([1, 2, 4], [1, 3, 4], [1, 1, 2, 3, 4, 4])
    check([], [], [])
    check([], [0], [0])
