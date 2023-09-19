


function show_clock(){ /*recupère l'heure actuelle a l'aide de l'objet "Date",
puis calcule les angles de rotation pour chaque aiguille*/

/*recupere les elements avec la class et les stockes dans les variables*/                           
let h = document.getElementsByClassName('hr')[0];
let m = document.getElementsByClassName('mn')[0];
let s = document.getElementsByClassName('ss')[0];

let date = new Date();/*cree un nouvel onglet Date qui represente la date et l'heure actuelles*/

let hours = date.getHours();   /*recupere les heures actuelle a partir de l'objet Date et les stocke dans les variable*/
let minutes = date.getMinutes();
let seconds = date.getSeconds();

/*calculer les angles de rotation necessaire pour afficher correctement les aiguilles sur l'horloge analogique
Chaque aiguille se deplace a un angle specifique en fonction de l'heure actuelles*/

h.style.transform = `rotate(${30 * hours + minutes/2}deg)`;  
m.style.transform = `rotate(${6 * minutes}deg)`;
s.style.transform = `rotate(${6 * seconds}deg)`;

/*cree un objet 'Audio' et charge un fichier audio*/

let sound = new Audio('sound.wav');
sound.play();  
}


setInterval(show_clock, 1000);  /*cette fonction appelle la fonction show_clock toutes les secondes*/