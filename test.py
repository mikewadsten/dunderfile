from dunderfile import __FILE__, __LINE__, __func__, helper


assert __FILE__() == __file__
assert helper.__FILE__ == __FILE__()
assert helper.__LINE__ == __LINE__()
# Because we're at top-level in the module.
assert __func__() == '<module>'

def my_function():
    assert __func__() == 'my_function'
    assert __func__() == helper.__func__
my_function()
