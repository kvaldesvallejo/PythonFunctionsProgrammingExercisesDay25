# Your code goes here:
def render_person(name, dateOfBirth, eyeColor, age, gender):
    return (name + " is a " + str(age) + " years old " + gender + " born in " + str(dateOfBirth) + " with " + str(eyeColor) + " eyes")


# Do not edit below this line
print(render_person('Bob', '05/22/1983', 'green', 23, 'male'))