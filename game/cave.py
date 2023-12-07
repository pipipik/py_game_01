"""cave - Copyright 20231201_01"""
import sys
import pygame
from pygame.locals import QUIT, Rect

pygame.init() # pygameモジュールを初期化
SURFACE = pygame.display.set_mode((800, 600)) #サイズを指定してウィンドウを作成
FPSCLOCK = pygame.time.Clock() # クロックオブジェクトを作成

def main():
  """main routine"""
  walls = 80 # 矩形の数
  holes = [] # 矩形を格納する配列を初期化
  for xpos in range(walls): # x座標を10ずつずらしながら80個の矩形を作成
    holes.append(Rect(xpos * 10, 100, 10, 400)) # (x, y, width, height)

  while True:
    for event in pygame.event.get(): # イベントキューからイベントを取得
      # 終了イベントを検出した時にプログラムを終了する
      if event.type == QUIT: # イベントがQUITの時
        pygame.quit() # pygameの初期化を解除
        sys.exit() # プログラム終了

    # 描画
    SURFACE.fill((0, 255, 0)) # ウィンドウを緑色(R,G,B)に塗りつぶす
    for hole in holes: # 画面オブジェクトに黒色の矩形リストholesを描画
      pygame.draw.rect(SURFACE, (0, 0, 0), hole)

    pygame.display.update() # プログラム中に描画した内容を画面に反映
    FPSCLOCK.tick(10) # 1秒間に10回ループが実行

# 自ファイルから開始された時にmain関数が実行
if __name__ == '__main__':
  main()