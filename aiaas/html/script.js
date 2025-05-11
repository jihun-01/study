const menuContainer = document.querySelector('.top_nav');
const submenu = document.querySelector('.menu_bar');

menuContainer.addEventListener('mouseenter', () => {
  submenu.style.display = 'flex';
});

menuContainer.addEventListener('mouseleave', () => {
  submenu.style.display = 'none';
});