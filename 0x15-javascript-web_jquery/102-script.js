$(document).ready(function() {
    $('#btn_translate').click(function() {
        const language = $('#language_code').val();
        const url = `https://www.fourtonfish.com/hellosalut/?lang=${language}`;

        $.get(url, function(data, status) {
            $('#hello').text(data.hello);
        });
    });
});

