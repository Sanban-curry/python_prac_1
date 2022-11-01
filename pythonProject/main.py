import roboter
import count
import reccomend

#挨拶
robot = roboter.robot()
name = robot.greeting()

#おすすめが好きか尋ねる
rec = reccomend.reccomend()
rec.reccomending()

#好きなレストランを尋ねる
rst = robot.asking(name)

#csvファイルに書き込む
wrt = count.write(rst.capitalize())
wrt.ranking()

#お別れの挨拶
robot.byebye(name)