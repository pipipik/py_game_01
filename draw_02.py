"""draw_polygon.py"""
import sys
from math import sin, cos, radians
import pygame
from pygame.locals import QUIT

pygame.init() # pygameモジュールを初期化
SURFACE = pygame.display.set_mode((400, 300)) #サイズを指定してウィンドウを作成
FPSCLOCK = pygame.time.Clock() # クロックオブジェクトを作成

def main():
  """main routine"""

  while True:
    for event in pygame.event.get(): # イベントキューからイベントを取得
      # 終了イベントを検出した時にプログラムを終了する
      if event.type == QUIT: # イベントがQUITの時
        pygame.quit() # pygameの初期化を解除
        sys.exit() # プログラム終了

    SURFACE.fill((0, 0, 0)) # ウィンドウを黒色(R,G,B)に塗りつぶす
    
    # 多角形(ポリゴン)
    pointlist0, pointlist1 = [], [] # 点のリストを初期化
    for theta in range(0, 360, 72): # 0°から360°まで72ずつの幅で増加するtheta
      rad = radians(theta) #度数法[°]→弧度法[rad]に単位変換
      pointlist0.append((cos(rad)*100 + 100, sin(rad)*100 + 150)) # (100, 150)を中心に点のリストを作成
      pointlist1.append((cos(rad)*100 + 300, sin(rad)*100 + 150)) # (300, 150)を中心に点のリストを作成
    # linesで作成した多角形
    pygame.draw.lines(SURFACE, (255, 255, 255), True, pointlist0)
    # lines(SURFACE: ベース画面オブジェクト, color: 色, pointlist: 点のリスト, width: 線の幅(0の時は塗りつぶし))
    pygame.draw.polygon(SURFACE, (255, 255, 255), pointlist1)

    pygame.display.update() # プログラム中に描画した内容を画面に反映
    FPSCLOCK.tick(1) # 1秒間に10回ループが実行

# 自ファイルから開始された時にmain関数が実行
if __name__ == '__main__':
  main()
