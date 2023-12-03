"""draw_04.py"""
import sys
import pygame
from pygame.locals import QUIT, Rect

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

    SURFACE.fill((255, 255, 255)) # ウィンドウを白色(R,G,B)に塗りつぶす
    
    # rect(SURFACE: ベース画面オブジェクト, color: 色, (x, y, width, height): 位置, サイズ, width: 線の幅)
    # 赤 : 矩形(塗りつぶし)
    pygame.draw.rect(SURFACE, (255,0,0), (10, 20, 100, 50))
    # 赤 : 矩形(太さ 3)
    pygame.draw.rect(SURFACE, (255, 0, 0), (150, 10, 100, 30), 3)
    # 緑 : 矩形
    pygame.draw.rect(SURFACE, (0,255,0), ((100, 80), (80, 50)))
    # 青 : 矩形、Rectオブジェクト
    rect0 = Rect(200, 60, 140, 80)
    pygame.draw.rect(SURFACE, (0, 0, 255), rect0)
    # 黄 : 矩形、Rectオブジェクト
    rect1 = Rect((30, 160), (100, 50))
    pygame.draw.rect(SURFACE, (255, 255, 0), rect1)

    # circle(SURFACE: ベース画面オブジェクト, color: 色, pos: 中心座標, radius: 半径, width: 線の幅)
    # 赤 : 塗りつぶし
    pygame.draw.circle(SURFACE, (255, 0, 0), (50, 50), 20)
    # 赤 : 太さ 10
    pygame.draw.circle(SURFACE, (255, 0, 0), (150, 50), 20, 3)
    # 緑 : 半径 10
    pygame.draw.circle(SURFACE, (0, 255, 0), (50, 150), 10)
    # 緑 : 半径 20
    pygame.draw.circle(SURFACE, (0, 255, 0), (150, 150), 20)
    # 緑 : 半径 30
    pygame.draw.circle(SURFACE, (0, 255, 0), (250, 150), 30)

    # circle(SURFACE: ベース画面オブジェクト, color: 色, Rect: 楕円に外接する矩形の位置、サイズ, width: 線の幅)
    # 赤
    pygame.draw.ellipse(SURFACE, (255, 0, 0), (50, 50, 140, 60))
    pygame.draw.ellipse(SURFACE, (255, 0, 0), (250, 30, 90, 90))
    # 緑
    pygame.draw.ellipse(SURFACE, (0, 255, 0), (50, 150, 110, 60), 5)
    pygame.draw.ellipse(SURFACE, (0, 255, 0), ((250, 130), (90, 90)), 20)

    # line(SURFACE: ベース画面オブジェクト, color: 色, start_pos: 始点, end_pos: 終点, width: 線の幅)
    # 赤 : 横線
    pygame.draw.line(SURFACE, (255, 0, 0), (10, 80), (200, 80))
    # 赤 : 横線(太さ 15)
    pygame.draw.line(SURFACE, (255, 0, 0), (10, 150), (200, 150), 15)
    # 緑 : 縦線
    pygame.draw.line(SURFACE, (0, 255, 0), (250, 30), (250, 200))
    # 青 : 斜線(太さ 10)
    start_pos = (300, 30)
    end_pos = (380, 200)
    pygame.draw.line(SURFACE, (0, 0, 255), start_pos, end_pos, 10)

    pygame.display.update() # プログラム中に描画した内容を画面に反映
    FPSCLOCK.tick(10) # 1秒間に10回ループが実行

# 自ファイルから開始された時にmain関数が実行
if __name__ == '__main__':
  main()
