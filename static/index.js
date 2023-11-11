function simulateCommandPrompt(element, texts, speed, wait) {
  const outputElement = document.getElementById(element);
  const cursor = document.createElement('span');
  cursor.classList.add('cursor');
  cursor.textContent = '█';

  let currentIndex = 0;

  function typeText() {
    const text = texts[currentIndex];
    let i = 0;

    function typeCharacter() {
      if (i <= text.length) {
        outputElement.textContent = text.slice(0, i);
        outputElement.appendChild(cursor);
        i++;
        setTimeout(typeCharacter, speed);
      } else {
        setTimeout(() => {
          currentIndex = (currentIndex + 1) % texts.length;
          outputElement.textContent = '';
          outputElement.appendChild(cursor);
          typeText();
        }, wait);
      }
    }

    typeCharacter();
  }

  typeText();
}

const texts = [
  'software',
  'reality',
  'solutions',
  'innovation',
  'technology'
];

simulateCommandPrompt('typing', texts, 100, 3000);
