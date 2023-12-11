"""saturn_voyager - Copyright 20231210_01"""
import sys
from random import randint
import pygame
from pygame.locals import QUIT, KEYDOWN, KEYUP, K_LEFT, K_RIGHT, K_UP, K_DOWN

pygame.init() # pygameモジュールを初期化
SURFACE = pygame.display.set_mode((800, 800)) #サイズを指定してウィンドウを作成
FPSCLOCK = pygame.time.Clock() # クロックオブジェクトを作成

def main():
  """main routine"""
  stars = [] # 隕石を格納するリスト
  ship = [0, 0] # 自機の座標
  speed = 25 # スピード(時間経過と共に加速)
  keymap = [] # どのキーが押下されているかを示すリスト
  game_over = False # ゲームオーバーフラグ
  score = 0 # スコア
  rock_image = pygame.image.load("rock.png") # 隕石_image
  scope_image = pygame.image.load("scope.png") # 自機_image

  scorefont = pygame.font.SysFont(None, 36) # Fontオブジェクト
  sysfont = pygame.font.SysFont(None, 72) # Fontオブジェクト
  message_over = sysfont.render("GAME OVER!!", True, (0, 255, 225)) # Surfaceオブジェクト
  message_rect = message_over.get_rect() # 画像の占める矩形をget_rect()メソッドで取得
  message_rect.center = (400, 400) # プロパティに中心の座標を設定

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
      elif event.type == KEYDOWN: # キー押下
        if not event.key in keymap: # keymapになければイベントを追加
          keymap.append(event.key)
      elif event.type == KEYUP: # キーを離せばイベントを削除
        keymap.remove(event.key)

    # フレーム毎の処理
    if not game_over: # ゲーム中の処理
      score += 1 # スコア加算
      if score % 10 == 0:
        speed += 1 # スピード加算

      # フレーム毎の処理
      if K_LEFT in keymap: # 左キー
        ship[0] -= 30
      elif K_RIGHT in keymap: # 右キー
        ship[0] += 30
      elif K_UP in keymap: # 上キー
        ship[1] -= 30
      elif K_DOWN in keymap: # 下キー
        ship[1] += 30

      ship[0] = max(-800, min(800, ship[0])) # x座標のガード
      ship[1] = max(-800, min(800, ship[1])) # y座標のガード

      # 隕石の移動
      for star in stars:
        star["pos"][2] -= speed # z座標をスピード分減らす(近づける)
        # 衝突判定
        if star["pos"][2] < 64: # XY平面にの近づき
          if abs(star["pos"][0] - ship[0]) < 50 and \
             abs(star["pos"][1] - ship[1]) < 50: # 隕石と自機の距離
            game_over = True
          star["pos"] = [randint(-1600, 1600), randint(-1600, 1600), 4095] # 衝突しなければ一番遠い位置に再配置

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

    if game_over: # ゲームオーバー
      SURFACE.blit(message_over, message_rect) # メッセージ描画
      pygame.mixer.music.stop()

    # スコアの描画
    score_str = str(score).zfill(6) # 文字列の左側を0で埋める
    score_image = scorefont.render(score_str, True, (0, 255, 0))
    SURFACE.blit(score_image, (700, 50)) # スコア描画

    pygame.display.update() # プログラム中に描画した内容を画面に反映
    FPSCLOCK.tick(15) # 1秒間に15回ループが実行

# 自ファイルから開始された時にmain関数が実行
if __name__ == '__main__':
  main()