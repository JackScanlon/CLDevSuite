const updateNavBarStyle = (navbar) => {
  const isHome = typeof navbar.getAttribute('data-home') !== 'object';
  const y = window.scrollY;
  if (y >= navbar.offsetHeight/2 - navbar.offsetTop) {
    navbar.classList.add('scrolled');
    
    if (isHome) {
      navbar.classList.remove('transparent');
    }
  } else {
    navbar.classList.remove('scrolled');

    if (isHome) {
      navbar.classList.add('transparent');
    }
  }
}

const computeBurgerProperty = (burger) => {
  return window.getComputedStyle(burger, ':after').getPropertyValue('--as-burger').replace(/[^\w!?]/g, '');
}

const initHamburgerMenu = () => {
  const burger = document.querySelector('.page-navigation .buttons');
  const panel = burger.querySelector('.items');
  
  burger.addEventListener('click', e => {
    if (panel.classList.contains('open'))
      return;
    
    const isBurger = computeBurgerProperty(burger);
    if (isBurger === "true") {
      panel.classList.add('open');
      return;
    }

    panel.classList.remove('open');
  });

  document.addEventListener('click', e => {
    const element = e.target;
    if (burger.contains(element)) {
      return;
    }

    panel.classList.remove('open');
  })
}

domReady.finally(() => {
  const navbar = document.querySelector('.page-navigation');
  updateNavBarStyle(navbar);

  document.addEventListener('scroll', e => {
    updateNavBarStyle(navbar);
  });

  initHamburgerMenu();
});