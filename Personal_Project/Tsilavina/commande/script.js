// Gestionnaire d'événement pour le bouton "Gestion des montants"
document.getElementById("accueil-btn").addEventListener("click", () => {
  window.location.href = "../index.html"; // Redirection vers la page de gestion des montants
});

// Sélection des éléments du DOM
const taskInput = document.querySelector(".task-input input"), // Champ de saisie de tâche
  taskDatetimeInput = document.querySelector(".task-input .task-datetime"), // Champ de saisie de la date et heure de la tâche
  clientNameInput = document.querySelector(".client-input input"), // Champ de saisie du nom du client
  clientContactInput = document.querySelector(".client-input .client-contact-input"), // Champ de saisie du contact du client
  vidinyInput = document.querySelector(".client-input .vidiny-input"), // Champ de saisie du montant "Vidiny"
  avanceInput = document.querySelector(".client-input .avance-input"), // Champ de saisie du montant "Avance"
  clientPlusInput = document.querySelector(".client-input .client-plus"), // Champ de saisie d'informations supplémentaires sur le client
  filters = document.querySelectorAll(".filters span"), // Filtres pour afficher toutes, en attente ou complétées
  clearAll = document.querySelector(".clear-btn"), // Bouton pour supprimer toutes les tâches affichées
  taskCounts = document.querySelectorAll(".filter-count"), // Compteurs pour afficher le nombre de tâches filtrées
  taskBox = document.querySelector(".task-box"), // Conteneur pour afficher la liste des tâches
  addTaskBtn = document.querySelector("#add-task-btn"), // Bouton pour ajouter une nouvelle tâche
  selectDay = document.getElementById("select-day"); // Sélecteur de jour pour filtrer les tâches par date

// Gestionnaire d'événement pour le bouton "myBtn" qui affiche ou masque le menu déroulant
document.getElementById("myBtn").onclick = function() {
  myFunction()
};

/* myFunction toggles between adding and removing the show class, which is used to hide and show the dropdown content */
// Fonction pour afficher ou masquer le menu déroulant
function myFunction() {
  document.getElementById("myDropdown").classList.toggle("show");
}

// Fonction pour rendre visible la barre latérale
function w3_open() {
  document.getElementById("mySidebar").style.display = "block";
}

// Fonction pour masquer la barre latérale
function w3_close() {
  document.getElementById("mySidebar").style.display = "none";
}


let editId; // Identifiant de la tâche en cours d'édition (utilisé lors de la modification d'une tâche)
let isEditedTask = false; // Indicateur pour savoir si une tâche est en cours de modification
let todos = JSON.parse(localStorage.getItem("todo-list")) || []; // Tableau des tâches récupéré depuis le stockage local ou un tableau vide s'il est vide

const todayDateElement = document.querySelector('.today-date'); // Élément du DOM pour afficher la date du jour

const malagasyDaysOfWeek = [
  'Alahady', // Dimanche
  'Alatsinainy', // Lundi
  'Talata', // Mardi
  'Alarobia', // Mercredi
  'Alakamisy', // Jeudi
  'Zoma', // Vendredi
  'Sabotsy' // Samedi
];

// Fonction pour mettre à jour le statut d'une tâche (terminée ou en attente)
function updateStatus(selectedTask) {
  let taskName = selectedTask.parentElement.lastElementChild; // Élément du DOM pour le nom de la tâche associée à la case à cocher
  if (selectedTask.checked) {
    taskName.classList.add("checked"); // Ajout de la classe "checked" pour indiquer que la tâche est terminée
    todos[selectedTask.id].status = "completed"; // Mise à jour du statut de la tâche dans le tableau "todos" à l'aide de son identifiant
  } else {
    taskName.classList.remove("checked"); // Suppression de la classe "checked" pour indiquer que la tâche est en attente
    todos[selectedTask.id].status = "pending"; // Mise à jour du statut de la tâche dans le tableau "todos" à l'aide de son identifiant
  }
  localStorage.setItem("todo-list", JSON.stringify(todos)); // Sauvegarde du tableau "todos" dans le stockage local (localStorage)
  updateTaskCounts(); // Appel de la fonction pour mettre à jour les compteurs de tâches filtrées
}

// Fonction pour mettre à jour les compteurs de tâches filtrées
function updateTaskCounts() {
  const countMap = {
    all: 0, // Compteur pour le nombre total de tâches
    pending: 0, // Compteur pour le nombre de tâches en attente
    completed: 0 // Compteur pour le nombre de tâches terminées
  };

  // Parcourir toutes les tâches dans le tableau "todos" pour les compter en fonction de leur statut
  todos.forEach(todo => {
    countMap.all++; // Incrémenter le compteur total de tâches
    countMap[todo.status]++; // Incrémenter le compteur de tâches selon leur statut (terminé ou en attente)
  });

  // Mettre à jour le contenu textuel des éléments du DOM représentant les compteurs de tâches filtrées
  taskCounts.forEach(taskCount => {
    const filter = taskCount.parentElement.id; // Récupérer l'ID du filtre associé au compteur de tâches
    const count = countMap[filter] || 0; // Obtenir le nombre de tâches correspondant au filtre ou 0 si le filtre n'existe pas dans "countMap"
    taskCount.textContent = ` (${count})`; // Mettre à jour le contenu textuel avec le nombre de tâches correspondant au filtre
  });
}
// Fonction pour afficher la liste des tâches filtrées
function showTodoList(filter, todos) {
  let li = ''; // Variable pour stocker le contenu HTML de la liste des tâches

  let filteredTodos = todos;
  // Filtrer les tâches en fonction du statut (terminé, en attente ou toutes)
  if (filter !== "all") {
    filteredTodos = filteredTodos.filter(todo => todo.status === filter);
  }

  // Trier les tâches par date d'échéance (du plus proche au plus éloigné)
  filteredTodos.sort((a, b) => new Date(a.dueDate) - new Date(b.dueDate));

  // Générer le contenu HTML pour chaque tâche filtrée
  if (filteredTodos.length > 0) {
    filteredTodos.forEach((todo, id) => {
      let isCompleted = todo.status === "completed" ? "checked" : ""; // Vérifier si la tâche est terminée pour cocher la case à cocher correspondante
      li += `<li class="task">
                <label for="${id}">
                    <input onclick="updateStatus(this)" type="checkbox" id="${id}" ${isCompleted}>
                    <p class="${isCompleted}">${todo.name}</p> 
                </label>
                <div class="form-date">
                  <span class="due-date">Mila vita: ${formatDateTime(todo.dueDate)}</span>
                  <span class="del_edit" onclick="deleteTask(${id})"><i><img src="icon/trash-regular-24.png" alt="trash"></i></span>
                  <span id="edit" class="del_edit" onclick="editTask(${id},'${todo.name}', '${todo.createdDate}', '${todo.dueDate}', '${todo.clientName}', '${todo.clientContact}','${todo.clientPlus}', '${todo.vidiny}', '${todo.avance}')"><i><img src="icon/edit-alt-regular-24.png" alt="edit"></i></span>  
                  <div class="settings">
                    <i onclick="showMenu(this)">...</i>
                    <ul class="task-menu">
                      <span class="created-date"><u>Nampidirina ny :</u> ${formatDateTime(todo.createdDate)}</span><br>
                      <span class="due-name"><u>Tompony :</u> ${todo.clientName}</span><br>
                      <span class="due-contact"><u>Finday :</u> ${todo.clientContact}</span><br>
                      <span class="due-plus"><u>Mombamomba :</u> ${todo.clientPlus}</span><br>
                      <span class="due-contact"><u>Vidiny :</u> ${todo.vidiny} Ar</span><br>
                      <span class="due-plus"><u>Avance :</u> ${todo.avance} Ar</span><br>
                    </ul>
                  </div>
                </div>
            </li>`;
    });
  } else {
    // Si aucune tâche n'est trouvée, afficher un message indiquant qu'il n'y a pas de tâches
    li = `<span class= "tsisy">Tsy misy asa</span>`;
  }

  // Mettre à jour le contenu de la liste des tâches dans le DOM
  taskBox.innerHTML = li;
}


// Fonction pour formater la date et l'heure dans un format personnalisé
function formatDateTime(datetime) {
  const date = new Date(datetime);
  const dayOfWeek = date.getDay(); // Récupérer le jour de la semaine (0-6)
  const day = date.getDate(); // Récupérer le jour du mois (1-31)
  const month = date.getMonth() + 1; // Récupérer le mois (0-11) et l'ajuster pour commencer à partir de 1
  const year = date.getFullYear(); // Récupérer l'année (ex: 2023)
  const hours = date.getHours(); // Récupérer l'heure (0-23)
  const minutes = date.getMinutes(); // Récupérer les minutes (0-59)

  // Créer une chaîne de caractères formatée contenant la date, l'heure et le jour de la semaine en malgache
  const formattedDate = `${malagasyDaysOfWeek[dayOfWeek]}, ${day}/${month}/${year} ${hours}:${minutes}`;

  return formattedDate; // Renvoyer la date et l'heure formatées
}

// Ajouter un gestionnaire d'événement à chaque élément de filtre pour les écouter lorsqu'ils sont cliqués
filters.forEach(filter => {
  filter.addEventListener("click", () => {
    const activeFilter = document.querySelector(".filters span.active");
    activeFilter.classList.remove("active"); // Retirer la classe "active" du filtre actif précédent
    filter.classList.add("active"); // Ajouter la classe "active" au filtre cliqué pour le marquer comme actif
    const selectedFilter = filter.id; // Récupérer l'ID du filtre sélectionné (all, pending ou completed)
    showTodoList(selectedFilter, todos); // Afficher la liste des tâches filtrées en fonction du filtre sélectionné
  });
});

updateTaskCounts(); // Mettre à jour les compteurs de tâches filtrées au chargement de la page

// Fonction pour afficher le menu contextuel (settings) d'une tâche lorsqu'elle est cliquée
function showMenu(selectedTask) {
  let taskMenu = selectedTask.parentElement.lastElementChild; // Sélectionner le menu contextuel associé à la tâche
  taskMenu.classList.add("show"); // Ajouter la classe "show" pour afficher le menu
  document.addEventListener("click", e => {
    // Ajouter un écouteur d'événement de clic sur tout le document
    if (e.target.tagName != "I" || e.target != selectedTask) {
      // Si le clic ne se produit pas sur l'icône "..." ou la tâche elle-même
      taskMenu.classList.remove("show"); // Cacher le menu contextuel
    }
  });
}
// Fonction pour formater la date et l'heure au format utilisé dans les champs d'entrée de date (type="datetime-local")
function formatDateTimeInput(datetime) {
  const date = new Date(datetime);
  const month = (date.getMonth() + 1).toString().padStart(2, '0'); // Obtenir le mois (0-11) et l'ajuster pour commencer à partir de 1
  const day = date.getDate().toString().padStart(2, '0'); // Obtenir le jour du mois (1-31) et le formater avec deux chiffres
  const hours = date.getHours().toString().padStart(2, '0'); // Obtenir les heures (0-23) et les formater avec deux chiffres
  const minutes = date.getMinutes().toString().padStart(2, '0'); // Obtenir les minutes (0-59) et les formater avec deux chiffres
  return `${date.getFullYear()}-${month}-${day}T${hours}:${minutes}`; // Renvoyer la date et l'heure au format ISO pour les champs d'entrée de date
}

// Fonction pour éditer une tâche existante en remplissant les champs d'entrée avec ses informations
function editTask(taskId, taskName, taskCreatedDate, taskDueDate, clientName, clientContact, clientPlus, vidiny, avance) {
  myFunction(); // Cacher le menu contextuel lors de l'édition de la tâche
  editId = taskId; // Définir l'ID de la tâche en cours d'édition
  isEditedTask = true; // Marquer la tâche comme étant en cours d'édition
  taskInput.value = taskName; // Remplir le champ d'entrée de nom de tâche avec le nom de la tâche existante
  taskDatetimeInput.value = formatDateTimeInput(taskDueDate); // Remplir le champ d'entrée de date et heure avec la date de fin de la tâche existante au format ISO
  clientNameInput.value = clientName; // Remplir le champ d'entrée de nom de client avec le nom de client existant
  clientContactInput.value = clientContact; // Remplir le champ d'entrée de contact de client avec le contact de client existant
  vidinyInput.value = vidiny; // Remplir le champ d'entrée "vidiny" avec la valeur existante
  avanceInput.value = avance; // Remplir le champ d'entrée "avance" avec la valeur existante
  clientPlusInput.value = clientPlus; // Remplir le champ d'entrée "clientPlus" avec la valeur existante
}

// Fonction pour supprimer une tâche en fonction de son ID
function deleteTask(deleteId) {
  const confirmation = confirm("Tena te-hamafa io safidinao io ve ianao ?");
  // Demander une confirmation à l'utilisateur avant de supprimer la tâche
  if (confirmation) {
    todos.splice(deleteId, 1); // Supprimer la tâche du tableau des tâches en utilisant l'ID de la tâche
    localStorage.setItem("todo-list", JSON.stringify(todos)); // Mettre à jour la liste des tâches dans le stockage local
    updateTaskCounts(); // Mettre à jour les compteurs de tâches filtrées
    showTodoList("all", todos); // Afficher la liste des tâches filtrées (toutes les tâches après la suppression)
  }
}

// Ajouter un gestionnaire d'événement pour détecter l'appui sur une touche dans le champ d'entrée de nom de tâche
taskInput.addEventListener("keyup", e => {
  let userTask = taskInput.value.trim(); // Récupérer le nom de la tâche sans espaces avant et après
  let dueDate = taskDatetimeInput.value; // Récupérer la date de fin de la tâche du champ d'entrée de date et heure
  let clientName = clientNameInput.value.trim(); // Récupérer le nom du client sans espaces avant et après
  let clientContact = clientContactInput.value.trim(); // Récupérer le contact du client sans espaces avant et après
  let clientPlus = clientPlusInput.value.trim(); // Récupérer la valeur du champ "clientPlus" sans espaces avant et après
  let vidiny = vidinyInput.value.trim(); // Récupérer la valeur du champ "vidiny" sans espaces avant et après
  let avance = avanceInput.value.trim(); // Récupérer la valeur du champ "avance" sans espaces avant et après

  // Vérifier si l'utilisateur appuie sur la touche "Enter" et que tous les champs requis sont remplis
  if (e.key == "Enter" && userTask && dueDate && clientName && clientContact && vidiny && avance && clientPlus) {
    if (!isEditedTask) {
      // Si la tâche n'est pas en cours d'édition, créer une nouvelle tâche avec les informations fournies
      let taskInfo = {
        name: userTask,
        status: "pending",
        createdDate: new Date(),
        dueDate,
        clientName,
        clientContact,
        vidiny,
        avance,
        clientPlus
      };
      todos.push(taskInfo); // Ajouter la nouvelle tâche à la liste des tâches
      myFunction(); // Cacher le menu contextuel après avoir ajouté la tâche
    } else {
      // Si la tâche est en cours d'édition, mettre à jour les informations de la tâche existante
      isEditedTask = false; // Réinitialiser le marqueur de tâche en cours d'édition
      todos[editId].name = userTask; // Mettre à jour le nom de la tâche existante avec le nouveau nom
      todos[editId].dueDate = dueDate; // Mettre à jour la date de fin de la tâche existante avec la nouvelle date
      todos[editId].clientName = clientName; // Mettre à jour le nom du client existant avec le nouveau nom de client
      todos[editId].clientContact = clientContact; // Mettre à jour le contact du client existant avec le nouveau contact de client
      todos[editId].clientPlus = clientPlus; // Mettre à jour la valeur du champ "clientPlus" de la tâche existante
      todos[editId].vidiny = vidiny; // Mettre à jour la valeur du champ "vidiny" de la tâche existante
      todos[editId].avance = avance; // Mettre à jour la valeur du champ "avance" de la tâche existante
      myFunction(); // Cacher le menu contextuel après avoir mis à jour la tâche
    }

    // Réinitialiser les champs d'entrée après avoir ajouté ou mis à jour la tâche
    taskInput.value = "";
    taskDatetimeInput.value = "";
    clientNameInput.value = "";
    clientContactInput.value = "";
    vidinyInput.value = "";
    avanceInput.value = "";
    clientPlusInput.value = "";

    localStorage.setItem("todo-list", JSON.stringify(todos)); // Mettre à jour la liste des tâches dans le stockage local
    updateTaskCounts(); // Mettre à jour les compteurs de tâches filtrées
    showTodoList("all", todos); // Afficher la liste de toutes les tâches filtrées
  }
});

// Ajouter un gestionnaire d'événement pour le bouton "Ajouter une tâche"
addTaskBtn.addEventListener("click", () => {
  let userTask = taskInput.value.trim(); // Récupérer le nom de la tâche sans espaces avant et après
  let dueDate = taskDatetimeInput.value; // Récupérer la date de fin de la tâche du champ d'entrée de date et heure
  let clientName = clientNameInput.value.trim(); // Récupérer le nom du client sans espaces avant et après
  let clientContact = clientContactInput.value.trim(); // Récupérer le contact du client sans espaces avant et après
  let clientPlus = clientPlusInput.value.trim(); // Récupérer la valeur du champ "clientPlus" sans espaces avant et après
  let vidiny = vidinyInput.value.trim(); // Récupérer la valeur du champ "vidiny" sans espaces avant et après
  let avance = avanceInput.value.trim(); // Récupérer la valeur du champ "avance" sans espaces avant et après

  // Vérifier si tous les champs requis sont remplis
  if (userTask && dueDate && clientName && clientContact && vidiny && avance && clientPlus) {
    if (!isEditedTask) {
      // Si la tâche n'est pas en cours d'édition, créer une nouvelle tâche avec les informations fournies
      let taskInfo = {
        name: userTask,
        status: "pending",
        createdDate: new Date(),
        dueDate,
        clientName,
        clientContact,
        vidiny,
        avance,
        clientPlus
      };
      todos.push(taskInfo); // Ajouter la nouvelle tâche à la liste des tâches
      myFunction(); // Cacher le menu contextuel après avoir ajouté la tâche
    } else {
      // Si la tâche est en cours d'édition, mettre à jour les informations de la tâche existante
      isEditedTask = false; // Réinitialiser le marqueur de tâche en cours d'édition
      todos[editId].name = userTask; // Mettre à jour le nom de la tâche existante avec le nouveau nom
      todos[editId].dueDate = dueDate; // Mettre à jour la date de fin de la tâche existante avec la nouvelle date
      todos[editId].clientName = clientName; // Mettre à jour le nom du client existant avec le nouveau nom de client
      todos[editId].clientContact = clientContact; // Mettre à jour le contact du client existant avec le nouveau contact de client
      todos[editId].vidiny = vidiny; // Mettre à jour la valeur du champ "vidiny" de la tâche existante
      todos[editId].avance = avance; // Mettre à jour la valeur du champ "avance" de la tâche existante
      todos[editId].clientPlus = clientPlus; // Mettre à jour la valeur du champ "clientPlus" de la tâche existante

      myFunction(); // Cacher le menu contextuel après avoir mis à jour la tâche
    }

    // Réinitialiser les champs d'entrée après avoir ajouté ou mis à jour la tâche
    taskInput.value = "";
    taskDatetimeInput.value = "";
    clientNameInput.value = "";
    clientContactInput.value = "";
    vidinyInput.value = "";
    avanceInput.value = "";
    clientPlusInput.value = "";

    localStorage.setItem("todo-list", JSON.stringify(todos)); // Mettre à jour la liste des tâches dans le stockage local
    updateTaskCounts(); // Mettre à jour les compteurs de tâches filtrées
    showTodoList("all", todos); // Afficher la liste de toutes les tâches filtrées
  }
});

// Ajouter un gestionnaire d'événement pour le sélecteur de jours (selectDay)
selectDay.addEventListener("change", () => {
  const selectedValue = selectDay.value; // Récupérer la valeur sélectionnée dans le sélecteur de jours
  const activeFilter = document.querySelector(".filters span.active").id; // Récupérer l'ID du filtre actuellement actif

  // Vérifier le filtre actif et filtrer les tâches par jour et statut en conséquence
  if (activeFilter === "all") {
    filterTasksByDayAndStatus(selectedValue, "all");
  } else if (activeFilter === "pending") {
    filterTasksByDayAndStatus(selectedValue, "pending");
  } else if (activeFilter === "completed") {
    filterTasksByDayAndStatus(selectedValue, "completed");
  }
});
// Fonction pour filtrer les tâches par jour et statut
function filterTasksByDayAndStatus(day, status) {
  let filteredTodos = todos; // Copie de la liste complète des tâches pour effectuer le filtrage
  const today = new Date();
  today.setHours(0, 0, 0, 0); // Réinitialiser les heures, minutes, secondes et millisecondes de la date actuelle à zéro

  // Filtrer les tâches en fonction du jour sélectionné
  if (day === "today") {
    filteredTodos = filteredTodos.filter(
      (todo) => new Date(todo.dueDate).setHours(0, 0, 0, 0) === today.getTime()
    );
  } else if (day === "tomorrow") {
    const tomorrow = new Date(today);
    tomorrow.setDate(tomorrow.getDate() + 1);
    filteredTodos = filteredTodos.filter(
      (todo) => new Date(todo.dueDate).setHours(0, 0, 0, 0) === tomorrow.getTime()
    );
  } else if (day === "next7days") {
    const next7days = new Date(today);
    next7days.setDate(next7days.getDate() + 7);
    filteredTodos = filteredTodos.filter(
      (todo) =>
        new Date(todo.dueDate) <= next7days &&
        new Date(todo.dueDate) >= today
    );
  }

  // Filtrer les tâches en fonction du statut (en cours ou terminées)
  if (status === "pending") {
    filteredTodos = filteredTodos.filter((todo) => todo.status === "pending");
  } else if (status === "completed") {
    filteredTodos = filteredTodos.filter((todo) => todo.status === "completed");
  }

  showTodoList("all", filteredTodos); // Afficher la liste filtrée des tâches
}

// Gestionnaire d'événement pour le bouton "Tout effacer"
clearAll.addEventListener("click", () => {
  const activeFilter = document.querySelector(".filters span.active").id; // Récupérer l'ID du filtre actuellement actif
  let filteredTodos = todos;

  // Filtrer les tâches en fonction du filtre actif
  if (activeFilter === "all") {
    filteredTodos = todos; // Si "Tout" est actif, afficher toutes les tâches
  } else if (activeFilter === "pending") {
    filteredTodos = todos.filter(todo => todo.status === "pending"); // Si "En cours" est actif, afficher uniquement les tâches en cours
  } else if (activeFilter === "completed") {
    filteredTodos = todos.filter(todo => todo.status === "completed"); // Si "Terminé" est actif, afficher uniquement les tâches terminées
  }

  if (filteredTodos.length === 0) {
    alert("Tsy misy asa ho fafana."); // Afficher une alerte si aucune tâche à supprimer
    return;
  }

  const confirmation = confirm("Tena te-hamafa ny asa rehetra amin'io karazana fanamarinana io ve ianao ?"); // Demander confirmation pour supprimer toutes les tâches filtrées
  if (confirmation) {
        todos = todos.filter(todo => !filteredTodos.includes(todo)); // Supprimer toutes les tâches filtrées de la liste complète des tâches
        localStorage.setItem("todo-list", JSON.stringify(todos)); // Mettre à jour la liste des tâches dans le stockage local
        updateTaskCounts(); // Mettre à jour les compteurs de tâches filtrées
        showTodoList("", todos); // Afficher la liste de toutes les tâches filtrées (non filtrées)
  }
});

// Appeler la fonction showTodoList avec le filtre initial pour afficher toutes les tâches
showTodoList("all", todos);
