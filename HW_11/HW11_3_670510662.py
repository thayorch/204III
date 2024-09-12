#!usr/bin/env python3
# Thadchanon Maidee (Ice-lnwza)
# 670510662
# HW11_3
# 204111 Sec 001


def runner_up() -> None:
    students_count = int(input("Total students: "))
    max_score = 0.0
    runner_up = 0.0
    average = 0.0

    for i in range(students_count):
        current_point = float(input("Enter score: "))
        average += current_point

        if current_point > max_score:
            runner_up = max_score
            max_score = current_point
        elif current_point > runner_up and current_point != max_score:
            runner_up = current_point


    print("---")

    if runner_up == 0.0:
        runner_up = None
        print(f"Max score is: {max_score:.2f}")
        print(f"Runner up is: {runner_up}")
        print(f"Average is: {(average/students_count):.2f}")
    else:
        print(f"Max score is: {max_score:.2f}")
        print(f"Runner up is: {runner_up:.2f}")
        print(f"Average is: {(average/students_count):.2f}")


if __name__ == "__main__":
    runner_up()
