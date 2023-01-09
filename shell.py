from click_shell import shell

@shell(prompt='amt.shell -> ', intro='enter the commands you want for more type help')
def my_shell():
    pass


@my_shell.command()
def help():
    print('''this is your shell guide
        1- add: add two numbers
        2- hello: to print a message''')


@my_shell.command()
def add():
    x = int(input('enter n1 '))
    y = int(input('enter n2 '))
    print(x+y)


@my_shell.command()
def hello():
    print('hello world!')


if __name__ == '__main__':
    my_shell()
