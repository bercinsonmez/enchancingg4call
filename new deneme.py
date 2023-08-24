def split_sequences_by_structure(sequence, structure):
    split_sequences = []
    current_sequence = ""
    current_position = 0
    current_level = 0

    for k,v in Open:
        if char == "(":
            if current_sequence:
                split_sequences.append((current_level, current_sequence, current_position))
                current_sequence = ""
            current_level += 1
        elif char == ".":
            current_sequence += sequence[i]
        elif char == ")":
            if current_sequence:
                split_sequences.append((current_level, current_sequence, current_position))
                current_sequence = ""
            current_level -= 1
        current_position += 1

    if current_sequence:
        split_sequences.append((0, current_sequence, current_position))

    return split_sequences


if __name__ == "__main__":


    split_sequences = split_sequences_by_structure(sequence, structure)

    for level, seq, pos in split_sequences:
        print(level, seq, pos)