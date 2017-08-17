将一张图片均匀向右移动，向下移动，每移动一次，切割出一个固定面积的图片。
思路：
我们知道图片实际上是有一个二维数组组成的，所以先控制横坐标不变，纵坐标截取，一直到纵坐标的边界，然后向下移动横坐标，重复上一步操作。
同时在这里我设置了三个不同的截取大小。
代码：

      # -*- coding:utf-8 -*-

      from PIL import Image

      '''
         @author:xunalove
          修改文件位置
          修改图片id

      '''
      def cut(id,vx,vy):
          #打开图片图片1.jpg
          name1 = "/home/xuna/桌面/3/图片"+ id + ".jpg"
          name2 = "/home/xuna/桌面/3/图片"+ id +"_切块_"
          im =Image.open(name1)

          #偏移量
          dx = 40
          dy = 40
          n = 1

          #左上角切割
          x1 = 0
          y1 = 0
          x2 = vx
          y2 = vy

          #纵向
          while x2 <= 320:
              #横向切
              while y2 <= 480:
                  name3 = name2 + str(n) + ".jpg"
                  #print n,x1,y1,x2,y2
                  im2 = im.crop((y1, x1, y2, x2))
                  im2.save(name3)
                  y1 = y1 + dy
                  y2 = y1 + vy
                  n = n + 1
              x1 = x1 + dx
              x2 = x1 + vx
              y1 = 0
              y2 = vy

          print "图片切割成功，切割得到的子图片数为"
          return n-1


      if __name__=="__main__":

          #取图片id的后两位
          id = "1"

          #切割图片的面积 vx,vy
          #大
          res = cut(id,160,160)

          #中
          #res = cut(id,120,120)

          #小
          #res = cut(id,80,80)

          print res
