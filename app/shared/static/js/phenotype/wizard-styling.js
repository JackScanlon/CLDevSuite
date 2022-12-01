const updateTrackerStyle = (navbar, trackers) => {
  for (let i = 0; i < trackers.length; i++) {
    const tracker = trackers[i];
    const offset = tracker.getBoundingClientRect().y - navbar.offsetHeight;
    const size = tracker.offsetHeight;

    let progress = 0;
    if (offset < 0) {
      progress = Math.min((Math.abs(offset) / (size - (size/1.25))) * 100, 100);
    }
    tracker.style.setProperty('--progress-percentage', `${progress}%`);
  }
}

const initStepsWizard = () => {
  document.querySelectorAll('.wizard-step-item').forEach(elem => {
    elem.addEventListener('click', e => {
      const target = document.querySelector(`#${elem.getAttribute('data-target')}`);
      if (target) {
        window.scroll({ top: target.offsetTop, left: 0, behavior: 'smooth' });
      }
    });
  });
  
  const navbar = document.querySelector('.page-navigation');
  const trackers = document.querySelectorAll('.progress-item');
  document.addEventListener('scroll', e => {
    updateTrackerStyle(navbar, trackers);
  });
}

const createDatePicker = (id, onSelect) => {
  return new Lightpick({
    field: document.getElementById(id),
    singleDate: false,
    selectForward: true,
    minDate: moment().startOf('month').add(7, 'day'),
    maxDate: moment().endOf('month').subtract(7, 'day'),
    onSelect: onSelect
  });
}

export { initStepsWizard, createDatePicker };
