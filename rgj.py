# coding="utf-8"

"""
Authors: KORKUT Caner
Date: 15-07-20
Description: This program allows to obtain the daily global radiation of the sun.
"""

"""
Hesite pas à intégrer des tas de print() pour voir les valeurs intermédiaires
"""

import requests

#on obtient la page html au format texte
page_html = requests.get("https://www.bdb.be/Productendiensten/Weerbericht/Onlineweerbericht/tabid/157/language/fr-BE/Default.aspx").text

"""
on crée une liste avec 2 éléments: 
1) Tout ce qui precede le mot "Rayonnement" 
2) Tout ce qui suit le mot "Rayonnement"
"""
experimental_ls = page_html.split("Rayonnement")


#idem que précédemment mais avec "Direction du vent"
experimental_ls_2 = experimental_ls[1].split('Direction du vent')

#idem avec "nowrap>"
experimental_ls_3 = experimental_ls_2[0].split("nowrap>")

#idem avec </td>
rayonnements_globaux_journaliers = []
for i in range(1, len(experimental_ls_3)):
	rayonnements_globaux_journaliers.append(experimental_ls_3[i].split("</td>")[0])

rayonnements_globaux_journaliers.remove("(global)")
rayonnements_globaux_journaliers.pop()

#liste finale, contient tout ce qu'il faut
#print(rayonnements_globaux_journaliers)

#les étapes qui suivent permettent d'obtenir les dates via la page HTML
experimental_ls_5 = []
for elem in page_html.split("<tr> <td class='weatherColCaption' valign='middle' align='center'  nowrap></td>")[1].split('</tr><tr>')[0].split("nowrap>"):
	experimental_ls_5.append(elem)

dates = []
for i in range(1, len(experimental_ls_5)):
	dates.append(experimental_ls_5[i].split('</th>')[0])

"""
Voici les valeurs intermédiaires intéressantes:
print(dates)
print(rayonnements_globaux_journaliers)
"""

if __name__ == "__main__":
	print("""
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

		""")
	for i in range(7):
		print("[*] {} => {} [J/cm2] : {}".format(dates[i], rayonnements_globaux_journaliers[i], rayonnements_globaux_journaliers[i+7]))

	print("\n*** Valeurs obtenues en temps réel sur le site du Service Pédologique de Belgique ASBL : https://www.bdb.be ***")