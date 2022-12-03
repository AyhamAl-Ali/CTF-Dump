setInterval(() => {
    document.querySelector("body").style.background = `#${Math.floor(Math.random()*16777215).toString(16)}`;
}, 50)