import nltk
from nltk.corpus import stopwords
text = open('D:/mayur/Masters/Text Analytics/assignment 4/Question1.txt')
combinedtext = text.read()
doc1 = "Well, I think that Apple is the best laptop brand. The laptops from this brand are really good to work on and are very smooth. But the cost of Apple laptops is on a higher side. In case, the budget is an issue then go with Dell. The brand manufactures durable and robust laptop with latest features."
doc2 = "Well, the choice of laptop brands also depends on your needs. Like if you require the laptop for gaming then MSI or Razer Blade or Asus is the brands to go with. But if you need the laptop for surfing the net, watching movies or playing light games then the laptops from Dell and Lenovo are good enough."
doc3 = "As I repair & trouble shoot laptops. I not only look at features but also serviceability. What is involved in changing out the battery, replacing the cooling fan & how well is the lcd protected from damage by a slight drop or bump against a solid object. Use a best piece of Laptop."
doc4 = "Before you purchase have a look at a You Tube strip down of what your looking to buy particularly in consumer laptops.If you don't feel up to servicing yourself get an extended warranty & cover against accidental damage so that if something goes ferral or breaks then you won't be paying an arm & a leg to get it working again."
doc5 = "As many publications are saying they seem to be ignoring their pc lines and concentrating on Ipads and Iphones. Also this is rating the overall brands which all Windows OEM's have model that hit all price ranges. The more expensive models of each OEM are better than their lower priced but the support is the same for all priced model from the same OEM. That is a big difference." 
doc6 = "Hi, this is not a shaming post. It is a warning post about a specific ASUS product: the built in battery. After less than three years it might blow up into your laptop like cellular phones Samsung batteries. This is my Asus laptop X455L , three years old. "
doc7 = "I contacted the ASUS service in Israel and they was not l impressed at all and they proposed me a regular out of warranty repair. A regular battery failure from their point of view. But I think they must analyze these battery problems seriously because one day it will happen like with the Samsung cellular phone battery."
doc8 = "Well, Apple is the good one but according to budget, I think Acer, Dell, HP is the good options. Lenovo is the good one but I experienced its heating problem while more working." 
doc9 = "Companies are in this business to make money so it is assured that there will be a positive correlation between quality and price. A laptop packed with features & priced reasonably is not built to last for more than 3–4 years (last without constant troubles) .This is where the Acers and Samsungs of the world operate."
doc10 = "Companies also have different lines of laptops in their portfolio, the quality varies across them. Take for example Lenovo, the ideapad range is not meant to work at full efficiency for more than 4 years while the thinkpad range can cross the 5 year mark with ease."
stop = stopwords.words('english')
combinedtext_s = [i for i in combinedtext.split() if i not in stop]
doc1_s = [i for i in doc1.split() if i not in stop]
doc2_s = [i for i in doc2.split() if i not in stop]
doc3_s = [i for i in doc3.split() if i not in stop]
doc4_s = [i for i in doc4.split() if i not in stop]
doc5_s = [i for i in doc5.split() if i not in stop]
doc6_s = [i for i in doc6.split() if i not in stop]
doc7_s = [i for i in doc7.split() if i not in stop]
doc8_s = [i for i in doc8.split() if i not in stop]
doc9_s = [i for i in doc9.split() if i not in stop]
doc10_s = [i for i in doc10.split() if i not in stop]
print(combinedtext_s)
print(doc1_s)
print(doc2_s)
print(doc3_s)
print(doc4_s)
print(doc5_s)
print(doc6_s)
print(doc7_s)
print(doc8_s)
print(doc9_s)
print(doc10_s)

