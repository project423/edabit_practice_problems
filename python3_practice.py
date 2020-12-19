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

#67
# Create a function which takes in a list of numbers and a number to find. Return the sum of every index in the list which matches the chosen number.
# sum_found_indexes([0, 3, 3, 0, 0, 3], 3) ➞ 8

# def sum_found_indexes(lst, n):
#     return sum(i for i, ltr in enumerate(lst) if ltr == n)

    # def find(str, ch):
    #     for i, ltr in enumerate(str):
    #     if ltr == ch:
    #         yield i

# def sum_found_indexes(lst, n):
#     found_indexes = []
#     for i, ltr in enumerate(lst):
#         if ltr == n:
#             found_indexes.append(i)
#     return sum(found_indexes)
            
    


# print(sum_found_indexes([0, 3, 3, 0, 0, 3], 3))

# Write a function that takes a positive integer and return its factorial.
# factorial(4) ➞ 24

#68
# def factorial(Z):
#     if Z == 0:
#         return 1
#     elif Z == 1:
#         return Z
#     else:
#         return Z * factorial(Z-1)        
    
    
    
# print(factorial(5))

#69
# destructuring a list 
# first, b, c, d, f, last = [1, 2, 3, 4, 5, 6]
# middle = [b,c,d,f]
# first, *middle, last = [1, 2, 3, 4, 5, 6]

#70
# Radian to Degree

# import math

# def to_degree(radian):
#     return radian * (180 / math.pi)

#70

# Volume of a Cone
# cone_volume(3, 2) ➞ 12.57

# from math import pi

# def cone_volume(h, r):
#     return round((1/3)*pi * (r**2) * h, 2)

# print(cone_volume(3, 2))

#71
#fixed broken code
# def grade_percentage(user_score, pass_score):
#     s = ''
#     if user_score[:-1] < pass_score[:-1]:
#         s = 'FAILED'
#     else:
#         s = 'PASSED'
#     return 'You ' + s +' the Exam'
# print(grade_percentage("85%", "85%"))

#72
# integer_boolean("100101") ➞ [True, False, False, True, False, True]

# def integer_boolean(n):
#     return [bool(int(num)) for num in n]

# print(integer_boolean('100101'))

#73

# Create a function that returns true if a given inequality expression is correct and false otherwise.
# correct_signs("3 < 7 < 11") ➞ True

# def correct_signs(txt):
#     # return eval(txt) obvious easy answer
#     # try to complete without eval
#     lst = txt.split('<')
#     print(lst[0],lst[1],lst[2])
#     return int(lst[0]) < int(lst[1]) <int (lst[2]) 
    


# print(correct_signs("3 < 7 < 11"))

# Recursion: Sum
# Write a function that finds the sum of the first n natural numbers. Make your function recursive.
# sum_numbers(5) ➞ 15
# 1 + 2 + 3 + 4 + 5 = 15

# def sum_numbers(n):
#     return n if n == 0 else n + sum_numbers(n - 1)
#     # if n == 0:
#     #     return n
#     # else:
#     #     return n + (sum_numbers(n-1))
    
# print(sum_numbers(100))

#74
# def triangle(n):
#     return int((n * (n + 1)) / 2)
    
# print(triangle(3))

# add_indexes([0, 0, 0, 0, 0]) ➞ [0, 1, 2, 3, 4]

#75

# def add_indexes(lst):
#     # total = []
#     # for i,v in enumerate(lst):
#     #     total.append(i+v)
#     # return total
#     return [i+v for i,v in enumerate(lst)]
# print(add_indexes([1, 2, 3, 4, 5]))

#76
# Recursion: Length of a String
# length("apple") ➞ 5

# def length(txt):
#     # if txt == '':
#     #     return 0
#     # else:
#     #     return 1 + length(txt[1:])
    # return 0 if txt == '' else 1 + length(txt[1:])
    

# print(length('shipment'))

#77
# setify([1, 3, 3, 5, 5]) ➞ [1, 3, 5]

# def setify(lst):
#     return sorted(list(set(lst)))

# print(setify([5,9,9]))

#78
# count_characters([
#   "22222222",
#   "22222222",
# ]) ➞ 16

# def count_characters(lst):
#    return len(lst)
    
# print(count_characters([
# '###',
# '###',
# '###'
# ]))

#78
# count_vowels("Celebration") ➞ 5

# def count_vowels(txt):
#     return len([c for c in txt.lower() if c in 'aeiou'])


# print(count_vowels("Celebration"))

#79
# def factorial(n):
#     return n if n == 1 else n * factorial(n-1)


# print(factorial(5))

#80
# mapping(["p", "s"]) ➞ { "p": "P", "s": "S" }


# def mapping(letters):
#     return {i.lower() : i.upper() for i in letters}
    
# print(mapping(["p", "s"]))

#81

# index_multiplier([1, 2, 3, 4, 5]) ➞ 40

# def index_multiplier(lst):
#     return sum(i * v for i,v in enumerate(lst))
    
    
# print(index_multiplier([9, 3, 7, -7]))

#82
# name_shuffle("Donald Trump") ➞ "Trump Donald"

# def name_shuffle(txt):
#     a, b = txt.split(' ')
#     return '{} {}'.format(b,a)

# print(name_shuffle("Donald Trump"))

#83
# (counterpartCharCode('a'), 65)
# def counterpartCharCode(char):
#     if char.islower():
#         return ord(char.upper())
#     return ord(char.lower())

# print(counterpartCharCode(''))
    
    
#84
# reverse(True) ➞ False
# def reverse(arg):
#     if type(arg) == bool:
#         return not arg
#     return 'boolean expected'

# print(reverse(False))

#85
# Filter out Strings from an Array
# filter_list([1, 2, "a", "b"]) ➞ [1, 2]

# def filter_list(lst):
#     # list comprehension
#     return [i for i in lst if type(i) == int]
#     # filter
#     # return list(filter(lambda x: type(x) == int, lst))

# print(filter_list([1, 2, "a", "b"]))

# Even Number Generator
# Using list comprehensions, create a function that finds all even numbers from 1 to the given number.

#86

# find_even_nums(8) ➞ [2, 4, 6, 8]
# def find_even_nums(num):
#     # return [i for i in range(1,num+1) if i % 2 == 0]
#     return [ x for x in range(2,num+1,2)]
    
    

# print(find_even_nums(8))

#87
# alphanumeric_restriction("Bold") ➞ True

# def alphanumeric_restriction(s):
#     return s.isalpha() or s.isdigit()
    
# print(alphanumeric_restriction("5554"))

#88
# Count Ones in Binary Representation of Integer

# def count_ones(n):
#     return bin(n).count('1')

# print(count_ones(12))

#89

# def XO(txt):
#     return txt.lower().count('o') == txt.lower().count('x')
    
# print(XO("Ooxx"))

#90
# Repeating Letters
# def double_char(txt):
#     return ''.join([l * 2 for l in txt])
    
# print(double_char("String")) 

#90
# import datetime

# def time_for_milk_and_cookies(date):
#     return date.month == 12 and date.day == 24


# print(time_for_milk_and_cookies(datetime.date(2013, 12, 24)))

#91
# Four Passengers and a Driver
# from math import ceil

# def cars_needed(n):
#     # return n // 5
#     return (n + 4) // 5

# print(cars_needed(12))

#92
# (alphabet_soup("hello"), "ehllo")
# def alphabet_soup(txt):
#     return ''.join(sorted(txt))
    
    
# print(alphabet_soup("hello"))

#93
# unique_sort([1, 2, 4, 3]) ➞ [1, 2, 3, 4]
# def unique_sort(lst):
#     return sorted(set(lst))

# print(unique_sort([1, 2, 4, 3]))

#94
# Find the Odd Integer
# find_odd([1, 1, 2, -2, 5, 2, 4, 4, -1, -2, 5]) ➞ -1
# def find_odd(lst):
#     lst1 = []
#     for num in lst:
#         if lst.count(num) % 2 != 0:
#             lst1.append(num)
#     return lst1[0]

# def find_odd(lst):
#       for num in lst:
#     if lst.count(num) % 2:
#       return num
    

    
    
    
# print(find_odd([20, 1, -1, 2, -2, 3, 3, 5, 5, 1, 2, 4, 20, 4, -1, -2, 5])) #-> 5

#95
# next_in_line([5, 6, 7, 8, 9], 1) ➞ [6, 7, 8, 9, 1]
# Stand in Line

# def next_in_line(lst, num):
#     if lst:
#         lst.pop(0)
#         lst.append(num)
#         return lst
#     else:
#         return 'No list has been selected'
    
# print(next_in_line([5, 6, 7, 8, 9], 1))

#96
# replace_vowels("the aardvark", "#") ➞ "th# ##rdv#rk"

# def replace_vowels(txt, ch):
#     # new_list = []
#     # for letter in txt:
#     #     if letter in 'aeiou':
#     #         new_list.append(ch)
#     #     else:
#     #         new_list.append(letter)
#     # return ''.join(new_list)
#     return ''.join([i if i not in 'aeoui' else ch for i in txt])


# print(replace_vowels("the aardvark", "#"))
#97

# def tuck_in(lst1, lst2):
#     for i,v in enumerate(lst2):
#         lst1.insert(i+1,v)
#     return lst1
#     # return [lst1.insert((i+1,v)) for i,v in enumerate(lst2)]
    
    
    
# print(tuck_in([1, 10], [2, 3, 4, 5, 6, 7, 8, 9]))
    
# tuck_in([1, 10], [2, 3, 4, 5, 6, 7, 8, 9]) ➞ [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

#98
# sort_by_length(["Google", "Apple", "Microsoft"])➞ ["Apple", "Google", "Microsoft"]
# def sort_by_length(lst):
#     return sorted(lst, key=len)
    
    
    
# print(sort_by_length(["Google", "Apple", "Microsoft"]))

#99
# simon_says([1, 2], [5, 1]) ➞ True

# def simon_says(lst1, lst2):
#     return lst1[:-1] == lst2[1:] 
    
    
    
# # print(simon_says([1, 2], [5, 1]))
# print(simon_says([1, 2,3, 4, 5], [0,1,2,3,4]))

#100
# list_operation(1, 10, 3) ➞ [3, 6, 9]
# list_operation(10, 50, 10), [10, 20, 30, 40, 50])

# def list_operation(x, y, n):
#     return [i for i in range(x,y+1) if i % n == 0]
    

# # print(list_operation(1, 10, 3))
# print(list_operation(10,50,10))

#100
# profit_margin(28, 39) ➞ "28.2%"
# def profit_margin(cost_price, sales_price):
#     return '{}%'.format(round(((sales_price - cost_price)/sales_price) * 100, 1)) 

# print(profit_margin(10, 15))


# remove_smallest([1, 2, 3, 4, 5] ) ➞ [2, 3, 4, 5]
# remove_smallest([1, 2, 3, 4, 5])

#101
# def remove_smallest(lst):
#     if lst:
#         lst.remove(min(lst))
#         return lst
#     return []
#     # if lst:
#     #   	lst.remove(min(lst))
#     # return lst
    
    
# print(remove_smallest([]))

# 102
# # " A  glittering  gem     is    not   enough.  "
# def correct_spacing(sentence):
#     return ' '.join(sentence.split())
    
# print(correct_spacing(" A  glittering  gem     is    not   enough.  "))

#103
# is_in_order("abc") ➞ True

# def is_in_order(txt):
#     return list(txt) == sorted(txt)
    
# print(is_in_order("ab") )

#104

# A Circle and Two Squares

# square_areas_difference(5) ➞ 50

# def square_areas_difference(r):
#     return 2 * (r**2)
    
    
# print(square_areas_difference(5))

#105

# nth_smallest([1, 3, 5, 7], 1)
# nth_smallest([1, 3, 5, 7], 1) ➞ 1
# nth_smallest([7, 3, 5, 1], 2) ➞ 3
# nth_smallest([5, 4, 3, 2, 1, -3], 5), 4)

# def nth_smallest(lst, n):
#     # if n > len(lst):
#     #     return None
#     # return sorted(lst)[n-1]
#     return None if n > len(lst) else sorted(lst)[n-1]
    
# # print(nth_smallest([4,5], 1))
# print(nth_smallest([5, 4, 3, 2, 1, -3], 1))

#106

# sort_by_length(["a", "ccc", "dddd", "bb"]) ➞ ["a", "bb", "ccc", "dddd"]

# def sort_by_length(lst):
#     return sorted(lst, key=len)
    
# print(sort_by_length(["a", "ccc", "dddd", "bb"]))

#107

# card_hide("1234123456785678") ➞ "************5678"


# def card_hide(card):
#     return len(card[:-4])* '*' + card[-4:] 
    
# print(card_hide("1234123456785678"))


#108

# society_name(["Adam", "Sarah", "Malcolm"]) ➞ "AMS"

# def society_name(friends):
#     return ''.join(sorted([f[0] for f in friends]))

# print(society_name(["Adam", "Sarah", "Malcolm"]))

#109

# filter_list([1, 2, 3, "a", "b", 4]) ➞ [1, 2, 3, 4]

# def filter_list(l):
#     return [i for i in l if type(i) == int]
    


# print(filter_list([1, 2, 3, "a", "b", 4]))

#110
# left_digit("TrAdE2W1n95!") ➞ 2

# def left_digit(num):
#     # return int(list(filter(lambda x: x.isdigit(), num))[0])
#     return [int(n) for n in num if n.isdigit()][0]    
    
# print(left_digit("TrAdE2W1n95!"))


#111
# Supposed to write more minimalistic
# def are_true(a, b):
#     if a and b:
#         return "both"
#     elif a:
#         return 'first'
#     elif b:
#         return 'second'
#     else:
#         return 'neither' 

# # return 'both' if a and b else 'first' if a else 'second' if b else 'neither'
# print(are_true(True, True))
# print(are_true(True, False))
# print(are_true(False, True))
# print(are_true(False, False))

#112
# Hamming distance is the number of characters that differ between two strings.
# hamming_distance("abcde", "bcdef") ➞ 5

# def hamming_distance(txt1, txt2):
#     count = 0
#     for first , second in zip(txt1,txt2):
#         if first != second:
#             count += 1
#     return count
            
# def hamming_distance(txt1, txt2):
#     return sum(x!=y for (x,y) in zip(txt1,txt2))  
    
# print(hamming_distance("a", "a"))


#113
# is_subset([3, 2, 5], [5, 3, 7, 9, 2]) ➞ True
# def is_subset(lst1, lst2):
#     return set(lst1).issubset(lst2)
    
# print(is_subset([1, 2], [3, 5, 9, 1]))

#114
# reverse("Hello World") ➞ "DLROw OLLEh"
# def reverse(txt):
#     return txt.swapcase()[::-1]


# print(reverse("Hello World"))

#115
# get_student_names({
#   "Student 1" : "Steve",
#   "Student 2" : "Becky",
#   "Student 3" : "John"
# }) ➞ ["Becky", "John", "Steve"]


# def get_student_names(students):
#     return sorted(s for s in students.values())
#     return sorted(students.values())

# print(get_student_names({
# 	"Student 1":"Steve",
# 	"Student 2":"Becky",
# 	"Student 3":"John"
# }))

#116
# compound_interest(10000, 10, 0.06, 12) ➞ 18193.97
# def compound_interest(p, t, r, n):
#     exponent = n * t
#     middle = (1 + (r/n))
#     middle_times_exponent = middle**exponent
#     return round(p * middle_times_exponent ,2)

# print(compound_interest(3500, 15, 0.1, 4))

#117
# evenly_divisible(1, 10, 20) ➞ 0
# def evenly_divisible(a, b, c):
#     return sum(i for i in range(a,b+1) if not i % c )

# print(evenly_divisible(1, 10, 2))

#118

# index_of_caps("eDaBiT") ➞ [1, 3, 5]
# def index_of_caps(word):
#     return [i  for i, l in enumerate(word) if l.isupper()] 

# print(index_of_caps("eDaBiT"))
# print(index_of_caps("@xCE#8S#i*$en"))

#119
# Encode Morse
# encode_morse("EDABBIT CHALLENGE") ➞ ". -.. .- -... -... .. -   -.-. .... .- .-.. .-.. . -. --. ."


# def encode_morse(message):
#     d = {
#   'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
#   'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
#   'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
#   'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
#   'Y': '-.--', 'Z': '--..', ' ': ' ', '0': '-----',
#   '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
#   '6': '-....', '7': '--...', '8': '---..', '9': '----.',
#   '&': '.-...', "'": '.----.', '@': '.--.-.', ')': '-.--.-', '(': '-.--.',
#   ':': '---...', ',': '--..--', '=': '-...-', '!': '-.-.--', '.': '.-.-.-',
#   '-': '-....-', '+': '.-.-.', '"': '.-..-.', '?': '..--..', '/': '-..-.'
# }
#     # return ' '.join(char_to_dots[l.upper()] for l in message)
#     return ' '.join(d[i] for i in message.upper())

# print(encode_morse("EDABBIT CHALLENGE"))

# Check for Anagrams
# is_anagram("cristian", "Cristina") ➞ True
#120

# def is_anagram(s1, s2):
#     return sorted(s1.lower()) == sorted(s2.lower())


# print(is_anagram("cristian", "Cristina"))

# Lexicographically First and Last
# first_and_last("marmite") ➞ ["aeimmrt", "trmmiea"]

#121
# def first_and_last(s):
#     return [''.join(sorted(list(s))),''.join(sorted(list(s), reverse = True))]


# print(first_and_last("marmite"))

# Find the Missing Number
# missing_num([1, 2, 3, 4, 6, 7, 8, 9, 10]) ➞ 5

# def missing_num(lst):
#     # for i in range (1, 11):
#     #     if i not in lst:
#     #         return i
#     return 55 - sum(lst)
    
    

# print(missing_num([1, 2, 3, 4, 6, 7, 8, 9, 10]))

#122# Inputs:
# User-typed: ["cat", "blue", "skt", "umbrells", "paddy"]
# Correct: ["cat", "blue", "sky", "umbrella", "paddy"]

# Output: [1, 1, -1, -1, 1]

# correct_stream(
#   ["it", "is", "find"],
#   ["it", "is", "fine"]
# ) ➞ [1, 1, -1]

# def correct_stream(user, correct):
#     # lst = []
#     # for x, y in zip(user,correct):
#     #     if x == y:
#     #         lst.append(1)
#     #     else:
#     #         lst.append(-1)
#     # return lst
#     return [1 if x == y else -1 for x, y in zip(user,correct) ]

        
# print(correct_stream(
#   ["it", "is", "find"],
#   ["it", "is", "fine"]
# ))

#123
# Count the Arguments
# num_args("foo", "bar") ➞ 2
# def num_args(*args):
#     return len(args)
    
    
# print(num_args("foo", "bar"))       
    

#124
# Factorial of a Number

# fact(3) ➞ 6

# def fact(n):
#     # if n == 1:
#     #     return n
#     # else:
#     #     return n * fact(n-1)
#     if n == 0: return 1
#     return n if n == 1 else n * fact(n-1)

# print(fact(3))

#125

# Return Odd > Even
# Given a list, return True if there are more odd numbers than even numbers, otherwise return False.
# oddeven([1, 2, 3, 4, 5, 6, 7, 8, 9]) ➞ True

# def oddeven(lst):
#     # return len([n for n in lst if n % 2 !=0]) >= len([n for n in lst if n % 2 == 0])
#     return sum(1 if int(i)%2 else -1 for i in lst) > 0
# print(oddeven([1, 2, 3, 4, 5, 6, 7, 8, 9]))

#125

# Find the Mean of All Digits
# mean(12345) ➞ 3

# def mean(num):
#     return sum(int(n) for n in str(num)) // len(str(num))

# print(mean(789))

#126
# letter_counter([
#   ["D", "E", "Y", "H", "A", "D"],
#   ["C", "B", "Z", "Y", "J", "K"],
#   ["D", "B", "C", "A", "M", "N"],
#   ["F", "G", "G", "R", "S", "R"],
#   ["V", "X", "H", "A", "S", "S"]
# ], "D") ➞ 3
# Create a function that counts the number of times a particular letter shows up in the word search.

# def letter_counter(lst, letter):
    # count = 0
    # for sublist in lst:
    #     for l in sublist:
    #         if l == letter:
    #             count +=1
    # return count 
    # return sum(sublist.count(letter) for sublist in lst )

# print(letter_counter([
# 	['D', 'D', 'Y', 'H', 'A', 'D'],
# 	['C', 'B', 'Z', 'Y', 'J', 'K'],
# 	['D', 'B', 'C', 'A', 'M', 'N'],
# 	['F', 'G', 'G', 'R', 'S', 'R'],
# 	['V', 'X', 'H', 'A', 'S', 'S']
# ], 'D'))

#127
# letters_only("R!=:~0o0./c&}9k`60=y") ➞ "Rocky"
# def letters_only(txt):
#     return ''.join([l for l in txt if l.isalpha()])
    

# print(letters_only("R!=:~0o0./c&}9k`60=y"))

#128

# def mood_today(mood):
#     return 'Today, I am feeling {}'.format(mood)    
    
# print(mood_today("happy"))

#129
# unique([3, 3, 3, 7, 3, 3]) ➞ 7

# def unique(lst):
#     # freq = {}
    
#     # for item in lst:
#     #     if item in freq:
#     #         freq[item] +=1
#     #     else:
#     #         freq[item] = 1
            
#     # return min(freq,key=freq.get)
    
#     return min(set(lst), key=lst.count)
    
        


# print(unique([3, 3, 3, 7, 3, 3]))
# lst = [3,3,4,4,5]
# print(min(lst, key=lst.count))
# print(min(("java", "python", "z++"), key=len))
# 'z++'

# 130
# [
#   { "tile": "N", "score": 1 },
#   { "tile": "K", "score": 5 },
#   { "tile": "Z", "score": 10 },
#   { "tile": "X", "score": 8 },
#   { "tile": "D", "score": 2 },
#   { "tile": "A", "score": 1 },
#   { "tile": "E", "score": 1 }
# ]

# maximum_score([
#   { "tile": "N", "score": 1 },
#   { "tile": "K", "score": 5 },
#   { "tile": "Z", "score": 10 },
#   { "tile": "X", "score": 8 },
#   { "tile": "D", "score": 2 },
#   { "tile": "A", "score": 1 },
#   { "tile": "E", "score": 1 }
# ]) ➞ 28


# def maximum_score(tile_hand):
#     return sum(d['score'] for d in tile_hand)
    
    
# print(maximum_score([
#   { "tile": "N", "score": 1 },
#   { "tile": "K", "score": 5 },
#   { "tile": "Z", "score": 10 },
#   { "tile": "X", "score": 8 },
#   { "tile": "D", "score": 2 },
#   { "tile": "A", "score": 1 },
#   { "tile": "E", "score": 1 }
# ]))

# 131
# Return Only the Integer
# return_only_integer([9, 2, "space", "car", "lion", 16]) ➞ [9, 2, 16]
# def return_only_integer(lst):
#     return [n for n in lst if type(n) == int]
    
    
# print(return_only_integer([9, 2, "space", "car", "lion", 16]))

# Get Sum of People's Budget


#131
# get_budgets([
#   { "name": "John", "age": 21, "budget": 23000 },
#   { "name": "Steve",  "age": 32, "budget": 40000 },
#   { "name": "Martin",  "age": 16, "budget": 2700 }
# ]) ➞ 65700


# def get_budgets(lst):
#     return sum(d['budget'] for d in lst)
    
# print(get_budgets([{"name": "John",  "age": 21, "budget": 23000}, {"name": "Steve",  "age": 32, "budget": 40000}, {"name": "Martin",  "age": 16, "budget": 2700}]))

#132

# How Many Solutions Does This Quadratic Have?

#132
# All About Lambda Expressions: Adding
# adds1 = adds_n(1)

# adds1 = lambda n : n + 1
    
# print(adds1(5))

# def adds_n(n):
# 	return lambda x: x + n

# Toy Car Workshop
# cars(2, 48, 76) ➞ 0
# 2 wheels, 48 car bodies, 76 figures

#133
# def cars(wheels, bodies, figures):
#     return min(wheels//4,figures // 2, bodies)


# print(cars(37, 50, 20))

#134

# has_digit("c8") ➞ True

# import re

# def has_digit(txt):
#     return bool(re.search(r'\d', txt))

# print(has_digit('cdf4'))

#135

# def can_alternate(s):
#     return True if abs(s.count('1') - s.count('0')) == 1 or s.count('1') == s.count('0') else False

#     return abs(s.count('0') - s.count('1')) in (0, 1)

# print(can_alternate('10101010'))

#136

# How Heavy Is It?
# from math import pi

# def weight(r, h):
#     return round((pi * (r**2) * h)/1000,2)


# print(weight(4, 10))
    
    
# weight(4, 10) ➞ 0.5

#137
# findLargest(1,2,3), 3)
# def findLargest(n1, n2, n3):
# 	return max(n1, n2, n3)


#138
# profit({
#   "cost_price": 32.67,
#   "sell_price": 45.00,
#   "inventory": 1200
# }) ➞ 14796

#139
# def profit(info):
#      return round(info['inventory'] * (info['sell_price'] - info['cost_price']))    
    
    
# print(profit({
#   "cost_price": 32.67,
#   "sell_price": 45.00,
#   "inventory": 1200
# }))

#140
# is_valid_PIN("1234") ➞ True

# def is_valid_PIN(pin):
#     return (len(pin) == 4 or len(pin) == 6)  and pin.isdigit()
#     return len(pin) in [4, 6] and pin.isdigit()

# print(is_valid_PIN("1234"))

#141
# 25-Mile Marathon
# marathon_distance([1, 2, 3, 4]) ➞ False

# def marathon_distance(d):
#     return sum(abs(n) for n in d) == 25

# print(marathon_distance([1, 9, 5, 8, 2]))

#142

# is_isogram("Algorism") ➞ True


# def is_isogram(txt):
#     return len(txt.lower()) == len(''.join(set(txt.lower())))
# print(is_isogram("Dermatoglyphics"))

#143

# Convert Year to Century
# century_from_year(2005) ➞ 21

# from math import ceil

# def century_from_year(year):
#     return ceil(year/100)

# print(century_from_year(1705))

#144
# Basic Calculator
# Create a function that takes two numbers and a mathematical operator + - / * and will perform a calculation with the given numbers.

# def calculator(num1, operator, num2):
#     if num2: 
#         return round(eval('{} {} {}'.format(num1,operator,num2)))
#     else:
#         return 'Can\'t divide by 0!'

# print(calculator(2, '/', 3))

#145
# Folding a Piece of Paper
# def num_layers(n):
#     if not n:
#         return "0.0005m"
#     return '{}m'.format(0.5*2**n/1000)
    
# print(num_layers(3))

#146

# find_bob(["Jimmy", "Layla", "Bob"]) ➞ 2
# def find_bob(names):
#     try:
#         return names.index("Bob")
#     except:
#         return -1    
    
# print(find_bob(["Jimmy", "Layla"]))

#145
# remove_enemies(["Adam", "Emmy", "Tanya", "Emmy"], ["Emmy"]) ➞ ["Adam", "Tanya"]
# remove_enemies(["John", "Emily", "Steve", "Sam"], ["Sam", "John"]) ➞ ["Emily", "Steve"]
# def remove_enemies(names, enemies):
#     return [n for n in names if n not in enemies]
    
    
# print(remove_enemies(["Adam", "Emmy", "Tanya", "Emmy"], ["Emmy"]))
# print(remove_enemies(["John", "Emily", "Steve", "Sam"], ["Sam", "John"]))

#146
# convert_to_decimal(["1%", "2%", "3%"]) ➞ [0.01, 0.02, 0.03]

# def convert_to_decimal(perc):
#     return [float(n.strip('%')) / 100 for n in perc]


# print(convert_to_decimal(["33%", "98.1%", "56.44%", "100%"]))

#147
# remove_vowels("I have never seen a thin person drinking Diet Coke.")
# ➞ " hv nvr sn  thn prsn drnkng Dt Ck."

# def remove_vowels(txt):
#     return ''.join(c for c in txt if c.lower() not in ['a','e','i','o','u'])
    
# print(remove_vowels("If Obama resigns from office NOW, thereby doing a great service to the country - I will give him free lifetime golf at any one of my courses!"))

#148
# trace([
#   [1, 4],
#   [4, 1]
# ]) ➞ 2

# def trace(lst):
#     total = 0
#     for i in range(len(lst)):
#         total += lst[i][i]
#     return total

# def trace(arr):
#     	return sum(arr[i][i] for i in range(len(arr)))
    

#     # return lst[0][0] + lst[1][1] + lst[2][2]
 
# print(trace([
#   [1, 4],
#   [4, 1]
# ])) 

# print(trace([
#   [1, 2, 3],
#   [4, 5, 6],
#   [7, 8, 9]
# ])) 
 
# trace([
#   [1, 4],
#   [4, 1]
# ]) 

#149
# Multi-division
# abcmath(42, 5, 10) ➞ False

# 42+42 = 84,84+84 = 168,168+168 = 336,336+336 = 672, 672+672 = 1344
# 1344 is not divisible by 10
# def abcmath(a, b, c):
#     for i in range(1,b+1):
#         a +=a
#     return a % c == 0
    
    

# print(abcmath(42, 5, 10))
# print(abcmath(261, 2, 1))

#150

# Probabilities (Part 1)
# probability([5, 1, 8, 9], 6) ➞ 50.0

# def probability(lst, n):
#    return round(len(list(filter(lambda i: i >= n, lst))) / len(lst) * 100,1)
    
    
    
# print(probability([11, 10, 9, 18, 16, 18, 4, 3, 5], 13)) 

#151
# Find the Second Largest Number
# second_largest([10, 40, 30, 20, 50]) ➞ 40
# def second_largest(lst):
#     return sorted(lst)[-2]

# print(second_largest([10, 40, 30, 20, 50]))

# print(second_largest([25, 143, 89, 13, 105])) 


#152

# jazzify(["G", "F", "C"]) ➞ ["G7", "F7", "C7"]

# def jazzify(lst):
#     return [l if l.endswith('7') else l + '7' for l in lst]
    
# print(jazzify(['G7', 'F7', 'C']))

#153

# clone([1, 1]) ➞ [1, 1, [1, 1]]

# def clone(lst):
#     lst.append(lst[:])
#     return lst
    
    

# print(clone([1, 1]))

#154
# List Multiplier

# def multiply(l):
#     if type(l[0]) == int:
#         return [[int(i) for i in str(elem).split(',') * len(l)] for elem in l]
#     else:
#         return [str(i).split(',') * len(l) for i in l]
        

    
    
# print(multiply([4,5]))
        # lst = []
        # for elem in l:
        #     # elem = str(elem)
        #     # temp = str(elem).split(',')
        #     lst.append([int(i) for i in str(elem).split(',') * len(l)])
        # return lst
        
# def multiply(lst):
# 	return [[i]*len(lst) for i in lst]

# print(multiply([4, 5]))

# print([3]*5)

# 155

# showdown(
#   "   Bang!        ",
#   "        Bang!   "
# ) ➞ "p1"


# def showdown(p1, p2):
#     if p1.find('B') == p2.find('B'):
#         return  "tie"
#     elif p1.find('B') > p2.find('B'):
#         return 'p2'
#     else:
#         return 'p1'   
#     # return "tie" if p1 == p2 else ("p1" if p1 > p2 else "p2")

# print(showdown(
# "  Bang!",
# " Bang!   "
# ))

#156
# Vowel Sandwich
# is_vowel_sandwich("cat") ➞ True
# is_vowel_sandwich("bake") ➞ False

# def is_vowel_sandwich(s):
#     if len(s) != 3:
#         return False
#     lst =  [i for i in s]
#     vowels = ['a','e','i','o','u']
#     return (lst[0] not in vowels) and (lst[1] in vowels) and (lst[2] not in vowels)
#     return [0, 1, 0] == [1 if l in 'aeiou' else 0 for l in s]
         
    
# print(is_vowel_sandwich("cat"))

#157


# # bitwise_and(7, 12) ➞ 4

# # bitwise_and(6, 23) ➞ 00000110
# # bitwise_and(7, 12) ➞ 4
# def bitwise_and(n1, n2):
#     return n1 & n2

# def bitwise_or(n1, n2):
#     return n1 | n2

# def bitwise_xor(n1, n2):
#     return n1 ^ n2


# print(bitwise_and(7, 12))
# # bitwise_or(6, 23) ➞ 00010111
# print(bitwise_or(7,12))
# # bitwise_or(7, 12) ➞ 15
# # def bitwise_or(n1, n2):
	

# # bitwise_xor(6, 23) ➞ 00010001
# print(bitwise_xor(7, 12)) #➞ 11
# # def bitwise_xor(n1, n2):


#158
# is_symmetrical(7227) ➞ True

# def is_symmetrical(num):
#     return str(num) == str(num)[::-1]
    
# print(is_symmetrical(7227))

#159

# sum_of_evens([
#   [1, 0, 2],
#   [5, 5, 7],
#   [9, 4, 3]
# ]) ➞ 6

# Create a function that returns the sum of all even elements in a 2D matrix.

# def sum_of_evens(lst):
#     # total = 0
#     # for sublist in lst:
#     #     for i in sublist:
#     #         if i % 2 == 0:
#     #             total += i
#     # return total   
#     return sum(i for sublist in lst for i in sublist if i % 2 == 0)
 
# print(sum_of_evens([
# 		[1, 5, 1, 3], 
# 		[4, 1, 2, 0], 
# 		[6, 9, 7, 4], 
# 		[5, 1, 2, 6]
# 	]))

# def count_ones(matrix):
#     # flat_list = []
#     # for sublist in matrix:
#     #     for i in sublist:
#     #         flat_list.append(i)
#     # return flat_list
#     return [i for sublist in matrix for  i in sublist]

#160
# Amplify the Multiples of Four
# If the number can be divided evenly by 4, amplify it by 10 (i.e. return 10 times the number).
# If the number cannot be divided evenly by 4, simply return the number.

# amplify(4) ➞ [1, 2, 3, 40]

# def amplify(num):
#     return [i * 10 if i % 4 == 0 else i for i in range(1, num+1)]

# print(amplify(4))

#161
# Move Capital Letters to the Front
# cap_to_front("moveMENT") ➞ "MENTmove"

# def cap_to_front(s):
#     upper = []
#     lower = []
#     str1 = ''
#     for char in [l for l in s]:
#         upper.append(char) if char.isupper() else lower.append(char)
#     upper.extend(lower)
#     return str1.join(upper)
    
# print(cap_to_front("moveMENT"))

#162
# Go Corona!
# end_corona(4000, 2000, 77000) ➞ 39

# def end_corona(recovers, new_cases, active_cases):
#     total_days = 0
#     while active_cases >= 0:
#         total_days += 1
#         active_cases += new_cases
#         active_cases -= recovers
#     return total_days
        
        
    
    
# print(end_corona(30000, 25000, 390205))

#163
# One Button Messaging Device
# Imagine a messaging device with only one button. For the letter A, you press the button one time, for E, you press it five times, for G, it's pressed seven times, etc, etc.
# Write a function that takes a string (the message) and returns the total number of times the button is pressed.


# def how_many_times(msg):
#     return sum(ord(letter) - 96 for letter in msg)
    
 
# print(how_many_times('abde'))

#164
# convert_cartesian([1, 5, 3, 3, 4], [5, 8, 9, 1, 0]) ➞ [[1, 5], [5, 8], [3, 9], [3, 1], [4, 0]]

# def convert_cartesian(x, y):
#     return [list(i) for i in zip(x,y)]
    
    
# print(convert_cartesian([1, 5, 3, 3, 4], [5, 8, 9, 1, 0]))

#165

# Moving to the End
# move_to_end([1, 3, 2, 4, 4, 1], 1) ➞ [3, 2, 4, 4, 1, 1]

# def move_to_end(lst, el):
#     return [x for x in lst if x !=el] + [y for y in lst if y == el]

# print(move_to_end([1, 3, 2, 4, 4, 1], 1))


#166
# split("abcde") ➞ "aebcd"
# def split(txt):
#     vowels = []
#     consonants = []
#     for l in txt:
#         if l in 'aeiou':
#             vowels.append(l)
#         else:
#             consonants.append(l)
#     return ''.join(vowels + consonants)

# print(split("abcde"))

#167

# 11/17/20
# Create a function that takes the age and return the age in days.
# calc_age(65) ➞ 23725

# calc_age(0) ➞ 0

# calc_age(20) ➞ 7300

# def calc_age(age):
#     return age * 365

# print(calc_age(10))

#168
# Burglary Series (04): Add its Name

# add_name({}, "Brutus", 300) ➞ { "Brutus": 300 }

# add_name({ "piano": 500 }, "Brutus", 400) ➞ { "piano": 500, "Brutus": 400 }

# add_name({ "piano": 500, "stereo": 300 }, "Caligula", 440) ➞ { "piano": 500, "stereo": 300, "Caligula": 440 }

# def add_name(obj, name, value):
#     obj.update({name:value})
#     return obj
    
    
# print(add_name({}, "Brutus", 300))

# 169
# Proper Modulo Operator

# mod(-13, 64) ➞ 51

# mod(50, 25) ➞ 0

# mod(-6, 3) ➞ 0

# def mod(m, n):
#     return m % n

# print(mod(-13, 64))

#170
# Two Lists inside a List to One

# one_list([[1, 2], [3, 4]]) ➞ [1, 2, 3, 4]

# def one_list(lst):
#     # new_list = []
#     # for sublist in lst:
#     #     for l in sublist:
#     #         new_list.append(l)
#     # return new_list
    
#     return [l for sublist in lst for l in sublist]
    
# print(one_list([[1, 2], [3, 4]]))

#171
# Is the String Odd or Even?
# Given a string, return True if its length is even or False if the length is odd.
# odd_or_even("apples") ➞ True

# def odd_or_even(word):
#     return len(word) % 2 == 0
# print(odd_or_even("apples")) 

# 172
# Convert All List items to String
# Create a function that takes a list of integers and strings. Convert integers to strings and return the new list.
# parse_list([1, 2, "a", "b"]) ➞ ["1", "2", "a", "b"]


# def parse_list(lst):
#     return [str(l) for l in lst]


# print(parse_list([1, 2, "a", "b"]))



# 173

# make_pair(1, 2) ➞ [1, 2]

# def make_pair(num1, num2):
#     return  [num1, num2]

# print(make_pair(1,2))

#174
# Tile Teamwork Tactics
# Given you and your friend's tile number, create a function that returns if it's possible to earn a bonus when you roll the dice.

# possible_bonus(3, 7) ➞ True

# def possible_bonus(a, b):
#     if a > b or a ==b:
#         return False
#     elif b - a < 7:
#         return True
#     else:
#         return False
    

# 175   
# def possible_bonus(a,b):
#     return b - a < 7 and b !=a and b > a

# print(possible_bonus(7, 6))
    
# 176
# Miserable Parody of a Calculator

# calculator("23+4") ➞ 27

#176
# def calculator(txt):
#     return eval(txt)


# print(calculator("23+4")) 

#177
# Sum of List Less Than 100 List Remix

# list_less_than_100([5, 57])
# Given a list of numbers, return True if the sum of the values in the list is less than 100; otherwise return False.

# list_less_than_100([5, 57])

# def list_less_than_100(lst):
#     return sum(lst) < 100

# print(list_less_than_100([5, 57]))


# 178

# WordCharWord

# Create a function that will put the first argument, a character, between every word in the second argument, a string.
# add("R", "python is fun") ➞ "pythonRisRfun"

# def add(char, txt):
#     return txt.replace(" ", char)


# print(add("R", "python is fun"))

# 179
# Create a function that counts how many D's are in a sentence.
# count_d("My friend Dylan got distracted in school.") ➞ 4

# def count_d(sentence):
#     return sentence.lower().count('d')
    
# print(count_d("My friend Dylan got distracted in school."))

# 180
# Recreating the abs() Function

# Create a function that recreates this functionality.

# absolute(-5) ➞ 5

# def absolute(n):
#     return n if n > 0 else n*(-1)

# print(absolute(0))

#181

# circuit_power(230, 10) ➞ 2300

# def circuit_power(voltage, current):
#     return voltage * current
    
    
# print(circuit_power(230,10))

# 182
# def inches_to_feet(inches):
#     return int(inches / 12) if inches >= 12 else 0
    
# # inches_to_feet(324) ➞ 27

# print(inches_to_feet(12))

#183

# def check_equals(lst1, lst2):
#     lst1.sort()
#     lst2.sort()    
#     return True if lst1 == lst2 else False


# print(check_equals([1, 2], [1, 3]))


#184
# from random import randint
# def random_int(a, b):
#     return randint(a,b)


# print(random_int(5, 9))


#185
# Luke, I Am Your ...

# def relation_to_luke(name):
#     dict = {
#         'Darth Vader': 'father',
#         'Leia': 'sister',
#         'Han': 'brother in law',
#         'R2D2': 'droid'
#     }
    
#     return "Luke, I am your {}.".format(dict[name])
    

# print(relation_to_luke("Darth Vader"))

# 186
# Convert a Number to Base-2

# binary(5) ➞ "101"

# def binary(decimal):
#     return bin(decimal)[2:]

# print(binary(100))

# 187

# Capitalize by ASCII
# Create a function that takes a string as input and capitalizes a letter if its ASCII code is even and returns its lower case version if its ASCII code is odd.

# def ascii_capitalize(txt):
#     my_str = ''
#     for letter in txt:
#         if ord(letter) % 2 == 0:
#             my_str += letter.upper()
#         else:
#             my_str += letter.lower()
#     return my_str
# # ascii_capitalize("to be or not to be!") ➞ "To Be oR NoT To Be!"
# print(ascii_capitalize("Oh what a beautiful morning."))

# print(ord('O'))

#188
# Say Hello to Guests

# In this exercise you will have to:

# Take a list of names.
# Add "Hello" to every name.
# Make one big string with all greetings.
# The solution should be one string with a comma in between every "Hello (Name)".
# greet_people(["Angela", "Joe"]) ➞ "Hello Angela, Hello Joe"

#189
# def greet_people(names):
#     return ', '.join("Hello " + name  for name in names)
        
    
    
# print(greet_people(["Angela", "Joe"]))

# 190
# Upper or Lower Case
# Return the smallest number of steps it takes to convert a string entirely into uppercase or entirely into lower case, whichever takes the fewest number of steps. A step consists of changing one character from lower to upper case, or vice versa.

# def steps_to_convert(txt):
#     return min(sum(1 for c in txt if c.isupper()), sum(1 for c in txt if c.islower()))
#     #     return sum(1 for c in txt if c.islower())
#     # else:
#     #     return sum(1 for c in txt if c.isupper())


# print(steps_to_convert("abCBA"))

#191

# Burglary Series (10): Calculate Difference
# calc_diff({ "baseball bat": 20 }, 5) ➞ 15

# def calc_diff(obj, limit):
#     return sum(value for value in obj.values()) - limit    
    


# # print(calc_diff({ "baseball bat": 20 }, 5))
# print(calc_diff({"skate": 10, "painting": 20 }, 19))


#192
# Square Every Digit
# Create a function that squares every digit of a number.

# def square_digits(n):
#     return int(''.join(str(int(i)**2) for i in str(n)))
    
    
# print(square_digits(9119))

#193
# Halloween Day
# Create a function that takes date in the format yyyy/mm/dd as an input and returns "Bonfire toffee" if the date is October 31, else return "toffee".

# halloween("2013/10/31") ➞ "Bonfire toffee"

# halloween("2012/07/31") ➞ "toffee"

# halloween("2011/10/12") ➞ "toffee"

# def halloween(dt):
#     month =  int(dt[5:].split('/')[0])
#     day =  int(dt[5:].split('/')[1])
#     if day == 31 and month == 10:
#         return 'Bonfire toffee'
#     else:
#         return 'toffee'
    


# dt[5:].split('/')[0]
    
    
# print(halloween("2013/10/31"))

# 194
# Something in the Box?
# Create a function that returns True if an asterisk * is inside a box.
# in_box([
#   "###",
#   "#*#",
#   "###"
# ]) ➞ True

# def in_box(lst):
#     for sublist in lst:
#         if sublist[0] =='#' and sublist[-1] == '#':
#             if '*' in sublist:
#                 return True
#     return False 
    
#     return any('*' in row for row in lst)           
            
# return "*" in [item for sublist in lst for item in sublist]
    
# print(in_box(["###","#*#","###"]))

# print(in_box([
#   "*####",
#   "# #",
#   "#  #*",
#   "####"
# ]))


# 195

# Automorphic Numbers
# A number n is automorphic if n^2 ends in n.
# Create a function that takes a number and returns True if the number is automorphic, False if it isn't.

# is_automorphic(5) ➞ True

# is_automorphic(8) ➞ False
# def is_automorphic(n):
#     return str(pow(n,2)).endswith(str(n))
    
# print(is_automorphic(5))

# 196
# Shhh Be Quiet Function
# shhh("HI THERE!") ➞ '"Hi there!", whispered Edabit.'
# shhh("tHaT'S Pretty awesOme") ➞ '"That's pretty awesome", whispered Edabit.'


# def shhh(txt):
#     return "\"{}\", whispered Edabit.".format(txt.capitalize())
    
    
# print(shhh("tHaT'S Pretty awesOme"))
# print(shhh("HI THERE!"))
# # 'Hi there!, whispered Edabit.' should equal '"Hi there!", whispered Edabit.'
# '"Hi there!, whispered Edabit."' should equal '"Hi there!", whispered Edabit.'

# 197
# Halve and Halve Again
# halve_count(1324, 98) ➞ 3
# (1324 -> 662 -> 331 -> 165.5)

# def halve_count(a, b):
#     i = 0
#     while a > b:
#         a = a/2
#         i+=1
#     return i-1
    
# print(halve_count(1324, 98))

# 198
# Total Volume of All Boxes
# total_volume([4, 2, 4], [3, 3, 3], [1, 1, 2], [2, 1, 1]) ➞ 63

# def total_volume(*boxes):
#     volumes = []
#     for sublist in boxes:
#         product = sublist[0] * sublist[1] * sublist[2]
#         volumes.append(product)
#     return sum(volumes)
            
            
    
# print(total_volume([4, 2, 4], [3, 3, 3], [1, 1, 2], [2, 1, 1]))

#199
# Numbers to Arrays and Vice Versa
# to_list(), which converts a number to an integer list of its digits.
# to_number(), which converts a list of integers back to its number.

# to_list(235) ➞ [2, 3, 5]

# to_list(0) ➞ [0]
# def to_list(num):
#     return [int(d) for d in str(num) ]

# print(to_list(235))

# to_number([2, 3, 5]) ➞ 235

# to_number([0]) ➞ 0
# def to_number(lst):
#     s = [str(i) for i in lst]
    
#     res = int("".join(s))
    
#     return res

# print(to_number([2, 3, 5]))

# 200
# Length of Number
# can't use len()
# number_length(5000) ➞ 4
# def number_length(num):
#     count = 0
#     if num == 0:
#         return 1
#     while num > 0:
#         count += 1
#         num = num // 10
#     return count
# print(number_length(40))

#201
# num_of_digits(1000) ➞ 4
# num_of_digits(1305981031) ➞ 10
# def num_of_digits(num):
#     return len(str(abs(num)))

# print(num_of_digits(-1305981031))

#202

# Equality of 3 Values

# equal(3, 4, 3) ➞ 2

# equal(1, 1, 1) ➞ 3

# equal(3, 4, 1) ➞ 0 

# def equal(a, b, c):
#     my_set = {a,b,c}
#     length_of_set = len(my_set)
#     if length_of_set  == 1:
#         return 3
#     elif length_of_set == 2:
#         return 2
#     else:
#         return 0
    
# print(equal(3, 3, 3))

#203
# Chat Room Status
# chatroom_status(["s234f", "mailbox2"]) ➞ "s234f and mailbox2 online"

# def chatroom_status(users):
#     if len(users) == 0:
#         return "no one online"
#     elif len(users) == 1:
#         return "{} online".format(users[0])
#     elif len(users) == 2:
#         return "{} and {} online".format(users[0],users[1])
#     else:
#         remaining_users = len(users) - 2
#         return "{}, {} and {} more online".format(users[0], users[1], remaining_users)
    
    
# # print(chatroom_status(["s234f", "mailbox2"]))
# print(chatroom_status(['john','kate','will','bob']))

#204
# Retrieve the Last N Elements
# last([1, 2, 3, 4, 5], 1) ➞ [5]
# last([1, 2, 3, 4, 5], 1) ➞ [5]

# last([4, 3, 9, 9, 7, 6], 3) ➞ [9, 7, 6]

# last([1, 2, 3, 4, 5], 7) ➞ "invalid"

# last([1, 2, 3, 4, 5], 0) ➞ []

# def last(a, n):
#     # if n == 0:
#     #     return []
#     # elif len(a) == 0:
#     #     return 'invalid'
#     # elif len(a) < n:
#     #     return 'invalid'
#     # return a[-n:] 
#     return 'invalid' if n>len(a) else a[len(a)-n:]

# print(last([4, 3, 9, 9, 7, 6], 3))
# print(last([1, 2, 3, 4, 5], 5))


#205
# Right Shift by Division

# shift_to_right(80, 3) ➞ 10
# shift_to_right(-24, 2) ➞ -6

# import math
# def shift_to_right(x, y):
#     return math.floor(x/pow(2,y))


# print(shift_to_right(80, 3))
# print(shift_to_right(4666, 6))
# print(shift_to_right(-5, 1))

#206
# Functioninator 8000

# inator_inator("Shrink") ➞ "Shrinkinator 6000"

# inator_inator("Doom") ➞ "Doominator 4000"

# inator_inator("EvilClone") ➞ "EvilClone-inator 9000"

# def inator_inator(inv):
#     if inv[-1].lower() in 'aeiou':
#         return '{}-inator {}000'.format(inv,len(inv))
#     else:
#         return '{}inator {}000'.format(inv,len(inv))


# print(inator_inator("bEE"))


# 207
# multiply_nums("2, 3") ➞ 6

# multiply_nums("1, 2, 3, 4") ➞ 24

# multiply_nums("54, 75, 453, 0") ➞ 0

# multiply_nums("10, -2") ➞ -20

# def multiply_nums(nums):
#     product = 1
#     for num in nums.split(', '):
#         product *= int(num)
#     return product

# print(multiply_nums("2, 3"))

#208
# Make a Circle with OOP
# circy = Circle(11)
# circy.getArea()

# Should return 380.132711084365

# circy = Circle(4.44)
# circy.getPerimeter()

# Should return 27.897342763877365

# from math import pi

# class Rectangle:
    
# 	def __init__(self, sideA=0, sideB=0):
# 		self.sideA = sideA
# 		self.sideB = sideB

# 	def getArea(self):
# 		return self.sideA * self.sideB
  
# 	def getPerimeter(self):
# 		return 2 * (self.sideA + self.sideB)

# class Circle:

#     def __init__(self, radius):
#         self.radius = radius

#     def getArea(self):
#         return pi * pow(self.radius,2)

#     def getPerimeter(self):
#         return 2 * pi * self.radius


# circle = Circle(11)
# print(circle.getArea())

# circy = Circle(4.44)
# print(circy.getPerimeter())

#209
# Odds vs. Evens
# Given an integer, return "odd" if the sum of all odd digits is greater than the sum of all even digits. Return "even" if the sum of even digits is greater than the sum of odd digits, and "equal" if both sums are the same.


# odds_vs_evens(97428) ➞ "odd"
# odds_vs_evens(81961) ➞ "even"
# odds_vs_evens(54870) ➞ "equal"

# def odds_vs_evens(num):
#     even_total =  sum(int(num) for num in str(num) if int(num) % 2 == 0)
#     odd_total =  sum(int(num) for num in str(num) if int(num) % 2 != 0)
#     return 'odd' if odd_total > even_total else 'even' if even_total > odd_total else 'equal'

# print(odds_vs_evens(97428))
