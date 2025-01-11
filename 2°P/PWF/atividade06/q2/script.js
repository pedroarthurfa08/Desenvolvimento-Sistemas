const input1 = document.getElementById('input1');
        const input2 = document.getElementById('input2');

        input1.addEventListener('keyup', () => {
            input2.value = input1.value.toUpperCase();
        });