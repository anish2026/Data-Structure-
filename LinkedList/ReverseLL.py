    def reverseList(self, head):
        prev = None
        while head:
            head.next,head,prev =  prev,head.next,head
        return prev  
