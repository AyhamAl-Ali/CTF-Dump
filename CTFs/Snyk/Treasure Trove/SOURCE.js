
const segementOne = document.getElementById('seg-1');
const segementTwo = document.getElementById('seg-2');
const segementThree = document.getElementById('seg-3');
const segementFour = document.getElementById('seg-4');
const segementFive = document.getElementById('seg-5');

const setError = (message) => {
  document.getElementById('error-msg').innerText = message;
}

setError('');
    const characters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789';
    const key = segementOne.value + segementTwo.value + segementThree.value + segementFour.value + segementFive.value;
    if (key.length != 25) {
      setError('Invalid redemtion code!')
      return;
    }

    let val = 0;
    for (let i = 0; i < 25; i++) {
      val += key.charCodeAt(i);
      if (!characters.includes(key[i])) {
        setError('invalid characters');
        return;
      }
    }

    if (val != 1800) {
      setError('invalid code');
      return;
    }

    fetch('/api/validatekey/' + key)
    .then(async res => {
      const result = await res.json();
      setError('Argg ye got it! ' + result.flag);
    });

