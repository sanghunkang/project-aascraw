#!/usr/bin/python
# -*- coding: utf-8 -*-

# Import built-in packages
import os, re, sys, time
from itertools import chain
from urllib import request

# Import external packages
from bs4 import BeautifulSoup
# import matplotlib.pyplot as plt
import numpy as np

# Import custom modules
from driverController.driver import webdriverTailored
from driverController.locator import get_attr_elem, locate_element, get_eigentext, get_eigentext_bw
from interInspector import InterInspector
from intraInspector import IntraInspector #, get_max_size_window, calculate_max_index_start, make_tsr_slice, get_seq_index_canddt, update_seq_index_canddt, calculate_dist_tsr
from xpathFinder import XpathFinder

# Import package-wide constants
from constGlobal import *

print("INITIATED!")
#############################################################################
# Inter

#############################################################################
# Generation

# url0 = "https://www.tripadvisor.co.kr/Attraction_Review-g294217-d2482919-Reviews-or30-Hong_Kong_Skyline-Hong_Kong.html"
# url1 = "https://www.tripadvisor.co.kr/Attraction_Review-g294217-d2482919-Reviews-or40-Hong_Kong_Skyline-Hong_Kong.html"
# url = "https://www.amazon.com/s/ref=br_pdt_mgUpt/136-5748595-7690834?_encoding=UTF8&rh=n%3A1055398&srs=10112675011&pf_rd_m=ATVPDKIKX0DER&pf_rd_s=&pf_rd_r=H0CVS4CGFH8ZKDF3N54G&pf_rd_t=36701&pf_rd_p=db21a8d3-3560-4f95-b840-a0a07adc52e0&pf_rd_i=desktop"
# url = "http://v.media.daum.net/v/20170609204506833?rcmd=r"

# Movies
# url0 = "http://movie.naver.com/movie/bi/mi/basic.nhn?code=155256"
# url1 = "http://movie.naver.com/movie/bi/mi/basic.nhn?code=156083"
# url2 = "http://movie.naver.com/movie/bi/mi/basic.nhn?code=125473"
# url3 = "http://movie.naver.com/movie/bi/mi/basic.nhn?code=137326"

# News
url0 = "http://news.naver.com/main/ranking/read.nhn?mid=etc&sid1=111&rankingType=popular_day&oid=008&aid=0003889934&date=20170618&type=1&rankingSeq=1&rankingSectionId=100"
url1 = "http://news.naver.com/main/ranking/read.nhn?mid=etc&sid1=111&rankingType=popular_day&oid=015&aid=0003783581&date=20170618&type=1&rankingSeq=1&rankingSectionId=105"
url2 = "http://news.naver.com/main/ranking/read.nhn?mid=etc&sid1=111&rankingType=popular_day&oid=001&aid=0009345375&date=20170618&type=1&rankingSeq=1&rankingSectionId=104"
url3 = "http://news.naver.com/main/ranking/read.nhn?mid=etc&sid1=111&rankingType=popular_day&oid=001&aid=0009345375&date=20170618&type=1&rankingSeq=1&rankingSectionId=102"

xpathFinder0 = XpathFinder(url0)
xpathFinder1 = XpathFinder(url1)
xpathFinder2 = XpathFinder(url2)

# Feed Samples
interInspector = InterInspector()
interInspector.receive_pageinfo(xpathFinder0)
interInspector.receive_pageinfo(xpathFinder1)
interInspector.receive_pageinfo(xpathFinder2)
# interInspector.receive_pageinfo(xpathFinder3)

interInspector.make_seq_xpath_canddt_inter()
seq_xpath_canddt_inter = interInspector.get_seq_xpath_canddt_inter()

#############################################################################
# Testing
xpathFinder3 = XpathFinder(url3)

soup2 = xpathFinder2.get_soup()
soup3 = xpathFinder3.get_soup()
for xpath in seq_xpath_canddt_inter:
	try:
		print(xpath)
		elems_located_test2 = locate_element(soup2, xpath, get_attr_elem)[-1]
		eigentext_test2 = get_eigentext(elems_located_test2)
		print(eigentext_test2)

		elems_located_test3 = locate_element(soup3, xpath, get_attr_elem)[-1]
		eigentext_test3 = get_eigentext(elems_located_test3)
		print(eigentext_test3)
	except IndexError:
		print(IndexError)
	print("#############################################################################")

#############################################################################
# Intra
url = "https://www.amazon.com/s?rh=i%3Akitchen%2Cn%3A1055398%2Cn%3A%211063498%2Cn%3A284507%2Cn%3A915194%2Cn%3A289748%2Cp_89%3ADeLonghi%2Cp_6%3AATVPDKIKX0DER&bbn=289748&ie=UTF8&ref=vs_cte_r1_c1_delonghi&pf_rd_r=XJ4PFY14DAG7JD44YNAN&pf_rd_m=ATVPDKIKX0DER&pf_rd_t=Landing&pf_rd_i=915194&pf_rd_p=c3a7580e-3bde-4497-8e61-232d912a1aeb&pf_rd_s=merchandised-search-grid-t1-r1-c1"
# url = "http://movie.naver.com/movie/bi/mi/basic.nhn?code=156083"
"""
xpathFinder = XpathFinder(url)
seq_xpath = xpathFinder.get_seq_xpath()

seq_xpath_encoded_occurence = xpathFinder.get_seq_xpath_encoded_occurence()
seq_xpath_encoded = xpathFinder.get_seq_xpath_encoded()
seq_xpath_encoded_3d = xpathFinder.get_seq_xpath_encoded_3d()

# plt.imshow(seq_xpath_encoded)
# plt.axes().set_aspect('auto', 'datalim')
# plt.show()

print(seq_xpath_encoded.shape)
print(seq_xpath_encoded_3d.shape)
soup = xpathFinder.soup

intraInspector = IntraInspector(seq_xpath_encoded, seq_xpath_encoded_occurence)
seq_set_canddt = intraInspector.get_seq_set_canddt()

for set_canddt in seq_set_canddt:
	print("#############################################################################")
	for canddt in set_canddt:
		print("_____________________________________________________________________________")
		print(canddt)
		xpath = seq_xpath[canddt[0]]
		elems_located = locate_element(soup, xpath, get_attr_elem)
		eigentext = get_eigentext(elems_located[-1])

		print(eigentext)

# Potentially some needed but skip for now...
"""
"""
seq_index_canddt = []
for i, xpath_encoded_3d_0 in enumerate(seq_xpath_encoded_3d):
	for j, xpath_encoded_3d_1 in enumerate(seq_xpath_encoded_3d[i+1:]):
		seq_index_canddt.append((i, i+1+j))


print(time.time())
dict_canddt = []
aa = []
seq_index_canddt_new = []

for size_window in range(1, 30):
	print("+++++++++++++++++++++++", str(size_window), "+++++++++++++++++++++++")
	print(len(seq_index_canddt))
	aa.append(len(seq_index_canddt))

	dict_canddt.append(set(chain.from_iterable(seq_index_canddt)))
	
	for index_canddt in seq_index_canddt:
		tsr_target = make_tsr_slice(seq_xpath_encoded_3d, index_canddt[0], size_window)
		tsr_compared = make_tsr_slice(seq_xpath_encoded_3d, index_canddt[1], size_window)
		dist = calculate_dist_tsr(tsr_target, tsr_compared)
		
		if dist <= 0:
			seq_index_canddt_new.append(index_canddt)
	
	seq_index_canddt = seq_index_canddt_new
	seq_index_canddt_new = []

	print(time.time())

for i, x in enumerate(dict_canddt):
	z = list(x)
	z.sort()
	print(i)
	print(z)
"""

# max_ws = get_max_size_window(seq_xpath_encoded_3d)

# size_window = max_ws
# max_index_start = calculate_max_index_start(seq_xpath_encoded_3d, size_window)
# threshold = 0

# seq_index_canddt = range(0, max_index_start)
# for size_window in range(1, max_ws):
# 	index_start_target = 0
# 	max_index_start = calculate_max_index_start(seq_xpath_encoded_3d, size_window)
	

# 	seq_index_canddt_new = []
# 	for index_start_target in seq_index_canddt: # +1?

# 	# while index_start_target < max_index_start:
# 		index_start_compared = index_start_target + size_window
		
# 		while index_start_compared <= max_index_start:
# 			tsr_target = make_tsr_slice(seq_xpath_encoded_3d, index_start_target, size_window)
# 			tsr_compared = make_tsr_slice(seq_xpath_encoded_3d, index_start_compared, size_window)

# 			dist = calculate_dist_tsr(tsr_target, tsr_compared)
			
# 			if dist <= threshold:
# 				index_start_compared += size_window
# 				seq_index_canddt_new.append(index_start_target)
# 				print(size_window, "...", index_start_target, index_start_compared, ":",dist)
# 			else:
# 				index_start_compared += 1
# 	set_index_canddt_new = set(seq_index_canddt_new)
# 	seq_index_canddt = list(set_index_canddt_new)
# 	print(time.time())

# for depth_eval in range(-1, -10, -1):
# 	seq_index_canddt = get_seq_index_canddt(seq_xpath_encoded, depth_eval)

# 	for size_slice in range(1, 10):
# 		seq_index_canddt_new = update_seq_index_canddt(seq_xpath_encoded, seq_index_canddt, size_slice)
# 		seq_index_canddt = seq_index_canddt_new
		# print(depth_eval, size_slice)
		# print(seq_index_canddt)
		# print("#############################################################################")
	

		# for index_canddt in seq_index_canddt:
		# 	for i in range(size_slice):
		# 		xpath = seq_xpath[index_canddt+i]
		# 		elems_located = locate_element(soup, xpath, get_attr_elem)
		# 		print(elems_located[-1].text)
		# 		print("#############################################################################")
		# 		print(i)
