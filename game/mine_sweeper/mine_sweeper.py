"""mine_sweeper - Copyright 20231209_01"""
import sys
from math import floor
import pygame
from random import randint
from pygame.locals import QUIT, MOUSEBUTTONDOWN

# グローバル変数定義
WIDTH = 20 # 横方向のマスの数
HEIGHT = 15 # 縦方向のマスの数
SIZE = 50 # 1マスの縦横のサイズ
NUM_OF_BOMBS = 20 # 爆弾の数
EMPTY = 0 # マップ上のタイルがからの状態
BOMB = 1 # マップ上のタイルに爆弾がある状態
OPENED = 2 # マップ上のタイルが開封状態
OPEN_COUNT = 0 # 開かれたタイルの数
CHECKED = [[0 for _ in range(WIDTH)] for _ in range(HEIGHT)] # タイルの状態を既にチェックしたか記録する配列

pygame.init() # pygameモジュールを初期化
SURFACE = pygame.display.set_mode([WIDTH*SIZE, HEIGHT*SIZE]) #サイズを指定してウィンドウを作成
FPSCLOCK = pygame.time.Clock() # クロックオブジェクトを作成

def num_of_bomb(field, x_pos, y_pos):
  """ 周囲にある爆弾の数を返す """
  count = 0 # 戻り値を初期化
  # x, y軸にそれぞれ-1, 0, 1と変化させて
  # (x_pos, y_pos)の周りにある爆弾の数をカウント
  for yoffset in range(-1, 2):
    for xoffset in range(-1, 2):
      xpos, ypos = (x_pos + xoffset, y_pos + yoffset) # (x_pos, y_pos)をoffset
      if 0 <= xpos < WIDTH and 0 <= ypos < HEIGHT and \
        field[ypos][xpos] == BOMB: # xpos, yposがマス内であるか and 爆弾有りか判定
        count += 1 # 判定成立でカウントアップ
  return count # 爆弾の数を返す

def open_tile(field, x_pos, y_pos):
  """ タイルをオープン """
  global OPEN_COUNT # グローバル変数を変更するためグローバル宣言する
  if CHECKED[y_pos][x_pos]:  # 既にチェック済みのタイルの時
    return # 何もしない

  CHECKED[y_pos][x_pos] = True # 指定されたタイルをチェック済みに変更

  # x, y軸にそれぞれ-1, 0, 1と変化させて
  # (x_pos, y_pos)の周りにある爆弾の数をカウント
  for yoffset in range(-1, 2):
    for xoffset in range(-1, 2):
      xpos, ypos = (x_pos + xoffset, y_pos + yoffset)
      if 0 <= xpos < WIDTH and 0 <= ypos < HEIGHT and \
        field[ypos][xpos] == EMPTY: # xpos, yposがマス内であるか and 未開封状態の時
        field[ypos][xpos] = OPENED # field状態を開封状態に変更
        OPEN_COUNT += 1 # 判定成立でカウントアップ
        count = num_of_bomb(field, xpos, ypos) # 関数を呼び出して爆弾の数を取得
        if count == 0 and \
          not (xpos == x_pos and ypos == y_pos): # 爆弾の数が0, 初めに指定したタイルでない時
          open_tile(field, xpos, ypos) # 再度関数を呼び出す

def main():
  """main routine"""
  smallfont = pygame.font.SysFont(None, 36) # 爆弾の数を表示するFontオブジェクトを作成
  game_over = False # gameoverのフラグをFalseで初期化
  # field1状態をからで初期化 field(list) = [0, 0, ...], [0, ...], ...
  field = [[EMPTY for xpos in range(WIDTH)] for ypos in range(HEIGHT)]

  # 爆弾を設置
  count = 0
  while count < NUM_OF_BOMBS: # 爆弾の数分繰り返す
    xpos, ypos = randint(0, WIDTH-1), randint(0, HEIGHT-1) # (x, y)座標をランダムに指定
    if field[ypos][xpos] == EMPTY: # 重複を避けるため、field状態がからの時
      field[ypos][xpos] = BOMB # 爆弾を設置
      count += 1 # 設置できたらカウントアップ

  while True:
    for event in pygame.event.get(): # イベントキューからイベントを取得
      # 終了イベントを検出した時にプログラムを終了する
      if event.type == QUIT: # イベントがQUITの時
        pygame.quit() # pygameの初期化を解除
        sys.exit() # プログラム終了
      if event.type == MOUSEBUTTONDOWN and event.button == 1: # 左クリックされた時
        # クリックされた位置からタイルの位置を取得
        # floor(): 小数点切り捨て(負数は負方向に丸められる)
        xpos, ypos = floor(event.pos[0] / SIZE), floor(event.pos[1] / SIZE)
        if field[ypos][xpos] == BOMB: # 指定したタイルが爆弾有りの時
          game_over = True # gameoverのフラグをTrueに変更
        else:
          open_tile(field, xpos, ypos) # 関数を呼び出して、タイルを開封状態に変更

    # 描画
    SURFACE.fill((0, 0, 0)) # ウィンドウを黒色(R,G,B)に塗りつぶす

    for ypos in range(HEIGHT):
      for xpos in range(WIDTH):
        tile = field[ypos][xpos] # 左上から順にfield状態をtileに格納
        rect = (xpos*SIZE, ypos*SIZE, SIZE, SIZE) # tileの矩形サイズを取得
        if tile == EMPTY or tile == BOMB: # field状態が未開封状態の時
          pygame.draw.rect(SURFACE, (192, 192, 192), rect) # 未開封状態を描画
          if game_over and tile == BOMB: # game_over状態かつfield状態が爆弾有りの時
            pygame.draw.ellipse(SURFACE, (225, 225, 0), rect) # 爆弾有りを描画
        elif tile == OPENED: # field状態が開封状態の時
          count = num_of_bomb(field, xpos, ypos) # 関数を呼び出して爆弾の数を取得
          if count > 0: # 爆弾有りの時
            # render(text: 描画するテキスト, antialias: アンチエイリアス(輪郭をスムーズに), color: 色)
            num_image = smallfont.render("{}".format(count), True, (255, 255, 0))
            SURFACE.blit(num_image, (xpos*SIZE+10, ypos*SIZE+10)) # 爆弾の数を描画(左上から+10ずつoffset)

    # 線の描画
    # line(SURFACE: ベース画面オブジェクト, color: 色, start_pos: 始点, end_pos: 終点, width: 線の幅)
    # 縦線
    for index in range(0, WIDTH*SIZE, SIZE): # 左端から右端までタイルのサイズごとにx座標を指定
      pygame.draw.line(SURFACE, (96, 96, 96), (index, 0), (index, HEIGHT*SIZE))
    # 横線
    for index in range(0, HEIGHT*SIZE, SIZE): # 上端から下端までタイルのサイズごとにy座標を指定
      pygame.draw.line(SURFACE, (96, 96, 96), (0, index), (WIDTH*SIZE, index))

    pygame.display.update() # プログラム中に描画した内容を画面に反映
    FPSCLOCK.tick(1) # 1秒間に1回ループが実行

# 自ファイルから開始された時にmain関数が実行
if __name__ == '__main__':
  main()