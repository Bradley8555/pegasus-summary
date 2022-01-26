import os


def textExtractFirstLine():
    # Opening Source text file to read content
    with open(r"output.txt") as f1:
        # Fetching first line of the text file
        lines = f1.read()
        first = lines.split('\n', 1)[0]
    # Writing into destination file
    with open(r"topegasus.txt", 'w') as f2:
        f2.write(first)


textExtractFirstLine()
