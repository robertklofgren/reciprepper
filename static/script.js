function expandRecipe() {
    var recipe = document.getElementById("recipeInput").value;

    fetch('/expand', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ recipe: recipe })
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById("expandedRecipe").innerText = data.expandedRecipe;
    });
}

