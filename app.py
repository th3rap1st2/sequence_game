def get_whole_number() -> str:
    while True:
        try:
            number = input("Enter a whole number: ")

            if number.isdigit() and int(number) > 0:
                return number
            else:
                print("Invalid input! Please enter a positive whole number.")

        except ValueError:
            print("Invalid input! Please enter a positive whole number.")


def get_pieces(number) -> str:
    while True:

        try:
            pieces = input("Enter the number of digits in each piece: ")

            if int(pieces) > 0 and len(number) % int(pieces) == 0:
                return pieces
            else:
                print(f"Invalid input! The piece length must be a divisor of the length of {number}")

        except ValueError:
            print(f"Invalid input! The piece length must be a divisor of the length of {number}")


def check_sequence(number, piece_length):
    new_list = []
    i = 0
    while i < len(number):
        new_list.append(number[i: piece_length + i])
        i = piece_length + i

    increasing_sequence(new_list)
    decreasing_sequence(new_list)

    return new_list


def increasing_sequence(sequence):
    i = 1
    prev = int(sequence[0])

    while i < len(sequence):
        if prev >= int(sequence[i]):
            return False

        prev = int(sequence[i])
        i += 1

    return True


def decreasing_sequence(sequence):
    i = 1
    prev = int(sequence[0])

    while i < len(sequence):
        if prev <= int(sequence[i]):
            return False

        prev = int(sequence[i])
        i += 1

    return True


def main():
    print("Welcome to the Number Sequence Game!\n"
          "------------------------------------\n")

    inc_score = 0
    dec_score = 0

    while inc_score != 5:
        number = get_whole_number()
        pieces = get_pieces(number)
        sequence = check_sequence(number, int(pieces))
        new_s = ', '.join(sequence)
        print(f"Pieces: {new_s}")

        if increasing_sequence(sequence):
            print("The pieces are in numerically increasing order!")
            inc_score += 1
        else:
            if decreasing_sequence(sequence):
                dec_score += 1
            print("The pieces are not in numerically increasing order.")

        print(f"Numerically Increasing Sequences: {inc_score}")
        print(f"Numerically Decreasing Sequences: {dec_score}\n")

    print("\nCongratulations! You've reached 5 numerically increasing sequences. You won!")


if __name__ == "__main__":
    main()
