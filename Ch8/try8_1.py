import utils
answer = utils.get_yesno("yes or no")
print(answer)

def describe_pet(animal_type, pet_name="www"):
    print("\n I have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")


describe_pet(animal_type="cat", pet_name="pp")
describe_pet("bruh", "dog")
describe_pet("wolf")


def build_person(first_name, last_name, age=''):
    person = {'first': first_name, 'last': last_name}
    if age:
        person['age'] = age
    return person


somebody = build_person('Bob', 'Jonson', 123)
print(somebody)


def say_hello(friends):
    for f in friends:
        print("Hello," + f)

say_hello(['Andy', 'Allan', 'Harry'])