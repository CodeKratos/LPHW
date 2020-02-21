from sys import argv
script  = argv
print("enter your user name ")

prompt = '>'
user_name = input(prompt)
print(f"Hi {user_name} ! I am the Awasys version 1.0. I run on the script {script}")
print("I would like to ask you some questions.")
print("Do you like machines ?")
response = input(prompt)

print(f"Why did you said : {response}? Any specific reason ?")
reason = input(prompt) 

print(f" Hmmmm ! {reason}. You have some content")


