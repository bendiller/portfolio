tabId = document.currentScript.getAttribute('tabId');
activateTab(tabId);
function activateTab(tabId) {
    // Deactivate tabs:
    tabs = document.getElementsByClassName("tab");
    var i;
    for (i=0; i<tabs.length; i++) {
        tabs[i].classList.remove("is-active")
    };

    // Activate chosen tab:
    tab_elem = document.getElementById(tabId);
    if (tab_elem) {
        tab_elem.classList.add("is-active");
    };
};