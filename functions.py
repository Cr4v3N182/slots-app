import random
# get a data from csv
with open("data.csv", "r") as file:
    data = file.readline()
    user_list = data.split(",")

result_list = []

# storing a data into vars
user_value = user_list[0]
money_value = int(user_list[1])

# list of items in machin wheels
machine_list = ["Leprachaun", "Goldbar", "Pyramid", "Blackcat"]
def spin():
    # getting random sample and assigning it to a variables.
    wheel_one = random.sample(machine_list,1)
    wheel_two = random.sample(machine_list,1)
    wheel_three = random.sample(machine_list,1)
    work_list = [wheel_one, wheel_two, wheel_three]
    new_list = [item for sublist in work_list for item in sublist]
    return new_list

# creating a result list witch will be added to main as a sg.Text
result_list = spin()
print(result_list)


