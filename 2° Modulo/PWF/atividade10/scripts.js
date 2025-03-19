document.addEventListener('DOMContentLoaded', fetchPosts); // Carrega os posts automaticamente ao abrir a página

        function fetchPosts() {
            fetch('https://jsonplaceholder.typicode.com/posts')
                .then(response => response.json())
                .then(posts => {
                    const postsContainer = document.getElementById('posts');
                    postsContainer.innerHTML = '';

                    posts.slice(0, 10).forEach(post => { // Pegamos apenas 5 posts
                        fetch(`https://jsonplaceholder.typicode.com/users/${post.userId}`)
                            .then(response => response.json())
                            .then(user => {
                                const postElement = document.createElement('div');
                                postElement.classList.add('post');
                                postElement.innerHTML = `
                                    <h2>${post.title}</h2>
                                    <p>${post.body}</p>
                                    <p><strong>Autor:</strong> ${user.username} (${user.email})</p>
                                    <button onclick="fetchComments(${post.id})">Ver Comentários</button>
                                `;
                                postsContainer.appendChild(postElement);
                            });
                    });
                })
                .catch(error => console.error('Erro ao buscar posts:', error));
        }

        function fetchComments(postId) {
            fetch(`https://jsonplaceholder.typicode.com/comments?postId=${postId}`)
                .then(response => response.json())
                .then(comments => {
                    const commentsContent = document.getElementById('commentsContent');
                    commentsContent.innerHTML = '';

                    comments.forEach(comment => {
                        const commentElement = document.createElement('p');
                        commentElement.innerHTML = `<strong>${comment.name}</strong>: ${comment.body}`;
                        commentsContent.appendChild(commentElement);
                    });

                    document.getElementById('commentsPopup').style.display = 'block';
                })
                .catch(error => console.error('Erro ao buscar comentários:', error));
        }

        function closePopup() {
            document.getElementById('commentsPopup').style.display = 'none';
        }