# coding="utf-8"

"""
Authors: KORKUT Caner
Date: 15-07-20
Description: This program allows to obtain the daily global radiation of the sun.
"""

import requests

class Rgj(object):
	"""Rgj pour Rayonnement global journalier"""
	def __init__(self):
		self.page_html = requests.get("https://www.bdb.be/Productendiensten/Weerbericht/Onlineweerbericht/tabid/157/language/fr-BE/Default.aspx").text
		self.experimental_ls = self.page_html.split("Rayonnement")
		self.experimental_ls_2 = self.experimental_ls[1].split('Direction du vent')
		self.experimental_ls_3 = self.experimental_ls_2[0].split("nowrap>")
		self.rayonnements_globaux_journaliers = []
		self.experimental_ls_5 = []
		self.dates = []
		self.results = []

		for i in range(1, len(self.experimental_ls_3)):
			self.rayonnements_globaux_journaliers.append(self.experimental_ls_3[i].split("</td>")[0])

		self.rayonnements_globaux_journaliers.remove("(global)")
		self.rayonnements_globaux_journaliers.pop()

		for elem in self.page_html.split("<tr> <td class='weatherColCaption' valign='middle' align='center'  nowrap></td>")[1].split('</tr><tr>')[0].split("nowrap>"):
			self.experimental_ls_5.append(elem)

		for i in range(1, len(self.experimental_ls_5)):
			self.dates.append(self.experimental_ls_5[i].split('</th>')[0])

		for i in range(7):
			self.results.append(html.unescape("[*] {} => {} [J/cm2] : {}".format(self.dates[i], self.rayonnements_globaux_journaliers[i], self.rayonnements_globaux_journaliers[i+7])))

		#print("\n*** Valeurs obtenues en temps réel sur le site du Service Pédologique de Belgique ASBL : https://www.bdb.be ***")
	def get_results(self):
		return self.results
	def init_message(self):

		return """
	 ____                                                         _
	|  _ \ __ _ _   _  ___  _ __  _ __   ___ _ __ ___   ___ _ __ | |_
	| |_) / _` | | | |/ _ \| '_ \| '_ \ / _ \ '_ ` _ \ / _ \ '_ \| __|
	|  _ < (_| | |_| | (_) | | | | | | |  __/ | | | | |  __/ | | | |_
	|_| \_\__,_|\__, |\___/|_| |_|_| |_|\___|_| |_| |_|\___|_| |_|\__|
	            |___/
	  ____ _       _           _
	 / ___| | ___ | |__   __ _| |
	| |  _| |/ _ \| '_ \ / _` | |
	| |_| | | (_) | |_) | (_| | |
	 \____|_|\___/|_.__/ \__,_|_|

	     _                              _ _
	    | | ___  _   _ _ __ _ __   __ _| (_) ___ _ __   _
	 _  | |/ _ \| | | | '__| '_ \ / _` | | |/ _ \ '__| (_)
	| |_| | (_) | |_| | |  | | | | (_| | | |  __/ |     _
	 \___/ \___/ \__,_|_|  |_| |_|\__,_|_|_|\___|_|    (_)

			"""

if __name__ == '__main__':
	query = Rgj()
	print(query.init_message())
	
	for elem in query.get_results():
		print(elem)
