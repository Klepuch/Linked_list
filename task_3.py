class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def has_cycle(head):
    slow = head
    fast = head

    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next
        if slow is fast:
            return True

    return False


# ---------- Допоміжні функції ----------

def build_list_with_cycle(values, pos):
    """Створює список; якщо pos >= 0, хвіст з'єднується з вузлом pos."""
    if not values:
        return None
    nodes = [ListNode(v) for v in values]
    for i in range(len(nodes) - 1):
        nodes[i].next = nodes[i + 1]
    if pos >= 0:
        nodes[-1].next = nodes[pos]
    return nodes[0]


def check(values, pos, expected):
    result = has_cycle(build_list_with_cycle(values, pos))
    print(f"Вхід: head = {values}, pos = {pos}")
    print(f"Вихід:     {result}")
    print(f"Очікувано: {expected}")
    print("OK" if result == expected else "ПОМИЛКА")
    print()


if __name__ == "__main__":
    check([3, 2, 0, -4], 1, True)
    check([1, 2], 0, True)
    check([1], -1, False)
    check([], -1, False)
