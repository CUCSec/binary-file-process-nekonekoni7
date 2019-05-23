import struct
import os
from PIL import Image


def tamper(student_id):
  student_id =[2,0,1,8,1,1,1,2,3,0,1,2]
  with open('lenna.bmp','r+b')as f:
    f.read(54)
    a=54
    f.write(b'\x00\x00\x00') 
    for i in student_id:
     if i==0:
        n=10
      else :
        n=i
      a=a+n*3+3
      f.read(a)
      f.write(b'\x00\x00\x00') 
        



def detect():
  with open('lenna.bmp', 'rb') as f:
    bmp_file_header = f.read(14)

    bm, size, r1, r2, offset = struct.unpack('<2sIHHI', bmp_file_header)

    f.seek(offset)

    count = 12
    offset = 0
    last_offset = 0
    while count > 0:
      color = f.read(3)

      if color == b'\x00\x00\x00':

        if offset - last_offset == 10:
          print(0)
        else:
          print(offset - last_offset)

        last_offset = offset
        count -= 1

      offset += 1


if __name__ == '__main__':
  import sys
  tamper(sys.argv[1])

  detect()
