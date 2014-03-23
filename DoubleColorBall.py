#!/usr/bin/python
# -*- coding: utf-8 -*-

import random
import urllib2
import sys
import re

def main():
	print "pick the double color ball:"

	# from 1 - 33  pick up 6 balls
	# from 1 - 16  pick up 1 ball

	herosBefore = getTheHerosBefore()

	alreadyPicked = []

	# 如果一组红色球，被选中了两次，那么认为它是幸运的
	while True:
		
		redBall=giveMe6RedBalls()
		blueBall=giveMe1BlueBalls()

		if redBall in alreadyPicked:
			# 将redBall 与 blueBall 拼接成一个[] 并且转换成 字符串形式
			heroNow = convertRedBallBlueBallToHero(redBall, blueBall) 

			if heroNow in herosBefore:
				print "	old hero, please rest!"#到这的概率原来很低很低...
				print heroNow
				
			else:
				break
		else:
			alreadyPicked.append(redBall)	

	#if redBall.empty() is False: 
	print "    redBalls:"+str(redBall)

	#if blueBall.empty() is False: 
	print "    blueBall:"+str(blueBall)

	print len(alreadyPicked)


# 将一组红蓝转化成 字符数字，便于和以往记录比对
def convertRedBallBlueBallToHero(reds, blue):
	hero = []
	for ball in reds:
		if ball < 10:
			bstr = '0'+str(ball)
		else:
			bstr = str(ball)
		hero.append(bstr)

	if blue < 10:
		hero.append('0'+str(blue))
	else:
		hero.append(str(blue))
	return hero

###随机生成六个红球，按顺序排好队，返回[]
def giveMe6RedBalls():
	bingoBalls = []
	balls =  range(1,33+1);

	for i in range(6):
		luckBall = random.choice(balls)
		balls.remove(luckBall)
		bingoBalls.append(luckBall)
		bingoBalls.sort()
	return bingoBalls

###随机生成一个蓝球
def giveMe1BlueBalls():
	return  random.randint(1,16)


def downloadThePages():
	# 从网上爬到网页 每一年对应一个页面 上面有这一年的数字
	response = urllib2.urlopen('http://baidu.lecai.com/lottery/draw/list/50')  
	html = response.read().decode('utf-8')

	outputFile = open('2014.dat','w')
	outputFile.write(html)
	outputFile.close()


	# response = urllib2.urlopen('http://baidu.lecai.com/lottery/draw/list/50?d=2003-01-01')  
	# html = response.read().decode('utf-8')

	# outputFile = open('2003.dat','w')
	# outputFile.write(html)
	# outputFile.close()


	# response = urllib2.urlopen('http://baidu.lecai.com/lottery/draw/list/50?d=2004-01-01')  
	# html = response.read().decode('utf-8')

	# outputFile = open('2004.dat','w')
	# outputFile.write(html)
	# outputFile.close()


	# response = urllib2.urlopen('http://baidu.lecai.com/lottery/draw/list/50?d=2005-01-01')  
	# html = response.read().decode('utf-8')

	# outputFile = open('2005.dat','w')
	# outputFile.write(html)
	# outputFile.close()


	# response = urllib2.urlopen('http://baidu.lecai.com/lottery/draw/list/50?d=2006-01-01')  
	# html = response.read().decode('utf-8')

	# outputFile = open('2006.dat','w')
	# outputFile.write(html)
	# outputFile.close()

	# response = urllib2.urlopen('http://baidu.lecai.com/lottery/draw/list/50?d=2007-01-01')  
	# html = response.read().decode('utf-8')

	# outputFile = open('2007.dat','w')
	# outputFile.write(html)
	# outputFile.close()

	# response = urllib2.urlopen('http://baidu.lecai.com/lottery/draw/list/50?d=2008-01-01')  
	# html = response.read().decode('utf-8')

	# outputFile = open('2008.dat','w')
	# outputFile.write(html)
	# outputFile.close()

	# response = urllib2.urlopen('http://baidu.lecai.com/lottery/draw/list/50?d=2009-01-01')  
	# html = response.read().decode('utf-8')

	# outputFile = open('2009.dat','w')
	# outputFile.write(html)
	# outputFile.close()

	# response = urllib2.urlopen('http://baidu.lecai.com/lottery/draw/list/50?d=2010-01-01')  
	# html = response.read().decode('utf-8')

	# outputFile = open('2010.dat','w')
	# outputFile.write(html)
	# outputFile.close()

	# response = urllib2.urlopen('http://baidu.lecai.com/lottery/draw/list/50?d=2011-01-01')  
	# html = response.read().decode('utf-8')

	# outputFile = open('2011.dat','w')
	# outputFile.write(html)
	# outputFile.close()

	# response = urllib2.urlopen('http://baidu.lecai.com/lottery/draw/list/50?d=2012-01-01')  
	# html = response.read().decode('utf-8')

	# outputFile = open('2012.dat','w')
	# outputFile.write(html)
	# outputFile.close()

	# response = urllib2.urlopen('http://baidu.lecai.com/lottery/draw/list/50?d=2013-01-01')  
	# html = response.read().decode('utf-8')

	# outputFile = open('2013.dat','w')
	# outputFile.write(html)
	# outputFile.close()

def pickTheNumsOutFromPages():
	# 从页面中把中奖数字通过正则，提取出来，2003 - 2013， 2014截止目前的数字 全部放到balls.dat里面

	readFile = open('2014.dat','r')
	writeFile = open('balls.dat', 'a+')

	pattern = re.compile(r'<span class="ball_1">')
	for line in readFile:
		if 'ball_1' in line:

			match = re.match(r'.*>[0-9][0-9]', line)
			if match:
				writeFile.write(line[match.end()-2: match.end()])
				writeFile.write("  ")
				#print line[match.end()-2: match.end()]
				#print match.group() 
				#print match.start(), match.end()

				# print "match.pos:", match.pos
				# print "match.endpos:", match.endpos
				# print "match.lastindex:", match.lastindex
				# print "match.lastgroup:", match.lastgroup

		if 'ball_2' in line:
			match = re.match(r'.*>[0-9][0-9]', line)
			if match:
				writeFile.write(line[match.end()-2: match.end()])
				writeFile.write('\n')
				# print line[match.end()-2: match.end()]
				# print match.group() 

# 得到以前的中奖号码，以[]形式返回
def getTheHerosBefore():
	balls = open('balls.dat', 'r')

	MrsRights = []

	for lines in balls:
		nums = lines.split()
		if nums in MrsRights:
			print nums
			break
		else:
			MrsRights.append(nums)

	return MrsRights


if __name__ == '__main__':

	reload(sys)
	sys.setdefaultencoding( "utf-8" )
	
	# downloadThePages()
	# pickTheNumsOutFromPages()
	# print getTheHerosBefore()
	# print convertRedBallBlueBallToHero([1,2,3,4,5,6],3)

	main()