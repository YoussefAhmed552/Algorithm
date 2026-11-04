import heapq
from collections import Counter

def top_k_frequent(words, k):
    counts = Counter(words)
    heap = []
    for word, count in counts.items():
        heapq.heappush(heap, (count, word))
        if len(heap) > k:
            heapq.heappop(heap)
    
    result = []
    while heap:
        result.append(heapq.heappop(heap)[1])
    return result[::-1]

text_words = ["to", "be", "or", "not", "to", "be"]
print("Top 2 words:", top_k_frequent(text_words, 2))
