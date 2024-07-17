$(document).ready(function () {
    $("#menu-toggle").click(function (e) {
        e.preventDefault();
        $("#wrapper").toggleClass("toggled");
    });
});

function confirmDelete(event, form) {
    event.preventDefault(); // Previne o envio padrão do formulário

    Swal.fire({
        title: 'Você tem certeza?',
        text: 'Essa ação não pode ser revertida',
        icon: 'warning',
        showCancelButton: true,
        confirmButtonColor: '#3085d6',
        cancelButtonColor: '#d33',
        confirmButtonText: 'Sim, Deletar!'
    }).then((result) => {
        if (result.isConfirmed) {
            form.submit(); // Envia o formulário se o usuário confirmar
        }
    });
}


