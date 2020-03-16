# 노드
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# 단일 연결 리스트
class SingleLinkedList:
    def __init__(self, data):
        new_node = Node(data)
        self.head = new_node
        self.list_size = 1

    def insertFirst(self,data):
        new_node = Node(data)       # 새 데이터 저장
        temp_node = self.head       # 기존 헤드 저장
        self.head = new_node        # 헤드에 새 데이터 저장
        self.head.next = temp_node  # 다음에 기존 데이터 저장

        self.list_size += 1

    def selectNode(self,num):
        if self.list_size<num:
            return                  # 밖에거 조사 대비용
        
        node = self.head
        count = 0
        while count<num:
            node = node.next        # 계속 다음걸 찾는다
            count += 1              # 카운트가 num이랑 같아질 때까지
        return node

    def insertMiddle(self,num,data):
        if self.head.next == None:  # 헤더가 만들어진 직후 이 메서드를 사용 할 때
            insertLast(data)
            return
        
        node = self.selectNode(num) # 노드 선택
        new_node = Node(data)
        temp_node = node.next
        node.next = new_node
        new_node.next = temp_node
        self.list_size += 1

    def insertLast(self,data):
        node = self.head
        while True:
            if node.next == None:
                break
            node = node.next
        
        new_node = Node(data)
        node.next = new_node
        self.list_size += 1

    def DeleteNode(self,num):
        if self.list_size<1:
            return
        elif self.list_size<num:
            return

        if num == 0:
            self.DeleteHead()
            return
        node = self.selectNode(num-1)
        node.next=node.next.next

        del_node = node.next
        del del_node

