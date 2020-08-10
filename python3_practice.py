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
# def to_array(txt):
#     return txt.split(', ') if txt else []
    
# print(to_array("watermelon, raspberry, orange"))
# print(to_array("x1, x2, x3, x4, x5"))

#38
# def get_filename(path):
#     return path.split('/')[-1]
    
# print(get_filename("C:/Projects/pil_tests/ascii/edabit.txt"))

#39

# def middle_earth(lst):
#     return abs(lst.index('Frodo')-lst.index('Sam')) == 1
    
    
# print(middle_earth(['Sam', 'Frodo', 'Gandalf']))

#40
# quarters, dimes, nickels, pennies.
# def change_enough(change, amount_due):
#     # total = change[0]*.25
#     # total += change[1]*.10
#     # total += change[2]*.5
#     # total +=change[3]*.01

# 	return sum([a*b for a, b in zip(change, values)]) >= amount_due
 
 
#41   
# Create a function that returns the total number of parameters passed in.
# number_args("a", "b", "c") ➞ 3

# def number_args(*args):
#     return len(args)


# print(number_args("a", "b", "c"))

#42 
# Write a function that stutters a word as if someone is struggling to read it. The first two letters are 
# repeated twice with an ellipsis ... 
# and space after each, and then the word is pronounced with a question mark ?.
# stutter("incredible") ➞ "in... in... incredible?"

# def stutter(word):
#     without f strings
#     return '{0}... {0}... {1}?'.format(word[:2], word)
#     return '{}... {}... {}?'.format(word[:2],word[:2],word)
    
# print(stutter('incredible'))

#43
# check_factors([2, 3, 4], 12) ➞ True
# Since 2, 3, and 4 are all factors of 12.

# check_factors([2, 3, 4], 12) ➞ True 
# def check_factors(factors, num):
#     return all(num % n == 0 for n in factors)

# print(check_factors([1,2, 3, 4], 12))

#44
# MultiplyByLength([2, 3, 1, 0]) ➞ [8, 12, 4, 0]
# def MultiplyByLength(arr):
#     return [n * len(arr) for n in arr]
#     # with map
#     return list (map(lambda x: x*len(arr), arr))

# print(MultiplyByLength([0]))

#45

# def is_valid(zip_code):
#     return zip_code.isdigit() and len(zip_code) == 5
    
    
# print(is_valid("853476"))

#45
# exists_higher([5, 3, 15, 22, 4], 10) ➞ True
# def exists_higher(lst, n):
#     return any(num >= n for num in lst)
#     # return max(lst) >= n if lst else False
    
# print(exists_higher([5, 3, 2, 4], 10))

#46
# def md_format(word, style):
#     # if style == 'b':
#     #     return '**{}**'.format(word)
#     # elif style == 'i':
#     #     return '_{}_'.format(word)
#     # elif style == 'c':
#     #     return '`{}`'.format(word)
#     # elif style == 's':
#     #     return '~~{}~~'.format(word)
#     markdown = {'b':'**', 'i':'_', 'c':'`', 's':'~~'}
#     return '{0}{1}{0}'.format(markdown[style], word)

# 47
# from math import pi
# def my_pi(n):
#     return 3 if n == 0 else round(pi,n)
    

# print(my_pi(3))

#48
# def get_extension(lst):
#     # return [i[-1] for i in [v.split('.') for v in lst]]
#     return [i.split(".")[1] for i in lst]
    
# print(get_extension(["project1.jpg", "project1.pdf", "project1.mp3"]))

#49
# remove_none(["a", None, "b", None]) ➞ ["a", "b"]

# def remove_none(lst):
#     return [v for v in lst if v != None]
    
    
# print(remove_none(['a', None, 'b', None]))

#50
# even_odd_partition([5, 8, 9, 2, 0]) ➞ [[8, 2, 0], [5, 9]]

# def even_odd_partition(lst):
#    return [[n for n in lst if n % 2 == 0],[n for n in lst if n % 2 != 0]]
# #    return [[i for i in lst if not i%2], [i for i in lst if i%2]]
   

# print(even_odd_partition([5, 8, 9, 2, 0]))


#51
# filter_unique(["abb", "abc", "abcdb", "aea", "bbb"]) ➞ ["abc"]
# def filter_unique(lst):
#     # return list(filter(lambda l: len(l) == len(set(l)), lst))
#     return [i for i in lst if(len(set(list(i)))) == len(i)]
    

# print(filter_unique(["abb", "abc", "abcdb", "aea", "bbb"])) 

#52
# dictionary("bu", ["button", "breakfast", "border"]) ➞ ["button"]
# def dictionary(initial, words):
#     # return [w for w in words if w.startswith(initial)]
#     return list(filter(lambda w: w.startswith(initial), words))
    
    
# print(dictionary('bu', ['button', 'breakfast', 'border']))

#53
# repeat("mice", 5) ➞ "mmmmmiiiiiccccceeeee"
# def repeat(txt, n):
#     return ''.join([l*n for l in txt])
    
    
# print(repeat("hello", 3)) 

# 54
# mirror([0, 2, 4, 6]) ➞ [0, 2, 4, 6, 4, 2, 0]

# def mirror(lst):
#     return lst + lst[:-1][::-1]

# print(mirror([0, 2, 4, 6]))

#55
# can_capture(["A8", "E8"]) ➞ True
# def can_capture(rooks):
#     A, B = rooks
#     return A[0] == B[0] or A[1] == B[1]
    # return  rooks[0][0] == rooks[1][0] or rooks[0][1] == rooks[1][1]
    
    
# print(can_capture(["A8", "A7"]))

#56
# after_n_years({
#   "Joel" : 32,
#   "Fred" : 44,
#   "Reginald" : 65,
#   "Susan" : 33,
#   "Julian" : 13
# }, 1) ➞ {
#   "Joel" : 33,
#   "Fred" : 45,
#   "Reginald" : 66,
#   "Susan" : 34,
#   "Julian" : 14
# }
# def after_n_years(names, n):
#     return {k:v+abs(n) for k,v in names.items()}

# print(after_n_years({
#   "Joel" : 32,
#   "Fred" : 44,
#   "Reginald" : 65,
#   "Susan" : 33,
#   "Julian" : 13
# }, 1))

#57 Create a function that goes through the array, incrementing (+1) for each odd number and decrementing (-1) for each even number.
# transform([1, 2, 3, 4, 5]) ➞ [2, 1, 4, 3, 6]


# def transform(lst):
#     return [n - 1 if n % 2 == 0 else n + 1 for n in lst ]    
    
# print(transform([1, 2, 3, 4, 5]))

#58
# FIZZ BUZZ
# fizz_buzz(3) ➞ "Fizz"

# fizz_buzz(5) ➞ "Buzz"

# fizz_buzz(15) ➞ "FizzBuzz"
# def fizz_buzz(num):
#     if num % 3 == 0 and num % 5 == 0:
#         return 'FizzBuzz'
#     elif num % 3 == 0:
#         return 'Fizz'
#     elif num % 5 == 0:
#         return 'Buzz'
#     else:
#         return str(num)
# def fizz_buzz(num):
#     return "Fizz" * (num % 3 == 0) + "Buzz"*(num % 5==0) or str(num)
    
    
# print('Hi'*True)

#59
# Write a function that takes a two-digit number and determines if it's the largest of two possible digit swaps.

# largest_swap(27) ➞ False

# def largest_swap(num):
#     if num == int(''.join([i for i in str(num)][::-1])):
#         return True
#     return True if num > int(''.join([i for i in str(num)][::-1])) else False
#     return num >= int(str(num)[::-1])
    
    
# print(largest_swap(99))

#60
# accept_into_movie(14, True) ➞ True

# def accept_into_movie(age, is_supervised):
#     return age >= 15 or is_supervised

# print(accept_into_movie(14, True))


# sub_reddit("https://www.reddit.com/r/funny/") ➞ "funny"
# def sub_reddit(link):
#     return link.split('/')[-2]
    
    
    
# print(sub_reddit("https://www.reddit.com/r/relationships/"))


#61
# Create a function to count the number of 1s in a 2D list.

# def count_ones(matrix):
#     # flat_list = []
#     # for sublist in matrix:
#     #     for i in sublist:
#     #         flat_list.append(i)
#     # return flat_list
#     return [i for sublist in matrix for  i in sublist]
#     # return sum(x.count(1) for x in matrix)    

# print(count_ones([[1, 0],[0, 0]]))


#62
# A value is omnipresent if it exists in every sublist inside the main list.
# is_omnipresent([[1, 1], [1, 3], [5, 1], [6, 1]], 1) ➞ True

# def is_omnipresent(lst, val):
#     return all(val in sublist for sublist in lst)

# print(is_omnipresent([[1, 1], [1, 3], [5, 1], [7, 1]], 1))

#63
# def is_prefix(word, prefix):
#     return word.startswith(prefix.strip('-'))
    
# print(is_prefix("mation", "auto-"))
    	
# def is_suffix(word, suffix):
#     return word.endswith(suffix.strip('-'))

# print(is_suffix("rhinoplasty", "-plasty"))


#63
# Write a function that takes all even-indexed characters and odd-indexed characters from a string and concatenates them together.
# index_shuffle("abcd") ➞ "acbd"
# // "ac" (even-indexed) + "bd" (odd-indexed)

# def index_shuffle(txt):
#     return txt[::2] + txt[1::2]
    
    
    
# print(index_shuffle("abcd"))

#64
# Create a function which takes in a sentence txt and a string of characters chars and return the sentence but with all the specified characters removed.
# strip_sentence("the quick brown fox jumps over the lazy dog", "aeiou") ➞ "th qck brwn fx jmps vr th lzy dg"
# def strip_sentence(txt, chars):
#     return ''.join([letter for letter in txt if letter not in chars])

# print(strip_sentence("the quick brown fox jumps over the lazy dog", "aeiou"))

# get_abs_sum([2, -1, 4, 8, 10]) ➞ 25

#65

# get_abs_sum([2, -1, 4, 8, 10]) ➞ 25

# def get_abs_sum(lst):
#     return sum(abs(n) for n in lst)
    


# print(get_abs_sum([2, -1, 4, 8, 10]))

#66
# Is the Average of All Elements a Whole Number?
# is_avg_whole([1, 3]) ➞ True

# def is_avg_whole(arr):
#     return (sum(arr)/len(arr)).is_integer()
    
# print(is_avg_whole([3, 9]))

