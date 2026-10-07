
def sample_02_lru_cache():
    title(2, "LRU Cache")
    cache = LRUCache(2)
    cache.put("a", 1)
    cache.put("b", 2)
    cache.get("a")          # 'a' becomes most recent
    cache.put("c", 3)       # evicts 'b'
    print("get a:", cache.get("a"), "| get b:", cache.get("b"), "| get c:", cache.get("c"))