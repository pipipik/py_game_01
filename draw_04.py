"""draw_text1.py"""
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
  message_rect.center = (200, 200) # プロパティに中心の座標を設定

  while True:
    for event in pygame.event.get(): # イベントキューからイベントを取得
      # 終了イベントを検出した時にプログラムを終了する
      if event.type == QUIT: # イベントがQUITの時
        pygame.quit() # pygameの初期化を解除
        sys.exit() # プログラム終了

    SURFACE.fill((255, 255, 255)) # ウィンドウを白色(R,G,B)に塗りつぶす
    # コピー先のSURFACEオブジェクト.blit(source: コピー元のSurfaceオブジェクト, dest: コピーする座標(左上))
    SURFACE.blit(message, message_rect)

    pygame.display.update() # プログラム中に描画した内容を画面に反映
    FPSCLOCK.tick(1) # 1秒間に1回ループが実行

# 自ファイルから開始された時にmain関数が実行
if __name__ == '__main__':
  main()