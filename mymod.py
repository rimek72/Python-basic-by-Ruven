print(f'Hello from {__name__}!')

x = 100

y = [10, 20, 30]

def hello(name):
    return f'Hello, {name}'


# this line means: Only execute the below block if we did *NOT* load the file via import
if __name__ == '__main__':
    print(f'Goodbye from {__name__}!')