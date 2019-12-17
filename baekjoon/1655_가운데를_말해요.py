import heapq

nums1 = []
nums2 = []
res = []
# nums1 == nums2 or nums1 == nums2+1
for _ in range(int(input())):
    x = int(input())
    # if not nums1 and not nums2:
    #     heapq.heappush(nums1, (-x, x))
    # else:
    #     if nums1[0][1] >= x:
    #         heapq.heappush(nums1, (-x, x))
    #     else:
    #         heapq.heappush(nums2, x)
    #     top1 = len(nums1)
    #     top2 = len(nums2)
    #     if top1 != top2 and top1 != top2 + 1:
    #         if top1 > top2:
    #             num = heapq.heappop(nums1)[1]
    #             heapq.heappush(nums2, num)
    #         else:
    #             num = heapq.heappop(nums2)
    #             heapq.heappush(nums1, (-num, num))
    if not nums1 or -nums1[0] >= x:
        heapq.heappush(nums1, -x)
        if len(nums1) > len(nums2) + 1:
            heapq.heappush(nums2, -heapq.heappop(nums1))
    else:
        heapq.heappush(nums2, x)
        if len(nums1) <= len(nums2) - 1:
            heapq.heappush(nums1, -heapq.heappop(nums2))
    res.append(-nums1[0])
print(' '.join(list(map(str, res))))
