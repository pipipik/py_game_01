"""draw_image_onkeydown.py"""
# キーの押下
import sys
import pygame
from pygame.locals import QUIT, KEYDOWN, K_LEFT, K_RIGHT, K_UP, K_DOWN

pygame.init() # pygameモジュールを初期化
pygame.key.set_repeat(5, 5) # キーの押しっ放しにした時にイベントを定期的に発生させる
SURFACE = pygame.display.set_mode((400, 300)) #サイズを指定してウィンドウを作成
FPSCLOCK = pygame.time.Clock() # クロックオブジェクトを作成

def main():
  """main routine"""
  logo = pygame.image.load("pythonlogo.jpg")
  pos = [200, 150] # 画像の中心座標
  while True:
    for event in pygame.event.get(): # イベントキューからイベントを取得
      # 終了イベントを検出した時にプログラムを終了する
      if event.type == QUIT: # イベントがQUITの時
        pygame.quit() # pygameの初期化を解除
        sys.exit() # プログラム終了
      elif event.type == KEYDOWN: # キー押下
        if event.key == K_LEFT: # 左キー押下で中心座標を-5
          pos[0] -= 5
        elif event.key == K_RIGHT: # 右キー押下で中心座標を5
          pos[0] += 5
        elif event.key == K_UP: # 上キー押下で中心座標を-5
          pos[1] -= 5
        elif event.key == K_DOWN: # 下キー押下で中心座標を5
          pos[1] += 5
    # 両端に到達した際に反対側から折り返す処理
    pos[0] = pos[0] % 400
    pos[1] = pos[1] % 300

    SURFACE.fill((255, 255, 255)) # ウィンドウを白色(R,G,B)に塗りつぶす

    rect = logo.get_rect() # 画像の占める矩形をget_rect()メソッドで取得
    rect.center = pos # プロパティに中心の座標を設定
    # コピー先のSURFACEオブジェクト.blit(source: コピー元のSurfaceオブジェクト, dest: コピーする座標(左上))
    SURFACE.blit(logo, rect)

    pygame.display.update() # プログラム中に描画した内容を画面に反映
    FPSCLOCK.tick(10) # 1秒間に10回ループが実行

# 自ファイルから開始された時にmain関数が実行
if __name__ == '__main__':
  main()