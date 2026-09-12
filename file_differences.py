"""
Project for Week 4 of "Python Data Representations".
Find differences in file contents.

Be sure to read the project description page for further information
about the expected behavior of the program.
"""

IDENTICAL = -1


def singleline_diff(line1, line2):
    """
    Inputs:
      line1 - first single line string
      line2 - second single line string
    Output:
      Returns the index where the first difference between
      line1 and line2 occurs.

      Returns IDENTICAL if the two lines are the same.
    """
    shorter = min(len(line1), len(line2))

    for idx in range(shorter):
        if line1[idx] != line2[idx]:
            return idx

    if len(line1) != len(line2):
        return shorter

    return IDENTICAL


def singleline_diff_format(line1, line2, idx):
    """
    Inputs:
      line1 - first single line string
      line2 - second single line string
      idx   - index at which to indicate difference
    Output:
      Returns a three line formatted string showing the location
      of the first difference between line1 and line2.

      If either input line contains a newline or carriage return,
      then returns an empty string.

      If idx is not a valid index, then returns an empty string.
    """
    if "\n" in line1 or "\r" in line1:
        return ""

    if "\n" in line2 or "\r" in line2:
        return ""

    if idx < 0 or idx > min(len(line1), len(line2)):
        return ""

    separator = "=" * idx + "^"

    return line1 + "\n" + separator + "\n" + line2 + "\n"


def multiline_diff(lines1, lines2):
    """
    Inputs:
      lines1 - list of single line strings
      lines2 - list of single line strings
    Output:
      Returns a tuple containing the line number (starting from 0) and
      the index in that line where the first difference between lines1
      and lines2 occurs.

      Returns (IDENTICAL, IDENTICAL) if the two lists are the same.
    """
    shorter = min(len(lines1), len(lines2))

    for line_number in range(shorter):
        idx = singleline_diff(lines1[line_number], lines2[line_number])

        if idx != IDENTICAL:
            return (line_number, idx)

    if len(lines1) != len(lines2):
        return (shorter, 0)

    return (IDENTICAL, IDENTICAL)


def get_file_lines(filename):
    """
    Inputs:
      filename - name of file to read
    Output:
      Returns a list of lines from the file named filename. Each
      line will be a single line string with no newline ('\n') or
      return ('\r') characters.

      If the file does not exist or is not readable, then the
      behavior of this function is undefined.
    """
    with open(filename, "r") as infile:
        return infile.read().splitlines()


def file_diff_format(filename1, filename2):
    """
    Inputs:
      filename1 - name of first file
      filename2 - name of second file
    Output:
      Returns a four line string showing the location of the first
      difference between the two files named by the inputs.

      If the files are identical, the function instead returns the
      string "No differences\n".

      If either file does not exist or is not readable, then the
      behavior of this function is undefined.
    """
    lines1 = get_file_lines(filename1)
    lines2 = get_file_lines(filename2)

    line_num, idx = multiline_diff(lines1, lines2)

    if line_num == IDENTICAL and idx == IDENTICAL:
        return "No differences\n"

    if line_num < len(lines1):
        line1 = lines1[line_num]
    else:
        line1 = ""

    if line_num < len(lines2):
        line2 = lines2[line_num]
    else:
        line2 = ""

    return ("Line " + str(line_num) + ":\n" +
            singleline_diff_format(line1, line2, idx))