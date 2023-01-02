def format_name(f_name, l_name):
  if f_name == "" or l_name == "":
    return "Please, provide valid inputs."
  return f"Your formatted names is as follows: {f_name.title()} {l_name.title()}"

#Storing output in a variable
formatted_name = format_name(input("Your first name: "), input("Your last name: "))
print(formatted_name)
