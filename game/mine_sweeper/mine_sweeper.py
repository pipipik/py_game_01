"""mine_sweeper - Copyright 20231209_01"""
import sys
import pygame
from random import randint
from pygame.locals import QUIT

# グローバル変数定義
WIDTH = 20 # 横方向のマスの数
HEIGHT = 15 # 縦方向のマスの数
SIZE = 50 # 1マスの縦横のサイズ
NUM_OF_BOMBS = 20 # 爆弾の数
EMPTY = 0 # マップ上のタイルがからの状態
BOMB = 1 # マップ上のタイルに爆弾がある状態

pygame.init() # pygameモジュールを初期化
SURFACE = pygame.display.set_mode([WIDTH*SIZE, HEIGHT*SIZE]) #サイズを指定してウィンドウを作成
FPSCLOCK = pygame.time.Clock() # クロックオブジェクトを作成

def main():
  """main routine"""

  # field1状態をからで初期化 field(list) = [0, 0, ...], [0, ...], ...
  field = [[EMPTY for xpos in range(WIDTH)] for ypos in range(HEIGHT)]

  # 爆弾を設置
  count = 0
  while count < NUM_OF_BOMBS: # 爆弾の数分繰り返す
    xpos, ypos = randint(0, WIDTH-1), randint(0, HEIGHT-1) # (x, y)座標をランダムに指定
    if field[ypos][xpos] == EMPTY: # 重複を避けるため、field状態がからの時
      field[ypos][xpos] = BOMB # 爆弾を設置
      count += 1 # 設置できたらカウントアップ

  while True:
    for event in pygame.event.get(): # イベントキューからイベントを取得
      # 終了イベントを検出した時にプログラムを終了する
      if event.type == QUIT: # イベントがQUITの時
        pygame.quit() # pygameの初期化を解除
        sys.exit() # プログラム終了

    # 描画
    SURFACE.fill((0, 0, 0)) # ウィンドウを黒色(R,G,B)に塗りつぶす

    for ypos in range(HEIGHT):
      for xpos in range(WIDTH):
        tile = field[ypos][xpos] # 左上から順にfield状態をtileに格納
        rect = (xpos*SIZE, ypos*SIZE, SIZE, SIZE) # tileの矩形サイズを取得
        if tile == EMPTY: # field状態がENPTYの時
          pygame.draw.rect(SURFACE, (192, 192, 192), rect) # 未開封状態を描画
        elif tile == BOMB:
          pygame.draw.ellipse(SURFACE, (225, 225, 0), rect) # 爆弾有りを描画

    # 線の描画
    # line(SURFACE: ベース画面オブジェクト, color: 色, start_pos: 始点, end_pos: 終点, width: 線の幅)
    # 縦線
    for index in range(0, WIDTH*SIZE, SIZE): # 左端から右端までタイルのサイズごとにx座標を指定
      pygame.draw.line(SURFACE, (96, 96, 96), (index, 0), (index, HEIGHT*SIZE))
    # 横線
    for index in range(0, HEIGHT*SIZE, SIZE): # 上端から下端までタイルのサイズごとにy座標を指定
      pygame.draw.line(SURFACE, (96, 96, 96), (0, index), (WIDTH*SIZE, index))

    pygame.display.update() # プログラム中に描画した内容を画面に反映
    FPSCLOCK.tick(1) # 1秒間に1回ループが実行

# 自ファイルから開始された時にmain関数が実行
if __name__ == '__main__':
  main()