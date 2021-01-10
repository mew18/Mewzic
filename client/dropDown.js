function dropdownMenu() {
    var ham = document.getElementById("hambg");
    if (ham.className === "topnav") {
        ham.className += " responsive";
    }

    else {
        ham.className = "topnav";
    }
}