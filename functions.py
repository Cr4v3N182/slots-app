import random
# get a data from csv
with open("data.csv", "r") as file:
    data = file.readline()
    user_list = data.split(",")

# storing a data into vars
user_value = user_list[0]
money_value = int(user_list[1])

# list of items in machin wheels
machine_list = ["Leprachaun", "Goldbar", "Pyramid", "Blackcat"]

# getting random sample and assigning it to a variables.
wheel_one = random.sample(machine_list,1)
wheel_two = random.sample(machine_list,1)
wheel_three = random.sample(machine_list,1)



result_list = []
