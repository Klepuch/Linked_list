class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def double_it(head):
    # Якщо старша цифра >= 5, число стане довшим на одну цифру
    if head.val > 4:
        head = ListNode(0, head)

    current = head
    while current is not None:
        current.val = (current.val * 2) % 10
        if current.next is not None and current.next.val > 4:
            current.val += 1  # перенесення з молодшого розряду
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
    result = to_list(double_it(build_list(values)))
    print(f"Вхід: head = {values}")
    print(f"Вихід:     {result}")
    print(f"Очікувано: {expected}")
    print("OK" if result == expected else "ПОМИЛКА")
    print()


if __name__ == "__main__":
    check([1, 8, 9], [3, 7, 8])
    check([9, 9, 9], [1, 9, 9, 8])
    check([0], [0])
