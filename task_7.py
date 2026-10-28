class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def merge_two(a, b):
    dummy = ListNode()
    tail = dummy
    while a is not None and b is not None:
        if a.val <= b.val:
            tail.next = a
            a = a.next
        else:
            tail.next = b
            b = b.next
        tail = tail.next
    tail.next = a if a is not None else b
    return dummy.next


def merge_k_lists(lists):
    if not lists:
        return None

    lists = list(lists)
    step = 1
    # На кожному кроці зливаємо пари списків, що стоять на відстані step
    while step < len(lists):
        for i in range(0, len(lists) - step, step * 2):
            lists[i] = merge_two(lists[i], lists[i + step])
        step *= 2

    return lists[0]


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


def check(values_lists, expected):
    heads = [build_list(values) for values in values_lists]
    result = to_list(merge_k_lists(heads))
    print(f"Вхід: lists = {values_lists}")
    print(f"Вихід:     {result}")
    print(f"Очікувано: {expected}")
    print("OK" if result == expected else "ПОМИЛКА")
    print()


if __name__ == "__main__":
    check([[1, 4, 5], [1, 3, 4], [2, 6]], [1, 1, 2, 3, 4, 4, 5, 6])
    check([], [])
    check([[]], [])
