import os
import time
import sys 

print('''

██╗   ██╗███████╗██████╗ ██╗   ██╗    ███████╗██╗███╗   ███╗██████╗ ██╗     ███████╗
██║   ██║██╔════╝██╔══██╗╚██╗ ██╔╝    ██╔════╝██║████╗ ████║██╔══██╗██║     ██╔════╝
██║   ██║█████╗  ██████╔╝ ╚████╔╝     ███████╗██║██╔████╔██║██████╔╝██║     █████╗  
╚██╗ ██╔╝██╔══╝  ██╔══██╗  ╚██╔╝      ╚════██║██║██║╚██╔╝██║██╔═══╝ ██║     ██╔══╝  
 ╚████╔╝ ███████╗██║  ██║   ██║       ███████║██║██║ ╚═╝ ██║██║     ███████╗███████╗
  ╚═══╝  ╚══════╝╚═╝  ╚═╝   ╚═╝       ╚══════╝╚═╝╚═╝     ╚═╝╚═╝     ╚══════╝╚══════╝
                                                                                    
████████╗██╗  ██╗████████╗    ███████╗██████╗ ██╗     ██╗████████╗                  
╚══██╔══╝╚██╗██╔╝╚══██╔══╝    ██╔════╝██╔══██╗██║     ██║╚══██╔══╝                  
   ██║    ╚███╔╝    ██║       ███████╗██████╔╝██║     ██║   ██║                     
   ██║    ██╔██╗    ██║       ╚════██║██╔═══╝ ██║     ██║   ██║                     
██╗██║   ██╔╝ ██╗   ██║       ███████║██║     ███████╗██║   ██║                     
╚═╝╚═╝   ╚═╝  ╚═╝   ╚═╝       ╚══════╝╚═╝     ╚══════╝╚═╝   ╚═╝                                                                       
''')

def create_file(out_path, num_file):
   new_file = open(out_path + str(num_file) + ".txt", "w")
   return new_file

def symbol(archive, out_path, symbol):
   num_file = 1
   new_file = create_file(out_path, num_file)
   for x in archive:
      if x.find(str(symbol) + '\n') > -1:
         num_file = num_file + 1
         new_file.close()
         new_file = create_file(out_path, num_file)
      else:
         new_file.write(x)

def by_lines(archive, out_path, number): 
   num_file = 1
   new_file = create_file(out_path, num_file)
   number = int(number)
   increment = number
   cont = 1
   for x in archive:
      if cont <= number:
         new_file.write(x)
         cont = cont + 1
      else:
         num_file = num_file + 1
         new_file.close()
         new_file = create_file(out_path, num_file)
         number = number + increment
         
def check_path(path):
   if os.name=='nt':
      return path + "/"
   else:
      return path

time.sleep(2)
os.system('cls' if os.name=='nt' else 'clear')

init_path = input('Enter a input .txt PATH: ')
init_path = check_path(init_path)
while os.path.exists(init_path) == False:
   print('Input PATH not found, try again')
   init_path = input('Enter a input .txt PATH: ')

out_path = input('Enter a output .txt PATH: ')
out_path = check_path(out_path)
while os.path.exists(out_path) == False:
   print('PATH not found, try again')
   out_path = input('Enter a out .txt PATH: ')

aux = 1
file_list = os.listdir(init_path)
for x in os.listdir(init_path):
   print(str(aux), " - ", x)
   aux += 1

aux = input('Select a file number: ')
init_path = init_path + str(file_list[int(aux) - 1])

try:
   archive = open(init_path, "r")
except:
   print("File or Directory not found")
   sys.exit()
   
print('\n')
print(
"""Select a operation:
1 - Use a Symbol for Splittig
2 - Size Splittig
3 - Separate by Lines
4 - Use a Regex for Splittig""")
print("\n")

opt = input("Option: ")
if opt == '1':
   txt_symbol = input("Enter a symbol: ")
   symbol(archive, out_path, txt_symbol)
elif opt == '3':
   number = input("Enter a line number: ")
   by_lines(archive, out_path, number)
else:
   print("Why did you put an invalid option??? What's your problem???")

archive.close()

print("Finish!")
