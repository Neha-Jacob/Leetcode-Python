"""
# Group Anagrams

Given an array of strings strs, group all anagrams together into sublists.
You may return the output in any order.

An anagram is a string that contains the exact same characters as another
string, but the order of the characters can be different.

## Example 1

```text
Input: strs = ["act","pots","tops","cat","stop","hat"]

Output: [["hat"],["act", "cat"],["stop", "pots", "tops"]]
```

## Example 2

```text
Input: strs = ["x"]

Output: [["x"]]
```

## Example 3

```text
Input: strs = [""]

Output: [[""]]
```

## Constraints

- 1 <= strs.length <= 10000.
- 0 <= strs[i].length <= 100
- strs[i] is made up of lowercase English letters.

## Topics

- Array
- Hash Table
- String
- Sorting
"""

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sorts = {}
        for word in strs:
            key = "".join(sorted(word))
            if key not in sorts:
                sorts[key] = []
            sorts[key].append(word)
        new_list = []
        for value in sorts.values():
            new_list.append(value)
        return new_list
