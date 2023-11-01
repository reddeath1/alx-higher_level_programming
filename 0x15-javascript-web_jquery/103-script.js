document.addEventListener('DOMContentLoaded', () => {
  $('INPUT#btn_translate').click(() =>
    $.get('https://www.fourtonfish.com/hellosalut/hello/' +
    $('INPUT#language_code').val(), (data) =>
      $('DIV#hello').html(data.hello)));
  $('INPUT#language_code').keydown((e) => {
    if (e.which === 13) {
      $.get('https://www.fourtonfish.com/hellosalut/hello/?lang=' +
      $('INPUT#language_code').val(), (data) =>
        $('DIV#hello').html(data.hello));
    } else return true;
  });
});
