document.getElementById("all-proj").onclick = function() {tabClick("", "proj", "tab-all-proj")};
document.getElementById("personal-proj").onclick = function() {tabClick("OpenSource", "Personal", "tab-pers-proj")};
document.getElementById("open-source-proj").onclick = function() {
    tabClick("Personal", "OpenSource", "tab-open-source-proj")
};

function tabClick(hideableClassName, showableClassName, activeTab) {
    // Hide un-selected cards:
    hideableElements = document.getElementsByClassName(hideableClassName);
    var i;
    for (i=0; i<hideableElements.length; i++) {
        hideableElements[i].style.display = "none";
    };
    // Show selected cards:
    showableElements = document.getElementsByClassName(showableClassName);
    for (i=0; i<showableElements.length; i++) {
        showableElements[i].style.display = "block";
    };
    // Set correct tab active state:
    tabIds = ["tab-all-proj", "tab-pers-proj", "tab-open-source-proj"];
    for (i=0; i<tabIds.length; i++) {
        if (tabIds[i] == activeTab) {
            document.getElementById(tabIds[i]).classList.add("is-active");
        }
        else {
            document.getElementById(tabIds[i]).classList.remove("is-active");
        };
    };
};