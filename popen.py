import subprocess_test

p = subprocess_test.Popen(["ls"], stdout=subprocess_test.PIPE)
output, error = p.communicate()
print(output.decode())
