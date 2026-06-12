#list[start:stop:step]
# DS     -  Synta - Changable - Java Cousin
# List   - []     - Mutable   - Like ArrarList
# truple - ()     - immutable - immutable arrary / record-ish
# set    - {}     - Mutable   - Hashset
# dict   - {k:v}  - Mutable   - Hashset

nums = [10, 20, 30, 40, 50, 60]

print(nums[1:5])
print(nums[:-3:-1])
print(nums[::-1])

word = "enginner"
print(f"reverse word = {word[::-1]}")
print(f"first 4 letter = {word[:5]}")

my_list=  [1, 1, 2, 3, 3, 3]
print(set(my_list))