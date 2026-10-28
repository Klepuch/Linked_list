class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reorder_list(head):
    if head is None or head.next is None:
        return

    # 1) Середина списку
    slow = head
    fast = head
    while fast.next is not None and fast.next.next is not None:
        slow = slow.next
        fast = fast.next.next

    # 2) Розвертаємо другу половину і відрізаємо її від першої
    second = slow.next
    slow.next = None
    prev = None
    while second is not None:
        nxt = second.next
        second.next = prev
        prev = second
        second = nxt
    second = prev

    # 3) Зшиваємо: L0 -> Ln -> L1 -> Ln-1 -> ...
    first = head
    while second is not None:
        first_next = first.next
        second_next = second.next
        first.next = second
        second.next = first_next
        first = first_next
        second = second_next


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
    head = build_list(values)
    reorder_list(head)
    result = to_list(head)
    print(f"Вхід: head = {values}")
    print(f"Вихід:     {result}")
    print(f"Очікувано: {expected}")
    print("OK" if result == expected else "ПОМИЛКА")
    print()


if __name__ == "__main__":
    check([1, 2, 3, 4], [1, 4, 2, 3])
    check([1, 2, 3, 4, 5], [1, 5, 2, 4, 3])
    check([1], [1])
