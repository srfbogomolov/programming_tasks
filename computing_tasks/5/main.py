ROW_COUNT = 4
OFFSET_CHAR = " "
ASTERISK_CHAR = "*"


def print_asterisk():
    print(ASTERISK_CHAR, end="")


def print_offsets(count):
    print(OFFSET_CHAR * count, end="")


def print_offsets_with_asterisk(offset_count):
    if offset_count < 0:
        return
    elif offset_count > 0:
        print_offsets(offset_count)

    print_asterisk()


def main():
    external_offset_count = -1 + 2 * (ROW_COUNT - 1)
    internal_offset_count = -1

    for i in range(ROW_COUNT):
        print_offsets_with_asterisk(i)

        print_offsets_with_asterisk(external_offset_count)
        print_offsets_with_asterisk(internal_offset_count)
        print_offsets_with_asterisk(external_offset_count)

        print()

        external_offset_count -= 2
        internal_offset_count += 2


if __name__ == "__main__":
    main()
