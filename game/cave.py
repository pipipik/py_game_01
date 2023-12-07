"""cave - Copyright 20231201_01"""
import sys
from random import randint
import pygame
from pygame.locals import QUIT, Rect, KEYDOWN, K_SPACE

pygame.init() # pygameモジュールを初期化
pygame.key.set_repeat(5, 5) # キーを押し続けた時に連続してKEYDOWNイベントを生成する
SURFACE = pygame.display.set_mode((800, 600)) #サイズを指定してウィンドウを作成
FPSCLOCK = pygame.time.Clock() # クロックオブジェクトを作成

def main():
  """main routine"""
  walls = 80 # 矩形の数
  holes = [] # 矩形を格納する配列を初期化
  slope = randint(1, 6) # 傾きを指定(randint: 0～6の範囲の整数値をランダムに取得)
  ship_y = 250 # 自機のY座標
  velocity = 0 # 自機が上下に移動する際の速度
  score = 0 # スコア
  sysfont = pygame.font.SysFont(None, 36) # フォントオブジェクト作成
  ship_image = pygame.image.load("ship.png") # 自機_image
  bang_image = pygame.image.load("bang.png") # gameover_image
  for xpos in range(walls): # x座標を10ずつずらしながら80個の矩形を作成
    holes.append(Rect(xpos * 10, 100, 10, 400)) # (x, y, width, height)
  game_over = False # gameoverのフラグをFalseで初期化

  while True:
    is_space_down = False # ループを開始する都度、Falseで初期化
    for event in pygame.event.get(): # イベントキューからイベントを取得
      # 終了イベントを検出した時にプログラムを終了する
      if event.type == QUIT: # イベントがQUITの時
        pygame.quit() # pygameの初期化を解除
        sys.exit() # プログラム終了
      elif event.type == KEYDOWN: # キー押下
        if event.key == K_SPACE: # SPACEキー押下
          is_space_down = True # flag_on

    # game中の処理
    if not game_over:
      score += 10 # スコア+10
      # 自機の移動
      # SPACEキー押下状態に応じて速度を-3(上昇)、+3(落下)変化させる
      velocity += -3 if is_space_down else 3
      ship_y += velocity

      # 洞窟のスクロール
      edge = holes[-1].copy() # 右端の矩形ををコピーしてedgeに格納
      test = edge.move(0, slope) # .move(x, y)->Rect y軸方向にslope移動
      if test.top <= 0 or test.bottom >= 600: # test(Rectオブジェクト)が天井、床に衝突したら
        slope = randint(1, 6) * (-1 if slope > 0 else 1) # 傾きを変更
        edge.inflate_ip(0, -20) # .inflate(x, y)->Rect y軸方向のサイズを-20縮小
      edge.move_ip(10, slope) # .move_ip(x, y) x軸方向に10, y軸方向にslope移動
      holes.append(edge) # 右端に追加
      del holes[0] # 左端を削除
      holes = [x.move(-10, 0) for x in holes] # .move(x, y) 全体を左へ10移動
            
      # 衝突判定
      # 左端の矩形のtopとbottomの範囲に収まっているか
      if holes[0].top > ship_y or holes[0].bottom < ship_y + 80:
        game_over = True

    # 描画
    SURFACE.fill((0, 255, 0)) # ウィンドウを緑色(R,G,B)に塗りつぶす
    for hole in holes: # 画面オブジェクトに黒色の矩形リストholesを描画
      pygame.draw.rect(SURFACE, (0, 0, 0), hole)
    SURFACE.blit(ship_image, (0, ship_y)) # 自機を描画
    # render(text: 描画するテキスト, antialias: アンチエイリアス(輪郭をスムーズに), color: 色)
    score_image = sysfont.render("score is {}".format(score), True, (0, 0, 225))
    SURFACE.blit(score_image, (600, 20))

    # gameover時のimageを描画
    if game_over:
      SURFACE.blit(bang_image, (0, ship_y-40))

    pygame.display.update() # プログラム中に描画した内容を画面に反映
    FPSCLOCK.tick(15) # 1秒間に10回ループが実行

# 自ファイルから開始された時にmain関数が実行
if __name__ == '__main__':
  main()