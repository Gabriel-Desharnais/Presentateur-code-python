#!/usr/bin/python3
# -*- coding: utf-8 -*

import cgi 
import cgitb
cgitb.enable()
print("Content-type: text/html; charset=utf-8\n")


html = """<!DOCTYPE html>
<html>
	<head>
		<link rel="stylesheet" href="http://localhost:8888/StylePres.css"> <!--Ceci importe le style dans le document-->
		<meta charset="utf-8">
		<title>Ma présentation</title>
	</head>


	<body> <!--Faudrait faire de quoi pour pouvoir changer le font d'écran-->
		
	<!--Ajouter les boutons et boites de texte-->
		<button class="button1" onclick="func1()">Exécuter</button>
		<textarea id="1" rows="1" cols="80"></textarea>
		<textarea id="2" rows="5" cols="80"></textarea>
		<pre id="sortie"></pre>
	<!--Script-->
		<script>
			function func1(){
				var xhttp = new XMLHttpRequest();
				xhttp.onreadystatechange = function() {
					if (xhttp.readyState == 4 && xhttp.status == 200) {
						document.getElementById("sortie").innerHTML = xhttp.responseText;
					}
				};
				xhttp.open("POST", "/cgi/doc.py", true);
				xhttp.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
				xhttp.send("test="+encodeURIComponent(document.getElementById("1").value));
			}
			<!--Fonction pour afficher dans la sortie l'entrée-->
			function func2(){
				document.getElementById("sortie").innerHTML= document.getElementById("1").value
			}
		</script>
	</body>   
</html>
"""

print(html)

