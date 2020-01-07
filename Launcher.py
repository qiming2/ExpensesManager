
from Manager import Manager

# print("ov" + "\t" + str(29) + "\t" + str(38) + "\n" + "bibu")
# peter = Account("ov")
# man = Manager()
# man.add_person("ov")
# man.add_person("peter")
# man.add_payed(99.132, "peter")
# man.add_expense(28.3, "ov")
# print(str(man.get_bill()))


def main():
    manager = Manager()
    print("Hi, Welcome to Peter's crappy 3-hour rushed bill manager")
    print("Below is the basic instructions (PS: instructions are case-insensitive)")
    print("1. Add people into current bill: People Person1 person2 PeRson3")
    print("2. Add paid amount into someone's account, and who are involved: Paid PersonWhoPaid 100(number) person1"
          " person2 person3 Person4")
    print("3. Print bill: print bill")
    print("4. Quit the app: quit")
    print("5. Write out the bill into a file: Output bill")
    print("Maybe I will add some features, maybe not~~~~")
    print("I mean it is only for our convenience, right? So it does not have to be perfect!")
    while True:
        command = input("What is next instruction: ")
        commands = command.split()
        bill = ""
        length = len(commands)
        if length == 0:
            print("This is not a valid instruction")
        else:
            instruction = commands[0].lower()
            if length == 1:
                if instruction.startswith("q"):
                    break
                else:
                    print("This is not a valid instruction")
            else:
                if instruction == "people":
                    people = commands[1:]
                    for person in people:
                        manager.add_people(person)
                elif instruction == "paid":
                    amount = float(commands[2])
                    person = commands[1]
                    manager.add_paid(amount, person)
                    people = commands[3:]
                    split_amount = amount / len(people)
                    for person in people:
                        manager.add_expense(split_amount, person)
                elif instruction == "print":
                    if commands[1] == "bill":
                        bill = manager.get_bill()
                        print(bill)
                    else:
                        print("Can't you even type 'bill' correctly?")
                elif instruction == "output":
                    if commands[1] == "bill":
                        bill_file = open("bill.txt", "w")
                        if bill != "":
                            bill_file.write(bill)
                        else:
                            bill_file.write(manager.get_bill())
                        bill_file.close()
                    else:
                        print("Can't you even type 'bill' correctly?")
                elif instruction == "load":
                    if commands[1] == "bill":
                        manager.clear()
                        bill_file = open("bill.txt", "r")
                        accounts = bill_file.readlines()
                        if length != 0:
                            load_account(accounts, manager)
                        else:
                            print("Obviously, you opened up an empty pandora box ^ ^")
                        bill_file.close()
                    else:
                        print("Can't you even type 'bill' correctly?")


def load_account(accounts, manager):
    length = len(accounts)
    for index in range(1, length - 1):
        categories = accounts[index].split()
        name = categories[0]
        expense = categories[1]
        paid = categories[2]
        manager.add_people(name)
        manager.add_expense(expense, name)
        manager.add_paid(paid, name)

main()