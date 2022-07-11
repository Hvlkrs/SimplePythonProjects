#https://appdividend.com/2021/06/21/how-to-read-file-into-list-in-python/#:~:text=To%20read%20a%20file%20in%20Python%2C%20use%20the%20file.&text=The%20string%20split()%20is,as%20our%20Python%20program%20file.

def main():

    file1 = open('Desktop/python deneme/books.txt', 'r+')
    file_contents = file1.read()

    length = len(file_contents)
    if length == 0:
        print("Book file is empty")
    else:
        file1 = open('Desktop/python deneme/books.txt', 'r+')
        file_contents = file1.read()
        content_list = file_contents.split(",")

        nonrepeated_values = set()
        repeated_values = set()

        for book in content_list:
            if book in repeated_values:
                continue
            if book in nonrepeated_values:
                nonrepeated_values.remove(book)
                repeated_values.add(book)
            else:
                nonrepeated_values.add(book)

    print(list(nonrepeated_values))
    file1.close
main()