def count_light_changes(status_list):
    changes = 0
    for i in range(1, len(status_list)):
        if status_list[i] != status_list[i - 1]:
            changes += 1
    return changes
def main():
    while True:    # Infinite loop for continuous input
        try:
            n = int(input("Enter the number of seconds (or -1 to exit): "))
            if n == -1:
                print("Exiting the program.")
                break  # Exit the loop if the user enters -1
            if n <= 0:
                print("Please enter a positive integer.")
                continue  # Prompt for input again
