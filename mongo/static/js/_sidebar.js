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
