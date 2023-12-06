"""draw_line_onmousemove.py"""
# マウスの移動
import sys
import pygame
from pygame.locals import QUIT, MOUSEBUTTONDOWN, MOUSEMOTION, MOUSEBUTTONUP

pygame.init() # pygameモジュールを初期化
SURFACE = pygame.display.set_mode((400, 300)) #サイズを指定してウィンドウを作成
FPSCLOCK = pygame.time.Clock() # クロックオブジェクトを作成

def main():
  """main routine"""
  mousepos = [] # マウスポジションを初期化
  mousedown = False # マウス押下されていない状態からスタート

  while True:
    for event in pygame.event.get(): # イベントキューからイベントを取得
      # 終了イベントを検出した時にプログラムを終了する
      if event.type == QUIT: # イベントがQUITの時
        pygame.quit() # pygameの初期化を解除
        sys.exit() # プログラム終了
      elif event.type == MOUSEBUTTONDOWN: # マウスの押下
        mousedown = True
      elif event.type == MOUSEMOTION: # マウスの移動
        if mousedown: # マウス移動中かつマウス押下中
          # マウス座標をリストに追加
          mousepos.append(event.pos) # event.pos: マウスの座標(x, y)タプル型
      elif event.type == MOUSEBUTTONUP: # マウスのリリース
        mousedown = False
        mousepos.clear() # マウスリリースで画面初期化

    SURFACE.fill((255, 255, 255)) # ウィンドウを白色(R,G,B)に塗りつぶす
    if len(mousepos) > 1: # 座標の個数が2個以上になったら
      # 線(赤色, 始点と終点を結ばない, 太さ1)を描画
      pygame.draw.lines(SURFACE, (255, 0, 0), False, mousepos)
      # より滑らかな線を描画するaalinsメソッド
      # aalines(Surface: 描画対象となるオブジェクト, color: 色, closed: 始点と終点を結ぶか否か,
      #         pointlist: 座標のリスト, blend: ブレンドするか否か)
      # pygame.draw.aalines(SURFACE, (255, 0, 255), False, mousepos, True)

    pygame.display.update() # プログラム中に描画した内容を画面に反映
    FPSCLOCK.tick(10) # 1秒間に10回ループが実行

# 自ファイルから開始された時にmain関数が実行
if __name__ == '__main__':
  main()