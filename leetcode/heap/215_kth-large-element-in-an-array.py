class heap:
    def __init__(self):
        self.items = [None]

    def __len__(self):
        return len(self.items) - 1

    def _perlocate_up(self):
        cur = len(self)  # 현재 힙의 길이- 가장 끝에 있는 노드부터 실행
        parent = cur // 2  # 부모를 찾기 위해 반띵
        while parent > 0:  # 부모가 1 이상일때까지 진행
            if self.items[cur] > self.items[parent]:  # 만약 부모 값이 작다면 자리 바꿔줌
                self.items[cur], self.items[parent] = self.items[parent], self.items[cur]
            cur = parent  # 다음 부모로 올라가기 위해 현재 노드를 다음 부모로 설정한다.
            parent = cur // 2  # 상위로 올라간다

    def _perlocate_down(self, k):
        big = k
        l = 2 * k
        r = 2 * k + 1
        if l <= len(self) and self.items[l] > self.items[big]:
            big = l
        if r <= len(self) and self.items[r] > self.items[big]:
            big = r
        if big != k:
            self.items[k], self.items[big] = self.items[big], self.items[k]
            self._perlocate_down(big)

    def insert(self, k):
        self.items.append(k)
        self._perlocate_up()

    def extract(self):
        if len(self) < 1:
            return None
        root = self.items[1]
        self.items[1] = self.items[-1]
        self.items.pop()
        self._perlocate_down(1)
        return root
