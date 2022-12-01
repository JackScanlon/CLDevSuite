const createCodeSearchResult = ({ id, code, description }) => {
  return `
  <div class="codelist-result-item">
    <form class="checkbox-group">
      <input class="checkbox-input" aria-label="Add code" type="checkbox" id="select-code_${id}" name="select-code_${id}" result-type="codelist-item">
      <label class="code" for="select-code_${id}">${code}</label>
      <label class="desc" for="select-code_${id}">${description}</label>
    </form>
  </div>`
}

const createConceptComponent = () => {
  return `
  <section class="component-group">
    <span class="component-item is-open">
      <span class="contextual-icon"></span>
      <label class="component-name">"Neoplasms"</label>
    </span>
    <section class="component-content">
      <section class="content">
        <section class="component-content-details">
          <label>Codelist</label>
        </section>
        <section class="codelist components">
          <section class="codelist-header">
            <label>Rule</label>
            <label>Code</label>
            <label>Description</label>
          </section>
          <section class="codelist-content">
            <div class="codelist-item">
              <label class="rule" id="rule">
                <form class="rule-button-group">
                  <input class="ruleset-button include" aria-label="Inclusion Rule" type="radio" id="include" name="ruleset" checked>
                  <input class="ruleset-button exclude" aria-label="Exclusion Rule" type="radio" id="exclude" name="ruleset">
                  <input class="ruleset-button remove" aria-label="Remove code" type="radio" id="remove" name="ruleset">
                </form>
              </label>
              <label class="item" id="code">C30.0</label>
              <label class="wrap" id="desc">Malignant neoplasms of respiratory and intrathoracic organs</label>
            </div>
            <div class="codelist-item">
              <label class="rule" id="rule">
                <form class="rule-button-group">
                  <input class="ruleset-button include" aria-label="Inclusion Rule" type="radio" id="include" name="ruleset" checked>
                  <input class="ruleset-button exclude" aria-label="Exclusion Rule" type="radio" id="exclude" name="ruleset">
                  <input class="ruleset-button remove" aria-label="Remove code" type="radio" id="remove" name="ruleset">
                </form>
              </label>
              <label class="item" id="code">C30.0</label>
              <label class="wrap" id="desc">Malignant neoplasms of respiratory and intrathoracic organs</label>
            </div>
          </section>
        </section>
      </section>
    </section>
  </section>`
}

const createConceptCodelistItem = () => {
  return `
  <div class="codelist-creation-item">
    <label class="rule" id="rule">
      <form class="rule-button-group">
        <input class="ruleset-button include" aria-label="Inclusion Rule" type="radio" id="include" name="ruleset" checked>
        <input class="ruleset-button exclude" aria-label="Exclusion Rule" type="radio" id="exclude" name="ruleset">
        <input class="ruleset-button remove" aria-label="Remove code" type="radio" id="remove" name="ruleset">
      </form>
    </label>
    <label class="item" id="code">C30.0</label>
    <label class="wrap" id="desc">Malignant neoplasms of respiratory and intrathoracic organs</label>
    <label class="item" id="source"><a class="search-term" title="Search term used to find this code">"Neoplasms"</a></label>
  </div>
  <div class="codelist-creation-item">
    <label class="rule" id="rule">
      <form class="rule-button-group">
        <input class="ruleset-button include" aria-label="Inclusion Rule" type="radio" id="include" name="ruleset" checked>
        <input class="ruleset-button exclude" aria-label="Exclusion Rule" type="radio" id="exclude" name="ruleset">
        <input class="ruleset-button remove" aria-label="Remove code" type="radio" id="remove" name="ruleset">
      </form>
    </label>
    <label class="item" id="code">C30.0</label>
    <label class="wrap" id="desc">Malignant neoplasms of respiratory and intrathoracic organs</label>
    <label class="item" id="source"><a class="file-import" title="Imported from file">Imported.csv</a></label>
  </div>
  <div class="codelist-creation-item">
    <label class="rule" id="rule">
      <form class="rule-button-group">
        <input class="ruleset-button include" aria-label="Inclusion Rule" type="radio" id="include" name="ruleset" checked>
        <input class="ruleset-button exclude" aria-label="Exclusion Rule" type="radio" id="exclude" name="ruleset">
        <input class="ruleset-button remove" aria-label="Remove code" type="radio" id="remove" name="ruleset">
      </form>
    </label>
    <label class="item" id="code">C30.0</label>
    <label class="wrap" id="desc">Malignant neoplasms of respiratory and intrathoracic organs</label>
    <label class="item" id="source"><a class="concept-import" title="Imported from existing Concept">PH123/23 → C456/89</a></label>
  </div>`
}

const createCodelistItem = ({ rule, code, desc, source }) => {
  return `
  <div class="codelist-item">
    <label class="rule inclusion-rule" id="rule" value="${rule}"></label>
    <label class="item" id="code">${code}</label>
    <label class="wrap" id="desc">${desc}</label>
    <label class="item" id="source">${source}</label>
  </div>`
}

const createConceptGroup = ({ name, coding, codelist }) => {
  let items = '';
  for (let i = 0; i < codelist.length; i++) {
    items += createCodelistItem(codelist[i]);
  }

  return `
  <section class="concept-group">
    <span class="concept-item is-open">
      <span class="contextual-icon"></span>
      <label class="concept-name">${name}</label>
      <span class="concept-buttons">
        <span class="edit-icon"></span>
        <span class="delete-icon"></span>
      </span>
    </span>
    <section class="concept-content">
      <section class="content">
        <section class="concept-content-details">
          <label>Codelist</label>
          <ul class="chips-group" id="coding-system-chip">
            <li class="chip bold washed-accent text-accent-darkest codelist-icon icon-accent-highlight">
              <a id="coding-system-info">${coding}</a>
            </li>
          </ul>
        </section>
        <section class="codelist">
          <section class="codelist-header">
            <label>Rule</label>
            <label>Code</label>
            <label>Description</label>
            <label>Source</label>
          </section>
          <section class="codelist-content">
            ${items}
          </section>
        </section>
      </section>
    </section>
  </section>`
}

export { createConceptGroup, createCodelistItem, createConceptCodelistItem, createConceptComponent, createCodeSearchResult };
