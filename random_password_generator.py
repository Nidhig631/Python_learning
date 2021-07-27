# random is a  module in python
import random
passlen = int(input("enter the length of password"))
s = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"
# sample is inbuilt function of a random module(takes two parameters
# (s can be list , tuple or set
# join() method is a string method and returns a string in which the elements of sequence have been joined by
# str separator
p = "".join(random.sample(s,passlen))
print(p)