function getApi() {
    const ul = document.querySelector('ul')
    ul.innerHTML = ''

    const user = document.quereySelector('#user').value

    fetch(`https://api.github.com/users/${user}/repos`)
}

