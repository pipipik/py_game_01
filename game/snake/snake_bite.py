"""snake_bite - Copyright 20231212_01"""
import sys
import random
import pygame
from pygame.locals import QUIT, Rect, KEYDOWN, K_LEFT, K_RIGHT, K_UP, K_DOWN

pygame.init() # pygameモジュールを初期化
SURFACE = pygame.display.set_mode((600, 600)) #サイズを指定してウィンドウを作成
FPSCLOCK = pygame.time.Clock() # クロックオブジェクトを作成

FOODS = [] # 餌の座標を格納した配列
SNAKE = [] # へびの座標を格納した配列
(W, H) = (20, 20) # 画面の幅Wと高さH

def add_food():
  """ ランダムな場所に餌を配置 """
  while True:
    pos = (random.randint(0, W-1), random.randint(0, H-1)) # ランダムな座標を指定
    if pos in FOODS or pos in SNAKE: # 重複を回避
      continue # ループの先頭に戻る
    FOODS.append(pos) # 座標を追加
    break # ループから抜けて呼び出し元に戻る

def move_food(pos):
  """ 餌を別の場所へ移動 """
  i = FOODS.index(pos) # 座標のindexを取得
  del FOODS[i] # 座標を削除
  add_food() # 餌を追加

def paint():
  """ 画面全体の描画 """
  SURFACE.fill((0, 0, 0)) # ウィンドウを黒色(R,G,B)に塗りつぶす
  for food in FOODS: # 配列から座標を取り出し、円を描画
    pygame.draw.ellipse(SURFACE, (0, 255, 0), Rect(food[0]*30, food[1]*30, 30, 30))

  for body in SNAKE: # 配列から座標を取り出し、矩形を描画
    pygame.draw.rect(SURFACE, (0, 255, 255), Rect(body[0]*30, body[1]*30, 30, 30))

  for index in range(20): # 20*20マス作成
    pygame.draw.line(SURFACE, (64, 64, 64), (index*30, 0), (index*30, 600))
    pygame.draw.line(SURFACE, (64, 64, 64), (0, index*30), (600, index*30))

  pygame.display.update() # プログラム中に描画した内容を画面に反映

def main():
  """main routine"""
  key = K_DOWN # 初期状態は下キー
  SNAKE.append((int(W/2), int(H/2))) # 初期状態は画面中央
  for _ in range(10):
    add_food() # 餌を10個配置

  while True:
    for event in pygame.event.get(): # イベントキューからイベントを取得
      # 終了イベントを検出した時にプログラムを終了する
      if event.type == QUIT: # イベントがQUITの時
        pygame.quit() # pygameの初期化を解除
        sys.exit() # プログラム終了
      elif event.type == KEYDOWN: # キー押下
        key = event.key

    if key == K_LEFT: # 左キー: x座標を-1
      head = (SNAKE[0][0] - 1, SNAKE[0][1])
    elif key == K_RIGHT: # 右キー: x座標を+1
      head = (SNAKE[0][0] + 1, SNAKE[0][1])
    elif key == K_UP: # 上キー: y座標を-1
      head = (SNAKE[0][0], SNAKE[0][1] - 1)
    elif key == K_DOWN: # 下キー: y座標を+1
      head = (SNAKE[0][0], SNAKE[0][1] + 1)

    SNAKE.insert(0, head) # キーに応じて要素を追加
    if head in FOODS: # 先頭headの座標に餌があった時
      move_food(head) # 餌を移動する関数呼び出し
    else:
      SNAKE.pop() # 末尾の座標を削除

    paint() # 描画関数呼び出し
    FPSCLOCK.tick(5) # 1秒間に5回ループが実行

# 自ファイルから開始された時にmain関数が実行
if __name__ == '__main__':
  main()