import termcolor
#print(dir(termcolor))
#print(help(termcolor))

print(termcolor.colored("Hi everyone!", color="cyan", on_color="on_green"))
print(termcolor.colored("Hi everyone!", color="cyan", on_color="on_green",attrs=["bold"]))
print(termcolor.colored("Hi everyone!", color="cyan",attrs=["blink","bold"]))

#===============================================================================================

import pyfiglet
print(help(pyfiglet.figlet_format))
result = pyfiglet.figlet_format("Bananas")
print(result)

 