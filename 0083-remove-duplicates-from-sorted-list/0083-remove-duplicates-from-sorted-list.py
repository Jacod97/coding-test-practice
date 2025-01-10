# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        ln = ListNode(0)
        answer = ln
        prev = None
        while head:
            if head.val != prev:  # 이전 값과 다르면 중복이 아님
                answer.next = head  # answer에 현재 노드 추가
                answer = answer.next  # answer를 다음 노드로
                prev = head.val  # prev를 현재 값으로 업데이트
            head = head.next  # 다음 노드로

        answer.next = None  
        return ln.next  