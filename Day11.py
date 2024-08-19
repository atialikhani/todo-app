date = input("Enter today's date: ")
mood = input ("how do you rate your today from 1 to 10 ")
thoughts = input ("let your thoughts flow :\n")


with open(f"{date}.txt", "w") as file:
    file.write(mood + 2 * "\n")
    file.write(thoughts)

