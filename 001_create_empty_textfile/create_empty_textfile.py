# カレントディレクトリに空ファイルを100個作成する
import pathlib

for i in range(100):
  touch_file = pathlib.Path('./test{}.txt'.format(i))
  touch_file.touch()
