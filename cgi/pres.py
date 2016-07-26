#!/usr/bin/python3
# -*- coding: utf-8 -*

import cgi 

form = cgi.FieldStorage()
print("Content-type: text/html; charset=utf-8\n")

print(form.getvalue("name"))

html = """<!DOCTYPE html>
<html>
   <head>
    <style>
      #page-wrap{
      width: 1040px;
      margin: 0 auto;
      }
      ul {
	list-style-type: none;
	margin:0;
	padding:0;
	overflow: hidden;
      }
      li {
	float: left;
      }
      a:link, a:visited{
	display: block;
	width: 200px;
	font-weight: bold;
	color: #FFFFFF;
	background-color: #686FFF;
	text-align: center;
	padding: 4px;
	text-decoration: none;
	text-transform: uppercase;
      }
      a:hover, a:active {
	background-color:#0000b0;
      }
    </style>
      <meta charset="utf-8">
      <title>Ma présentation</title>
   </head>
	
   <body background = "background.png">
      <div id ="page-wrap">
      <canvas id="banière du dessus" width="1040" height="100">
      </canvas>
      
      <script>
	var c = document.getElementById("banière du dessus");
	var ctx = c.getContext("2d");
	img = new Image;
	img.src="daphnie.jpg";
	ctx.drawImage(img,0,0,100,100);
	ctx.fillStyle = "#000000";
	ctx.fillRect(100,0,940,100);
	ctx.font = "40px Arial";
	ctx.fillStyle = "#FFFFFF";
	ctx.fillText("Société de calcul scientifique distribué",150,60);
      </script>
      <ul>
	<li><a href="index.html">Exécuter</a></li>
	<li><a href="nouvelles">Exécuter tout</a></li>
	<li><a href="téléchargements">Quiter</a></li>
	<li><a href="contribuer">Contribuer</a></li>
	<li><a href="ensavoirplus">En savoir plus</a></li>
      </ul>
      <table bgcolor="#ffffff" width="1040">
      <tr><td>
      
      </td></tr>
      </table>
      </div>
   </body>   
</html>
"""

print(html)

