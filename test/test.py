#!/Users/zhaoxinqiang/.pyenv/shims/python
#-*- coding:utf8 -*-
import time

def timeit(func):
  def wrapper():
    print "func is begin!"
    start = time.clock()
    func()
    end = time.clock()
    print "used:", end - start
    print "func is end!"
  return wrapper

@timeit
def foo():
  print "hello world!"

if __name__ == '__main__':
  foo()
