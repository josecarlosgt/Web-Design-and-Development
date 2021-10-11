// https://learn.jquery.com/using-jquery-core/document-ready/
$( document ).ready(function() {
    $('#exampleModal').on('show.bs.modal', function (e) {
        // $('#modal-body').innerHTML = 'Hello, World!';

        // Review email
        let email = $('#exampleInputEmail1').val();
        $('#exampleInputEmail1_v').val(email);

        // Review name
        $('#exampleInputEmail2_v').val(
            $('#exampleInputEmail2').val());

        // Review comment
        $('#exampleFormControlTextarea1_v').val(
            $('#exampleFormControlTextarea1').val());
    });
});
