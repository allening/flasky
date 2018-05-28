def a(b):
  def c():
    b()
    print "hello"
  return c

def b():
  print "world!"

a(b)(c)
