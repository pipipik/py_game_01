"""draw_circle_onclick.py"""
# クリックした場所に点を描画
import sys
import pygame
from pygame.locals import QUIT, MOUSEBUTTONDOWN

pygame.init() # pygameモジュールを初期化
SURFACE = pygame.display.set_mode((400, 300)) #サイズを指定してウィンドウを作成
FPSCLOCK = pygame.time.Clock() # クロックオブジェクトを作成

def main():
  """main routine"""
  mousepos = [] # マウスポジションを初期化

  while True:
    SURFACE.fill((255, 255, 255)) # ウィンドウを白色(R,G,B)に塗りつぶす

    for event in pygame.event.get(): # イベントキューからイベントを取得
      # 終了イベントを検出した時にプログラムを終了する
      if event.type == QUIT: # イベントがQUITの時
        pygame.quit() # pygameの初期化を解除
        sys.exit() # プログラム終了
      elif event.type == MOUSEBUTTONDOWN: # マウスの押下
        # マウス座標をリストに追加
        mousepos.append(event.pos) # event.pos: マウスの座標(x, y)タプル型
    # リストを1つ1つ座標を取り出し円(緑色, 太さ5)を描画
    for i, j in mousepos:
      pygame.draw.circle(SURFACE, (0, 255, 0), (i, j), 5)

    pygame.display.update() # プログラム中に描画した内容を画面に反映
    FPSCLOCK.tick(10) # 10秒間に1回ループが実行

# 自ファイルから開始された時にmain関数が実行
if __name__ == '__main__':
  main()