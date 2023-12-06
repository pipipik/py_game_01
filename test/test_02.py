"""fps_test2.py"""
import sys
import pygame
from pygame.locals import QUIT

pygame.init() # pygameモジュールを初期化
SURFACE = pygame.display.set_mode((400, 300)) #サイズを指定してウィンドウを作成
FPSCLOCK = pygame.time.Clock() # クロックオブジェクトを作成

def main():
  """main routine"""
  sysfont = pygame.font.SysFont(None, 36) # フォントオブジェクト作成(ファイル, サイズ)
  counter = 0 # カウンター初期化
  while True:
    for event in pygame.event.get(): # イベントキューからイベントを取得
      # 終了イベントを検出した時にプログラムを終了する
      if event.type == QUIT: # イベントがQUITの時
        pygame.quit() # pygameの初期化を解除
        sys.exit() # プログラム終了

    counter += 1 
    SURFACE.fill((0, 0, 0)) # ウィンドウを黒色(R,G,B)に塗りつぶす
    # フォントオブジェクト.render(テキスト, アンチエイリアス, 文字色, background=背景色)
    # アンチエイリアス : 文字の角を滑らかにする
    count_image = sysfont.render(
      "count is {}".format(counter), True, (255, 255, 255))
    # ベース画面オブジェクト.blit(テキスト画面オブジェクト, 表示座標, area=表示エリア, special_flags=色合成)
    SURFACE.blit(count_image, (50, 50))
    pygame.display.update() # プログラム中に描画した内容を画面に反映
    FPSCLOCK.tick(10) # 1秒間に10回ループが実行

# 自ファイルから開始された時にmain関数が実行
if __name__ == '__main__':
  main()
