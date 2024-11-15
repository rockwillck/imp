let ban = document.getElementById("banner")
ban.style.backgroundImage = `url(${ban.dataset.bg})`

for (let div of document.getElementsByClassName("card")) {
    div.style.backgroundImage = `url(${div.dataset.bg})`
}