class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverse_k_group(head, k):
    dummy = ListNode(0, head)
    group_prev = dummy

    while True:
        # Шукаємо k-й вузол від group_prev
        kth = group_prev
        for _ in range(k):
            kth = kth.next
            if kth is None:
                return dummy.next  # залишилось менше k вузлів

        group_next = kth.next

        # Розвертаємо групу: перший вузол групи має вказувати на group_next
        prev = group_next
        current = group_prev.next
        while current is not group_next:
            nxt = current.next
            current.next = prev
            prev = current
            current = nxt

        # Вшиваємо розвернуту групу
        old_first = group_prev.next   # після розвороту став останнім
        group_prev.next = kth         # kth тепер перший у групі
        group_prev = old_first


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


def check(values, k, expected):
    result = to_list(reverse_k_group(build_list(values), k))
    print(f"Вхід: head = {values}, k = {k}")
    print(f"Вихід:     {result}")
    print(f"Очікувано: {expected}")
    print("OK" if result == expected else "ПОМИЛКА")
    print()


if __name__ == "__main__":
    check([1, 2, 3, 4, 5], 2, [2, 1, 4, 3, 5])
    check([1, 2, 3, 4, 5], 3, [3, 2, 1, 4, 5])
    check([1, 2, 3, 4, 5], 1, [1, 2, 3, 4, 5])
    check([1, 2, 3, 4], 4, [4, 3, 2, 1])
