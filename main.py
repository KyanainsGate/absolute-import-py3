import top
from module import m2
from module import m1  # Without __init__.py in module/, this import will fail.
from module.child import m3
from module.child import m4  # As "module/child" is registered in __init__.py yb defining PKGS it works

if __name__ == '__main__':
    # Top directory
    top.hello()

    # Parent dir
    print(m2.hello())
    print(m1.hello_1())

    # Child dir
    m3.hellom3()
    m4.hellom4()
    pass
