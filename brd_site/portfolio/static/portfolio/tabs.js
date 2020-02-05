var allProj = document.getElementById("all-proj");
allProj.onclick = function(){
    console.log("Clicked allProj!");
    // Show all project cards:
    projObjects = document.getElementsByClassName("proj");
    var i;
    for (i=0; i<projObjects.length; i++) {
        projObjects[i].style.display = "block";
    }
    // Set correct tab active state:
    document.getElementById("tab-all-proj").classList.add("is-active");
    document.getElementById("tab-pers-proj").classList.remove("is-active");
    document.getElementById("tab-open-source-proj").classList.remove("is-active");
};

var personalProj = document.getElementById("personal-proj");
personalProj.onclick = function(){
    console.log("Clicked personalProj!");
    // Show personal project cards:
    persObjects = document.getElementsByClassName("Personal");
    var i;
    for (i=0; i<persObjects.length; i++) {
        persObjects[i].style.display = "block";
    }
    // Hide open source project cards:
    openSrcObjects = document.getElementsByClassName("OpenSource");
    for (i=0; i<openSrcObjects.length; i++) {
        openSrcObjects[i].style.display = "none";
    }
    // Set correct tab active state:
    document.getElementById("tab-all-proj").classList.remove("is-active");
    document.getElementById("tab-pers-proj").classList.add("is-active");
    document.getElementById("tab-open-source-proj").classList.remove("is-active");
};

var openSourceProj = document.getElementById("open-source-proj");
openSourceProj.onclick = function(){
    console.log("Clicked openSourceProj!");
    // Hide personal project cards:
    var i;
    for (i=0; i<persObjects.length; i++) {
        persObjects[i].style.display = "none";
    }
    // Show open source project cards:
    openSrcObjects = document.getElementsByClassName("OpenSource");
    for (i=0; i<openSrcObjects.length; i++) {
        openSrcObjects[i].style.display = "block";
    }
    // Set correct tab active state:
    document.getElementById("tab-all-proj").classList.remove("is-active");
    document.getElementById("tab-pers-proj").classList.remove("is-active");
    document.getElementById("tab-open-source-proj").classList.add("is-active");
};