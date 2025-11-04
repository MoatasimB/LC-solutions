class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        class MinHeap:
            def __init__(self):
                self.heap = []
            
            def __len__(self):
                return len(self.heap)
            
            def parent(self, idx):
                return (idx - 1) // 2 if idx > 0 else None
            def left(self, idx):
                return (2 * idx + 1) if (2 * idx + 1) < len(self.heap) else None
            def right(self, idx):
                return (2 * idx + 2) if (2 * idx + 2) < len(self.heap) else None
            
            def pop_heap(self):
                if  len(self.heap) == 0:
                    return None
                min_el = self.heap[0]

                last_el = self.heap.pop()

                if len(self.heap) > 0:
                    self.heap[0] = last_el
                    self.bubble_down(0)

                return min_el
            def peek(self):
                return self.heap[0]
            def insert_heap(self, val):
                self.heap.append(val)
                self.bubble_up(len(self.heap) - 1)
            
            def bubble_up(self, idx):
                
                parent_idx = self.parent(idx)

                while parent_idx is not None and self.heap[parent_idx] > self.heap[idx]:
                    self.heap[idx], self.heap[parent_idx] = self.heap[parent_idx], self.heap[idx]
                    idx = parent_idx
                    parent_idx = self.parent(idx)
            
            def bubble_down(self, idx):
                while True:
                    min_idx = idx

                    left_idx = self.left(idx)
                    right_idx = self.right(idx)

                    if left_idx and self.heap[left_idx] < self.heap[min_idx]:
                        min_idx = left_idx
                    
                    if right_idx and self.heap[right_idx] < self.heap[min_idx]:
                        min_idx = right_idx
                    
                    if min_idx == idx:
                        break
                    
                    self.heap[idx], self.heap[min_idx] = self.heap[min_idx], self.heap[idx]

                    idx = min_idx
                
        
        p = MinHeap()

        for i in range(len(nums)):
            p.insert_heap(nums[i])

            if len(p) > k:
                p.pop_heap()
        
        return p.peek()

