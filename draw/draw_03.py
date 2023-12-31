"""draw_image4.py"""
import sys
import pygame
from pygame.locals import QUIT

pygame.init() # pygameモジュールを初期化
SURFACE = pygame.display.set_mode((400, 300)) #サイズを指定してウィンドウを作成
FPSCLOCK = pygame.time.Clock() # クロックオブジェクトを作成

def main():
  """main routine"""
  # 画像ファイルをロード
  # load(filename: 画像ファイル)
  logo = pygame.image.load("pythonlogo.jpg")
  theta = 0 # 回転角を初期化

  while True:
    for event in pygame.event.get(QUIT): # イベントキューからイベントを取得
      pygame.quit() # pygameの初期化を解除
      sys.exit() # プログラム終了
    theta += 1

    SURFACE.fill((255, 255, 255)) # ウィンドウを白色(R,G,B)に塗りつぶす
    
    # 回転することで画像の縦横サイズが変化する
    # ロゴを回転し、左上が(100, 30)の位置にロゴを描画
    # transform.rotate(Surface: 回転対象となるオブジェクト, angle: 回転角)
    new_logo = pygame.transform.rotate(logo, theta) # 回転した画像を作成
    SURFACE.blit(new_logo, (100, 30)) #回転した画像を再描画

    # 画像の中心を軸として回転する
    # ロゴを回転し、中心が(200, 150)の位置にロゴを描画
    new_logo = pygame.transform.rotate(logo, theta) # 回転した画像を作成
    rect = new_logo.get_rect() # 画像の占める矩形をget_rect()メソッドで取得
    rect.center = (200, 150) # プロパティに中心の座標を設定
    SURFACE.blit(new_logo, rect) # 第2引数に指定

    pygame.display.update() # プログラム中に描画した内容を画面に反映
    FPSCLOCK.tick(1) # 1秒間に1回ループが実行

# 自ファイルから開始された時にmain関数が実行
if __name__ == '__main__':
  main()
