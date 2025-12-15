import os


'''
playing with string method rfind(),
saw it in the background of a DS and algorithms
video and got curious. also used basic string slicing to start at target and end at next "." in the text.

also  a last minute option to reverse the found string.

sorry for the messy global scope but i was having fun
'''

string ='''
Ruby is an elegant programming language that emphasizes developer happiness and productivity. Created by Yukihiro Matsumoto, Ruby features clean syntax that reads almost like natural language. The Ruby community values writing beautiful, expressive code that's easy to understand and maintain.
Ruby on Rails revolutionized web development when David Heinemeier Hansson extracted it from Basecamp. Rails embraced Ruby's philosophy, introducing convention over configuration and don't repeat yourself principles. Ruby on Rails enables developers to build sophisticated web applications rapidly, making Ruby an excellent choice for startups and established companies alike.
The Ruby ecosystem offers powerful gems that extend Ruby's capabilities. RubyGems serves as Ruby's package manager, providing thousands of libraries. Ruby's metaprogramming features allow developers to write incredibly flexible code, while Ruby's blocks and iterators make data manipulation elegant.
Modern Ruby continues evolving with each release. Ruby 3 introduced significant performance improvements, making Ruby applications faster than ever. Whether you're building APIs, web applications, or automation scripts, Ruby remains a delightful language. The Ruby community maintains exceptional documentation and tutorials, ensuring newcomers can learn Ruby effectively. Ruby's influence extends beyond Rails, powering tools like Jekyll, Vagrant, and Homebrew.
'''
target = input('what is your target?:\n')

#this will find the index of the last instance of the target, used casefold() method to normalize input instead of lower() since there are some edge cases where it gives errors like with that one capital german leter that lower() converts into "ss" instead of the right character
uwu = string.casefold().rfind(target)
period_position = string.find('.', uwu)

os.system('clear')
result = f'Result:\n\nthe last instance of \"{target}\" is at index number {uwu}\n'

print(result)

uwu_to_dot = string[uwu:period_position]
    
"with this i will print the entire string starting at the index found"
print(f'\"{uwu_to_dot}\"\n')

def backwards(i):
    #and just for fun here is how id reverse it
    print(uwu_to_dot[::-1])

back=input('do u wanna see it backwards?\n\n')
os.system('clear')

if "yes" in back:
    backwards(uwu_to_dot)
else:
    print('k bye!')
