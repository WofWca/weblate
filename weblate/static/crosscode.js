$(() => {
  // Rudimentary completion
  Mousetrap.bindGlobal('ctrl+space', (event) => {
    if (!event.target.matches('textarea.translation-editor')) return;
    let textarea = event.target;
    let container = textarea.closest('tbody.zen-unit');
    if (container == null) {
      container = textarea.closest('form.translation-form');
    }
    if (container == null) {
      return;
    }
    event.preventDefault();

    let translationText = textarea.value;
    let originalText;
    let allTexts = [translationText];
    for (let element of container.querySelectorAll(
      '.language + .list-group .list-group-item-text[lang] > button[data-clipboard-text]'
    )) {
      let text = element.dataset.clipboardText;
      if (originalText == null) {
        originalText = text;
      }
      allTexts.push(text);
    }

    function* splitWords(text) {
      let pattern = /\S+/g;
      while (true) {
        let match = pattern.exec(text);
        if (match == null) break;
        yield { str: match[0], start: match.index, end: match[0].length + match.index };
      }
    }

    if (translationText.length > 0) {
      // Logic from <https://github.com/L-Sherry/Localize-Me-Tools/blob/d3d124af392da85422d303242e43673a817b360f/jsontr.py#L385-L396>
      let words = new Set();
      for (let text of allTexts) {
        for (let word of splitWords(text)) {
          words.add(word.str);
        }
      }

      let currentWord;
      for (let word of splitWords(textarea.value)) {
        if (word.start <= textarea.selectionStart && textarea.selectionStart <= word.end) {
          currentWord = word.str.slice(0, Math.max(0, textarea.selectionStart - word.start));
          break;
        }
      }

      if (currentWord != null && currentWord.length > 0) {
        for (let word of words) {
          if (word !== currentWord && word.startsWith(currentWord)) {
            $(textarea).insertAtCaret(word.slice(currentWord.length));
            break;
          }
        }
      }
    } else if (translationText != null) {
      // Logic from <https://github.com/L-Sherry/Localize-Me-Tools/blob/d3d124af392da85422d303242e43673a817b360f/jsontr.py#L398-L402>
      // <https://github.com/WeblateOrg/weblate/blob/030f9c241b46d4d10a97211cbe8d4ae1b629488e/weblate/static/loader-bootstrap.js#L54>
      $(textarea).insertAtCaret(originalText);
    }
  });
});
