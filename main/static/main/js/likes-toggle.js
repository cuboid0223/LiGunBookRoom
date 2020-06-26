$(document).ready(function () {
    $('#not-like').on('toggle-click', function () {
        $('.yes-like ').css('opacity', '1');
        $('#not-like ').css('opacity', '0');
    });
});

// .like: hover #not - like {
//     transform: rotateY(180deg);
//     /*當hover時，front從正面轉到背面*/
// }

// .like: hover #like {
//     transform: rotateY(0deg);
//     /*當hover時，back從背面轉到正面*/
// }