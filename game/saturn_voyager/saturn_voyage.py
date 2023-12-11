"""saturn_voyager - Copyright 20231210_01"""
import sys
from random import randint
import pygame
from pygame.locals import QUIT

pygame.init() # pygameモジュールを初期化
SURFACE = pygame.display.set_mode((800, 800)) #サイズを指定してウィンドウを作成
FPSCLOCK = pygame.time.Clock() # クロックオブジェクトを作成

def main():
  """main routine"""
  stars = [] # 隕石を格納するリスト
  ship = [0, 0] # 自機の座標
  speed = 25 # スピード(時間経過と共に加速)
  rock_image = pygame.image.load("rock.png") # 隕石_image
  scope_image = pygame.image.load("scope.png") # 自機_image

  while len(stars) < 200: # 隕石を200個(x, y, z)座標と回転角をランダムに配置
    stars.append({
      "pos": [randint(-1600, 1600),randint(-1600, 1600), randint(0, 4095)],
      "theta": randint(0, 360)}) # カラのstarsリストに200回append

  while True:
    for event in pygame.event.get(): # イベントキューからイベントを取得
      # 終了イベントを検出した時にプログラムを終了する
      if event.type == QUIT: # イベントがQUITの時
        pygame.quit() # pygameの初期化を解除
        sys.exit() # プログラム終了

    # 隕石の移動
    for star in stars:
      star["pos"][2] -= speed # z座標をスピード分減らす(近づける)

    # 描画
    SURFACE.fill((0, 0, 0)) # ウィンドウを黒色(R,G,B)に塗りつぶす
    stars = sorted(stars, key=lambda x: x["pos"][2], reverse=True) # x["pos"][2](z軸)の大きい順にソート
    for star in stars:
      zpos = star["pos"][2]
      # <<: ビットシフト, 2の9乗拡大する⇦立体化を出すため
      # ((star["pos"][0]) - ship[0])/zpos: (隕石を自機の差分)/z座標⇦中心からの差分を出すため
      # +400: 描画領域(800*800)の中心を原点にするため
      xpos = ((star["pos"][0] - ship[0]) << 9) / zpos + 400
      ypos = ((star["pos"][1] - ship[1]) << 9) / zpos + 400
      size = (50 << 9) / zpos
      # rotozoom(Surface: 回転とズームを行うSurface, angle: 回転角, scale: ズームの倍率)
      rotated = pygame.transform.rotozoom(rock_image, star["theta"], size / 145)
      SURFACE.blit(rotated, (xpos, ypos))

    SURFACE.blit(scope_image, (0, 0)) # 自機の描画

    pygame.display.update() # プログラム中に描画した内容を画面に反映
    FPSCLOCK.tick(15) # 1秒間に15回ループが実行

# 自ファイルから開始された時にmain関数が実行
if __name__ == '__main__':
  main()