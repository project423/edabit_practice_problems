# def is_odd(num):
# 	return num % 2 != 0


# print(is_odd(-50))

# def distance_home(lst):
#     return abs(sum(lst))

# print(distance_home([2, 4, 2, 5]))
# print(distance_home([-1, -4, -3, -2]) )
# print(distance_home([3, 4, -5, -2]))

# def zip_it(women, men):
#     if len(women) == len(men):
#         return list(zip(women,men))
#     return "sizes don't match"
    
# # print(zip_it(['Elise', 'Mary'], ['John', 'Rick'])) 
# print(zip_it(['Elise', 'Mary'], ['John', 'Rick'])) 

# def is_equal(num1, num2):
#     if type(num1) != int or type(num2) != int:
#         return False
#     return num1 == num2
     
    

# print(is_equal("1",5))

# def find_the_falsehoods(lst):
#     return [item for item in lst if not item]

# print(find_the_falsehoods([0,1,2,3]))

# def is_potential_friend(set1, set2):
#     return len(set1.intersection(set2)) >=2 or set1 == set2

# print(is_potential_friend(
# 	{"films"},
# 	{"films"}
# ))

# def twoSum(nums, target):
#     for i in range(len(nums)):
#         if nums[i] + nums[i+1] == target:
#             return [i,i+1]
    
    
# print(twoSum([2,7,11,15],9))
# print(twoSum([3,2,3],6))
# a = [1, 2, 3]
# b = [3, 2, 1]

# def compareTriplets(a, b):
#     scores = [0,0]
#     for i in range(len(a)):
#         if a[i]>b[i]:
#             scores[0]+=1
#         elif b[i]>a[i]:
#             scores[1]+=1
#     return scores
        
# print(compareTriplets(a,b))
# nested_list = [[1,2,3],[4,5,6],[9,8,9]]

# def diagonalDifference(arr):
#     lr = rl = 0
#     for i in range(len(arr)):
#         lr +=arr[i][i]
#         rl +=arr[i][len(arr)-1-i-1]
#     return abs(lr-rl)
        
        
        
# print(diagonalDifference(nested_list))

# def has23(nums):
#   return any(num for num in nums if num == 2 or num == 3)

# print(has23([2,5]))

# def paths(n):
#   if n == 1:
#       return n
#   else:
#       return n * paths(n-1)

# print(paths(4))

# def list_to_string(lst):
#   list_to_join = [str(val) for val in lst]
#   return ''.join(list_to_join)

# print(list_to_string([1,2]))

# def how_many_stickers(n):
#   return 6 * n **2

# print(how_many_stickers(2))

# def skip_the_sugar(drinks):
#       return [drink for drink in drinks if drink not in ['cola', 'fanta']]
  
  
# print(skip_the_sugar(["fanta", "cola", "water"]))

# def area_shape(base, height, shape):
#   if shape =='triangle':
#     return base * height * 0.5
#   return base * height

# def match_houses(step):
#       if step > 0:
#         return 1 + step * 5
#       return 0

# print(match_houses(0))

# def match_houses(step):
#   return step*5+1 if step else 0