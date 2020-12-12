from xml.dom.minidom import parse
import xml.dom.minidom

dom_tree = parse("example.xml")
menu = dom_tree.documentElement
data = menu.getElementsByTagName("food")

for food in data:
    print(f"Name: {food.getElementsByTagName('name')[0].childNodes[0].nodeValue}\n"
          f"Price: {food.getElementsByTagName('price')[0].childNodes[0].nodeValue}\n"
          f"Description: {food.getElementsByTagName('description')[0].childNodes[0].nodeValue}\n"
          f"Calories: {food.getElementsByTagName('calories')[0].childNodes[0].nodeValue}\n")

data[0] = menu.getElementsByTagName('name')[0].childNodes[0].nodeValue = "Bacon Burger"
modified = open("example_m.xml", "w")
dom_tree.writexml(modified)
modified.close()

