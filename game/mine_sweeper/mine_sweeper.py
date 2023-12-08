"""mine_sweeper - Copyright 20231209_01"""
import sys
import pygame
from pygame.locals import QUIT

# グローバル変数定義
WIDTH = 20 # 横方向のマスの数
HEIGHT = 15 # 縦方向のマスの数
SIZE = 50 # 1マスの縦横のサイズ

pygame.init() # pygameモジュールを初期化
SURFACE = pygame.display.set_mode([WIDTH*SIZE, HEIGHT*SIZE]) #サイズを指定してウィンドウを作成
FPSCLOCK = pygame.time.Clock() # クロックオブジェクトを作成

def main():
  """main routine"""

  while True:
    for event in pygame.event.get(): # イベントキューからイベントを取得
      # 終了イベントを検出した時にプログラムを終了する
      if event.type == QUIT: # イベントがQUITの時
        pygame.quit() # pygameの初期化を解除
        sys.exit() # プログラム終了

    # 描画
    SURFACE.fill((0, 0, 0)) # ウィンドウを黒色(R,G,B)に塗りつぶす

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