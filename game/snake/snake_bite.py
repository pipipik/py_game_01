"""snake_bite - Copyright 20231212_01"""
import sys
import random
import pygame
from pygame.locals import QUIT, Rect

pygame.init() # pygameモジュールを初期化
SURFACE = pygame.display.set_mode((600, 600)) #サイズを指定してウィンドウを作成
FPSCLOCK = pygame.time.Clock() # クロックオブジェクトを作成

FOODS = [] # 餌の座標を格納した配列
(W, H) = (20, 20) # 画面の幅Wと高さH

def add_food():
  """ ランダムな場所に餌を配置 """
  while True:
    pos = (random.randint(0, W-1), random.randint(0, H-1)) # ランダムな座標を指定
    if pos in FOODS: # 重複を回避
      continue # ループの先頭に戻る
    FOODS.append(pos) # 座標を追加
    break # ループから抜けて呼び出し元に戻る

def paint():
  """ 画面全体の描画 """
  SURFACE.fill((0, 0, 0)) # ウィンドウを黒色(R,G,B)に塗りつぶす
  for food in FOODS: # 配列から座標を取り出し、円を描画
    pygame.draw.ellipse(SURFACE, (0, 255, 0), Rect(food[0]*30, food[1]*30, 30, 30))

  for index in range(20): # 20*20マス作成
    pygame.draw.line(SURFACE, (64, 64, 64), (index*30, 0), (index*30, 600))
    pygame.draw.line(SURFACE, (64, 64, 64), (0, index*30), (600, index*30))

  pygame.display.update() # プログラム中に描画した内容を画面に反映

def main():
  """main routine"""
  for _ in range(10):
    add_food() # 餌を10個配置

  while True:
    for event in pygame.event.get(): # イベントキューからイベントを取得
      # 終了イベントを検出した時にプログラムを終了する
      if event.type == QUIT: # イベントがQUITの時
        pygame.quit() # pygameの初期化を解除
        sys.exit() # プログラム終了

    paint() # 描画関数呼び出し
    FPSCLOCK.tick(1) # 1秒間に1回ループが実行

# 自ファイルから開始された時にmain関数が実行
if __name__ == '__main__':
  main()