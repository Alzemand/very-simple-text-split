import os
import time

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

# time.sleep(2)
os.system('cls' if os.name=='nt' else 'clear')

init_path = input('Enter a input .txt PATH: ')
while os.path.exists(init_path) == False:
   print('Input PATH not found, try again')
   init_path = input('Enter a input .txt PATH: ')

out_path = input('Enter a output .txt PATH: ')
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

txt_symbol = input("Enter a symbol: ")

symbol(archive, out_path, symbol)

archive.close()