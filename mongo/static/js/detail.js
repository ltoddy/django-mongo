function showOrigin(element) {
    if (element.nextSibling.nextSibling.style.display === 'none' || element.nextSibling.nextSibling.style.display === '') {
        element.nextSibling.nextSibling.style.display = 'block';
    } else {
        element.nextSibling.nextSibling.style.display = 'none';
    }
}
