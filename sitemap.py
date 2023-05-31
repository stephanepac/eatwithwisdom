import csv
site="https://github.com/stephanepac/eatwithwisdom/"
sitemap="<urlset>"
pages=['a_propos.html',"index.html","articles.html"]
for page in pages:
    sitemap+="<url><loc>"+site+page+"/</loc></url> \n"
fichier=open("pages.csv","r")

reader=csv.reader(fichier,delimiter=";")

for ligne in reader:
    sitemap+="<url> <loc>"+site+ligne[0]+"/</loc></url>  \n"

sitemap+="</urlset>"

fichier.close()

fichier_sitemap=open("site.xml","w")
fichier_sitemap.write(sitemap)
fichier_sitemap.close()