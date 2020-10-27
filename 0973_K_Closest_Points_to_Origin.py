class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        new = [(pt[0] ** 2 + pt[1] ** 2, pt[0], pt[1]) for pt in points]
        new.sort(key=lambda x:x[0])
        return [[x, y] for _, x, y in new[:K]]
