$(document).ready(function () {
    $('form#business').submit(function (event) {
        event.preventDefault()
        form = $('form#business')

        $.ajax({
            'url': '/ajax/business/',
            'type': 'POST',
            'data': form.serialize(),
            'dataType': 'json',
            'success': function (data) {
                alert(data['success'])
            }
        })
        $('#id_business_name').val('')
        $('#id_business_email').val('')
        $('#id_business_hood').val('')
    })
})