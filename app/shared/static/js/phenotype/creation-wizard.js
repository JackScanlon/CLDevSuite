import Tagify from '../components/tagify.js'
import { initStepsWizard, createDatePicker } from './wizard-styling.js'
import { DEFAULT } from './constants.js'
import { createConceptGroup, createCodelistItem, createConceptCodelistItem, createConceptComponent, createCodeSearchResult } from './render.js'

/*

  Field issues:
    1. Daterangepicker should update when the text is edited

  Model issues:
    1. Need to add codelist and assoc. object(s)
  
*/

class CreationWizard {
  constructor() {
    this.phenotype = deepCopy(DEFAULT);
    this.searchParams = {
      'page': 1,
      'query': '',
    };
    this.#populateFields();
    this.#initialiseElements();
  }

  /* Public */
  PopulateForm(phenotype) {
    this.phenotype = phenotype;

    // Populate forms with current phenotype data
    
  }

  /* Private */
  #toggleView = (val) => {
    const componentView = document.querySelector('#component-view-area');
    const codelistView = document.querySelector('#codelist-view-area');
  
    if (val) {
      componentView.classList.add('hide');
      codelistView.classList.remove('hide');
    } else {
      componentView.classList.remove('hide');
      codelistView.classList.add('hide');
    }
  }

  #clearConceptCodeSearch() {
    const creationView = document.querySelector('#create-concept-view');
    creationView.querySelectorAll('.codelist-result-item').forEach(e => {
      e.remove();
    });
  }

  #toggleCreationArea(toggle) {
    const creationView = document.querySelector('#create-concept-view');
    if (toggle) {
      creationView.querySelector('#codelist-creation-area').classList.remove('hide');
      creationView.querySelector('#codelist-search-area').classList.remove('hide');
      return;
    }
    
    creationView.querySelector('#codelist-creation-area').classList.add('hide');
    creationView.querySelector('#codelist-search-area').classList.add('hide');
  }

  #clearConceptFields() {
    document.getElementById('concept-name').value = '';
    document.getElementById('concept-coding-system').selectedIndex = 0;
    
    const creationView = document.querySelector('#create-concept-view');
    creationView.querySelectorAll('.component-group').forEach(e => {
      e.remove();
    });

    creationView.querySelectorAll('.codelist-item').forEach(e => {
      e.remove();
    });

    creationView.querySelector('#no-codesearch-results').classList.add('show');
    creationView.querySelector('#no-components-result').classList.add('show');
    creationView.querySelector('#no-codelist-result').classList.add('show');
    
    this.#clearConceptCodeSearch();
    this.#toggleCreationArea(false);
  }

  #populateConceptFields(concept) {
    
  }

  #setConceptToggle = (toggle) => {
    const toggleItem = document.querySelector('#concepts-view-toggle');
    if (toggle) {
      toggleItem.classList.toggle('show');
    } else {
      toggleItem.classList.remove('show');
    }
  
    toggleItem.querySelector('label').innerText = toggleItem.classList.contains('show') ? 'Collapse' : 'Expand';
  }

  #toggleCreationView(toggle) {
    const conceptsView = document.querySelector('#concepts-view');
    const creationView = document.querySelector('#create-concept-view');

    this.#clearConceptFields();
    this.#setConceptToggle(!toggle);

    if (toggle) {
      conceptsView.classList.remove('show');
      creationView.classList.add('show');

      if (this.currentConcept) {
        this.#populateConceptFields(this.currentConcept);
      }
    } else {
      conceptsView.classList.add('show');
      creationView.classList.remove('show');
    }
  }

  #renderSearchResults() {
    const coding = this.currentConcept.coding_system;
    if (!coding) {
      return;
    }

    this.#clearConceptCodeSearch();
    
    const csrftoken = getCookie('csrftoken');
    const data = JSON.stringify({
      page: this.searchParams.page,
      query: this.searchParams.query,
      id: coding.id,
    });

    fetch(`/codelist/`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'X-CSRFToken': csrftoken,
      },
      body: data,
    })
    .then(res => {
      if (!res.ok) {
        throw Error(res.statusText);
      }

      return res;
    })
    .then(res => res.json())
    .then(data => {
      const results = document.getElementById('codelist-search-results');
      const noresults = document.getElementById('no-codesearch-results');
      const rescount = document.getElementById('codesearch-result-count');
      
      const codes = data.codes;
      if (codes.length <= 0) {
        noresults.classList.add('show');
        results.classList.remove('show');
      } else {
        noresults.classList.remove('show');
        results.classList.add('show');
      }
      rescount.innerText = `Found ${data.total} Code(s)`;

      for (let i = 0; i < codes.length; i++) {
        const code = codes[i]
        const node = new DOMParser().parseFromString(createCodeSearchResult(code), 'text/html').body.firstElementChild;
        
        const index = this.currentConcept.codelist.findIndex(e => e.id == code.id);
        if (index >= 0) {
          node.querySelector('input[type="checkbox"]').setAttribute('checked', true);
        }

        results.append(node);
      }
    })
    .catch(err => console.error(err));
  }

  #initialiseElements() {
    // Create concept(s)
    const createConceptBtn = document.querySelector('#create-concept-btn');
    createConceptBtn.addEventListener('click', e => {
      this.currentConcept = {
        'id': null,
        'name': '',
        'coding_system': null,
        'codelist': [],
      };

      this.#toggleCreationView(true);
    }, false);
    
    // Expanding / Collapsing concept view(s)
    const toggleItem = document.querySelector('#concepts-view-toggle');
    toggleItem.addEventListener('click', e => {
      this.#setConceptToggle(true);
    }, false);

    // Concept creation menu
    const creationView = document.querySelector('#create-concept-view');
    const conceptCreationBtn = creationView.querySelector('#add-concept');
    conceptCreationBtn.addEventListener('click', e => {
      this.#toggleCreationView(false);
    });
  
    const cancelCreationBtns = creationView.querySelectorAll('#quit-creation');
    cancelCreationBtns.forEach(elem => {
      elem.addEventListener('click', e => {
        this.#toggleCreationView(false);
      });
    });

    const tableRadio = document.querySelector('#codelist-table-view');
    tableRadio.addEventListener('change', e => {
      this.#toggleView(true);
    });

    const componentRadio = document.querySelector('#codelist-component-view');
    componentRadio.addEventListener('change', e => {
      this.#toggleView(false);
    });

    const codingSelector = creationView.querySelector('#concept-coding-system');
    codingSelector.addEventListener('input', e => {
      const target = e.target.options[e.target.selectedIndex];
      this.currentConcept.coding_system = {
        id: target.value,
        name: target.innerText.trim(),
      };

      this.#toggleCreationArea(true);
      this.searchParams = {'page': 1, 'query': ''};
      this.#renderSearchResults();
    })

    const searchInput = creationView.querySelector('#codelist-search');
    searchInput.addEventListener('keydown', (e) => {
      const code = e.which || e.keyCode;
      if (code == 13) {
        e.preventDefault();
  
        const value = e.target.value;
        this.searchParams.query = value;
        this.#renderSearchResults();
      }
    })

    // Code handling
    
  }

  #populateFields() {
    // Valid event date range
    this.datepicker = createDatePicker('phenotype-entry-range', (start, end) => {
      let str = '';
      str += start ? start.format('Do MMMM YYYY') + ' to ' : '';
      str += end ? end.format('Do MMMM YYYY') : '...';
      document.getElementById('phenotype-entry-range').innerHTML = str;
    });

    // Phenotype types
    const types = document.getElementById('phenotype-type');
    for (let i = 0; i < phenotype_types.length; ++i) {
      const pt = phenotype_types[i];
      types.options[types.options.length] = new Option(pt.name, pt.id);
    }

    // Concept coding system(s)
    const coding = document.getElementById('concept-coding-system');
    for (let i = 0; i < coding_system.length; ++i) {
      const cs = coding_system[i];
      coding.options[coding.options.length] = new Option(cs.name, cs.id);
    }

    // Tag input(s)
    this.tagInputs = {
      'phenotype-tags': new Tagify('phenotype-tags', {
        'autocomplete': true,
        'useValue': true,
        'allowDuplicates': false,
        'restricted': true,
        'items': tags.map(e => {
          return {name: e.name, value: e.id};
        }),
      }),
      'phenotype-collections': new Tagify('phenotype-collections', {
        'autocomplete': true,
        'useValue': true,
        'allowDuplicates': false,
        'restricted': true,
        'items': collections.map(e => {
          return {name: e.name, value: e.id};
        }),
      }),
      'phenotype-datasources': new Tagify('phenotype-datasources', {
        'autocomplete': true,
        'useValue': true,
        'allowDuplicates': false,
        'restricted': true,
        'items': data_sources.map(e => {
          return {name: e.name, value: e.id};
        }),
      }),
    };

    // Concept(s)
    const message = document.getElementById('no-available-concepts');
    message.classList.add('show');
  }
}

domReady.finally(() => {
  const wizard = new CreationWizard();
  if (typeof phenotype !== 'undefined') {
    wizard.PopulateForm(phenotype);
  }

  initStepsWizard();
});
