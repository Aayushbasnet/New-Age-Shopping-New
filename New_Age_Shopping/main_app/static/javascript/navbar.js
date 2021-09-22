// displaying search bar in navbar after clicking search icon

let navbar_searchbar_input = document.querySelector('.navbar_searchbar_input');

function navbar_searchbar_icon(element) {
    if (navbar_searchbar_input.style.display === 'block') {
        navbar_searchbar_input.style.display = 'none';
    } else {
        navbar_searchbar_input.style.display = 'block';
    }
}