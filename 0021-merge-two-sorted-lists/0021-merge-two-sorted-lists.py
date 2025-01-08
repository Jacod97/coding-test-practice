# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # 더미 노드 생성 (결과 리스트의 시작점)
        dummy = ListNode(-1)
        current = dummy

        # 두 리스트를 순회하며 병합
        while list1 and list2:
            if list1.val <= list2.val:
                current.next = list1  # list1의 노드를 추가
                list1 = list1.next   # list1 포인터 이동
            else:
                current.next = list2  # list2의 노드를 추가
                list2 = list2.next   # list2 포인터 이동
            current = current.next   # 결과 리스트 포인터 이동

        # 남아 있는 노드 처리
        if list1:
            current.next = list1
        if list2:
            current.next = list2

        return dummy.next  # 더미 노드 다음 노드가 결과 리스트의 시작점