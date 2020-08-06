#1 def is_odd(num):
# 	return num % 2 != 0


# print(is_odd(-50))

#2 def distance_home(lst):
#     return abs(sum(lst))

# print(distance_home([2, 4, 2, 5]))
# print(distance_home([-1, -4, -3, -2]) )
# print(distance_home([3, 4, -5, -2]))

#3 def zip_it(women, men):
#     if len(women) == len(men):
#         return list(zip(women,men))
#     return "sizes don't match"
    
# # print(zip_it(['Elise', 'Mary'], ['John', 'Rick'])) 
# print(zip_it(['Elise', 'Mary'], ['John', 'Rick'])) 

#4 def is_equal(num1, num2):
#     if type(num1) != int or type(num2) != int:
#         return False
#     return num1 == num2
     
    

# print(is_equal("1",5))

#5 def find_the_falsehoods(lst):
#     return [item for item in lst if not item]

# print(find_the_falsehoods([0,1,2,3]))

#6 def is_potential_friend(set1, set2):
#     return len(set1.intersection(set2)) >=2 or set1 == set2

# print(is_potential_friend(
# 	{"films"},
# 	{"films"}
# ))

#7 def twoSum(nums, target):
#     for i in range(len(nums)):
#         if nums[i] + nums[i+1] == target:
#             return [i,i+1]
    
    
# print(twoSum([2,7,11,15],9))
# print(twoSum([3,2,3],6))
# a = [1, 2, 3]
# b = [3, 2, 1]

#8 def compareTriplets(a, b):
#     scores = [0,0]
#     for i in range(len(a)):
#         if a[i]>b[i]:
#             scores[0]+=1
#         elif b[i]>a[i]:
#             scores[1]+=1
#     return scores
        
# print(compareTriplets(a,b))
# nested_list = [[1,2,3],[4,5,6],[9,8,9]]

#9 def diagonalDifference(arr):
#     lr = rl = 0
#     for i in range(len(arr)):
#         lr +=arr[i][i]
#         rl +=arr[i][len(arr)-1-i-1]
#     return abs(lr-rl)
        
        
        
# print(diagonalDifference(nested_list))

# 10 def has23(nums):
#   return any(num for num in nums if num == 2 or num == 3)

# print(has23([2,5]))

# 11 def paths(n):
#   if n == 1:
#       return n
#   else:
#       return n * paths(n-1)

# print(paths(4))

# 12 def list_to_string(lst):
#   list_to_join = [str(val) for val in lst]
#   return ''.join(list_to_join)

# print(list_to_string([1,2]))

# 13 def how_many_stickers(n):
#   return 6 * n **2

# print(how_many_stickers(2))

# 14 def skip_the_sugar(drinks):
#       return [drink for drink in drinks if drink not in ['cola', 'fanta']]
  
  
# print(skip_the_sugar(["fanta", "cola", "water"]))

# 15 def area_shape(base, height, shape):
#   if shape =='triangle':
#     return base * height * 0.5
#   return base * height

# 16 def match_houses(step):
#       if step > 0:
#         return 1 + step * 5
#       return 0

# print(match_houses(0))

# 17 def match_houses(step):
#   return step*5+1 if step else 0

# (is_first_superior([1, 2, 3, 4], [1, 2, 3, 3]), True)
# 18 def is_first_superior(lst1, lst2):
#   return False if lst1 == lst2 else lst1 > lst2
      
  

  
# print(is_first_superior([True, 10, 'zebra'], [True, 10, 'ant']))
# print(is_first_superior(['a', 'b', 'c'], ['a', 'd', 'c']))
# print(is_first_superior([1, 2, 3, 4], [1, 2, 3, 3]))


# 19 def check_all_even(lst):
#   return all(x % 2 == 0 for x in lst)

# check_all_even([1, 2, 3, 4])

# 20
# countdown(5) ➞ [5, 4, 3, 2, 1, 0]

# def countdown(start):
#       return [num for num in range(start+1)][::-1]
    
# def countdown(start):
#     	return [i for i in range(start,-1,-1)]

# print(countdown(5))


#21

# def test_jackpot(result):
# 	return len(set(result)) == 1

# print(test_jackpot(['@', '@', '@', '#']))


# def reverse(txt):
# 	return txt[::-1]
 
 
# print(reverse("Think different."))
# , ".tnereffid knihT"

#22
# get_triangle_type([2, 3, 4]), "scalene")

# def get_triangle_type(lst):
    	
# 	if len(lst) != 3:
# 		return 'not a triangle'
# 	a,b,c = tuple(lst)
# 	if len(set(lst)) == 1:
# 		return 'equilateral'
# 	elif a!=b and a!=c and b !=c:
# 		return 'scalene'
# 	else:
# 		return 'isosceles'


# def get_triangle_type(lst):
#     if len(lst) == 3:
# 		  return ['equilateral', 'isosceles', 'scalene'][len(set(lst)) - 1]
#     return 'not a triangle'
  
  
# print(get_triangle_type([2,3,4]))

# def reverse_list(num):
#     return [int(num) for num in str(num)][::-1]

# print(reverse_list(1485979))

# def filter_digit_length(lst, num):
#     return [n for n in lst if len(str(n)) == num]

#23
# def filter_digit_length(lst,num):
#     return list(filter(lambda x: len(str(x))==num, lst))



# print(filter_digit_length([88, 232, 4, 9721, 555], 3))    

#24
# minimum_removals([1, 2, 3, 4, 5]) ➞ 1
# def minimum_removals(lst):
#     return 0 if sum(num for num in lst) % 2 == 0 else 1
    
    
# def minimum_removals(lst):
#     	return sum(lst) % 2     
    
#   return False if lst1 == lst2 else lst1 > lst2


# print(minimum_removals([5, 7, 9, 11]))

#25
# not_not_not(1, True) ➞ False
# def not_not_not(n, b):
#     return b if n % 2 ==0 else not b


# print(not_not_not(13, True))

#26
# city_facts({
#   name: "Paris",
#   population: "2,140,526",
#   continent: "Europe"
# }) 
#  "Paris has a population of 2,140,526 and is situated in Europe"

# def city_facts(city):
#     return '{} has a population of {} and is situated in {}'.format(city['name'], city['population'],city['continent'])
    
# print(city_facts({'name': 'Manila', 'population': '1,780,148', 'continent': 'Asia'})) 
    
    # 'Manila has a population of 1,780,148 and is situated in Asia'
    
# 27
# owofied("I'm gonna ride 'til I can't no more")
# ➞ "I'm gonna rwidwe 'twil I can't no morwe owo"


# def owofied(sentence):
#     return sentence.replace('i','wi').replace('e','we') + ' owo'
    
    
# print(owofied("I'm gonna ride 'til I can't no more"))
# , "I'm gonna rwidwe 'twil I can't no morwe owo"

#28
# def retrieve_major(semver):
#     	return semver.split('.')[0]

# def retrieve_minor(semver):
# 	return semver.split('.')[1]	

# def retrieve_patch(semver):
# 	return semver.split('.')[2]

#29
# def hurdle_jump(hurdles, jump_height):
#     return all(num<= jump_height for num in hurdles)

# print(hurdle_jump([1, 2, 3, 4, 4], 5))

#30
# def rev(n):
#     return str(abs(n))[::-1]
    
    
# print(rev(215))
# (rev(215), "512")

#31
# def calc_kinetic_energy(m, v):
#     return round((1/2)*m*(v**2))

# print(calc_kinetic_energy(60,3))
# calc_kinetic_energy(60, 3) 270

#32
# remove_first_last("hello") ➞ "ell"

# def remove_first_last(txt):
#     return txt if len(txt) <=2 else txt[1:-1]


    
# print(remove_first_last("help"))

# #33
# def join_path(portion1, portion2):
#     # if portion1[-1] != '/' and portion2[0] !='/':
#     #     return '{}/{}'.format(portion1,portion2)
#     # elif portion1[-1] == '/' and portion2[0] != '/':
#     #     return '{}{}'.format(portion1,portion2)
#     # elif portion1[-1] != '/' and portion2[0] == '/':
#     #     return '{}{}'.format(portion1,portion2)
#     # elif portion1[-1] == '/' and portion2[0] == '/':
#     #     return '{}{}'.format(portion1[0:-1],portion2)
    
    
#     return '/'.join((portion1.rstrip('/'), portion2.lstrip('/')))
#     # return portion1.replace('/','') + '/' +portion2.replace('/','')
    
# print(join_path("portion1", "/portion2"))

#34
# def subset(lst1, lst2):
#     return set(lst1).issubset(lst2)


# print(subset([1, 3], [1, 3, 3, 5]))

#35

# def repeat(item, times):
#     # return [item]*times
#     # with list comprehension
#     return [item for i in range(times)]

# print(repeat("edabit", 3))


#36
# def has_hidden_fee(prices, t):
#     return sum(int(item[1:]) for item in prices) < int(t[1:])
    
# # has_hidden_fee(["$2", "$4", "$1", "$8"], "$15") ➞ False

# print(has_hidden_fee(["$25", "$6", "$19", "$9", "$32", "$15", "$10", "$9", "$7", "$8", "$37", "$23", "$18"], "$232"))
# # print(has_hidden_fee(["$2", "$4", "$1", "$8"], "$15"))
# # print(has_hidden_fee(["$1", "$2", "$3"], "$6"))
# # print(has_hidden_fee(["$31", "$30", "$21", "$12", "$10", "$38", "$42", "$27", "$51"], "$297"))

#37
def to_array(txt):
    return txt.split(', ') if txt else []
    
print(to_array("watermelon, raspberry, orange"))
print(to_array("x1, x2, x3, x4, x5"))