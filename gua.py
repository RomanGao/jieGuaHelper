import re
class Gua:
	@staticmethod
	def get_gua8():
		gua8 = {}
		gua8['乾'] = '天'
		gua8['兑'] = '泽'
		gua8['离'] = '火'
		gua8['震'] = '雷'
		gua8['巽'] = '风'
		gua8['坎'] = '水'
		gua8['艮'] = '山'
		gua8['坤'] = '地'
		return gua8
	
	@staticmethod
	def num_to_gua(num):
		#num为str类型 	 
		num2gua = dict()
		#自下而上
		num2gua['111'] = '乾'  #乾：天
		num2gua['011'] = '巽'  #巽：风 
		num2gua['110'] = '兑'  #兑:泽（水利）
		num2gua['100'] = '震'  #震:雷
		num2gua['001'] = '艮'  #艮:山
		num2gua['000'] = '坤'  #坤:地
		num2gua['010'] = '坎'  #坎:水（水害）
		num2gua['101'] = '离'  #离:火
		if num not in num2gua:
			return None
		return num2gua[num]
	
	@staticmethod
	def gua_to_num(name):
		#name为str类型
		#自下而上
		gua2num = dict()
		gua2num['乾'] = '111'
		gua2num['兑'] = '110'
		gua2num['离'] = '101'
		gua2num['震'] = '100'
		gua2num['巽'] = '011'
		gua2num['坎'] = '010'
		gua2num['艮'] = '001'
		gua2num['坤'] = '000'
		if name not in gua2num:
			return None
		return gua2num[name]
	@staticmethod
	def find_key(dict_obj, value):
		for key, val in dict_obj.items():
			if val == value:
				return key
		return None

	@staticmethod
	def get_gua64():
		#先下后上
		ct = 0
		num2gua64 = {}
		ls_gua64 = []
		gua8 = Gua.get_gua8()
		file = open("./64.txt", 'r', encoding='utf-8')
		lines = file.readlines()
		for i,line in enumerate(lines):
			line = line.strip()
			ls = line.split(" ")
			#print(ls, len(ls))
			if len(ls)>1:
				#五行找卦
				up = ls[1][0]
				down =  ls[1][1]
				if down == '为':
					#print(up, down)
					name = Gua.gua_to_num(up)+ Gua.gua_to_num(up)
				else:
					up_name = Gua.find_key(gua8, up)
					down_name = Gua.find_key(gua8, down)
					#print(up_name, down_name)
					if up_name is None or down_name is None:
						continue
					name = Gua.gua_to_num(down_name)+ Gua.gua_to_num(up_name)
				#print(name)
				if len(name)==6:
					patten = r'\（.*?\）'
					matches = re.findall(patten, line)
					#print(matches)
					if len(matches)>1:
						ls_gua64.append(matches[1].strip("（").strip('）'))
						num2gua64[name] = matches[1].strip("（").strip('）')
					elif len(matches)==1:
						ls_gua64.append(matches[0].strip("（").strip('）'))
						num2gua64[name] = matches[0].strip("（").strip('）')
					
		if len(ls_gua64) == 64:
			return num2gua64, ls_gua64
		else:
			return None
