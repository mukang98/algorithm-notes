# %%
# ================================================================= #
#                        辅助函数（嵌套）                            #
# ================================================================= #
def outer_function(msg):
    message = msg

    def inner_function():
        print(message)  # 使用外部函数的局部变量message

    return inner_function  # 返回inner_function，它有访问外部变量message的能力

# 使用闭包
my_func = outer_function('Hello, World!')
my_func()  # 调用内部函数，它记住了message变量，这就是闭包
'''
闭包的本质是在返回的函数对象中保存了对外部作用域的局部变量的引用，
使得这些局部变量即使在外部函数执行结束后，仍然可以被内部函数访问。
'''
# %%
