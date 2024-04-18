document.addEventListener('DOMContentLoaded', function () {
          const flashOk = document.getElementById('flash_ok');

          flashOk.addEventListener('animationend', function () {
            flashOk.remove();
          });
        });

document.addEventListener('DOMContentLoaded', function () {
        const flashErr = document.getElementById('flash_err');

        flashErr.addEventListener('animationend', function () {
          flashErr.remove();
        });
      });
