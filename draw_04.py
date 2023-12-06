"""draw_text2.py"""
import sys
import pygame
from pygame.locals import QUIT

pygame.init() # pygameモジュールを初期化
SURFACE = pygame.display.set_mode((400, 300)) #サイズを指定してウィンドウを作成
FPSCLOCK = pygame.time.Clock() # クロックオブジェクトを作成

def main():
  """main routine"""
  # pygame.font.SysFont(name: フォント名(デフォルトはNone), size: フォントサイズ,
  #                     bold: 太字か否か(省略時はFalse), italic: イタリックか否か(省略時はFalse))
  sysfont = pygame.font.SysFont(None, 72) # Fontオブジェクト作成
  # render(text: 描画するテキスト, antialias: アンチエイリアス(輪郭をスムーズに), color: 色, background: 背景色(省略時はFalse))
  message = sysfont.render("Hello Python", True, (0, 128, 128)) # ビットマップ(Surface)を作成
  message_rect = message.get_rect() # 画像の占める矩形をget_rect()メソッドで取得
  theta = 0 # 回転角を初期化
  scale = 1 # ズームの倍率を初期化

  while True:
    for event in pygame.event.get(): # イベントキューからイベントを取得
      # 終了イベントを検出した時にプログラムを終了する
      if event.type == QUIT: # イベントがQUITの時
        pygame.quit() # pygameの初期化を解除
        sys.exit() # プログラム終了

    SURFACE.fill((255, 255, 255)) # ウィンドウを白色(R,G,B)に塗りつぶす
    theta += 5 # 回転角を5ずつ増加
    scale = (theta % 360) / 180 # ズームの倍率の計算(半回転で倍率1, 1回転でリセット)
    # rotozoom(Surface: 回転とズームを行うSurface, angle: 回転角, scale: ズームの倍率)
    tmp_msg = pygame.transform.rotozoom(message, theta, scale)
    tmp_rect = tmp_msg.get_rect() # 画像の占める矩形をget_rect()メソッドで取得
    tmp_rect.center = (200, 150) # プロパティに中心の座標を設定
    # コピー先のSURFACEオブジェクト.blit(source: コピー元のSurfaceオブジェクト, dest: コピーする座標(左上))
    SURFACE.blit(tmp_msg, tmp_rect)

    pygame.display.update() # プログラム中に描画した内容を画面に反映
    FPSCLOCK.tick(1) # 1秒間に1回ループが実行

# 自ファイルから開始された時にmain関数が実行
if __name__ == '__main__':
  main()