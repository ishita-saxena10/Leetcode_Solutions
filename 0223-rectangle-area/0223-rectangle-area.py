class Solution:
    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:
        overlap_x = overlap_y = 0
        if min(ax2, bx2) > max(ax1, bx1): overlap_x = min(ax2, bx2) - max(ax1, bx1)
        if min(ay2, by2) > max(ay1, by1): overlap_y = min(ay2, by2) - max(ay1, by1)
        
        return (ax2 - ax1) * (ay2 - ay1) + (bx2 - bx1) * (by2 - by1) - overlap_x * overlap_y