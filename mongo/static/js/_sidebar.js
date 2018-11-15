function _toggleSideBarHelper() {
    const sideBarNode = document.getElementsByClassName("side-nav")[0];
    const mainNode = document.getElementsByClassName("main")[0];

    let on = true;
    function toggle() {

        if (on) {
            sideBarNode.style.width = 0;
            mainNode.style.marginLeft = 0;
            on = false;
        } else {
            sideBarNode.style.width = "260px";
            mainNode.style.marginLeft = "260px";
            on = true;
        }
    }

    return toggle;
}

const toggleSideBar = _toggleSideBarHelper();

function changeOpenAndCloseIconAndCollections(element) {
    const mongoDBNameItems = document.getElementsByClassName('mongo-db-name');

    for (mongoDBNameItem of mongoDBNameItems) {
        mongoDBNameItem.className = 'mongo-db-name';
        mongoDBNameItem.childNodes[1].innerText = "∇";
        mongoDBNameItem.nextSibling.nextSibling.style.display = 'none';
    }

    element.className = 'mongo-db-active' + ' ' + element.className;
    element.childNodes[1].innerText = "Δ";
    element.nextSibling.nextSibling.style.display = 'block';
}
