let codeArea = new CodeFlask('#root', {
    language: 'css',
    lineNumbers: true,
  })
  
let code = String.raw `body {
  margin: 0;
}
`
codeArea.updateCode(code)

$(document).ready(function() {
    $(document).on("click", ".upload_code", function () {
        $(this).prop('disabled', true)
        const code = codeArea.getCode();
        $.ajax({
            url: '/upload_code',
            type: 'POST',
            data: {code: code, captcha: grecaptcha.getResponse()},
            success: function (data) {
                document.location = document.location.href+"static/uploads/"+data.filename+".css";
            },
            error: function (data) {
                console.log(data);
                toastr.error(data.responseJSON.message);
                $('.upload_code').prop('disabled', false);
                grecaptcha.reset()
            }
        });
    });
});