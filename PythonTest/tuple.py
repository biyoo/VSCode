'''
def divide_and_remainder(a,b):
    quotient=a//b
    remainder=a%b
    return quotient, remainder

result=divide_and_remainder(10,3)
print(result)
quotient, remainder =divide_and_remainder(10,3)
print(quotient,remainder)




x,y=5,10
print(x,y)
x,y=y,x
print(x,y)

fruits=('apple','banana','cherry')
for index, fruit in enumerate(fruits):
    print(f"{index}: {fruit}")


def func(*args):
    print("Type:", type(args))
    print("Length:", len(args))
    print(args)

func([1,2],3,4,(5))


def func(**kwargs):
    print("Type:", type(kwargs))
    print("Length:", len(kwargs))
    print(kwargs)

func(a=1,b=2,c=3)


def func(*data, **method):
    num=sum(data)*method["scale"]
    print(num,method["unit"]+"입니다")
    

func(3,4,5,scale=10,unit="개")

'''



class daesung:
    '''
    test
    '''
    def __new__(cls,*args,**kwargs):
        print("인스턴스 할당")
        return super(daesung,cls).__new__(cls)
    
    def __init__(self,site="076923"):
        print("인스턴스 초기화")
        self.site=site
        self.link=site+".github.io"
        
    def __call__(self,protocol=True):
        print("인스턴스 호출")
        if protocol==True:
            return "https://" + self.link
        else:
            return "http://" + self.link
        
    def __del__(self):
        print("인스턴스 소멸")
    
instance=daesung()
print(instance.link)
print(instance(False))
del instance




class Daeheeyun:
    """ Daeheeyun CLASS
    
    Callable types example.
    blah blah..

    To use:
    >>> instance = Daeheeyun(value)

    Args:
        value   : int
    
    Returns:
        null
    """

    def __init__(self, value: int):
        self.value = value

    def func(self) -> int:
        """func : Execute value * 2"""
        return self.value * 2


instance = Daeheeyun(5)

print(instance.__doc__)
print("---------")
print(instance.func.__doc__)
print("---------")
print(instance.func.__name__)
print(instance.func.__qualname__)
print(instance.func.__module__)
print(instance.func.__annotations__)
print(instance.__dict__)