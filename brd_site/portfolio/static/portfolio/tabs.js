var allProj = document.getElementById("all-proj");
allProj.onclick = function(){
    console.log("Clicked allProj!");
    projObjects = document.getElementsByClassName("proj");
    var i;
    for (i=0; i<projObjects.length; i++) {
        projObjects[i].style.display = "block";
    }
};

var personalProj = document.getElementById("personal-proj");
personalProj.onclick = function(){
    console.log("Clicked personalProj!");
    persObjects = document.getElementsByClassName("Personal");
    var i;
    for (i=0; i<persObjects.length; i++) {
        persObjects[i].style.display = "block";
    }
    openSrcObjects = document.getElementsByClassName("OpenSource");
    for (i=0; i<openSrcObjects.length; i++) {
        openSrcObjects[i].style.display = "none";
    }
};

var openSourceProj = document.getElementById("open-source-proj");
openSourceProj.onclick = function(){
    console.log("Clicked openSourceProj!");
    var i;
    for (i=0; i<persObjects.length; i++) {
        persObjects[i].style.display = "none";
    }
    openSrcObjects = document.getElementsByClassName("OpenSource");
    for (i=0; i<openSrcObjects.length; i++) {
        openSrcObjects[i].style.display = "block";
    }

};