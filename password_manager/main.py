from cryptography.fernet import Fernet

'''
def write_key():
  key = Fernet.generate_key()
  with open('key.key','wb') as key_file:
    key_file.write(key)
'''
def load_key():
  file = open('key.key','rb')
  key = file.read()
  file.close()
  return key


key = load_key()
fer = Fernet(key)


def view():
  with open('passwords.txt', 'r') as f:
    for line in f.readlines():
      line = line.rstrip()
      name, password = line.split('|')
      print('Account name:', name , 'Password:',fer.decrypt(password.encode()).decode())
def add():
  name = input('Account Name: ')
  password = input('Password: ')

  with open('passwords.txt', 'a') as f:
    f.write(name + '|'+ fer.encrypt(password.encode()).decode() + "\n")

while True:
  mode = input('Would you like to add a new password or view existing ones (view,add, or q to quit)? ').lower()
  if mode == 'view':
   view()
  elif mode == 'add':
    add()
  elif mode == 'q':
    break
  else:
   print('Invalid mode')
   continue