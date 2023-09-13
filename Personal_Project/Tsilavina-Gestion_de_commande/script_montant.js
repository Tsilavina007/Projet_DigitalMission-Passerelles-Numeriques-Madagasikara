// Gestionnaire d'événement pour le bouton "Gestion des montants"
// Lorsque le bouton "Gestion des montants" (avec l'ID "accueil-btn") est cliqué,
// cette fonction de rappel redirige l'utilisateur vers la page "index.html".
document.getElementById("accueil-btn").addEventListener("click", () => {
    window.location.href = "index.html"; // Redirection vers la page de gestion des montants
});

// Fonction pour ouvrir la boîte de dialogue
// Cette fonction ouvre la boîte de dialogue (élément HTML avec l'ID "myDialog").
function openDialog() {
    var dialog = document.getElementById("myDialog");
    dialog.showModal();
}

// Fonction pour fermer la boîte de dialogue
// Cette fonction ferme la boîte de dialogue (élément HTML avec l'ID "myDialog").
function closeDialog() {
    var dialog = document.getElementById("myDialog");
    dialog.close();
}

// Sélection des éléments HTML nécessaires
// On sélectionne des éléments HTML avec leurs ID pour les utiliser plus tard.
const montantInput = document.getElementById("montant-input");
const descriptionInput = document.getElementById("description-input");
const ajouterBtn = document.getElementById("ajouter-btn");
const montantsTodayList = document.getElementById("montants-today");
const bilanSemaine = document.getElementById("bilan-semaine");
const bilanMois = document.getElementById("bilan-mois");

// Variables globales pour stocker les montants
// On initialise une variable "montants" qui contiendra les montants sous forme d'objet JavaScript.
// On récupère également les montants depuis le stockage local (localStorage) si des montants existent déjà.
let montants = JSON.parse(localStorage.getItem("montants")) || [];

// Fonction pour ajouter un nouveau montant
// Cette fonction est appelée lorsque le bouton d'ajout (avec l'ID "ajouter-btn") est cliqué.
function ajouterMontant() {
    // On récupère le montant et la description saisis par l'utilisateur.
    const montant = Number(montantInput.value);
    const description = descriptionInput.value.trim();

    // On vérifie si le montant et la description ne sont pas vides/nulls.
    if (montant && description) {
        // On crée un nouvel objet "nouveauMontant" avec les valeurs saisies par l'utilisateur et la date actuelle.
        const nouveauMontant = {
            montant,
            description,
            date: formatDateTime(new Date())
        };

        // On ajoute le nouvel objet "nouveauMontant" au tableau "montants".
        montants.push(nouveauMontant);

        // On sauvegarde la liste des montants dans le stockage local (localStorage).
        localStorage.setItem("montants", JSON.stringify(montants));

        // On met à jour l'affichage des montants et les bilans.
        afficherMontants();
        calculerBilanSemaine();
        calculerBilanMois();

        // On vide les champs de saisie après l'ajout.
        montantInput.value = "";
        descriptionInput.value = "";
    }
}



// Fonction pour afficher les montants obtenus aujourd'hui
// Cette fonction filtre les montants pour obtenir ceux d'aujourd'hui,
// puis les affiche dans des listes distinctes sur la page.
function afficherMontants() {
    // On crée une date d'aujourd'hui pour filtrer les montants.
    const today = new Date();

    // On filtre les montants pour obtenir ceux d'aujourd'hui (montantsToday).
    const montantsToday = montants.filter(montant => {
        const montantDate = new Date(montant.date);
        const isToday = (
            montantDate.getFullYear() === today.getFullYear() &&
            montantDate.getMonth() === today.getMonth() &&
            montantDate.getDate() === today.getDate()
        );
        return isToday; // Retourne true si c'est un montant d'aujourd'hui, sinon false.
    });

    // On réinitialise les listes HTML pour afficher les montants.
    montantsTodayList.innerHTML = "";

    // On affiche les montants d'aujourd'hui dans une liste HTML.
    if (montantsToday.length > 0) {
        montantsToday.forEach((montant, index) => {
            // On crée les éléments HTML pour chaque montant.
            const span_btn = document.createElement("span");
            const div = document.createElement("div");
            const li = document.createElement("li");
            li.textContent = `${montant.description} : ${montant.montant} Ar`;
            const li1 = document.createElement("li");
            li1.textContent = `${montant.date}`;
            const supprimerBtn = document.createElement("button");
            supprimerBtn.textContent = "Fafaina";
            supprimerBtn.addEventListener("click", () => supprimerMontant(index));

            // On organise les éléments et les ajoute à la liste d'aujourd'hui.
            div.appendChild(li);
            div.appendChild(li1);
            span_btn.appendChild(div)
            span_btn.appendChild(supprimerBtn);
            montantsTodayList.appendChild(span_btn);
        });
    } else {
        // Si aucun montant n'a été ajouté aujourd'hui, on affiche un message dans la liste.
        montantsTodayList.innerHTML = "<li>Tsy misy vola androany</li>";
    }

    // On calcule le bilan d'aujourd'hui.
    calculerBilanAujourdhui();
}











// Fonction pour formater la date au format "yyyy-MM-dd"
function formatDate(date) {
    const year = date.getFullYear();
    const month = String(date.getMonth() + 1).padStart(2, "0");
    const day = String(date.getDate()).padStart(2, "0");
    return `${year}-${month}-${day}`;
}

// Tableau des jours de la semaine en malgache
const malagasyDaysOfWeek = [
    'Alahady', // Dimanche
    'Alatsinainy', // Lundi
    'Talata', // Mardi
    'Alarobia', // Mercredi
    'Alakamisy', // Jeudi
    'Zoma', // Vendredi
    'Sabotsy' // Samedi
];

// Fonction pour formater la date et l'heure au format "jour, yyyy-MM-dd hh:mm"
// Cette fonction prend une date en paramètre et renvoie une chaîne de caractères
// au format "jour, yyyy-MM-dd hh:mm" en utilisant le tableau "malagasyDaysOfWeek".
function formatDateTime(datetime) {
    const date = new Date(datetime);
    const dayOfWeek = date.getDay(); // Récupérer le jour de la semaine (0-6)
    const day = date.getDate();
    const month = date.getMonth() + 1;
    const year = date.getFullYear();
    const hours = date.getHours();
    const minutes = date.getMinutes();

    // On forme la chaîne de caractères avec la date et l'heure formatées.
    const formattedDate = `${malagasyDaysOfWeek[dayOfWeek]}, ${year}-${month}-${day} ${hours}:${minutes}`;

    return formattedDate;
}

// Fonction pour supprimer un montant
// Cette fonction supprime un montant de la liste en utilisant l'index fourni,
// puis met à jour le stockage local et l'affichage des montants et des bilans.
function supprimerMontant(index) {
    const confirmation = confirm("Tena te-hamafa io safidinao io ve ianao ?");
    if (confirmation) {
        montants.splice(index, 1);
        localStorage.setItem("montants", JSON.stringify(montants));
        afficherMontants();
        calculerBilanAujourdhui();
        calculerBilanSemaine();
        calculerBilanMois();
    }
}

// Fonction pour calculer le bilan d'aujourd'hui
// Cette fonction calcule le total des montants d'aujourd'hui et l'affiche dans l'élément HTML avec l'ID "bilan-aujourd'hui".
function calculerBilanAujourdhui() {
    const today = new Date(); // Récupérer la date d'aujourd'hui

    // Filtrer les montants pour obtenir ceux enregistrés aujourd'hui
    const montantsAujourdhui = montants.filter(montant => {
        const montantDate = new Date(montant.date); // Convertir la date du montant en objet Date
        // Vérifier si la date du montant correspond à la date d'aujourd'hui (même année, même mois, même jour)
        return (
            montantDate.getFullYear() === today.getFullYear() &&
            montantDate.getMonth() === today.getMonth() &&
            montantDate.getDate() === today.getDate()
        );
    });

    // Calculer le total des montants enregistrés aujourd'hui en utilisant la méthode reduce()
    const totalAujourdhui = montantsAujourdhui.reduce((acc, montant) => acc + montant.montant, 0);

    // Récupérer l'élément HTML où le bilan d'aujourd'hui sera affiché
    const bilanAujourdhui = document.getElementById("bilan-aujourd'hui");
    // Modifier le contenu de l'élément HTML pour afficher le bilan d'aujourd'hui
    bilanAujourdhui.textContent = `Ny vola niditra : ${totalAujourdhui} Ar`;
}


// Fonction pour calculer le bilan de la semaine
function calculerBilanSemaine() {
    const today = new Date(); // Récupère la date d'aujourd'hui
    const lastWeek = new Date(today.getFullYear(), today.getMonth(), today.getDate() - 7); // Crée une nouvelle date qui correspond à il y a 7 jours
    
    // Filtrer les montants pour obtenir ceux de la semaine en cours
    const montantsSemaine = montants.filter(montant => {
        const montantDate = new Date(montant.date); // Convertir la date du montant en objet Date
        return montantDate >= lastWeek; // Vérifier si la date du montant est supérieure ou égale à il y a 7 jours
    });
    const totalSemaine = montantsSemaine.reduce((acc, montant) => acc + montant.montant, 0); // Calculer le total des montants de la semaine

    bilanSemaine.textContent = `Vola niditra : ${totalSemaine} Ar`; // Afficher le résultat dans l'élément HTML ayant l'ID "bilan-semaine"
}

// Fonction pour calculer le bilan du mois
function calculerBilanMois() {
    const today = new Date(); // Récupère la date d'aujourd'hui
    const firstDayOfMonth = new Date(today.getFullYear(), today.getMonth(), 1); // Crée une nouvelle date qui correspond au premier jour du mois en cours

    // Filtrer les montants pour obtenir ceux du mois en cours
    const montantsMois = montants.filter(montant => {
        const montantDate = new Date(montant.date); // Convertir la date du montant en objet Date
        return montantDate >= firstDayOfMonth; // Vérifier si la date du montant est supérieure ou égale au premier jour du mois
    });
    const totalMois = montantsMois.reduce((acc, montant) => acc + montant.montant, 0); // Calculer le total des montants du mois

    bilanMois.textContent = `Vola niditra : ${totalMois} Ar`; // Afficher le résultat dans l'élément HTML ayant l'ID "bilan-mois"
}


// Gestionnaire d'événement pour le bouton d'ajout
// Lorsque le bouton d'ajout (avec l'ID "ajouter-btn") est cliqué, cette fonction de rappel appelle la fonction ajouterMontant().
ajouterBtn.addEventListener("click", ajouterMontant);

// Appel des fonctions au chargement de la page
// Ces fonctions sont appelées au chargement de la page pour afficher les montants et les bilans.
afficherMontants();
calculerBilanSemaine();
calculerBilanMois();



// Fonction pour afficher les montants obtenus à une date spécifique
// Cette fonction prend une date en paramètre et affiche les montants correspondants dans une boîte de dialogue (modal).
function afficherMontantsParDate(date) {
    const selectedDate = new Date(date); // Convertir la date au format de type Date
    const formattedDate = selectedDate.toLocaleDateString(); // Formater la date au format "MM/dd/yyyy"

    // Filtrer les montants pour obtenir ceux correspondant à la date sélectionnée
    const montantsByDate = montants.filter(montant => {
        const montantDate = new Date(montant.date); // Convertir la date du montant en objet Date
        return montantDate.toLocaleDateString() === formattedDate; // Vérifier si la date du montant correspond à la date sélectionnée
    });

    const modalContent = document.getElementById("modal-content"); // Récupérer l'élément HTML où les montants seront affichés
    modalContent.innerHTML = ""; // Réinitialiser le contenu de l'élément HTML pour afficher les montants

    if (montantsByDate.length > 0) {
        // Si des montants sont trouvés pour la date sélectionnée, les afficher un par un dans la boîte de dialogue modale
        montantsByDate.forEach(montant => {
            const li = document.createElement("li"); // Créer un nouvel élément <li> pour chaque montant
            li.textContent = `${montant.montant} Ar - ${montant.description}`; // Remplir le texte du <li> avec les informations du montant
            modalContent.appendChild(li); // Ajouter le <li> à l'élément HTML où les montants sont affichés
        });

        // Calculer le bilan du jour sélectionné
        const totalMontantsByDate = montantsByDate.reduce((acc, montant) => acc + montant.montant, 0);

        // Créer un élément <p> pour afficher le bilan du jour sélectionné
        const bilanParDate = document.createElement("p");
        bilanParDate.textContent = `Vola azo tamin'ny: ${formattedDate} : ${totalMontantsByDate} Ar`;
        modalContent.appendChild(bilanParDate); // Ajouter le <p> à l'élément HTML où les montants sont affichés
    } else {
        // Si aucun montant n'est trouvé pour la date sélectionnée, afficher un message indiquant qu'il n'y a pas de montant
        const noMontantMessage = document.createElement("p"); // Créer un nouvel élément <p>
        noMontantMessage.textContent = "Tsy nisy"; // Remplir le texte du <p> avec le message indiquant qu'il n'y a pas de montant
        modalContent.appendChild(noMontantMessage); // Ajouter le <p> à l'élément HTML où les montants sont affichés
    }

    // Afficher la modal
    const modal = document.getElementById("modal"); // Récupérer l'élément HTML de la boîte de dialogue modale
    modal.style.display = "block"; // Modifier le style pour afficher la boîte de dialogue modale
}







// JavaScript : Écouter l'événement de soumission du formulaire
document.getElementById("select-month-form").addEventListener("submit", function (event) {
    event.preventDefault(); // Empêcher le rechargement de la page

    const month = parseInt(document.getElementById("month-select").value); // Récupérer le mois sélectionné
    const year = parseInt(document.getElementById("year-select").value); // Récupérer l'année sélectionnée

    afficherMontantsParMois(month, year); // Appeler la fonction pour afficher les montants du mois sélectionné
});



// Fonction pour afficher les montants obtenus pour un mois donné
function afficherMontantsParMois(month, year) {
    // Filtrer les montants pour obtenir ceux du mois et de l'année sélectionnés (montantsByMonth).
    const montantsByMonth = montants.filter(montant => {
        const montantDate = new Date(montant.date);
        return (
            montantDate.getFullYear() === year &&
            montantDate.getMonth() === month - 1 // Les mois commencent à 0 dans JavaScript (0 = janvier, 1 = février, etc.)
        );
    });

    const modalContent = document.getElementById("modal-content1");
    modalContent.innerHTML = "";

    if (montantsByMonth.length > 0) {

        // Calculer le bilan du mois sélectionné
        const totalMontantsByMonth = montantsByMonth.reduce((acc, montant) => acc + montant.montant, 0);

        const bilanParMois = document.createElement("p");
        bilanParMois.textContent = `Vola azo tamin'ny volana ${formatMonth(month)} ${year} : ${totalMontantsByMonth} Ar`;
        modalContent.appendChild(bilanParMois);
    } else {
        const noMontantMessage = document.createElement("p");
        noMontantMessage.textContent = "Tsy nisy";
        modalContent.appendChild(noMontantMessage);
    }

    const modal = document.getElementById("modal");
    modal.style.display = "block";
}

// Fonction utilitaire pour formater le nom du mois (par exemple, "1" => "Janvier", "2" => "Février", etc.)
function formatMonth(month) {
    const months = [
        "Janvier", "Février", "Mars", "Avril", "Mai", "Juin",
        "Juillet", "Août", "Septembre", "Octobre", "Novembre", "Décembre"
    ];
    return months[month - 1];
}












// Fonction pour ouvrir la modal et afficher les montants par date sélectionnée
// Cette fonction est appelée lorsque le bouton "Ouvrir modal" (avec l'ID "ouvrir-modal-btn") est cliqué.
function ouvrirModal() {
    // On récupère la date sélectionnée par l'utilisateur depuis l'élément "date-input".
    const selectedDate = document.getElementById("date-input").value;
    // On appelle la fonction pour afficher les montants correspondants à la date sélectionnée.
    afficherMontantsParDate(selectedDate);
}

// Gestionnaire d'événement pour le bouton d'ouverture de la modal
// Lorsque le bouton "Ouvrir modal" (avec l'ID "ouvrir-modal-btn") est cliqué, cette fonction de rappel appelle la fonction ouvrirModal().
const ouvrirModalBtn = document.getElementById("ouvrir-modal-btn");
ouvrirModalBtn.addEventListener("click", ouvrirModal);

// Gestionnaire d'événement pour le bouton de fermeture de la modal
// Lorsque le bouton de fermeture de la modal (avec l'ID "fermer-modal-btn") est cliqué,
// cette fonction de rappel ferme la modal en changeant son style "display" en "none".
const fermerModalBtn = document.getElementById("fermer-modal-btn");
fermerModalBtn.addEventListener("click", () => {
    const modal = document.getElementById("modal");
    modal.style.display = "none";
});
