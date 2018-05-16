def hello(name):
    return 'Hello, {}.'.format(name)

def test_hello():
    assert 'Hello, Fred.' == hello('Fred')

if __name__ == '__main__':
    print(hello('Taro'))
