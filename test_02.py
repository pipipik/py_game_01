"""fps_test2.py"""
import sys
import pygame
from pygame.locals import QUIT

pygame.init() # pygameモジュールを初期化
SURFACE = pygame.display.set_mode((400, 300)) #サイズを指定してウィンドウを作成
pygame.display.set_caption("Just Window") # ウィンドウのタイトルを設定

def main():
  """main routine"""
  while True:
    SURFACE.fill((255, 255, 255)) # ウィンドウを白色(R,G,B)に塗りつぶす

    for event in pygame.event.get(): # イベントキューからイベントを取得
      # 終了イベントを検出した時にプログラムを終了する
      if event.type == QUIT: # イベントがQUITの時
        pygame.quit() # pygameの初期化を解除
        sys.exit() # プログラム終了

    pygame.display.update() # プログラム中に描画した内容を画面に反映

# 自ファイルから開始された時にmain関数が実行
if __name__ == '__main__':
  main()
