f = open('hi.txt', 'w')
try:
    f.write('hi')
finally:
    f.close()
# finally 절은 try문 수행 도중 예외 발생 여부에 상관없이 항상 수행된다.
# finally 절은 사용한 리소스를 close 해야 할 때에 많이 사용한다.
