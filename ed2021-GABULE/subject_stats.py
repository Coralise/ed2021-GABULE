
# rectangles = lambda n: sum(sum(i for i in range(n+1))*j for j in range(n+1))

# for i in range(11):
#     print(rectangles(i))
    
# # rectangles2=lambda m:.25*(m**2+m)**2

# # for i in range(11):
# #     print(rectangles2(i))
    
# # rectangles3 = lambda m: (m*.5*(m+1))**2

# # for i in range(11):
# #     print(rectangles3(i))
    
# # first_n_vowels = lambda s,n: ''.join([j for j in s if j in 'aeiou'][i] for i in range(n)) if len([j for j in s if j in 'aeiou']) >= n else 'invalid'

# # print(first_n_vowels("sharpening skills", 3))
# # print(first_n_vowels("major league", 5))
# # print(first_n_vowels("hostess", 5))

# # find_broken_keys = lambda x,y: list(dict.fromkeys([x[i] for i in range(len(x)) if x[i] != y[i]]))

# # print(find_broken_keys("beethoven", "affthoif5"))

# # freed_prisoners = lambda p:  if p[0] == 1 else 0

# from itertools import count


# def freed_prisoners(p):
#     if p[0] == 0:
#         return 0
#     f = 0
#     for i in p:
#         if i == 1:
#             f+=1
#             for j in range(len(p)):
#                 p[j] = {0:1,1:0}[p[j]]
#     return f

# def freed_prisoners6(p):
#     if p[0] == 0:
#         return 0
#     f = 0
#     for i in p:
#         if i == 1:
#             f+=1
#             for j in range(len(p)):
#                 p[j] = {0:1,1:0}[p[j]]
#     return f

# # freed_prisoners2 = lambda p: [i for i in map(lambda i,p: [{0:1,1:0}[j] for j in p] if i == 1 else p, i, p) if i == 1] if p[0] == 1 else 0

# # freed_prisoners3 = lambda p: 

# def freed_prisoners4(p):
#     if p[0] == 0:
#         return 0
#     f = 0
#     for i in p:
#         if (f%2)+i == 1:
#             f+=1
#     return f

# def freed_prisoners6(p):
#     if p[0] == 0:
#         return 0
#     f = []
#     for i in p:
#         f.append((sum(f)%2)+i)
#     return f.count(1)

# freed_prisoners7 = lambda p: [((sum()%2)+i) for i in p] if p[0] == 1 else 0

# # freed_prisoners5 = lambda p: [(f := 0)+1 for i in p if (f%2)+i == 1] if p[0] == 1 else 0

# print(freed_prisoners([1, 1, 0, 0, 0, 1, 0]))
# print(freed_prisoners([1, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 1, 0, 1, 0, 1, 1]))
# print(freed_prisoners([1, 1, 1]))
# print(freed_prisoners([0, 0, 0]))
# print(freed_prisoners([0, 1, 1, 1]))
# print("split")
# print(freed_prisoners6([1, 1, 0, 0, 0, 1, 0]))
# print(freed_prisoners6([1, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 1, 0, 1, 0, 1, 1]))
# print(freed_prisoners6([1, 1, 1]))
# print(freed_prisoners6([0, 0, 0]))
# print(freed_prisoners6([0, 1, 1, 1]))
# print("split")
# print(freed_prisoners7([1, 1, 0, 0, 0, 1, 0]))
# print(freed_prisoners7([1, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 1, 0, 1, 0, 1, 1]))
# print(freed_prisoners7([1, 1, 1]))
# print(freed_prisoners7([0, 0, 0]))
# print(freed_prisoners7([0, 1, 1, 1]))
# print("split")
# # print((f := len(f) for i in [1,1,1,1]))

# is_valid_phone_number = lambda n: bool(__import__("re").match(r"\(([0-9]){3}\) ([0-9]){3}-([0-9]){4}", n))

# print(is_valid_phone_number("(123) 456-7890"))
# print(is_valid_phone_number("1111)555 2345"))

# color_pattern_times = lambda l: sum([2 if i==0 or l[i]==l[i-1] else 3 for i in range(len(l))])

# print(color_pattern_times(["Red", "Blue", "Red", "Blue", "Red"]))
# print(color_pattern_times(["Red", "Yellow", "Green", "Blue"]))
# print(color_pattern_times(["Blue", "Blue", "Blue", "Red", "Red", "Red"]))
# print(color_pattern_times(["Blue"]))