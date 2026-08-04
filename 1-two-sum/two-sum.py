class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        hash_map=dict()
        for i in range(len(nums)):
            this=target-nums[i]
            if this in hash_map.keys():
                return [hash_map[this],i]
                break
            hash_map[nums[i]]=i


"""
        ### `seen` is a hash set

When you insert `55` into a Python `set`, Python computes its hash value.

For integers, the hash is essentially the integer itself (with a few implementation details):

```python
hash(55) = 55
```

Suppose the hash table has **8 buckets**. Python determines the bucket by taking the hash modulo the number of buckets:

```python
55 % 8 = 7
```

So `55` is stored in **bucket 7**.

```text
Bucket 0
Bucket 1
Bucket 2
Bucket 3
Bucket 4
Bucket 5
Bucket 6
Bucket 7 --> 55
```

Now, when Python evaluates:

```python
55 in seen
```

it computes the **same hash** again:

```python
hash(55) = 55
55 % 8 = 7
```

Instead of checking every element in the set, Python **jumps directly to bucket 7** and looks there.

This direct access is why membership testing (`target in seen`) has an **average time complexity of O(1)**.

If you'd like, I can also make this explanation more visual with a real hash table example containing collisions.

        
        """