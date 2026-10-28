class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def delete_duplicates(head):
    current = head

    while current is not None and current.next is not None:
        if current.next.val == current.val:
            current.next = current.next.next  # видаляємо дублікат
        else:
            current = current.next

    return head


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


def check(values, expected):
    result = to_list(delete_duplicates(build_list(values)))
    print(f"Вхід: head = {values}")
    print(f"Вихід:     {result}")
    print(f"Очікувано: {expected}")
    print("OK" if result == expected else "ПОМИЛКА")
    print()


if __name__ == "__main__":
    check([1, 1, 2], [1, 2])
    check([1, 1, 2, 3, 3], [1, 2, 3])
    check([], [])
