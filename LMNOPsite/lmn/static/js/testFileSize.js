/**
 * Client-side file size verification
 *
 * Include only after jQuery is loaded
 *
 * This is easily disabled by end user and server-side checking should still be performed
 *
 */

// https://stackoverflow.com/questions/2472422/django-file-upload-size-limit
$("form").submit(function() {
  if (window.File && window.FileReader && window.FileList && window.Blob) {
    var file = $('#id_file')[0].files[0];

    if (file && file.size > 2 * 1024 * 1024) {
      alert("File " + file.name + " of type " + file.type + " is too big");
      return false;
    }
  }
});
