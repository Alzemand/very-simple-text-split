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
   print("Falha no engano")
   #Chamar uma função aqui


def create_file(out_path, num, file):
   out_path = out_path + str(num) + ".txt"
   archive = open(out_path, "a")
   while True:
      if file.readline().find('-\n') > -1:
         num = num + 1
         create_file(out_path, num, file) 
      elif file.readline() == '':
         return 'Ok'
         archive.close()
      else:
         archive.write(file.readline())
   