class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def delete_node(node):
    node.val = node.next.val
    node.next = node.next.next


# ---------- Допоміжні функції ----------

def build_list(values):
    dummy = ListNode()
    tail = dummy
    for v in values:
        tail.next = ListNode(v)
        tail = tail.next
    return dummy.next


def find_node(head, value):
    while head is not None and head.val != value:
        head = head.next
    return head


def to_list(head):
    result = []
    while head is not None:
        result.append(head.val)
        head = head.next
    return result


def check(values, node_value, expected):
    head = build_list(values)
    delete_node(find_node(head, node_value))
    result = to_list(head)
    print(f"Вхід: head = {values}, node = {node_value}")
    print(f"Вихід:     {result}")
    print(f"Очікувано: {expected}")
    print("OK" if result == expected else "ПОМИЛКА")
    print()


if __name__ == "__main__":
    check([4, 5, 1, 9], 5, [4, 1, 9])
    check([4, 5, 1, 9], 1, [4, 5, 9])
