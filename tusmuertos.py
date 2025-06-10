def read_file(filename):
    assert filename!= "", "Filename cannot be empty"
    with open(filename,'r') as file:
        content = file.read()
        print(content)
read_file('tusmuertos.txt')